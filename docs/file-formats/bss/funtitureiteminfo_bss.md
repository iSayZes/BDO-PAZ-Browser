# `funtitureiteminfo.bss` Format

## Purpose

Furniture items: one 9-byte row per item that places a house or manor
furnishing, with the installation type of the object it places. The file
name is spelled `funtiture` in the client. Each item places one
[`characterobject.dbss`](../dbss/characterobject_dbss.md) object (the record whose
item ID is the row's item), and `installation_type` equals that object's
`installation_type` on 520 of 520 rows of client 3482. No Lua file of
client 3482 names the table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                    | Bytes | Records | Row bytes |
| ------ | -------------- | ----------------------- | ----- | ------- | --------- |
| 1      | 1333 and later | `funtitureiteminfo.bss` | 4,700 | 520 Row | 9         |

| Layout | File                    | Known            | Unknown    |
| ------ | ----------------------- | ---------------- | ---------- |
| 1      | `funtitureiteminfo.bss` | 4,700 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `9c75188b7f22`  |
| 3482   | Layout 1 | `9c75188b7f22`  |
| 3474   | Layout 1 | `9c75188b7f22`  |
| 3473   | Layout 1 | `9c75188b7f22`  |
| 3464   | Layout 1 | `9c75188b7f22`  |
| 3458   | Layout 1 | `9c75188b7f22`  |
| 3454   | Layout 1 | `9c75188b7f22`  |
| 3444   | Layout 1 | `9c75188b7f22`  |
| 3435   | Layout 1 | `9c75188b7f22`  |
| 3426   | Layout 1 | `9c75188b7f22`  |
| 3418   | Layout 1 | `9c75188b7f22`  |
| 3412   | Layout 1 | `9c75188b7f22`  |
| 3402   | Layout 1 | `9c75188b7f22`  |
| 3396   | Layout 1 | `9c75188b7f22`  |
| 3387   | Layout 1 | `9c75188b7f22`  |
| 3381   | Layout 1 | `9c75188b7f22`  |
| 3373   | Layout 1 | `9c75188b7f22`  |
| 3364   | Layout 1 | `9c75188b7f22`  |
| 3356   | Layout 1 | `9c75188b7f22`  |
| 3349   | Layout 1 | `9c75188b7f22`  |
| 3342   | Layout 1 | `9c75188b7f22`  |
| 3335   | Layout 1 | `9c75188b7f22`  |
| 3326   | Layout 1 | `9c75188b7f22`  |
| 3321   | Layout 1 | `9c75188b7f22`  |
| 3314   | Layout 1 | `9c75188b7f22`  |
| 3303   | Layout 1 | `9c75188b7f22`  |
| 3302   | Layout 1 | `9c75188b7f22`  |
| 3293   | Layout 1 | `9c75188b7f22`  |
| 3283   | Layout 1 | `9c75188b7f22`  |
| 3275   | Layout 1 | `9c75188b7f22`  |
| 3267   | Layout 1 | `9c75188b7f22`  |
| 3258   | Layout 1 | `9c75188b7f22`  |
| 3251   | Layout 1 | `9c75188b7f22`  |
| 3242   | Layout 1 | `9c75188b7f22`  |
| 3235   | Layout 1 | `9c75188b7f22`  |
| 3229   | Layout 1 | `9c75188b7f22`  |
| 3212   | Layout 1 | `9c75188b7f22`  |
| 3203   | Layout 1 | `9c75188b7f22`  |
| 3193   | Layout 1 | `9c75188b7f22`  |
| 3186   | Layout 1 | `9c75188b7f22`  |
| 3177   | Layout 1 | `9c75188b7f22`  |
| 3169   | Layout 1 | `9c75188b7f22`  |
| 3158   | Layout 1 | `9c75188b7f22`  |
| 3151   | Layout 1 | `9c75188b7f22`  |
| 3144   | Layout 1 | `9c75188b7f22`  |
| 3133   | Layout 1 | `9c75188b7f22`  |
| 3125   | Layout 1 | `9c75188b7f22`  |
| 3118   | Layout 1 | `9c75188b7f22`  |
| 3111   | Layout 1 | `9c75188b7f22`  |
| 3103   | Layout 1 | `9c75188b7f22`  |
| 3095   | Layout 1 | `9c75188b7f22`  |
| 3086   | Layout 1 | `9c75188b7f22`  |
| 3072   | Layout 1 | `9c75188b7f22`  |
| 3062   | Layout 1 | `9c75188b7f22`  |
| 3052   | Layout 1 | `9c75188b7f22`  |
| 3045   | Layout 1 | `9c75188b7f22`  |
| 3037   | Layout 1 | `9c75188b7f22`  |
| 3030   | Layout 1 | `9c75188b7f22`  |
| 3021   | Layout 1 | `9c75188b7f22`  |
| 3012   | Layout 1 | `9c75188b7f22`  |
| 3002   | Layout 1 | `9c75188b7f22`  |
| 2995   | Layout 1 | `9c75188b7f22`  |
| 2987   | Layout 1 | `9c75188b7f22`  |
| 2978   | Layout 1 | `9c75188b7f22`  |
| 2970   | Layout 1 | `9c75188b7f22`  |
| 2959   | Layout 1 | `9c75188b7f22`  |
| 2951   | Layout 1 | `9c75188b7f22`  |
| 2942   | Layout 1 | `9c75188b7f22`  |
| 2935   | Layout 1 | `9c75188b7f22`  |
| 2932   | Layout 1 | `9c75188b7f22`  |
| 2923   | Layout 1 | `9c75188b7f22`  |
| 2919   | Layout 1 | `9c75188b7f22`  |
| 2907   | Layout 1 | `9c75188b7f22`  |
| 2900   | Layout 1 | `9c75188b7f22`  |
| 2891   | Layout 1 | `9c75188b7f22`  |
| 2882   | Layout 1 | `9c75188b7f22`  |
| 2872   | Layout 1 | `9c75188b7f22`  |
| 2863   | Layout 1 | `9c75188b7f22`  |
| 2855   | Layout 1 | `9c75188b7f22`  |
| 2849   | Layout 1 | `9c75188b7f22`  |
| 2844   | Layout 1 | `9c75188b7f22`  |
| 2834   | Layout 1 | `9c75188b7f22`  |
| 2825   | Layout 1 | `9c75188b7f22`  |
| 2819   | Layout 1 | `9c75188b7f22`  |
| 2811   | Layout 1 | `9c75188b7f22`  |
| 2803   | Layout 1 | `9c75188b7f22`  |
| 2794   | Layout 1 | `9c75188b7f22`  |
| 2783   | Layout 1 | `9c75188b7f22`  |
| 2774   | Layout 1 | `9c75188b7f22`  |
| 2765   | Layout 1 | `9c75188b7f22`  |
| 2756   | Layout 1 | `9c75188b7f22`  |
| 2750   | Layout 1 | `9c75188b7f22`  |
| 2743   | Layout 1 | `9c75188b7f22`  |
| 2736   | Layout 1 | `9c75188b7f22`  |
| 2726   | Layout 1 | `9c75188b7f22`  |
| 2717   | Layout 1 | `9c75188b7f22`  |
| 2709   | Layout 1 | `9c75188b7f22`  |
| 2703   | Layout 1 | `9c75188b7f22`  |
| 2695   | Layout 1 | `9c75188b7f22`  |
| 2684   | Layout 1 | `9c75188b7f22`  |
| 2672   | Layout 1 | `9c75188b7f22`  |
| 2665   | Layout 1 | `9c75188b7f22`  |
| 2657   | Layout 1 | `9c75188b7f22`  |
| 2649   | Layout 1 | `9c75188b7f22`  |
| 2644   | Layout 1 | `9c75188b7f22`  |
| 2637   | Layout 1 | `9c75188b7f22`  |
| 2629   | Layout 1 | `9c75188b7f22`  |
| 2619   | Layout 1 | `9c75188b7f22`  |
| 2612   | Layout 1 | `9c75188b7f22`  |
| 2606   | Layout 1 | `9c75188b7f22`  |
| 2602   | Layout 1 | `9c75188b7f22`  |
| 2601   | Layout 1 | `9c75188b7f22`  |
| 2592   | Layout 1 | `9c75188b7f22`  |
| 2583   | Layout 1 | `9c75188b7f22`  |
| 2575   | Layout 1 | `9c75188b7f22`  |
| 2567   | Layout 1 | `9c75188b7f22`  |
| 2560   | Layout 1 | `9c75188b7f22`  |
| 2553   | Layout 1 | `9c75188b7f22`  |
| 2545   | Layout 1 | `9c75188b7f22`  |
| 2538   | Layout 1 | `9c75188b7f22`  |
| 2529   | Layout 1 | `9c75188b7f22`  |
| 2519   | Layout 1 | `9c75188b7f22`  |
| 2513   | Layout 1 | `9c75188b7f22`  |
| 2510   | Layout 1 | `9c75188b7f22`  |
| 2507   | Layout 1 | `9c75188b7f22`  |
| 2503   | Layout 1 | `9c75188b7f22`  |
| 2498   | Layout 1 | `9c75188b7f22`  |
| 2492   | Layout 1 | `9c75188b7f22`  |
| 2487   | Layout 1 | `9c75188b7f22`  |
| 2480   | Layout 1 | `9c75188b7f22`  |
| 2474   | Layout 1 | `9c75188b7f22`  |
| 2468   | Layout 1 | `9c75188b7f22`  |
| 2460   | Layout 1 | `9c75188b7f22`  |
| 2453   | Layout 1 | `9c75188b7f22`  |
| 2444   | Layout 1 | `9c75188b7f22`  |
| 2438   | Layout 1 | `9c75188b7f22`  |
| 2434   | Layout 1 | `9c75188b7f22`  |
| 2429   | Layout 1 | `9c75188b7f22`  |
| 2421   | Layout 1 | `9c75188b7f22`  |
| 2414   | Layout 1 | `9c75188b7f22`  |
| 2407   | Layout 1 | `9c75188b7f22`  |
| 2401   | Layout 1 | `9c75188b7f22`  |
| 2397   | Layout 1 | `9c75188b7f22`  |
| 2393   | Layout 1 | `9c75188b7f22`  |
| 2384   | Layout 1 | `9c75188b7f22`  |
| 2378   | Layout 1 | `9c75188b7f22`  |
| 2372   | Layout 1 | `9c75188b7f22`  |
| 2358   | Layout 1 | `9c75188b7f22`  |
| 2352   | Layout 1 | `9c75188b7f22`  |
| 2347   | Layout 1 | `9c75188b7f22`  |
| 2343   | Layout 1 | `9c75188b7f22`  |
| 2335   | Layout 1 | `9c75188b7f22`  |
| 2327   | Layout 1 | `9c75188b7f22`  |
| 2324   | Layout 1 | `9c75188b7f22`  |
| 2319   | Layout 1 | `9c75188b7f22`  |
| 2313   | Layout 1 | `9c75188b7f22`  |
| 2308   | Layout 1 | `9c75188b7f22`  |
| 2302   | Layout 1 | `9c75188b7f22`  |
| 2295   | Layout 1 | `9c75188b7f22`  |
| 2290   | Layout 1 | `9c75188b7f22`  |
| 2284   | Layout 1 | `9c75188b7f22`  |
| 2276   | Layout 1 | `9c75188b7f22`  |
| 2269   | Layout 1 | `9c75188b7f22`  |
| 2259   | Layout 1 | `9c75188b7f22`  |
| 2250   | Layout 1 | `9c75188b7f22`  |
| 2243   | Layout 1 | `9c75188b7f22`  |
| 2235   | Layout 1 | `9c75188b7f22`  |
| 2229   | Layout 1 | `9c75188b7f22`  |
| 2224   | Layout 1 | `9c75188b7f22`  |
| 2218   | Layout 1 | `9c75188b7f22`  |
| 2215   | Layout 1 | `9c75188b7f22`  |
| 2207   | Layout 1 | `9c75188b7f22`  |
| 2203   | Layout 1 | `9c75188b7f22`  |
| 2196   | Layout 1 | `9c75188b7f22`  |
| 2192   | Layout 1 | `9c75188b7f22`  |
| 2189   | Layout 1 | `9c75188b7f22`  |
| 2183   | Layout 1 | `9c75188b7f22`  |
| 2179   | Layout 1 | `9c75188b7f22`  |
| 2171   | Layout 1 | `9c75188b7f22`  |
| 2163   | Layout 1 | `9c75188b7f22`  |
| 2156   | Layout 1 | `9c75188b7f22`  |
| 2151   | Layout 1 | `9c75188b7f22`  |
| 2147   | Layout 1 | `9c75188b7f22`  |
| 2142   | Layout 1 | `9c75188b7f22`  |
| 2138   | Layout 1 | `9c75188b7f22`  |
| 2134   | Layout 1 | `9c75188b7f22`  |
| 2130   | Layout 1 | `9c75188b7f22`  |
| 2122   | Layout 1 | `9c75188b7f22`  |
| 2107   | Layout 1 | `9c75188b7f22`  |
| 2098   | Layout 1 | `9c75188b7f22`  |
| 2089   | Layout 1 | `9c75188b7f22`  |
| 2081   | Layout 1 | `9c75188b7f22`  |
| 2073   | Layout 1 | `9c75188b7f22`  |
| 2067   | Layout 1 | `9c75188b7f22`  |
| 2063   | Layout 1 | `9c75188b7f22`  |
| 2059   | Layout 1 | `9c75188b7f22`  |
| 2052   | Layout 1 | `9c75188b7f22`  |
| 2044   | Layout 1 | `9c75188b7f22`  |
| 2039   | Layout 1 | `9c75188b7f22`  |
| 2032   | Layout 1 | `9c75188b7f22`  |
| 2025   | Layout 1 | `9c75188b7f22`  |
| 2011   | Layout 1 | `9c75188b7f22`  |
| 2005   | Layout 1 | `9c75188b7f22`  |
| 2000   | Layout 1 | `9c75188b7f22`  |
| 1996   | Layout 1 | `9c75188b7f22`  |
| 1991   | Layout 1 | `9c75188b7f22`  |
| 1985   | Layout 1 | `9c75188b7f22`  |
| 1980   | Layout 1 | `9c75188b7f22`  |
| 1969   | Layout 1 | `9c75188b7f22`  |
| 1964   | Layout 1 | `9c75188b7f22`  |
| 1958   | Layout 1 | `9c75188b7f22`  |
| 1950   | Layout 1 | `9c75188b7f22`  |
| 1945   | Layout 1 | `9c75188b7f22`  |
| 1937   | Layout 1 | `9c75188b7f22`  |
| 1933   | Layout 1 | `9c75188b7f22`  |
| 1927   | Layout 1 | `9c75188b7f22`  |
| 1921   | Layout 1 | `9c75188b7f22`  |
| 1914   | Layout 1 | `9c75188b7f22`  |
| 1908   | Layout 1 | `9c75188b7f22`  |
| 1897   | Layout 1 | `9c75188b7f22`  |
| 1892   | Layout 1 | `9c75188b7f22`  |
| 1886   | Layout 1 | `9c75188b7f22`  |
| 1881   | Layout 1 | `9c75188b7f22`  |
| 1871   | Layout 1 | `9c75188b7f22`  |
| 1866   | Layout 1 | `9c75188b7f22`  |
| 1862   | Layout 1 | `9c75188b7f22`  |
| 1854   | Layout 1 | `9c75188b7f22`  |
| 1846   | Layout 1 | `9c75188b7f22`  |
| 1838   | Layout 1 | `9c75188b7f22`  |
| 1832   | Layout 1 | `9c75188b7f22`  |
| 1826   | Layout 1 | `9c75188b7f22`  |
| 1822   | Layout 1 | `9c75188b7f22`  |
| 1818   | Layout 1 | `9c75188b7f22`  |
| 1804   | Layout 1 | `9c75188b7f22`  |
| 1794   | Layout 1 | `9c75188b7f22`  |
| 1790   | Layout 1 | `9c75188b7f22`  |
| 1784   | Layout 1 | `9c75188b7f22`  |
| 1774   | Layout 1 | `9c75188b7f22`  |
| 1771   | Layout 1 | `9c75188b7f22`  |
| 1762   | Layout 1 | `9c75188b7f22`  |
| 1759   | Layout 1 | `9c75188b7f22`  |
| 1754   | Layout 1 | `9c75188b7f22`  |
| 1749   | Layout 1 | `9c75188b7f22`  |
| 1743   | Layout 1 | `9c75188b7f22`  |
| 1737   | Layout 1 | `9c75188b7f22`  |
| 1731   | Layout 1 | `9c75188b7f22`  |
| 1725   | Layout 1 | `9c75188b7f22`  |
| 1717   | Layout 1 | `9c75188b7f22`  |
| 1710   | Layout 1 | `9c75188b7f22`  |
| 1704   | Layout 1 | `9c75188b7f22`  |
| 1698   | Layout 1 | `9c75188b7f22`  |
| 1690   | Layout 1 | `9c75188b7f22`  |
| 1685   | Layout 1 | `9c75188b7f22`  |
| 1680   | Layout 1 | `9c75188b7f22`  |
| 1674   | Layout 1 | `9c75188b7f22`  |
| 1668   | Layout 1 | `9c75188b7f22`  |
| 1659   | Layout 1 | `9c75188b7f22`  |
| 1649   | Layout 1 | `9c75188b7f22`  |
| 1642   | Layout 1 | `9c75188b7f22`  |
| 1636   | Layout 1 | `9c75188b7f22`  |
| 1628   | Layout 1 | `9c75188b7f22`  |
| 1622   | Layout 1 | `9c75188b7f22`  |
| 1614   | Layout 1 | `9c75188b7f22`  |
| 1608   | Layout 1 | `9c75188b7f22`  |
| 1602   | Layout 1 | `9c75188b7f22`  |
| 1598   | Layout 1 | `9c75188b7f22`  |
| 1594   | Layout 1 | `9c75188b7f22`  |
| 1590   | Layout 1 | `9c75188b7f22`  |
| 1587   | Layout 1 | `9c75188b7f22`  |
| 1584   | Layout 1 | `9c75188b7f22`  |
| 1579   | Layout 1 | `9c75188b7f22`  |
| 1572   | Layout 1 | `9c75188b7f22`  |
| 1565   | Layout 1 | `9c75188b7f22`  |
| 1559   | Layout 1 | `9c75188b7f22`  |
| 1554   | Layout 1 | `9c75188b7f22`  |
| 1547   | Layout 1 | `9c75188b7f22`  |
| 1537   | Layout 1 | `9c75188b7f22`  |
| 1529   | Layout 1 | `9c75188b7f22`  |
| 1524   | Layout 1 | `9c75188b7f22`  |
| 1519   | Layout 1 | `9c75188b7f22`  |
| 1509   | Layout 1 | `9c75188b7f22`  |
| 1506   | Layout 1 | `9c75188b7f22`  |
| 1504   | Layout 1 | `9c75188b7f22`  |
| 1500   | Layout 1 | `9c75188b7f22`  |
| 1493   | Layout 1 | `9c75188b7f22`  |
| 1489   | Layout 1 | `9c75188b7f22`  |
| 1485   | Layout 1 | `9c75188b7f22`  |
| 1481   | Layout 1 | `9c75188b7f22`  |
| 1474   | Layout 1 | `9c75188b7f22`  |
| 1466   | Layout 1 | `9c75188b7f22`  |
| 1462   | Layout 1 | `9c75188b7f22`  |
| 1459   | Layout 1 | `9c75188b7f22`  |
| 1453   | Layout 1 | `9c75188b7f22`  |
| 1450   | Layout 1 | `9c75188b7f22`  |
| 1445   | Layout 1 | `9c75188b7f22`  |
| 1439   | Layout 1 | `9c75188b7f22`  |
| 1433   | Layout 1 | `9c75188b7f22`  |
| 1430   | Layout 1 | `9c75188b7f22`  |
| 1426   | Layout 1 | `9c75188b7f22`  |
| 1421   | Layout 1 | `9c75188b7f22`  |
| 1417   | Layout 1 | `9c75188b7f22`  |
| 1416   | Layout 1 | `9c75188b7f22`  |
| 1409   | Layout 1 | `9c75188b7f22`  |
| 1405   | Layout 1 | `9c75188b7f22`  |
| 1401   | Layout 1 | `9c75188b7f22`  |
| 1396   | Layout 1 | `9c75188b7f22`  |
| 1391   | Layout 1 | `9c75188b7f22`  |
| 1390   | Layout 1 | `9c75188b7f22`  |
| 1386   | Layout 1 | `9c75188b7f22`  |
| 1381   | Layout 1 | `9c75188b7f22`  |
| 1379   | Layout 1 | `9c75188b7f22`  |
| 1372   | Layout 1 | `9c75188b7f22`  |
| 1366   | Layout 1 | `9c75188b7f22`  |
| 1364   | Layout 1 | `9c75188b7f22`  |
| 1363   | Layout 1 | `9c75188b7f22`  |
| 1360   | Layout 1 | `9c75188b7f22`  |
| 1358   | Layout 1 | `9c75188b7f22`  |
| 1355   | Layout 1 | `9c75188b7f22`  |
| 1351   | Layout 1 | `9c75188b7f22`  |
| 1348   | Layout 1 | `9c75188b7f22`  |
| 1346   | Layout 1 | `9c75188b7f22`  |
| 1341   | Layout 1 | `9c75188b7f22`  |
| 1340   | Layout 1 | `9c75188b7f22`  |
| 1338   | Layout 1 | `9c75188b7f22`  |
| 1335   | Layout 1 | `9c75188b7f22`  |
| 1333   | Layout 1 | `9c75188b7f22`  |
| 1329   | No file  | `9c75188b7f22`  |
| 1327   | No file  | `9c75188b7f22`  |
| 1324   | No file  | `9c75188b7f22`  |
| 1321   | No file  | `9c75188b7f22`  |
| 1319   | No file  | `9c75188b7f22`  |
| 1318   | No file  | `9c75188b7f22`  |
| 1316   | No file  | `9c75188b7f22`  |
| 1313   | No file  | `9c75188b7f22`  |
| 1311   | No file  | `9c75188b7f22`  |
| 1309   | No file  | `9c75188b7f22`  |
| 1304   | No file  | `9c75188b7f22`  |
| 1292   | No file  | `9c75188b7f22`  |
| 1286   | No file  | `9c75188b7f22`  |
| 1280   | No file  | `9c75188b7f22`  |
| 1276   | No file  | `9c75188b7f22`  |
| 1267   | No file  | `9c75188b7f22`  |
| 1261   | No file  | `9c75188b7f22`  |
| 1256   | No file  | `9c75188b7f22`  |
| 1250   | No file  | `9c75188b7f22`  |
| 1246   | No file  | `9c75188b7f22`  |
| 1239   | No file  | `9c75188b7f22`  |
| 1230   | No file  | `9c75188b7f22`  |
| 1226   | No file  | `9c75188b7f22`  |
| 1220   | No file  | `9c75188b7f22`  |
| 1217   | No file  | `9c75188b7f22`  |
| 1211   | No file  | `9c75188b7f22`  |
| 1210   | No file  | `9c75188b7f22`  |
| 1208   | No file  | `9c75188b7f22`  |
| 1203   | No file  | `9c75188b7f22`  |
| 1197   | No file  | `9c75188b7f22`  |
| 1194   | No file  | `9c75188b7f22`  |
| 1192   | No file  | `9c75188b7f22`  |
| 1187   | No file  | `9c75188b7f22`  |
| 1183   | No file  | `9c75188b7f22`  |
| 1177   | No file  | `9c75188b7f22`  |
| 1173   | No file  | `9c75188b7f22`  |
| 1167   | No file  | `9c75188b7f22`  |
| 1164   | No file  | `9c75188b7f22`  |
| 1156   | No file  | `9c75188b7f22`  |
| 1149   | No file  | `9c75188b7f22`  |
| 1144   | No file  | `9c75188b7f22`  |
| 1137   | No file  | `9c75188b7f22`  |
| 1132   | No file  | `9c75188b7f22`  |
| 1127   | No file  | `9c75188b7f22`  |
| 1122   | No file  | `9c75188b7f22`  |
| 1118   | No file  | `9c75188b7f22`  |
| 1114   | No file  | `9c75188b7f22`  |
| 1109   | No file  | `9c75188b7f22`  |
| 1102   | No file  | `9c75188b7f22`  |
| 1096   | No file  | `9c75188b7f22`  |
| 1088   | No file  | `9c75188b7f22`  |
| 1081   | No file  | `9c75188b7f22`  |
| 1076   | No file  | `9c75188b7f22`  |
| 1069   | No file  | `9c75188b7f22`  |
| 1064   | No file  | `9c75188b7f22`  |
| 1058   | No file  | `9c75188b7f22`  |
| 1051   | No file  | `9c75188b7f22`  |
| 1044   | No file  | `9c75188b7f22`  |
| 1036   | No file  | `9c75188b7f22`  |
| 1026   | No file  | `9c75188b7f22`  |
| 1016   | No file  | `9c75188b7f22`  |
| 1009   | No file  | `9c75188b7f22`  |
| 1005   | No file  | `9c75188b7f22`  |
| 1000   | No file  | `9c75188b7f22`  |
| 998    | No file  | `9c75188b7f22`  |
| 990    | No file  | `9c75188b7f22`  |
| 979    | No file  | `9c75188b7f22`  |
| 972    | No file  | `9c75188b7f22`  |
| 963    | No file  | `9c75188b7f22`  |
| 955    | No file  | `9c75188b7f22`  |
| 946    | No file  | `9c75188b7f22`  |
| 938    | No file  | `9c75188b7f22`  |
| 927    | No file  | `9c75188b7f22`  |
| 911    | No file  | `9c75188b7f22`  |
| 904    | No file  | `9c75188b7f22`  |
| 899    | No file  | `9c75188b7f22`  |
| 894    | No file  | `9c75188b7f22`  |
| 885    | No file  | `9c75188b7f22`  |
| 879    | No file  | `9c75188b7f22`  |
| 872    | No file  | `9c75188b7f22`  |
| 864    | No file  | `9c75188b7f22`  |
| 855    | No file  | `9c75188b7f22`  |
| 853    | No file  | `9c75188b7f22`  |
| 845    | No file  | `9c75188b7f22`  |
| 837    | No file  | `9c75188b7f22`  |
| 829    | No file  | `9c75188b7f22`  |
| 822    | No file  | `9c75188b7f22`  |
| 814    | No file  | `9c75188b7f22`  |
| 805    | No file  | `9c75188b7f22`  |
| 794    | No file  | `9c75188b7f22`  |
| 787    | No file  | `9c75188b7f22`  |
| 780    | No file  | `9c75188b7f22`  |
| 771    | No file  | `9c75188b7f22`  |
| 760    | No file  | `9c75188b7f22`  |
| 748    | No file  | `9c75188b7f22`  |
| 741    | No file  | `9c75188b7f22`  |
| 736    | No file  | `9c75188b7f22`  |
| 731    | No file  | `9c75188b7f22`  |
| 723    | No file  | `9c75188b7f22`  |
| 711    | No file  | `9c75188b7f22`  |
| 707    | No file  | `9c75188b7f22`  |
| 697    | No file  | `9c75188b7f22`  |
| 689    | No file  | `9c75188b7f22`  |
| 683    | No file  | `9c75188b7f22`  |
| 678    | No file  | `9c75188b7f22`  |
| 670    | No file  | `9c75188b7f22`  |
| 661    | No file  | `9c75188b7f22`  |
| 656    | No file  | `9c75188b7f22`  |
| 652    | No file  | `9c75188b7f22`  |
| 643    | No file  | `9c75188b7f22`  |
| 637    | No file  | `9c75188b7f22`  |
| 630    | No file  | `9c75188b7f22`  |
| 627    | No file  | `9c75188b7f22`  |
| 621    | No file  | `9c75188b7f22`  |
| 617    | No file  | `9c75188b7f22`  |
| 615    | No file  | `9c75188b7f22`  |
| 606    | No file  | `9c75188b7f22`  |
| 599    | No file  | `9c75188b7f22`  |
| 592    | No file  | `9c75188b7f22`  |
| 586    | No file  | `9c75188b7f22`  |
| 577    | No file  | `9c75188b7f22`  |
| 569    | No file  | `9c75188b7f22`  |
| 561    | No file  | `9c75188b7f22`  |
| 554    | No file  | `9c75188b7f22`  |
| 542    | No file  | `9c75188b7f22`  |
| 532    | No file  | `9c75188b7f22`  |
| 531    | No file  | `9c75188b7f22`  |
| 526    | No file  | `9c75188b7f22`  |
| 521    | No file  | `9c75188b7f22`  |
| 517    | No file  | `9c75188b7f22`  |
| 510    | No file  | `9c75188b7f22`  |
| 508    | No file  | `9c75188b7f22`  |
| 504    | No file  | `9c75188b7f22`  |
| 497    | No file  | `9c75188b7f22`  |
| 491    | No file  | `9c75188b7f22`  |
| 485    | No file  | `9c75188b7f22`  |
| 478    | No file  | `9c75188b7f22`  |
| 472    | No file  | `9c75188b7f22`  |
| 466    | No file  | `9c75188b7f22`  |
| 457    | No file  | `9c75188b7f22`  |
| 452    | No file  | `9c75188b7f22`  |
| 449    | No file  | `9c75188b7f22`  |
| 435    | No file  | `9c75188b7f22`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                |
| --------------------- | -------- | ------------------- |
| `languagedata_en.loc` | Optional | Item names (type 0) |

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

### Row (9 bytes)

| Offset  | Type | Field             | Notes                                                                        |
| ------- | ---- | ----------------- | ---------------------------------------------------------------------------- |
| `+0x00` | u32  | item_key          | The furniture item (LOC type 0 name); unique per row                         |
| `+0x04` | u32  | item_key_dup      | Equal to `item_key` on every row (clients 1784 and 3482)                     |
| `+0x08` | u8   | installation_type | `CppEnums.InstallationType` of the placed object; see Installation Types     |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                           |
| ------- | ------------------ | ------------ | ----------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on clients 1784 and 3482 |
| `+0x04` | pstr[string_count] | strings      | Empty                                           |

## Installation Types

`CppEnums.InstallationType` in `global_define_cpp_enum.luac` (client
3482) names the values. Rows per value are from client 3482. For `9` and
up the items match the enum name; for `1` to `8` (except `4`) they are
pieces of furniture the enum names do not describe, in the order of the
`interiorrelationpoint.dbss` relation columns.

| Value | Enum name     | Rows | Items                                                     |
| ----- | ------------- | ---- | --------------------------------------------------------- |
| 0     | Default       | 92   | [Manor] decorations                                        |
| 1     | Carpenter     | 31   | Dressers (`서랍장`)                                        |
| 2     | Alchemy1      | 29   | Bedside cabinets (`협탁`)                                  |
| 3     | Founding      | 33   | Wardrobes (`옷장`)                                         |
| 4     | Cooking       | 2    | Advanced and Supreme Cooking Utensil                       |
| 5     | Forging       | 31   | Dining tables (`식탁`)                                     |
| 6     | Treasure      | 34   | Tables (`탁자`)                                            |
| 7     | Smithing      | 33   | Chairs                                                     |
| 8     | Weaving       | 33   | Sofas                                                      |
| 9     | Bed           | 32   | Beds                                                       |
| 10    | Havest        | 2    | Cherry Blossom Seed and its [Event] copy                   |
| 17    | Buff          | 3    | [Event] 3rd Anniversary Cake, Halloween Jack-O'-Lantern, Halloween Pumpkin Doll Lamp |
| 19    | Bookcase      | 31   | Bookcases and desks                                        |
| 20    | WarehouseBox  | 1    | Premium Container                                          |
| 21    | Alchemy       | 2    | Advanced and Supreme Alchemy Tool                          |
| 22    | JukeBox       | 15   | Jukebox records                                            |
| 24    | WallPaper     | 49   | Wallpapers                                                 |
| 25    | FloorMaterial | 43   | Floor coverings                                            |
| 26    | Chandelier    | 10   | Chandeliers                                                |
| 27    | Curtain       | 4    | Curtains                                                   |
| 30    | Maid          | 2    | Maid contracts                                             |
| 31    | Curtain_Tied  | 4    | Tied curtains                                              |
| 34    | InstanceWater | 3    | Margoria Whale Hexagonal Fish Tank, L'elisir d'amore Aquarium Table and Hot Tub |
| 35    | Shelf         | 1    | L'elisir d'amore Wall Shelf                                |

## Notes

- 313 of the 520 items of client 3482 place an object that has a row in
  [`interiorrelationpoint.dbss`](../dbss/interiorrelationpoint_dbss.md); every
  item of types `2`, `5`, `7`, `8` and `9` does. 17 of the 92
  type `0` items place an object listed in
  [`mansiondata.dbss`](../dbss/mansiondata_dbss.md). Both tables are keyed by the
  object's character key, not by the item, so the link runs through
  `characterobject.dbss`.
- The `interiorrelationpoint.dbss` relation columns `on_dresser` to
  `on_bed`, `on_book_case` and `on_shelf` are the furniture of types `1`,
  `2`, `3`, `5` to `9`, `19` and `35` in that order.
- Client 1784 has 489 rows with the same layout; it has no type `4`, `20`
  or `21` row.

## Open Questions

### Types 1 to 8

The dressers, bedside cabinets, wardrobes, dining tables, tables, chairs
and sofas carry the `InstallationType` values `1`, `2`, `3` and `5` to `8`,
which the Lua enum names Carpenter, Alchemy1, Founding, Forging, Treasure,
Smithing and Weaving. Whether the client reads these values as furniture
kinds for this table (the `interiorrelationpoint.dbss` column order
suggests it) or the enum names are left over from older workshop types is
open.
