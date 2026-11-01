# `supplyservantquestlist.bss` Format

## Purpose

Quest list with no entries: the `count` is `0` on client 3474 and on client 1784, and the file is the 20 bytes of an empty list. The file name points to the stable's supply-for-quest entry of the client Lua (see [Client Use](#client-use)); which quests the list would hold is not known.

Same layout as [`allquestlist.bss`](allquestlist_bss.md), read by the same handler: a `PABR` list of packed quest IDs. Each `packed_quest_id` would be `(quest_id << 16) | quest_chain_id`, the LOC type 18 title key. The trailer's `end_of_entries` is `8 + count * 4`, here `8`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                         | Bytes | Records        | Row bytes |
| ------ | -------------- | ---------------------------- | ----- | -------------- | --------- |
| 1      | 1173 and later | `supplyservantquestlist.bss` | 20    | 1 String Table | 4         |

| Layout | File                         | Known         | Unknown    |
| ------ | ---------------------------- | ------------- | ---------- |
| 1      | `supplyservantquestlist.bss` | 20 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `cf58d8232e2e`  |
| 3482   | Layout 1 | `cf58d8232e2e`  |
| 3474   | Layout 1 | `cf58d8232e2e`  |
| 3473   | Layout 1 | `cf58d8232e2e`  |
| 3464   | Layout 1 | `cf58d8232e2e`  |
| 3458   | Layout 1 | `cf58d8232e2e`  |
| 3454   | Layout 1 | `cf58d8232e2e`  |
| 3444   | Layout 1 | `cf58d8232e2e`  |
| 3435   | Layout 1 | `cf58d8232e2e`  |
| 3426   | Layout 1 | `cf58d8232e2e`  |
| 3418   | Layout 1 | `cf58d8232e2e`  |
| 3412   | Layout 1 | `cf58d8232e2e`  |
| 3402   | Layout 1 | `cf58d8232e2e`  |
| 3396   | Layout 1 | `cf58d8232e2e`  |
| 3387   | Layout 1 | `cf58d8232e2e`  |
| 3381   | Layout 1 | `cf58d8232e2e`  |
| 3373   | Layout 1 | `cf58d8232e2e`  |
| 3364   | Layout 1 | `cf58d8232e2e`  |
| 3356   | Layout 1 | `cf58d8232e2e`  |
| 3349   | Layout 1 | `cf58d8232e2e`  |
| 3342   | Layout 1 | `cf58d8232e2e`  |
| 3335   | Layout 1 | `cf58d8232e2e`  |
| 3326   | Layout 1 | `cf58d8232e2e`  |
| 3321   | Layout 1 | `cf58d8232e2e`  |
| 3314   | Layout 1 | `cf58d8232e2e`  |
| 3303   | Layout 1 | `cf58d8232e2e`  |
| 3302   | Layout 1 | `cf58d8232e2e`  |
| 3293   | Layout 1 | `cf58d8232e2e`  |
| 3283   | Layout 1 | `cf58d8232e2e`  |
| 3275   | Layout 1 | `cf58d8232e2e`  |
| 3267   | Layout 1 | `cf58d8232e2e`  |
| 3258   | Layout 1 | `cf58d8232e2e`  |
| 3251   | Layout 1 | `cf58d8232e2e`  |
| 3242   | Layout 1 | `cf58d8232e2e`  |
| 3235   | Layout 1 | `cf58d8232e2e`  |
| 3229   | Layout 1 | `cf58d8232e2e`  |
| 3212   | Layout 1 | `cf58d8232e2e`  |
| 3203   | Layout 1 | `cf58d8232e2e`  |
| 3193   | Layout 1 | `cf58d8232e2e`  |
| 3186   | Layout 1 | `cf58d8232e2e`  |
| 3177   | Layout 1 | `cf58d8232e2e`  |
| 3169   | Layout 1 | `cf58d8232e2e`  |
| 3158   | Layout 1 | `cf58d8232e2e`  |
| 3151   | Layout 1 | `cf58d8232e2e`  |
| 3144   | Layout 1 | `cf58d8232e2e`  |
| 3133   | Layout 1 | `cf58d8232e2e`  |
| 3125   | Layout 1 | `cf58d8232e2e`  |
| 3118   | Layout 1 | `cf58d8232e2e`  |
| 3111   | Layout 1 | `cf58d8232e2e`  |
| 3103   | Layout 1 | `cf58d8232e2e`  |
| 3095   | Layout 1 | `cf58d8232e2e`  |
| 3086   | Layout 1 | `cf58d8232e2e`  |
| 3072   | Layout 1 | `cf58d8232e2e`  |
| 3062   | Layout 1 | `cf58d8232e2e`  |
| 3052   | Layout 1 | `cf58d8232e2e`  |
| 3045   | Layout 1 | `cf58d8232e2e`  |
| 3037   | Layout 1 | `cf58d8232e2e`  |
| 3030   | Layout 1 | `cf58d8232e2e`  |
| 3021   | Layout 1 | `cf58d8232e2e`  |
| 3012   | Layout 1 | `cf58d8232e2e`  |
| 3002   | Layout 1 | `cf58d8232e2e`  |
| 2995   | Layout 1 | `cf58d8232e2e`  |
| 2987   | Layout 1 | `cf58d8232e2e`  |
| 2978   | Layout 1 | `cf58d8232e2e`  |
| 2970   | Layout 1 | `cf58d8232e2e`  |
| 2959   | Layout 1 | `cf58d8232e2e`  |
| 2951   | Layout 1 | `cf58d8232e2e`  |
| 2942   | Layout 1 | `cf58d8232e2e`  |
| 2935   | Layout 1 | `cf58d8232e2e`  |
| 2932   | Layout 1 | `cf58d8232e2e`  |
| 2923   | Layout 1 | `cf58d8232e2e`  |
| 2919   | Layout 1 | `cf58d8232e2e`  |
| 2907   | Layout 1 | `cf58d8232e2e`  |
| 2900   | Layout 1 | `cf58d8232e2e`  |
| 2891   | Layout 1 | `cf58d8232e2e`  |
| 2882   | Layout 1 | `cf58d8232e2e`  |
| 2872   | Layout 1 | `cf58d8232e2e`  |
| 2863   | Layout 1 | `cf58d8232e2e`  |
| 2855   | Layout 1 | `cf58d8232e2e`  |
| 2849   | Layout 1 | `cf58d8232e2e`  |
| 2844   | Layout 1 | `cf58d8232e2e`  |
| 2834   | Layout 1 | `cf58d8232e2e`  |
| 2825   | Layout 1 | `cf58d8232e2e`  |
| 2819   | Layout 1 | `cf58d8232e2e`  |
| 2811   | Layout 1 | `cf58d8232e2e`  |
| 2803   | Layout 1 | `cf58d8232e2e`  |
| 2794   | Layout 1 | `cf58d8232e2e`  |
| 2783   | Layout 1 | `cf58d8232e2e`  |
| 2774   | Layout 1 | `cf58d8232e2e`  |
| 2765   | Layout 1 | `cf58d8232e2e`  |
| 2756   | Layout 1 | `cf58d8232e2e`  |
| 2750   | Layout 1 | `cf58d8232e2e`  |
| 2743   | Layout 1 | `cf58d8232e2e`  |
| 2736   | Layout 1 | `cf58d8232e2e`  |
| 2726   | Layout 1 | `cf58d8232e2e`  |
| 2717   | Layout 1 | `cf58d8232e2e`  |
| 2709   | Layout 1 | `cf58d8232e2e`  |
| 2703   | Layout 1 | `cf58d8232e2e`  |
| 2695   | Layout 1 | `cf58d8232e2e`  |
| 2684   | Layout 1 | `cf58d8232e2e`  |
| 2672   | Layout 1 | `cf58d8232e2e`  |
| 2665   | Layout 1 | `cf58d8232e2e`  |
| 2657   | Layout 1 | `cf58d8232e2e`  |
| 2649   | Layout 1 | `cf58d8232e2e`  |
| 2644   | Layout 1 | `cf58d8232e2e`  |
| 2637   | Layout 1 | `cf58d8232e2e`  |
| 2629   | Layout 1 | `cf58d8232e2e`  |
| 2619   | Layout 1 | `cf58d8232e2e`  |
| 2612   | Layout 1 | `cf58d8232e2e`  |
| 2606   | Layout 1 | `cf58d8232e2e`  |
| 2602   | Layout 1 | `cf58d8232e2e`  |
| 2601   | Layout 1 | `cf58d8232e2e`  |
| 2592   | Layout 1 | `cf58d8232e2e`  |
| 2583   | Layout 1 | `cf58d8232e2e`  |
| 2575   | Layout 1 | `cf58d8232e2e`  |
| 2567   | Layout 1 | `cf58d8232e2e`  |
| 2560   | Layout 1 | `cf58d8232e2e`  |
| 2553   | Layout 1 | `cf58d8232e2e`  |
| 2545   | Layout 1 | `cf58d8232e2e`  |
| 2538   | Layout 1 | `cf58d8232e2e`  |
| 2529   | Layout 1 | `cf58d8232e2e`  |
| 2519   | Layout 1 | `cf58d8232e2e`  |
| 2513   | Layout 1 | `cf58d8232e2e`  |
| 2510   | Layout 1 | `cf58d8232e2e`  |
| 2507   | Layout 1 | `cf58d8232e2e`  |
| 2503   | Layout 1 | `cf58d8232e2e`  |
| 2498   | Layout 1 | `cf58d8232e2e`  |
| 2492   | Layout 1 | `cf58d8232e2e`  |
| 2487   | Layout 1 | `cf58d8232e2e`  |
| 2480   | Layout 1 | `cf58d8232e2e`  |
| 2474   | Layout 1 | `cf58d8232e2e`  |
| 2468   | Layout 1 | `cf58d8232e2e`  |
| 2460   | Layout 1 | `cf58d8232e2e`  |
| 2453   | Layout 1 | `cf58d8232e2e`  |
| 2444   | Layout 1 | `cf58d8232e2e`  |
| 2438   | Layout 1 | `cf58d8232e2e`  |
| 2434   | Layout 1 | `cf58d8232e2e`  |
| 2429   | Layout 1 | `cf58d8232e2e`  |
| 2421   | Layout 1 | `cf58d8232e2e`  |
| 2414   | Layout 1 | `cf58d8232e2e`  |
| 2407   | Layout 1 | `cf58d8232e2e`  |
| 2401   | Layout 1 | `cf58d8232e2e`  |
| 2397   | Layout 1 | `cf58d8232e2e`  |
| 2393   | Layout 1 | `cf58d8232e2e`  |
| 2384   | Layout 1 | `cf58d8232e2e`  |
| 2378   | Layout 1 | `cf58d8232e2e`  |
| 2372   | Layout 1 | `cf58d8232e2e`  |
| 2358   | Layout 1 | `cf58d8232e2e`  |
| 2352   | Layout 1 | `cf58d8232e2e`  |
| 2347   | Layout 1 | `cf58d8232e2e`  |
| 2343   | Layout 1 | `cf58d8232e2e`  |
| 2335   | Layout 1 | `cf58d8232e2e`  |
| 2327   | Layout 1 | `cf58d8232e2e`  |
| 2324   | Layout 1 | `cf58d8232e2e`  |
| 2319   | Layout 1 | `cf58d8232e2e`  |
| 2313   | Layout 1 | `cf58d8232e2e`  |
| 2308   | Layout 1 | `cf58d8232e2e`  |
| 2302   | Layout 1 | `cf58d8232e2e`  |
| 2295   | Layout 1 | `cf58d8232e2e`  |
| 2290   | Layout 1 | `cf58d8232e2e`  |
| 2284   | Layout 1 | `cf58d8232e2e`  |
| 2276   | Layout 1 | `cf58d8232e2e`  |
| 2269   | Layout 1 | `cf58d8232e2e`  |
| 2259   | Layout 1 | `cf58d8232e2e`  |
| 2250   | Layout 1 | `cf58d8232e2e`  |
| 2243   | Layout 1 | `cf58d8232e2e`  |
| 2235   | Layout 1 | `cf58d8232e2e`  |
| 2229   | Layout 1 | `cf58d8232e2e`  |
| 2224   | Layout 1 | `cf58d8232e2e`  |
| 2218   | Layout 1 | `cf58d8232e2e`  |
| 2215   | Layout 1 | `cf58d8232e2e`  |
| 2207   | Layout 1 | `cf58d8232e2e`  |
| 2203   | Layout 1 | `cf58d8232e2e`  |
| 2196   | Layout 1 | `cf58d8232e2e`  |
| 2192   | Layout 1 | `cf58d8232e2e`  |
| 2189   | Layout 1 | `cf58d8232e2e`  |
| 2183   | Layout 1 | `cf58d8232e2e`  |
| 2179   | Layout 1 | `cf58d8232e2e`  |
| 2171   | Layout 1 | `cf58d8232e2e`  |
| 2163   | Layout 1 | `cf58d8232e2e`  |
| 2156   | Layout 1 | `cf58d8232e2e`  |
| 2151   | Layout 1 | `cf58d8232e2e`  |
| 2147   | Layout 1 | `cf58d8232e2e`  |
| 2142   | Layout 1 | `cf58d8232e2e`  |
| 2138   | Layout 1 | `cf58d8232e2e`  |
| 2134   | Layout 1 | `cf58d8232e2e`  |
| 2130   | Layout 1 | `cf58d8232e2e`  |
| 2122   | Layout 1 | `cf58d8232e2e`  |
| 2107   | Layout 1 | `cf58d8232e2e`  |
| 2098   | Layout 1 | `cf58d8232e2e`  |
| 2089   | Layout 1 | `cf58d8232e2e`  |
| 2081   | Layout 1 | `cf58d8232e2e`  |
| 2073   | Layout 1 | `cf58d8232e2e`  |
| 2067   | Layout 1 | `cf58d8232e2e`  |
| 2063   | Layout 1 | `cf58d8232e2e`  |
| 2059   | Layout 1 | `cf58d8232e2e`  |
| 2052   | Layout 1 | `cf58d8232e2e`  |
| 2044   | Layout 1 | `cf58d8232e2e`  |
| 2039   | Layout 1 | `cf58d8232e2e`  |
| 2032   | Layout 1 | `cf58d8232e2e`  |
| 2025   | Layout 1 | `cf58d8232e2e`  |
| 2011   | Layout 1 | `cf58d8232e2e`  |
| 2005   | Layout 1 | `cf58d8232e2e`  |
| 2000   | Layout 1 | `cf58d8232e2e`  |
| 1996   | Layout 1 | `cf58d8232e2e`  |
| 1991   | Layout 1 | `cf58d8232e2e`  |
| 1985   | Layout 1 | `cf58d8232e2e`  |
| 1980   | Layout 1 | `cf58d8232e2e`  |
| 1969   | Layout 1 | `cf58d8232e2e`  |
| 1964   | Layout 1 | `cf58d8232e2e`  |
| 1958   | Layout 1 | `cf58d8232e2e`  |
| 1950   | Layout 1 | `cf58d8232e2e`  |
| 1945   | Layout 1 | `cf58d8232e2e`  |
| 1937   | Layout 1 | `cf58d8232e2e`  |
| 1933   | Layout 1 | `cf58d8232e2e`  |
| 1927   | Layout 1 | `cf58d8232e2e`  |
| 1921   | Layout 1 | `cf58d8232e2e`  |
| 1914   | Layout 1 | `cf58d8232e2e`  |
| 1908   | Layout 1 | `cf58d8232e2e`  |
| 1897   | Layout 1 | `cf58d8232e2e`  |
| 1892   | Layout 1 | `cf58d8232e2e`  |
| 1886   | Layout 1 | `cf58d8232e2e`  |
| 1881   | Layout 1 | `cf58d8232e2e`  |
| 1871   | Layout 1 | `cf58d8232e2e`  |
| 1866   | Layout 1 | `cf58d8232e2e`  |
| 1862   | Layout 1 | `cf58d8232e2e`  |
| 1854   | Layout 1 | `cf58d8232e2e`  |
| 1846   | Layout 1 | `cf58d8232e2e`  |
| 1838   | Layout 1 | `cf58d8232e2e`  |
| 1832   | Layout 1 | `cf58d8232e2e`  |
| 1826   | Layout 1 | `cf58d8232e2e`  |
| 1822   | Layout 1 | `cf58d8232e2e`  |
| 1818   | Layout 1 | `cf58d8232e2e`  |
| 1804   | Layout 1 | `cf58d8232e2e`  |
| 1794   | Layout 1 | `cf58d8232e2e`  |
| 1790   | Layout 1 | `cf58d8232e2e`  |
| 1784   | Layout 1 | `cf58d8232e2e`  |
| 1774   | Layout 1 | `cf58d8232e2e`  |
| 1771   | Layout 1 | `cf58d8232e2e`  |
| 1762   | Layout 1 | `cf58d8232e2e`  |
| 1759   | Layout 1 | `cf58d8232e2e`  |
| 1754   | Layout 1 | `cf58d8232e2e`  |
| 1749   | Layout 1 | `cf58d8232e2e`  |
| 1743   | Layout 1 | `cf58d8232e2e`  |
| 1737   | Layout 1 | `cf58d8232e2e`  |
| 1731   | Layout 1 | `cf58d8232e2e`  |
| 1725   | Layout 1 | `cf58d8232e2e`  |
| 1717   | Layout 1 | `cf58d8232e2e`  |
| 1710   | Layout 1 | `cf58d8232e2e`  |
| 1704   | Layout 1 | `cf58d8232e2e`  |
| 1698   | Layout 1 | `cf58d8232e2e`  |
| 1690   | Layout 1 | `cf58d8232e2e`  |
| 1685   | Layout 1 | `cf58d8232e2e`  |
| 1680   | Layout 1 | `cf58d8232e2e`  |
| 1674   | Layout 1 | `cf58d8232e2e`  |
| 1668   | Layout 1 | `cf58d8232e2e`  |
| 1659   | Layout 1 | `cf58d8232e2e`  |
| 1649   | Layout 1 | `cf58d8232e2e`  |
| 1642   | Layout 1 | `cf58d8232e2e`  |
| 1636   | Layout 1 | `cf58d8232e2e`  |
| 1628   | Layout 1 | `cf58d8232e2e`  |
| 1622   | Layout 1 | `cf58d8232e2e`  |
| 1614   | Layout 1 | `cf58d8232e2e`  |
| 1608   | Layout 1 | `cf58d8232e2e`  |
| 1602   | Layout 1 | `cf58d8232e2e`  |
| 1598   | Layout 1 | `cf58d8232e2e`  |
| 1594   | Layout 1 | `cf58d8232e2e`  |
| 1590   | Layout 1 | `cf58d8232e2e`  |
| 1587   | Layout 1 | `cf58d8232e2e`  |
| 1584   | Layout 1 | `cf58d8232e2e`  |
| 1579   | Layout 1 | `cf58d8232e2e`  |
| 1572   | Layout 1 | `cf58d8232e2e`  |
| 1565   | Layout 1 | `cf58d8232e2e`  |
| 1559   | Layout 1 | `cf58d8232e2e`  |
| 1554   | Layout 1 | `cf58d8232e2e`  |
| 1547   | Layout 1 | `cf58d8232e2e`  |
| 1537   | Layout 1 | `cf58d8232e2e`  |
| 1529   | Layout 1 | `cf58d8232e2e`  |
| 1524   | Layout 1 | `cf58d8232e2e`  |
| 1519   | Layout 1 | `cf58d8232e2e`  |
| 1509   | Layout 1 | `cf58d8232e2e`  |
| 1506   | Layout 1 | `cf58d8232e2e`  |
| 1504   | Layout 1 | `cf58d8232e2e`  |
| 1500   | Layout 1 | `cf58d8232e2e`  |
| 1493   | Layout 1 | `cf58d8232e2e`  |
| 1489   | Layout 1 | `cf58d8232e2e`  |
| 1485   | Layout 1 | `cf58d8232e2e`  |
| 1481   | Layout 1 | `cf58d8232e2e`  |
| 1474   | Layout 1 | `cf58d8232e2e`  |
| 1466   | Layout 1 | `cf58d8232e2e`  |
| 1462   | Layout 1 | `cf58d8232e2e`  |
| 1459   | Layout 1 | `cf58d8232e2e`  |
| 1453   | Layout 1 | `cf58d8232e2e`  |
| 1450   | Layout 1 | `cf58d8232e2e`  |
| 1445   | Layout 1 | `cf58d8232e2e`  |
| 1439   | Layout 1 | `cf58d8232e2e`  |
| 1433   | Layout 1 | `cf58d8232e2e`  |
| 1430   | Layout 1 | `cf58d8232e2e`  |
| 1426   | Layout 1 | `cf58d8232e2e`  |
| 1421   | Layout 1 | `cf58d8232e2e`  |
| 1417   | Layout 1 | `cf58d8232e2e`  |
| 1416   | Layout 1 | `cf58d8232e2e`  |
| 1409   | Layout 1 | `cf58d8232e2e`  |
| 1405   | Layout 1 | `cf58d8232e2e`  |
| 1401   | Layout 1 | `cf58d8232e2e`  |
| 1396   | Layout 1 | `cf58d8232e2e`  |
| 1391   | Layout 1 | `cf58d8232e2e`  |
| 1390   | Layout 1 | `cf58d8232e2e`  |
| 1386   | Layout 1 | `cf58d8232e2e`  |
| 1381   | Layout 1 | `cf58d8232e2e`  |
| 1379   | Layout 1 | `cf58d8232e2e`  |
| 1372   | Layout 1 | `cf58d8232e2e`  |
| 1366   | Layout 1 | `cf58d8232e2e`  |
| 1364   | Layout 1 | `cf58d8232e2e`  |
| 1363   | Layout 1 | `cf58d8232e2e`  |
| 1360   | Layout 1 | `cf58d8232e2e`  |
| 1358   | Layout 1 | `cf58d8232e2e`  |
| 1355   | Layout 1 | `cf58d8232e2e`  |
| 1351   | Layout 1 | `cf58d8232e2e`  |
| 1348   | Layout 1 | `cf58d8232e2e`  |
| 1346   | Layout 1 | `cf58d8232e2e`  |
| 1341   | Layout 1 | `cf58d8232e2e`  |
| 1340   | Layout 1 | `cf58d8232e2e`  |
| 1338   | Layout 1 | `cf58d8232e2e`  |
| 1335   | Layout 1 | `cf58d8232e2e`  |
| 1333   | Layout 1 | `cf58d8232e2e`  |
| 1329   | Layout 1 | `cf58d8232e2e`  |
| 1327   | Layout 1 | `cf58d8232e2e`  |
| 1324   | Layout 1 | `cf58d8232e2e`  |
| 1321   | Layout 1 | `cf58d8232e2e`  |
| 1319   | Layout 1 | `cf58d8232e2e`  |
| 1318   | Layout 1 | `cf58d8232e2e`  |
| 1316   | Layout 1 | `cf58d8232e2e`  |
| 1313   | Layout 1 | `cf58d8232e2e`  |
| 1311   | Layout 1 | `cf58d8232e2e`  |
| 1309   | Layout 1 | `cf58d8232e2e`  |
| 1304   | Layout 1 | `cf58d8232e2e`  |
| 1292   | Layout 1 | `cf58d8232e2e`  |
| 1286   | Layout 1 | `cf58d8232e2e`  |
| 1280   | Layout 1 | `cf58d8232e2e`  |
| 1276   | Layout 1 | `cf58d8232e2e`  |
| 1267   | Layout 1 | `cf58d8232e2e`  |
| 1261   | Layout 1 | `cf58d8232e2e`  |
| 1256   | Layout 1 | `cf58d8232e2e`  |
| 1250   | Layout 1 | `cf58d8232e2e`  |
| 1246   | Layout 1 | `cf58d8232e2e`  |
| 1239   | Layout 1 | `cf58d8232e2e`  |
| 1230   | Layout 1 | `cf58d8232e2e`  |
| 1226   | Layout 1 | `cf58d8232e2e`  |
| 1220   | Layout 1 | `cf58d8232e2e`  |
| 1217   | Layout 1 | `cf58d8232e2e`  |
| 1211   | Layout 1 | `cf58d8232e2e`  |
| 1210   | Layout 1 | `cf58d8232e2e`  |
| 1208   | Layout 1 | `cf58d8232e2e`  |
| 1203   | Layout 1 | `cf58d8232e2e`  |
| 1197   | Layout 1 | `cf58d8232e2e`  |
| 1194   | Layout 1 | `cf58d8232e2e`  |
| 1192   | Layout 1 | `cf58d8232e2e`  |
| 1187   | Layout 1 | `cf58d8232e2e`  |
| 1183   | Layout 1 | `cf58d8232e2e`  |
| 1177   | Layout 1 | `cf58d8232e2e`  |
| 1173   | Layout 1 | `cf58d8232e2e`  |
| 1167   | No file  | `cf58d8232e2e`  |
| 1164   | No file  | `cf58d8232e2e`  |
| 1156   | No file  | `cf58d8232e2e`  |
| 1149   | No file  | `cf58d8232e2e`  |
| 1144   | No file  | `cf58d8232e2e`  |
| 1137   | No file  | `cf58d8232e2e`  |
| 1132   | No file  | `cf58d8232e2e`  |
| 1127   | No file  | `cf58d8232e2e`  |
| 1122   | No file  | `cf58d8232e2e`  |
| 1118   | No file  | `cf58d8232e2e`  |
| 1114   | No file  | `cf58d8232e2e`  |
| 1109   | No file  | `cf58d8232e2e`  |
| 1102   | No file  | `cf58d8232e2e`  |
| 1096   | No file  | `cf58d8232e2e`  |
| 1088   | No file  | `cf58d8232e2e`  |
| 1081   | No file  | `cf58d8232e2e`  |
| 1076   | No file  | `cf58d8232e2e`  |
| 1069   | No file  | `cf58d8232e2e`  |
| 1064   | No file  | `cf58d8232e2e`  |
| 1058   | No file  | `cf58d8232e2e`  |
| 1051   | No file  | `cf58d8232e2e`  |
| 1044   | No file  | `cf58d8232e2e`  |
| 1036   | No file  | `cf58d8232e2e`  |
| 1026   | No file  | `cf58d8232e2e`  |
| 1016   | No file  | `cf58d8232e2e`  |
| 1009   | No file  | `cf58d8232e2e`  |
| 1005   | No file  | `cf58d8232e2e`  |
| 1000   | No file  | `cf58d8232e2e`  |
| 998    | No file  | `cf58d8232e2e`  |
| 990    | No file  | `cf58d8232e2e`  |
| 979    | No file  | `cf58d8232e2e`  |
| 972    | No file  | `cf58d8232e2e`  |
| 963    | No file  | `cf58d8232e2e`  |
| 955    | No file  | `cf58d8232e2e`  |
| 946    | No file  | `cf58d8232e2e`  |
| 938    | No file  | `cf58d8232e2e`  |
| 927    | No file  | `cf58d8232e2e`  |
| 911    | No file  | `cf58d8232e2e`  |
| 904    | No file  | `cf58d8232e2e`  |
| 899    | No file  | `cf58d8232e2e`  |
| 894    | No file  | `cf58d8232e2e`  |
| 885    | No file  | `cf58d8232e2e`  |
| 879    | No file  | `cf58d8232e2e`  |
| 872    | No file  | `cf58d8232e2e`  |
| 864    | No file  | `cf58d8232e2e`  |
| 855    | No file  | `cf58d8232e2e`  |
| 853    | No file  | `cf58d8232e2e`  |
| 845    | No file  | `cf58d8232e2e`  |
| 837    | No file  | `cf58d8232e2e`  |
| 829    | No file  | `cf58d8232e2e`  |
| 822    | No file  | `cf58d8232e2e`  |
| 814    | No file  | `cf58d8232e2e`  |
| 805    | No file  | `cf58d8232e2e`  |
| 794    | No file  | `cf58d8232e2e`  |
| 787    | No file  | `cf58d8232e2e`  |
| 780    | No file  | `cf58d8232e2e`  |
| 771    | No file  | `cf58d8232e2e`  |
| 760    | No file  | `cf58d8232e2e`  |
| 748    | No file  | `cf58d8232e2e`  |
| 741    | No file  | `cf58d8232e2e`  |
| 736    | No file  | `cf58d8232e2e`  |
| 731    | No file  | `cf58d8232e2e`  |
| 723    | No file  | `cf58d8232e2e`  |
| 711    | No file  | `cf58d8232e2e`  |
| 707    | No file  | `cf58d8232e2e`  |
| 697    | No file  | `cf58d8232e2e`  |
| 689    | No file  | `cf58d8232e2e`  |
| 683    | No file  | `cf58d8232e2e`  |
| 678    | No file  | `cf58d8232e2e`  |
| 670    | No file  | `cf58d8232e2e`  |
| 661    | No file  | `cf58d8232e2e`  |
| 656    | No file  | `cf58d8232e2e`  |
| 652    | No file  | `cf58d8232e2e`  |
| 643    | No file  | `cf58d8232e2e`  |
| 637    | No file  | `cf58d8232e2e`  |
| 630    | No file  | `cf58d8232e2e`  |
| 627    | No file  | `cf58d8232e2e`  |
| 621    | No file  | `cf58d8232e2e`  |
| 617    | No file  | `cf58d8232e2e`  |
| 615    | No file  | `cf58d8232e2e`  |
| 606    | No file  | `cf58d8232e2e`  |
| 599    | No file  | `cf58d8232e2e`  |
| 592    | No file  | `cf58d8232e2e`  |
| 586    | No file  | `cf58d8232e2e`  |
| 577    | No file  | `cf58d8232e2e`  |
| 569    | No file  | `cf58d8232e2e`  |
| 561    | No file  | `cf58d8232e2e`  |
| 554    | No file  | `cf58d8232e2e`  |
| 542    | No file  | `cf58d8232e2e`  |
| 532    | No file  | `cf58d8232e2e`  |
| 531    | No file  | `cf58d8232e2e`  |
| 526    | No file  | `cf58d8232e2e`  |
| 521    | No file  | `cf58d8232e2e`  |
| 517    | No file  | `cf58d8232e2e`  |
| 510    | No file  | `cf58d8232e2e`  |
| 508    | No file  | `cf58d8232e2e`  |
| 504    | No file  | `cf58d8232e2e`  |
| 497    | No file  | `cf58d8232e2e`  |
| 491    | No file  | `cf58d8232e2e`  |
| 485    | No file  | `cf58d8232e2e`  |
| 478    | No file  | `cf58d8232e2e`  |
| 472    | No file  | `cf58d8232e2e`  |
| 466    | No file  | `cf58d8232e2e`  |
| 457    | No file  | `cf58d8232e2e`  |
| 452    | No file  | `cf58d8232e2e`  |
| 449    | No file  | `cf58d8232e2e`  |
| 435    | No file  | `cf58d8232e2e`  |

<!-- versions:end -->

## Companion Files

The same as [`allquestlist.bss`](allquestlist_bss.md).

All multi-byte values are little-endian.

## Client Use

`panel_dialog_servantlist_all_1.luac` and `panel_dialog_servantlist_all_2.luac` (client 3474, also in client 1784) have a stable submenu entry `_SUPPLYFORQUEST` next to the Imperial delivery entry `_SUPPLYHORSE`:

- The submenu adds `_SUPPLYFORQUEST` when `servantInfo:isSuppliableForQuest()` is true and the servant is not rented, not a PC room servant and not in stallion training. The check sits outside the vehicle type test, so it applies to every servant type.
- `HandleEventLUp_ServantList_All_SupplyForQueset()` sends `ToClient_RequestSupplyServant(servantNo)`. The Imperial delivery entry (`HandleEventLUp_ServantList_All_SupplyServant()`) calls `stable_changeToReward(servantNo, CppEnums.ServantToRewardType.Type_Money)` instead.
- The entry's label is the resource string `PANEL_WINDOW_STABLEFUNCTION_LOOKCHANGE`, the same key as the change-look entry `_CHANGELOOK`.

No Lua names this file or reads a quest list for the entry; `isSuppliableForQuest()` is a client function.

## Notes

- Bytes on client 3474 and client 1784: `PABR`, `count` `0`, then the 12-byte trailer `0`, `8`, `0` (`string_count`, `end_of_entries`, `zero`).
- The `binary/` folder of a private server on client 1784 holds the same 20 bytes. Its `DataSheets.bexcel` has no column or cell naming a supply quest (`Quest_Table` has `DoGuide`, the source of [`doguildquestlist.bss`](doguildquestlist_bss.md), but no supply column), and the 2016 client PDB has no symbol for it.
- `test_supply_servant_quest_list.py` checks the declared count and that any entry is a quest of `allquestlist.bss`.

## Open Questions

### What Fills the List

The list is empty on clients 1784 and 3474, so no entry shows which quests it holds. A guess from the Lua: the quests whose objective is to hand over a servant through the stable's supply-for-quest entry, with `isSuppliableForQuest()` true while such a quest is in progress. No source sheet or Lua confirms the link.
