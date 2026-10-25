# `petchangelook.dbss` Format

## Purpose

The looks a pet can change to, per look key: each record holds the looks of
one `change_look_key` of [`pet.dbss`](pet_dbss.md), each look with its
action index (the look the client asks the server for), its icons, a skill
and, from client 3474 on, a Korean skin name. Fairies use the same table (look
key `25001`) for their skins. Companion `petchangelookoffset.dbss` lists
where every record's payload sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                       | Bytes  | Records                           | Row bytes                 |
| ------ | -------------- | -------------------------- | ------ | --------------------------------- | ------------------------- |
| 2      | 3458 and later | `petchangelook.dbss`       | 70,196 | 653 Look, 149 Payload, 149 Record | 99 to 211, 106 on average |
| 2      | 3458 and later | `petchangelookoffset.dbss` | 1,494  | 149 Offset Row                    | 10                        |
| 1      | 1433 to 3412   | `petchangelook.dbss`       | 61,219 | 651 Look, 149 Payload, 149 Record | 86 to 184, 92 on average  |
| 1      | 1433 to 3412   | `petchangelookoffset.dbss` | 1,494  | 149 Offset Row                    | 10                        |

| Layout | File                       | Known             | Unknown        |
| ------ | -------------------------- | ----------------- | -------------- |
| 2      | `petchangelook.dbss`       | 66,931 B (95.3%)  | 3,265 B (4.7%) |
| 2      | `petchangelookoffset.dbss` | 1,494 B (100.0%)  | 0 B (0.0%)     |
| 1      | `petchangelook.dbss`       | 61,219 B (100.0%) | 0 B (0.0%)     |
| 1      | `petchangelookoffset.dbss` | 1,494 B (100.0%)  | 0 B (0.0%)     |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `8cf4f085de92`  |
| 3482   | Layout 2             | `8cf4f085de92`  |
| 3474   | Layout 2             | `8cf4f085de92`  |
| 3473   | Layout 2             | `8cf4f085de92`  |
| 3464   | Layout 2             | `8cf4f085de92`  |
| 3458   | Layout 2             | `8cf4f085de92`  |
| 3454   | No documented layout | `8cf4f085de92`  |
| 3444   | No documented layout | `8cf4f085de92`  |
| 3435   | No documented layout | `8cf4f085de92`  |
| 3426   | No documented layout | `8cf4f085de92`  |
| 3418   | No documented layout | `8cf4f085de92`  |
| 3412   | Layout 1             | `8cf4f085de92`  |
| 3402   | Layout 1             | `8cf4f085de92`  |
| 3396   | Layout 1             | `8cf4f085de92`  |
| 3387   | Layout 1             | `8cf4f085de92`  |
| 3381   | Layout 1             | `8cf4f085de92`  |
| 3373   | Layout 1             | `8cf4f085de92`  |
| 3364   | Layout 1             | `8cf4f085de92`  |
| 3356   | Layout 1             | `8cf4f085de92`  |
| 3349   | Layout 1             | `8cf4f085de92`  |
| 3342   | Layout 1             | `8cf4f085de92`  |
| 3335   | Layout 1             | `8cf4f085de92`  |
| 3326   | Layout 1             | `8cf4f085de92`  |
| 3321   | Layout 1             | `8cf4f085de92`  |
| 3314   | Layout 1             | `8cf4f085de92`  |
| 3303   | Layout 1             | `8cf4f085de92`  |
| 3302   | Layout 1             | `8cf4f085de92`  |
| 3293   | Layout 1             | `8cf4f085de92`  |
| 3283   | Layout 1             | `8cf4f085de92`  |
| 3275   | Layout 1             | `8cf4f085de92`  |
| 3267   | Layout 1             | `8cf4f085de92`  |
| 3258   | Layout 1             | `8cf4f085de92`  |
| 3251   | Layout 1             | `8cf4f085de92`  |
| 3242   | Layout 1             | `8cf4f085de92`  |
| 3235   | Layout 1             | `8cf4f085de92`  |
| 3229   | Layout 1             | `8cf4f085de92`  |
| 3212   | Layout 1             | `8cf4f085de92`  |
| 3203   | Layout 1             | `8cf4f085de92`  |
| 3193   | Layout 1             | `8cf4f085de92`  |
| 3186   | Layout 1             | `8cf4f085de92`  |
| 3177   | Layout 1             | `8cf4f085de92`  |
| 3169   | Layout 1             | `8cf4f085de92`  |
| 3158   | Layout 1             | `8cf4f085de92`  |
| 3151   | Layout 1             | `8cf4f085de92`  |
| 3144   | Layout 1             | `8cf4f085de92`  |
| 3133   | Layout 1             | `8cf4f085de92`  |
| 3125   | Layout 1             | `8cf4f085de92`  |
| 3118   | Layout 1             | `8cf4f085de92`  |
| 3111   | Layout 1             | `8cf4f085de92`  |
| 3103   | Layout 1             | `8cf4f085de92`  |
| 3095   | Layout 1             | `8cf4f085de92`  |
| 3086   | Layout 1             | `8cf4f085de92`  |
| 3072   | Layout 1             | `8cf4f085de92`  |
| 3062   | Layout 1             | `8cf4f085de92`  |
| 3052   | Layout 1             | `8cf4f085de92`  |
| 3045   | Layout 1             | `8cf4f085de92`  |
| 3037   | Layout 1             | `8cf4f085de92`  |
| 3030   | Layout 1             | `8cf4f085de92`  |
| 3021   | Layout 1             | `8cf4f085de92`  |
| 3012   | Layout 1             | `8cf4f085de92`  |
| 3002   | Layout 1             | `8cf4f085de92`  |
| 2995   | Layout 1             | `8cf4f085de92`  |
| 2987   | Layout 1             | `8cf4f085de92`  |
| 2978   | Layout 1             | `8cf4f085de92`  |
| 2970   | Layout 1             | `8cf4f085de92`  |
| 2959   | Layout 1             | `8cf4f085de92`  |
| 2951   | Layout 1             | `8cf4f085de92`  |
| 2942   | Layout 1             | `8cf4f085de92`  |
| 2935   | Layout 1             | `8cf4f085de92`  |
| 2932   | Layout 1             | `8cf4f085de92`  |
| 2923   | Layout 1             | `8cf4f085de92`  |
| 2919   | Layout 1             | `8cf4f085de92`  |
| 2907   | Layout 1             | `8cf4f085de92`  |
| 2900   | Layout 1             | `8cf4f085de92`  |
| 2891   | Layout 1             | `8cf4f085de92`  |
| 2882   | Layout 1             | `8cf4f085de92`  |
| 2872   | Layout 1             | `8cf4f085de92`  |
| 2863   | Layout 1             | `8cf4f085de92`  |
| 2855   | Layout 1             | `8cf4f085de92`  |
| 2849   | Layout 1             | `8cf4f085de92`  |
| 2844   | Layout 1             | `8cf4f085de92`  |
| 2834   | Layout 1             | `8cf4f085de92`  |
| 2825   | Layout 1             | `8cf4f085de92`  |
| 2819   | Layout 1             | `8cf4f085de92`  |
| 2811   | Layout 1             | `8cf4f085de92`  |
| 2803   | Layout 1             | `8cf4f085de92`  |
| 2794   | Layout 1             | `8cf4f085de92`  |
| 2783   | Layout 1             | `8cf4f085de92`  |
| 2774   | Layout 1             | `8cf4f085de92`  |
| 2765   | Layout 1             | `8cf4f085de92`  |
| 2756   | Layout 1             | `8cf4f085de92`  |
| 2750   | Layout 1             | `8cf4f085de92`  |
| 2743   | Layout 1             | `8cf4f085de92`  |
| 2736   | Layout 1             | `8cf4f085de92`  |
| 2726   | Layout 1             | `8cf4f085de92`  |
| 2717   | Layout 1             | `8cf4f085de92`  |
| 2709   | Layout 1             | `8cf4f085de92`  |
| 2703   | Layout 1             | `8cf4f085de92`  |
| 2695   | Layout 1             | `8cf4f085de92`  |
| 2684   | Layout 1             | `8cf4f085de92`  |
| 2672   | Layout 1             | `8cf4f085de92`  |
| 2665   | Layout 1             | `8cf4f085de92`  |
| 2657   | Layout 1             | `8cf4f085de92`  |
| 2649   | Layout 1             | `8cf4f085de92`  |
| 2644   | Layout 1             | `8cf4f085de92`  |
| 2637   | Layout 1             | `8cf4f085de92`  |
| 2629   | Layout 1             | `8cf4f085de92`  |
| 2619   | Layout 1             | `8cf4f085de92`  |
| 2612   | Layout 1             | `8cf4f085de92`  |
| 2606   | Layout 1             | `8cf4f085de92`  |
| 2602   | Layout 1             | `8cf4f085de92`  |
| 2601   | Layout 1             | `8cf4f085de92`  |
| 2592   | Layout 1             | `8cf4f085de92`  |
| 2583   | Layout 1             | `8cf4f085de92`  |
| 2575   | Layout 1             | `8cf4f085de92`  |
| 2567   | Layout 1             | `8cf4f085de92`  |
| 2560   | Layout 1             | `8cf4f085de92`  |
| 2553   | Layout 1             | `8cf4f085de92`  |
| 2545   | Layout 1             | `8cf4f085de92`  |
| 2538   | Layout 1             | `8cf4f085de92`  |
| 2529   | Layout 1             | `8cf4f085de92`  |
| 2519   | Layout 1             | `8cf4f085de92`  |
| 2513   | Layout 1             | `8cf4f085de92`  |
| 2510   | Layout 1             | `8cf4f085de92`  |
| 2507   | Layout 1             | `8cf4f085de92`  |
| 2503   | Layout 1             | `8cf4f085de92`  |
| 2498   | Layout 1             | `8cf4f085de92`  |
| 2492   | Layout 1             | `8cf4f085de92`  |
| 2487   | Layout 1             | `8cf4f085de92`  |
| 2480   | Layout 1             | `8cf4f085de92`  |
| 2474   | Layout 1             | `8cf4f085de92`  |
| 2468   | Layout 1             | `8cf4f085de92`  |
| 2460   | Layout 1             | `8cf4f085de92`  |
| 2453   | Layout 1             | `8cf4f085de92`  |
| 2444   | Layout 1             | `8cf4f085de92`  |
| 2438   | Layout 1             | `8cf4f085de92`  |
| 2434   | Layout 1             | `8cf4f085de92`  |
| 2429   | Layout 1             | `8cf4f085de92`  |
| 2421   | Layout 1             | `8cf4f085de92`  |
| 2414   | Layout 1             | `8cf4f085de92`  |
| 2407   | Layout 1             | `8cf4f085de92`  |
| 2401   | Layout 1             | `8cf4f085de92`  |
| 2397   | Layout 1             | `8cf4f085de92`  |
| 2393   | Layout 1             | `8cf4f085de92`  |
| 2384   | Layout 1             | `8cf4f085de92`  |
| 2378   | Layout 1             | `8cf4f085de92`  |
| 2372   | Layout 1             | `8cf4f085de92`  |
| 2358   | Layout 1             | `8cf4f085de92`  |
| 2352   | Layout 1             | `8cf4f085de92`  |
| 2347   | Layout 1             | `8cf4f085de92`  |
| 2343   | Layout 1             | `8cf4f085de92`  |
| 2335   | Layout 1             | `8cf4f085de92`  |
| 2327   | Layout 1             | `8cf4f085de92`  |
| 2324   | Layout 1             | `8cf4f085de92`  |
| 2319   | Layout 1             | `8cf4f085de92`  |
| 2313   | Layout 1             | `8cf4f085de92`  |
| 2308   | Layout 1             | `8cf4f085de92`  |
| 2302   | Layout 1             | `8cf4f085de92`  |
| 2295   | Layout 1             | `8cf4f085de92`  |
| 2290   | Layout 1             | `8cf4f085de92`  |
| 2284   | Layout 1             | `8cf4f085de92`  |
| 2276   | Layout 1             | `8cf4f085de92`  |
| 2269   | Layout 1             | `8cf4f085de92`  |
| 2259   | Layout 1             | `8cf4f085de92`  |
| 2250   | Layout 1             | `8cf4f085de92`  |
| 2243   | Layout 1             | `8cf4f085de92`  |
| 2235   | Layout 1             | `8cf4f085de92`  |
| 2229   | Layout 1             | `8cf4f085de92`  |
| 2224   | Layout 1             | `8cf4f085de92`  |
| 2218   | Layout 1             | `8cf4f085de92`  |
| 2215   | Layout 1             | `8cf4f085de92`  |
| 2207   | Layout 1             | `8cf4f085de92`  |
| 2203   | Layout 1             | `8cf4f085de92`  |
| 2196   | Layout 1             | `8cf4f085de92`  |
| 2192   | Layout 1             | `8cf4f085de92`  |
| 2189   | Layout 1             | `8cf4f085de92`  |
| 2183   | Layout 1             | `8cf4f085de92`  |
| 2179   | Layout 1             | `8cf4f085de92`  |
| 2171   | Layout 1             | `8cf4f085de92`  |
| 2163   | Layout 1             | `8cf4f085de92`  |
| 2156   | Layout 1             | `8cf4f085de92`  |
| 2151   | Layout 1             | `8cf4f085de92`  |
| 2147   | Layout 1             | `8cf4f085de92`  |
| 2142   | Layout 1             | `8cf4f085de92`  |
| 2138   | Layout 1             | `8cf4f085de92`  |
| 2134   | Layout 1             | `8cf4f085de92`  |
| 2130   | Layout 1             | `8cf4f085de92`  |
| 2122   | Layout 1             | `8cf4f085de92`  |
| 2107   | Layout 1             | `8cf4f085de92`  |
| 2098   | Layout 1             | `8cf4f085de92`  |
| 2089   | Layout 1             | `8cf4f085de92`  |
| 2081   | Layout 1             | `8cf4f085de92`  |
| 2073   | Layout 1             | `8cf4f085de92`  |
| 2067   | Layout 1             | `8cf4f085de92`  |
| 2063   | Layout 1             | `8cf4f085de92`  |
| 2059   | Layout 1             | `8cf4f085de92`  |
| 2052   | Layout 1             | `8cf4f085de92`  |
| 2044   | Layout 1             | `8cf4f085de92`  |
| 2039   | Layout 1             | `8cf4f085de92`  |
| 2032   | Layout 1             | `8cf4f085de92`  |
| 2025   | Layout 1             | `8cf4f085de92`  |
| 2011   | Layout 1             | `8cf4f085de92`  |
| 2005   | Layout 1             | `8cf4f085de92`  |
| 2000   | Layout 1             | `8cf4f085de92`  |
| 1996   | Layout 1             | `8cf4f085de92`  |
| 1991   | Layout 1             | `8cf4f085de92`  |
| 1985   | Layout 1             | `8cf4f085de92`  |
| 1980   | Layout 1             | `8cf4f085de92`  |
| 1969   | Layout 1             | `8cf4f085de92`  |
| 1964   | Layout 1             | `8cf4f085de92`  |
| 1958   | Layout 1             | `8cf4f085de92`  |
| 1950   | Layout 1             | `8cf4f085de92`  |
| 1945   | Layout 1             | `8cf4f085de92`  |
| 1937   | Layout 1             | `8cf4f085de92`  |
| 1933   | Layout 1             | `8cf4f085de92`  |
| 1927   | Layout 1             | `8cf4f085de92`  |
| 1921   | Layout 1             | `8cf4f085de92`  |
| 1914   | Layout 1             | `8cf4f085de92`  |
| 1908   | Layout 1             | `8cf4f085de92`  |
| 1897   | Layout 1             | `8cf4f085de92`  |
| 1892   | Layout 1             | `8cf4f085de92`  |
| 1886   | Layout 1             | `8cf4f085de92`  |
| 1881   | Layout 1             | `8cf4f085de92`  |
| 1871   | Layout 1             | `8cf4f085de92`  |
| 1866   | Layout 1             | `8cf4f085de92`  |
| 1862   | Layout 1             | `8cf4f085de92`  |
| 1854   | Layout 1             | `8cf4f085de92`  |
| 1846   | Layout 1             | `8cf4f085de92`  |
| 1838   | Layout 1             | `8cf4f085de92`  |
| 1832   | Layout 1             | `8cf4f085de92`  |
| 1826   | Layout 1             | `8cf4f085de92`  |
| 1822   | Layout 1             | `8cf4f085de92`  |
| 1818   | Layout 1             | `8cf4f085de92`  |
| 1804   | Layout 1             | `8cf4f085de92`  |
| 1794   | Layout 1             | `8cf4f085de92`  |
| 1790   | Layout 1             | `8cf4f085de92`  |
| 1784   | Layout 1             | `8cf4f085de92`  |
| 1774   | Layout 1             | `8cf4f085de92`  |
| 1771   | Layout 1             | `8cf4f085de92`  |
| 1762   | Layout 1             | `8cf4f085de92`  |
| 1759   | Layout 1             | `8cf4f085de92`  |
| 1754   | Layout 1             | `8cf4f085de92`  |
| 1749   | Layout 1             | `8cf4f085de92`  |
| 1743   | Layout 1             | `8cf4f085de92`  |
| 1737   | Layout 1             | `8cf4f085de92`  |
| 1731   | Layout 1             | `8cf4f085de92`  |
| 1725   | Layout 1             | `8cf4f085de92`  |
| 1717   | Layout 1             | `8cf4f085de92`  |
| 1710   | Layout 1             | `8cf4f085de92`  |
| 1704   | Layout 1             | `8cf4f085de92`  |
| 1698   | Layout 1             | `8cf4f085de92`  |
| 1690   | Layout 1             | `8cf4f085de92`  |
| 1685   | Layout 1             | `8cf4f085de92`  |
| 1680   | Layout 1             | `8cf4f085de92`  |
| 1674   | Layout 1             | `8cf4f085de92`  |
| 1668   | Layout 1             | `8cf4f085de92`  |
| 1659   | Layout 1             | `8cf4f085de92`  |
| 1649   | Layout 1             | `8cf4f085de92`  |
| 1642   | Layout 1             | `8cf4f085de92`  |
| 1636   | Layout 1             | `8cf4f085de92`  |
| 1628   | Layout 1             | `8cf4f085de92`  |
| 1622   | Layout 1             | `8cf4f085de92`  |
| 1614   | Layout 1             | `8cf4f085de92`  |
| 1608   | Layout 1             | `8cf4f085de92`  |
| 1602   | Layout 1             | `8cf4f085de92`  |
| 1598   | Layout 1             | `8cf4f085de92`  |
| 1594   | Layout 1             | `8cf4f085de92`  |
| 1590   | Layout 1             | `8cf4f085de92`  |
| 1587   | Layout 1             | `8cf4f085de92`  |
| 1584   | Layout 1             | `8cf4f085de92`  |
| 1579   | Layout 1             | `8cf4f085de92`  |
| 1572   | Layout 1             | `8cf4f085de92`  |
| 1565   | Layout 1             | `8cf4f085de92`  |
| 1559   | Layout 1             | `8cf4f085de92`  |
| 1554   | Layout 1             | `8cf4f085de92`  |
| 1547   | Layout 1             | `8cf4f085de92`  |
| 1537   | Layout 1             | `8cf4f085de92`  |
| 1529   | Layout 1             | `8cf4f085de92`  |
| 1524   | Layout 1             | `8cf4f085de92`  |
| 1519   | Layout 1             | `8cf4f085de92`  |
| 1509   | Layout 1             | `8cf4f085de92`  |
| 1506   | Layout 1             | `8cf4f085de92`  |
| 1504   | Layout 1             | `8cf4f085de92`  |
| 1500   | Layout 1             | `8cf4f085de92`  |
| 1493   | Layout 1             | `8cf4f085de92`  |
| 1489   | Layout 1             | `8cf4f085de92`  |
| 1485   | Layout 1             | `8cf4f085de92`  |
| 1481   | Layout 1             | `8cf4f085de92`  |
| 1474   | Layout 1             | `8cf4f085de92`  |
| 1466   | Layout 1             | `8cf4f085de92`  |
| 1462   | Layout 1             | `8cf4f085de92`  |
| 1459   | Layout 1             | `8cf4f085de92`  |
| 1453   | Layout 1             | `8cf4f085de92`  |
| 1450   | Layout 1             | `8cf4f085de92`  |
| 1445   | Layout 1             | `8cf4f085de92`  |
| 1439   | Layout 1             | `8cf4f085de92`  |
| 1433   | Layout 1             | `8cf4f085de92`  |
| 1430   | No documented layout | `8cf4f085de92`  |
| 1426   | No documented layout | `8cf4f085de92`  |
| 1421   | No documented layout | `8cf4f085de92`  |
| 1417   | No documented layout | `8cf4f085de92`  |
| 1416   | No documented layout | `8cf4f085de92`  |
| 1409   | No documented layout | `8cf4f085de92`  |
| 1405   | No documented layout | `8cf4f085de92`  |
| 1401   | No documented layout | `8cf4f085de92`  |
| 1396   | No documented layout | `8cf4f085de92`  |
| 1391   | No documented layout | `8cf4f085de92`  |
| 1390   | No documented layout | `8cf4f085de92`  |
| 1386   | No documented layout | `8cf4f085de92`  |
| 1381   | No documented layout | `8cf4f085de92`  |
| 1379   | No documented layout | `8cf4f085de92`  |
| 1372   | No documented layout | `8cf4f085de92`  |
| 1366   | No documented layout | `8cf4f085de92`  |
| 1364   | No documented layout | `8cf4f085de92`  |
| 1363   | No documented layout | `8cf4f085de92`  |
| 1360   | No documented layout | `8cf4f085de92`  |
| 1358   | No documented layout | `8cf4f085de92`  |
| 1355   | No documented layout | `8cf4f085de92`  |
| 1351   | No documented layout | `8cf4f085de92`  |
| 1348   | No documented layout | `8cf4f085de92`  |
| 1346   | No documented layout | `8cf4f085de92`  |
| 1341   | No documented layout | `8cf4f085de92`  |
| 1340   | No documented layout | `8cf4f085de92`  |
| 1338   | No documented layout | `8cf4f085de92`  |
| 1335   | No documented layout | `8cf4f085de92`  |
| 1333   | No documented layout | `8cf4f085de92`  |
| 1329   | No documented layout | `8cf4f085de92`  |
| 1327   | No documented layout | `8cf4f085de92`  |
| 1324   | No documented layout | `8cf4f085de92`  |
| 1321   | No documented layout | `8cf4f085de92`  |
| 1319   | No documented layout | `8cf4f085de92`  |
| 1318   | No documented layout | `8cf4f085de92`  |
| 1316   | No documented layout | `8cf4f085de92`  |
| 1313   | No documented layout | `8cf4f085de92`  |
| 1311   | No documented layout | `8cf4f085de92`  |
| 1309   | No documented layout | `8cf4f085de92`  |
| 1304   | No documented layout | `8cf4f085de92`  |
| 1292   | No documented layout | `8cf4f085de92`  |
| 1286   | No documented layout | `8cf4f085de92`  |
| 1280   | No file              | `8cf4f085de92`  |
| 1276   | No file              | `8cf4f085de92`  |
| 1267   | No documented layout | `8cf4f085de92`  |
| 1261   | No documented layout | `8cf4f085de92`  |
| 1256   | No file              | `8cf4f085de92`  |
| 1250   | No file              | `8cf4f085de92`  |
| 1246   | No file              | `8cf4f085de92`  |
| 1239   | No file              | `8cf4f085de92`  |
| 1230   | No file              | `8cf4f085de92`  |
| 1226   | No file              | `8cf4f085de92`  |
| 1220   | No file              | `8cf4f085de92`  |
| 1217   | No file              | `8cf4f085de92`  |
| 1211   | No file              | `8cf4f085de92`  |
| 1210   | No file              | `8cf4f085de92`  |
| 1208   | No file              | `8cf4f085de92`  |
| 1203   | No file              | `8cf4f085de92`  |
| 1197   | No file              | `8cf4f085de92`  |
| 1194   | No file              | `8cf4f085de92`  |
| 1192   | No file              | `8cf4f085de92`  |
| 1187   | No file              | `8cf4f085de92`  |
| 1183   | No file              | `8cf4f085de92`  |
| 1177   | No file              | `8cf4f085de92`  |
| 1173   | No file              | `8cf4f085de92`  |
| 1167   | No file              | `8cf4f085de92`  |
| 1164   | No file              | `8cf4f085de92`  |
| 1156   | No file              | `8cf4f085de92`  |
| 1149   | No file              | `8cf4f085de92`  |
| 1144   | No file              | `8cf4f085de92`  |
| 1137   | No file              | `8cf4f085de92`  |
| 1132   | No file              | `8cf4f085de92`  |
| 1127   | No file              | `8cf4f085de92`  |
| 1122   | No file              | `8cf4f085de92`  |
| 1118   | No file              | `8cf4f085de92`  |
| 1114   | No file              | `8cf4f085de92`  |
| 1109   | No file              | `8cf4f085de92`  |
| 1102   | No file              | `8cf4f085de92`  |
| 1096   | No file              | `8cf4f085de92`  |
| 1088   | No file              | `8cf4f085de92`  |
| 1081   | No file              | `8cf4f085de92`  |
| 1076   | No file              | `8cf4f085de92`  |
| 1069   | No file              | `8cf4f085de92`  |
| 1064   | No file              | `8cf4f085de92`  |
| 1058   | No file              | `8cf4f085de92`  |
| 1051   | No file              | `8cf4f085de92`  |
| 1044   | No file              | `8cf4f085de92`  |
| 1036   | No file              | `8cf4f085de92`  |
| 1026   | No file              | `8cf4f085de92`  |
| 1016   | No file              | `8cf4f085de92`  |
| 1009   | No file              | `8cf4f085de92`  |
| 1005   | No file              | `8cf4f085de92`  |
| 1000   | No file              | `8cf4f085de92`  |
| 998    | No file              | `8cf4f085de92`  |
| 990    | No file              | `8cf4f085de92`  |
| 979    | No file              | `8cf4f085de92`  |
| 972    | No file              | `8cf4f085de92`  |
| 963    | No file              | `8cf4f085de92`  |
| 955    | No file              | `8cf4f085de92`  |
| 946    | No file              | `8cf4f085de92`  |
| 938    | No file              | `8cf4f085de92`  |
| 927    | No file              | `8cf4f085de92`  |
| 911    | No file              | `8cf4f085de92`  |
| 904    | No file              | `8cf4f085de92`  |
| 899    | No file              | `8cf4f085de92`  |
| 894    | No file              | `8cf4f085de92`  |
| 885    | No file              | `8cf4f085de92`  |
| 879    | No file              | `8cf4f085de92`  |
| 872    | No file              | `8cf4f085de92`  |
| 864    | No file              | `8cf4f085de92`  |
| 855    | No file              | `8cf4f085de92`  |
| 853    | No file              | `8cf4f085de92`  |
| 845    | No file              | `8cf4f085de92`  |
| 837    | No file              | `8cf4f085de92`  |
| 829    | No file              | `8cf4f085de92`  |
| 822    | No file              | `8cf4f085de92`  |
| 814    | No file              | `8cf4f085de92`  |
| 805    | No file              | `8cf4f085de92`  |
| 794    | No file              | `8cf4f085de92`  |
| 787    | No file              | `8cf4f085de92`  |
| 780    | No file              | `8cf4f085de92`  |
| 771    | No file              | `8cf4f085de92`  |
| 760    | No file              | `8cf4f085de92`  |
| 748    | No file              | `8cf4f085de92`  |
| 741    | No file              | `8cf4f085de92`  |
| 736    | No file              | `8cf4f085de92`  |
| 731    | No file              | `8cf4f085de92`  |
| 723    | No file              | `8cf4f085de92`  |
| 711    | No file              | `8cf4f085de92`  |
| 707    | No file              | `8cf4f085de92`  |
| 697    | No file              | `8cf4f085de92`  |
| 689    | No file              | `8cf4f085de92`  |
| 683    | No file              | `8cf4f085de92`  |
| 678    | No file              | `8cf4f085de92`  |
| 670    | No file              | `8cf4f085de92`  |
| 661    | No file              | `8cf4f085de92`  |
| 656    | No file              | `8cf4f085de92`  |
| 652    | No file              | `8cf4f085de92`  |
| 643    | No file              | `8cf4f085de92`  |
| 637    | No file              | `8cf4f085de92`  |
| 630    | No file              | `8cf4f085de92`  |
| 627    | No file              | `8cf4f085de92`  |
| 621    | No file              | `8cf4f085de92`  |
| 617    | No file              | `8cf4f085de92`  |
| 615    | No file              | `8cf4f085de92`  |
| 606    | No file              | `8cf4f085de92`  |
| 599    | No file              | `8cf4f085de92`  |
| 592    | No file              | `8cf4f085de92`  |
| 586    | No file              | `8cf4f085de92`  |
| 577    | No file              | `8cf4f085de92`  |
| 569    | No file              | `8cf4f085de92`  |
| 561    | No file              | `8cf4f085de92`  |
| 554    | No file              | `8cf4f085de92`  |
| 542    | No file              | `8cf4f085de92`  |
| 532    | No file              | `8cf4f085de92`  |
| 531    | No file              | `8cf4f085de92`  |
| 526    | No file              | `8cf4f085de92`  |
| 521    | No file              | `8cf4f085de92`  |
| 517    | No file              | `8cf4f085de92`  |
| 510    | No file              | `8cf4f085de92`  |
| 508    | No file              | `8cf4f085de92`  |
| 504    | No file              | `8cf4f085de92`  |
| 497    | No file              | `8cf4f085de92`  |
| 491    | No file              | `8cf4f085de92`  |
| 485    | No file              | `8cf4f085de92`  |
| 478    | No file              | `8cf4f085de92`  |
| 472    | No file              | `8cf4f085de92`  |
| 466    | No file              | `8cf4f085de92`  |
| 457    | No file              | `8cf4f085de92`  |
| 452    | No file              | `8cf4f085de92`  |
| 449    | No file              | `8cf4f085de92`  |
| 435    | No file              | `8cf4f085de92`  |

<!-- versions:end -->

## Companion Files

| File                        | Required | Role                                                                          |
| --------------------------- | -------- | ----------------------------------------------------------------------------- |
| `petchangelookoffset.dbss`  | Optional | `change_look_key -> (offset, size)` of every payload; the parser walks the main file without it |
| `pet.dbss` + `petoffset.dbss` | Optional | The LOC names of the pets whose `change_look_key` is the record's key       |

The handler names a look's skill by its LOC type 10 name (`skill_no`).

All multi-byte values are little-endian.

## Layout 2

### File Layout

A record count, then the records back to back. Each record is a 2-byte key
prefix and the payload that `petchangelookoffset.dbss` addresses.

| Offset  | Type          | Field   | Notes             |
| ------- | ------------- | ------- | ----------------- |
| `+0x00` | u32           | count   | Number of records |
| `+0x04` | Record[count] | records | See Record        |

### Record (variable: 2 bytes + payload)

| Offset  | Type    | Field      | Notes                                                 |
| ------- | ------- | ---------- | ----------------------------------------------------- |
| `+0x00` | u16     | key_prefix | Equals `change_look_key`                              |
| `+0x02` | Payload | payload    | `size` bytes; the offset row points at this field     |

### Payload (variable: 6 bytes + looks, size from `petchangelookoffset.dbss`)

| Offset  | Type             | Field           | Notes                                                                 |
| ------- | ---------------- | --------------- | --------------------------------------------------------------------- |
| `+0x00` | u16              | change_look_key | The `change_look_key` of [`pet.dbss`](pet_dbss.md); equals the key prefix |
| `+0x02` | u32              | look_count      | Number of looks; 1 to 16 on client 3474                               |
| `+0x06` | Look[look_count] | looks           | See Look                                                              |

### Look (variable: 45 bytes + icon paths and skin name)

| Offset               | Type     | Field                   | Notes                                                                       |
| -------------------- | -------- | ----------------------- | --------------------------------------------------------------------------- |
| `+0x00`              | u32      | action_index            | The look's index, unique within its record                                  |
| `+0x04`              | str8     | icon_path               | Pet window icon (`New_UI_Common_forLua\Window\Stable\Pet\...`)              |
| `icon_path+0x00`     | str8     | icon_path_1             | Fairy skin slot icon; empty except on look key `25001` (fairy skins)        |
| `icon_path_1+0x00`   | str8     | icon_path_2             | Fairy window title image; empty except on look key `25001`                  |
| `icon_path_2+0x00`   | u16      | skill_level             | Level of the look's `gc::SkillKey`; `1` with a skill, else `0`              |
| `icon_path_2+0x02`   | u16      | skill_no                | Skill number of the look's skill (LOC type 10 names it); `0` for none      |
| `icon_path_2+0x04`   | u8       | unknown_icon_path_2_04  | `1` on the six looks with a skill, `0` on the rest (client 3474)           |
| `icon_path_2+0x05`   | str16    | skin_name_kr            | Korean skin name; empty except on ten looks of key `25001`                  |
| `skin_name_kr+0x00`  | u8       | unknown_skin_name_kr_00 | `0` on every look (client 3474)                                             |
| `skin_name_kr+0x01`  | bytes[3] | unknown_skin_name_kr_01 | `63 4F 37` on every look (client 3474)                                      |

### `petchangelookoffset.dbss`

Bare offset table into `petchangelook.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                 |
| ------- | ----------------- | ----- | ------------------------------------- |
| `+0x00` | u32               | count | Equals the `petchangelook.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                        |

### Offset Row (10 bytes)

| Offset  | Type | Field           | Notes                                                                       |
| ------- | ---- | --------------- | --------------------------------------------------------------------------- |
| `+0x00` | u16  | change_look_key | Key of the record it points at                                              |
| `+0x02` | u32  | offset          | Absolute byte offset in `petchangelook.dbss` of the payload, past the key prefix |
| `+0x06` | u32  | size            | Payload size in bytes, without the key prefix                               |

The offset rows are not in file order; read in offset order they cover the
main file from `+0x04` to its end, each record's key prefix included.

## Layout 1

### Look (variable: 32 bytes + icon paths)

The look ends after the skill: no `unknown_icon_path_2_04`, skin name or
tail bytes.

| Offset             | Type | Field        | Notes                                              |
| ------------------ | ---- | ------------ | -------------------------------------------------- |
| `+0x00`            | u32  | action_index |                                                    |
| `+0x04`            | str8 | icon_path    |                                                    |
| `icon_path+0x00`   | str8 | icon_path_1  |                                                    |
| `icon_path_1+0x00` | str8 | icon_path_2  |                                                    |
| `icon_path_2+0x00` | u16  | skill_level  | `1` on the one look with a skill (client 1784)     |
| `icon_path_2+0x02` | u16  | skill_no     | `49166` on look key `25001`, action index `6`      |

## Fairy Skins

On client 3474 look key `25001` holds the fairy skins. Ten of its looks
store a skin name and both extra icons (`Combine\Etc\...`), six of them a
skill:

| `action_index` | `skin_name_kr`  | `skill_no` | Skill (LOC type 10) |
| -------------- | --------------- | ---------- | ------------------- |
| 5              | 파크 요정       | 0          |                     |
| 6              | 똑딱똑딱 요정   | 49166      | Skill EXP +10%      |
| 7              | 월향화 요정     | 49182      | Death Penalty Resistance +5% |
| 8              | 베네실 요정     | 49183      | Processing EXP +10% |
| 9              | 키벨리우스 요정 | 49182      | Death Penalty Resistance +5% |
| 10             | 흑정령 요정     | 0          |                     |
| 11             | 진혼 요정       | 0          |                     |
| 12             | 명혼 요정       | 0          |                     |
| 18             | 새싹 꼬마 요정  | 49185      | Fishing EXP +20%    |
| 19             | 새벽 꼬마 요정  | 49184      | Combat EXP +200%    |

## Field Names

The `Pet_ChangeLook_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `PetChangeLookKey`, `ActionIndex`,
`IconPath`, `IconPath1`, `IconPath2` and `SkillNo`, and its 560 rows match
the file by (`PetChangeLookKey`, `ActionIndex`) on all 560 looks and all
four value columns, on client 1784 (560 looks) and on client 3474 (653
looks). Empty cells (`<null>`) are the empty strings and the zero
`skill_no` of the file. The 2016 client's debug symbols have
`gc::PetChangeLookStaticStatus` with a u16 `_petChangeLookKey` and a map
from a u32 to `_PET_LOOK_DATA` (`_iconPath` only), the `action_index` to
`icon_path` part of the record. `skill_level` and `skill_no` are one
`gc::SkillKey`, level first, as in
[`petequipskill.bss`](petequipskill_bss.md); `skill_level` is `1` exactly
where `SkillNo` is set.

The client Lua of client 3474 reads the table through
`ToClient_getPetChangeLookCount(petStaticStatus)`,
`ToClient_getPetChangeLook_IconPath(petStaticStatus, lookIndex)` and
`ToClient_getPetChangeLook_ActionIndex(petStaticStatus, lookIndex)` in the
pet look change window (`panel_window_petlookchange_all_1.luac`), which
lists a pet only when it has more than one look and requests the change by
action index. The fairy skin window
(`panel_window_fairyskinchange_all_new_1.luac`) reads a look's
`getIconPath1()`, `getSkinName()`, `getShowSkinList()` and
`getChangeLookSkillKey()`. `skin_name_kr` is the only text field besides
the paths, so it is the skin name; which of the two u8 fields is
`getShowSkinList()` is open.

## Notes

- Layout 2 adds 13 bytes and the skin name text to every look. On client
  3474 the 653 looks are 149 records; on client 1784, 560 looks in 130
  records.
- The pet whose `change_look_key` is `23061` has no record, and nine
  records (`35001`, `49007`, `49009` to `49014`, `49017`) belong to no pet
  of `pet.dbss` (client 3474).
- `unknown_skin_name_kr_01` holds the same three bytes on every look, which
  reads as the unset upper bytes of a 4-byte member whose low byte is
  `unknown_skin_name_kr_00`, as the alignment bytes of
  [`petfusionnew.dbss`](petfusionnew_dbss.md); no source names it.
- The fairy info window (`panel_window_fairy_all_2.luac`) shows the
  current skin's `getIconPath2()` as its title image; the fairy skin window
  shows `getIconPath1()` in each skin slot.

## Open Questions

### The Two u8 Fields of Layout 2

`unknown_icon_path_2_04` is `1` on the six looks with a skill and
`unknown_skin_name_kr_00` is `0` on every look. The fairy skin window reads
`getShowSkinList()` (show a skin the player does not own yet) for each
look; one of the two bytes may be that flag, but the client data does not
tell which, and `unknown_icon_path_2_04` may as well mark the skill as
present.
