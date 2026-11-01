# `restrictcontentsregion.dbss` Format

## Purpose

The functions a region turns off: per region key one flag each for the
maid, the world map, character change, muster, camp, compass, item map and
minimap. The client Lua asks for them by region with
`ToClient_RestrictContentsByRegion(__eRestrictContentsType_WorldMap)` (the
world map, minimap and family character list) and
`__eRestrictContentsType_Maid` (the maid list). On client 3474 the 48 rows
are regions such as Orze's Garden (`1550`), Syca's Garden (`1102`) and
Vaha's Cradle (`1078`). Companion `restrictcontentsregionoffset.dbss` lists
where every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                | Bytes | Records       | Row bytes |
| ------ | -------------- | ----------------------------------- | ----- | ------------- | --------- |
| 2      | 1794 and later | `restrictcontentsregion.dbss`       | 628   | 48 Row        | 13        |
| 2      | 1794 and later | `restrictcontentsregionoffset.dbss` | 484   | 48 Offset Row | 10        |
| 1      | 1602 to 1790   | `restrictcontentsregion.dbss`       | 292   | 24 Row        | 12        |
| 1      | 1602 to 1790   | `restrictcontentsregionoffset.dbss` | 244   | 24 Offset Row | 10        |

| Layout | File                                | Known          | Unknown     |
| ------ | ----------------------------------- | -------------- | ----------- |
| 2      | `restrictcontentsregion.dbss`       | 580 B (92.4%)  | 48 B (7.6%) |
| 2      | `restrictcontentsregionoffset.dbss` | 484 B (100.0%) | 0 B (0.0%)  |
| 1      | `restrictcontentsregion.dbss`       | 292 B (100.0%) | 0 B (0.0%)  |
| 1      | `restrictcontentsregionoffset.dbss` | 244 B (100.0%) | 0 B (0.0%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `e6ae841dbcfe`  |
| 3482   | Layout 2             | `e6ae841dbcfe`  |
| 3474   | Layout 2             | `e6ae841dbcfe`  |
| 3473   | Layout 2             | `e6ae841dbcfe`  |
| 3464   | Layout 2             | `e6ae841dbcfe`  |
| 3458   | Layout 2             | `e6ae841dbcfe`  |
| 3454   | Layout 2             | `e6ae841dbcfe`  |
| 3444   | Layout 2             | `e6ae841dbcfe`  |
| 3435   | Layout 2             | `e6ae841dbcfe`  |
| 3426   | Layout 2             | `e6ae841dbcfe`  |
| 3418   | Layout 2             | `e6ae841dbcfe`  |
| 3412   | Layout 2             | `e6ae841dbcfe`  |
| 3402   | Layout 2             | `e6ae841dbcfe`  |
| 3396   | Layout 2             | `e6ae841dbcfe`  |
| 3387   | Layout 2             | `e6ae841dbcfe`  |
| 3381   | Layout 2             | `e6ae841dbcfe`  |
| 3373   | Layout 2             | `e6ae841dbcfe`  |
| 3364   | Layout 2             | `e6ae841dbcfe`  |
| 3356   | Layout 2             | `e6ae841dbcfe`  |
| 3349   | Layout 2             | `e6ae841dbcfe`  |
| 3342   | Layout 2             | `e6ae841dbcfe`  |
| 3335   | Layout 2             | `e6ae841dbcfe`  |
| 3326   | Layout 2             | `e6ae841dbcfe`  |
| 3321   | Layout 2             | `e6ae841dbcfe`  |
| 3314   | Layout 2             | `e6ae841dbcfe`  |
| 3303   | Layout 2             | `e6ae841dbcfe`  |
| 3302   | Layout 2             | `e6ae841dbcfe`  |
| 3293   | Layout 2             | `e6ae841dbcfe`  |
| 3283   | Layout 2             | `e6ae841dbcfe`  |
| 3275   | Layout 2             | `e6ae841dbcfe`  |
| 3267   | Layout 2             | `e6ae841dbcfe`  |
| 3258   | Layout 2             | `e6ae841dbcfe`  |
| 3251   | Layout 2             | `e6ae841dbcfe`  |
| 3242   | Layout 2             | `e6ae841dbcfe`  |
| 3235   | Layout 2             | `e6ae841dbcfe`  |
| 3229   | Layout 2             | `e6ae841dbcfe`  |
| 3212   | Layout 2             | `e6ae841dbcfe`  |
| 3203   | Layout 2             | `e6ae841dbcfe`  |
| 3193   | Layout 2             | `e6ae841dbcfe`  |
| 3186   | Layout 2             | `e6ae841dbcfe`  |
| 3177   | Layout 2             | `e6ae841dbcfe`  |
| 3169   | Layout 2             | `e6ae841dbcfe`  |
| 3158   | Layout 2             | `e6ae841dbcfe`  |
| 3151   | Layout 2             | `e6ae841dbcfe`  |
| 3144   | Layout 2             | `e6ae841dbcfe`  |
| 3133   | Layout 2             | `e6ae841dbcfe`  |
| 3125   | Layout 2             | `e6ae841dbcfe`  |
| 3118   | Layout 2             | `e6ae841dbcfe`  |
| 3111   | Layout 2             | `e6ae841dbcfe`  |
| 3103   | Layout 2             | `e6ae841dbcfe`  |
| 3095   | Layout 2             | `e6ae841dbcfe`  |
| 3086   | Layout 2             | `e6ae841dbcfe`  |
| 3072   | Layout 2             | `e6ae841dbcfe`  |
| 3062   | Layout 2             | `e6ae841dbcfe`  |
| 3052   | Layout 2             | `e6ae841dbcfe`  |
| 3045   | Layout 2             | `e6ae841dbcfe`  |
| 3037   | Layout 2             | `e6ae841dbcfe`  |
| 3030   | Layout 2             | `e6ae841dbcfe`  |
| 3021   | Layout 2             | `e6ae841dbcfe`  |
| 3012   | Layout 2             | `e6ae841dbcfe`  |
| 3002   | Layout 2             | `e6ae841dbcfe`  |
| 2995   | Layout 2             | `e6ae841dbcfe`  |
| 2987   | Layout 2             | `e6ae841dbcfe`  |
| 2978   | Layout 2             | `e6ae841dbcfe`  |
| 2970   | Layout 2             | `e6ae841dbcfe`  |
| 2959   | Layout 2             | `e6ae841dbcfe`  |
| 2951   | Layout 2             | `e6ae841dbcfe`  |
| 2942   | Layout 2             | `e6ae841dbcfe`  |
| 2935   | Layout 2             | `e6ae841dbcfe`  |
| 2932   | Layout 2             | `e6ae841dbcfe`  |
| 2923   | Layout 2             | `e6ae841dbcfe`  |
| 2919   | Layout 2             | `e6ae841dbcfe`  |
| 2907   | Layout 2             | `e6ae841dbcfe`  |
| 2900   | Layout 2             | `e6ae841dbcfe`  |
| 2891   | Layout 2             | `e6ae841dbcfe`  |
| 2882   | Layout 2             | `e6ae841dbcfe`  |
| 2872   | Layout 2             | `e6ae841dbcfe`  |
| 2863   | Layout 2             | `e6ae841dbcfe`  |
| 2855   | Layout 2             | `e6ae841dbcfe`  |
| 2849   | Layout 2             | `e6ae841dbcfe`  |
| 2844   | Layout 2             | `e6ae841dbcfe`  |
| 2834   | Layout 2             | `e6ae841dbcfe`  |
| 2825   | Layout 2             | `e6ae841dbcfe`  |
| 2819   | Layout 2             | `e6ae841dbcfe`  |
| 2811   | Layout 2             | `e6ae841dbcfe`  |
| 2803   | Layout 2             | `e6ae841dbcfe`  |
| 2794   | Layout 2             | `e6ae841dbcfe`  |
| 2783   | Layout 2             | `e6ae841dbcfe`  |
| 2774   | Layout 2             | `e6ae841dbcfe`  |
| 2765   | Layout 2             | `e6ae841dbcfe`  |
| 2756   | Layout 2             | `e6ae841dbcfe`  |
| 2750   | Layout 2             | `e6ae841dbcfe`  |
| 2743   | Layout 2             | `e6ae841dbcfe`  |
| 2736   | Layout 2             | `e6ae841dbcfe`  |
| 2726   | Layout 2             | `e6ae841dbcfe`  |
| 2717   | Layout 2             | `e6ae841dbcfe`  |
| 2709   | Layout 2             | `e6ae841dbcfe`  |
| 2703   | Layout 2             | `e6ae841dbcfe`  |
| 2695   | Layout 2             | `e6ae841dbcfe`  |
| 2684   | Layout 2             | `e6ae841dbcfe`  |
| 2672   | Layout 2             | `e6ae841dbcfe`  |
| 2665   | Layout 2             | `e6ae841dbcfe`  |
| 2657   | Layout 2             | `e6ae841dbcfe`  |
| 2649   | Layout 2             | `e6ae841dbcfe`  |
| 2644   | Layout 2             | `e6ae841dbcfe`  |
| 2637   | Layout 2             | `e6ae841dbcfe`  |
| 2629   | Layout 2             | `e6ae841dbcfe`  |
| 2619   | Layout 2             | `e6ae841dbcfe`  |
| 2612   | Layout 2             | `e6ae841dbcfe`  |
| 2606   | Layout 2             | `e6ae841dbcfe`  |
| 2602   | Layout 2             | `e6ae841dbcfe`  |
| 2601   | Layout 2             | `e6ae841dbcfe`  |
| 2592   | Layout 2             | `e6ae841dbcfe`  |
| 2583   | Layout 2             | `e6ae841dbcfe`  |
| 2575   | Layout 2             | `e6ae841dbcfe`  |
| 2567   | Layout 2             | `e6ae841dbcfe`  |
| 2560   | Layout 2             | `e6ae841dbcfe`  |
| 2553   | Layout 2             | `e6ae841dbcfe`  |
| 2545   | Layout 2             | `e6ae841dbcfe`  |
| 2538   | Layout 2             | `e6ae841dbcfe`  |
| 2529   | Layout 2             | `e6ae841dbcfe`  |
| 2519   | Layout 2             | `e6ae841dbcfe`  |
| 2513   | Layout 2             | `e6ae841dbcfe`  |
| 2510   | Layout 2             | `e6ae841dbcfe`  |
| 2507   | Layout 2             | `e6ae841dbcfe`  |
| 2503   | Layout 2             | `e6ae841dbcfe`  |
| 2498   | Layout 2             | `e6ae841dbcfe`  |
| 2492   | Layout 2             | `e6ae841dbcfe`  |
| 2487   | Layout 2             | `e6ae841dbcfe`  |
| 2480   | Layout 2             | `e6ae841dbcfe`  |
| 2474   | Layout 2             | `e6ae841dbcfe`  |
| 2468   | Layout 2             | `e6ae841dbcfe`  |
| 2460   | Layout 2             | `e6ae841dbcfe`  |
| 2453   | Layout 2             | `e6ae841dbcfe`  |
| 2444   | Layout 2             | `e6ae841dbcfe`  |
| 2438   | Layout 2             | `e6ae841dbcfe`  |
| 2434   | Layout 2             | `e6ae841dbcfe`  |
| 2429   | Layout 2             | `e6ae841dbcfe`  |
| 2421   | Layout 2             | `e6ae841dbcfe`  |
| 2414   | Layout 2             | `e6ae841dbcfe`  |
| 2407   | Layout 2             | `e6ae841dbcfe`  |
| 2401   | Layout 2             | `e6ae841dbcfe`  |
| 2397   | Layout 2             | `e6ae841dbcfe`  |
| 2393   | Layout 2             | `e6ae841dbcfe`  |
| 2384   | Layout 2             | `e6ae841dbcfe`  |
| 2378   | Layout 2             | `e6ae841dbcfe`  |
| 2372   | Layout 2             | `e6ae841dbcfe`  |
| 2358   | Layout 2             | `e6ae841dbcfe`  |
| 2352   | Layout 2             | `e6ae841dbcfe`  |
| 2347   | Layout 2             | `e6ae841dbcfe`  |
| 2343   | Layout 2             | `e6ae841dbcfe`  |
| 2335   | Layout 2             | `e6ae841dbcfe`  |
| 2327   | Layout 2             | `e6ae841dbcfe`  |
| 2324   | Layout 2             | `e6ae841dbcfe`  |
| 2319   | Layout 2             | `e6ae841dbcfe`  |
| 2313   | Layout 2             | `e6ae841dbcfe`  |
| 2308   | Layout 2             | `e6ae841dbcfe`  |
| 2302   | Layout 2             | `e6ae841dbcfe`  |
| 2295   | Layout 2             | `e6ae841dbcfe`  |
| 2290   | Layout 2             | `e6ae841dbcfe`  |
| 2284   | Layout 2             | `e6ae841dbcfe`  |
| 2276   | Layout 2             | `e6ae841dbcfe`  |
| 2269   | Layout 2             | `e6ae841dbcfe`  |
| 2259   | Layout 2             | `e6ae841dbcfe`  |
| 2250   | Layout 2             | `e6ae841dbcfe`  |
| 2243   | Layout 2             | `e6ae841dbcfe`  |
| 2235   | Layout 2             | `e6ae841dbcfe`  |
| 2229   | Layout 2             | `e6ae841dbcfe`  |
| 2224   | Layout 2             | `e6ae841dbcfe`  |
| 2218   | Layout 2             | `e6ae841dbcfe`  |
| 2215   | Layout 2             | `e6ae841dbcfe`  |
| 2207   | Layout 2             | `e6ae841dbcfe`  |
| 2203   | Layout 2             | `e6ae841dbcfe`  |
| 2196   | Layout 2             | `e6ae841dbcfe`  |
| 2192   | Layout 2             | `e6ae841dbcfe`  |
| 2189   | Layout 2             | `e6ae841dbcfe`  |
| 2183   | Layout 2             | `e6ae841dbcfe`  |
| 2179   | Layout 2             | `e6ae841dbcfe`  |
| 2171   | Layout 2             | `e6ae841dbcfe`  |
| 2163   | Layout 2             | `e6ae841dbcfe`  |
| 2156   | Layout 2             | `e6ae841dbcfe`  |
| 2151   | Layout 2             | `e6ae841dbcfe`  |
| 2147   | Layout 2             | `e6ae841dbcfe`  |
| 2142   | Layout 2             | `e6ae841dbcfe`  |
| 2138   | Layout 2             | `e6ae841dbcfe`  |
| 2134   | Layout 2             | `e6ae841dbcfe`  |
| 2130   | Layout 2             | `e6ae841dbcfe`  |
| 2122   | Layout 2             | `e6ae841dbcfe`  |
| 2107   | Layout 2             | `e6ae841dbcfe`  |
| 2098   | Layout 2             | `e6ae841dbcfe`  |
| 2089   | Layout 2             | `e6ae841dbcfe`  |
| 2081   | Layout 2             | `e6ae841dbcfe`  |
| 2073   | Layout 2             | `e6ae841dbcfe`  |
| 2067   | Layout 2             | `e6ae841dbcfe`  |
| 2063   | Layout 2             | `e6ae841dbcfe`  |
| 2059   | Layout 2             | `e6ae841dbcfe`  |
| 2052   | Layout 2             | `e6ae841dbcfe`  |
| 2044   | Layout 2             | `e6ae841dbcfe`  |
| 2039   | Layout 2             | `e6ae841dbcfe`  |
| 2032   | Layout 2             | `e6ae841dbcfe`  |
| 2025   | Layout 2             | `e6ae841dbcfe`  |
| 2011   | Layout 2             | `e6ae841dbcfe`  |
| 2005   | Layout 2             | `e6ae841dbcfe`  |
| 2000   | Layout 2             | `e6ae841dbcfe`  |
| 1996   | Layout 2             | `e6ae841dbcfe`  |
| 1991   | Layout 2             | `e6ae841dbcfe`  |
| 1985   | Layout 2             | `e6ae841dbcfe`  |
| 1980   | Layout 2             | `e6ae841dbcfe`  |
| 1969   | Layout 2             | `e6ae841dbcfe`  |
| 1964   | Layout 2             | `e6ae841dbcfe`  |
| 1958   | Layout 2             | `e6ae841dbcfe`  |
| 1950   | Layout 2             | `e6ae841dbcfe`  |
| 1945   | Layout 2             | `e6ae841dbcfe`  |
| 1937   | Layout 2             | `e6ae841dbcfe`  |
| 1933   | Layout 2             | `e6ae841dbcfe`  |
| 1927   | Layout 2             | `e6ae841dbcfe`  |
| 1921   | Layout 2             | `e6ae841dbcfe`  |
| 1914   | Layout 2             | `e6ae841dbcfe`  |
| 1908   | Layout 2             | `e6ae841dbcfe`  |
| 1897   | Layout 2             | `e6ae841dbcfe`  |
| 1892   | Layout 2             | `e6ae841dbcfe`  |
| 1886   | Layout 2             | `e6ae841dbcfe`  |
| 1881   | Layout 2             | `e6ae841dbcfe`  |
| 1871   | Layout 2             | `e6ae841dbcfe`  |
| 1866   | Layout 2             | `e6ae841dbcfe`  |
| 1862   | Layout 2             | `e6ae841dbcfe`  |
| 1854   | Layout 2             | `e6ae841dbcfe`  |
| 1846   | Layout 2             | `e6ae841dbcfe`  |
| 1838   | Layout 2             | `e6ae841dbcfe`  |
| 1832   | Layout 2             | `e6ae841dbcfe`  |
| 1826   | Layout 2             | `e6ae841dbcfe`  |
| 1822   | Layout 2             | `e6ae841dbcfe`  |
| 1818   | Layout 2             | `e6ae841dbcfe`  |
| 1804   | Layout 2             | `e6ae841dbcfe`  |
| 1794   | Layout 2             | `e6ae841dbcfe`  |
| 1790   | Layout 1             | `e6ae841dbcfe`  |
| 1784   | Layout 1             | `e6ae841dbcfe`  |
| 1774   | Layout 1             | `e6ae841dbcfe`  |
| 1771   | Layout 1             | `e6ae841dbcfe`  |
| 1762   | Layout 1             | `e6ae841dbcfe`  |
| 1759   | Layout 1             | `e6ae841dbcfe`  |
| 1754   | Layout 1             | `e6ae841dbcfe`  |
| 1749   | Layout 1             | `e6ae841dbcfe`  |
| 1743   | Layout 1             | `e6ae841dbcfe`  |
| 1737   | Layout 1             | `e6ae841dbcfe`  |
| 1731   | Layout 1             | `e6ae841dbcfe`  |
| 1725   | Layout 1             | `e6ae841dbcfe`  |
| 1717   | Layout 1             | `e6ae841dbcfe`  |
| 1710   | Layout 1             | `e6ae841dbcfe`  |
| 1704   | Layout 1             | `e6ae841dbcfe`  |
| 1698   | Layout 1             | `e6ae841dbcfe`  |
| 1690   | Layout 1             | `e6ae841dbcfe`  |
| 1685   | Layout 1             | `e6ae841dbcfe`  |
| 1680   | Layout 1             | `e6ae841dbcfe`  |
| 1674   | Layout 1             | `e6ae841dbcfe`  |
| 1668   | Layout 1             | `e6ae841dbcfe`  |
| 1659   | Layout 1             | `e6ae841dbcfe`  |
| 1649   | Layout 1             | `e6ae841dbcfe`  |
| 1642   | Layout 1             | `e6ae841dbcfe`  |
| 1636   | Layout 1             | `e6ae841dbcfe`  |
| 1628   | Layout 1             | `e6ae841dbcfe`  |
| 1622   | Layout 1             | `e6ae841dbcfe`  |
| 1614   | Layout 1             | `e6ae841dbcfe`  |
| 1608   | Layout 1             | `e6ae841dbcfe`  |
| 1602   | Layout 1             | `e6ae841dbcfe`  |
| 1598   | No documented layout | `e6ae841dbcfe`  |
| 1594   | No documented layout | `e6ae841dbcfe`  |
| 1590   | No documented layout | `e6ae841dbcfe`  |
| 1587   | No documented layout | `e6ae841dbcfe`  |
| 1584   | No file              | `e6ae841dbcfe`  |
| 1579   | No file              | `e6ae841dbcfe`  |
| 1572   | No file              | `e6ae841dbcfe`  |
| 1565   | No file              | `e6ae841dbcfe`  |
| 1559   | No file              | `e6ae841dbcfe`  |
| 1554   | No file              | `e6ae841dbcfe`  |
| 1547   | No file              | `e6ae841dbcfe`  |
| 1537   | No file              | `e6ae841dbcfe`  |
| 1529   | No file              | `e6ae841dbcfe`  |
| 1524   | No file              | `e6ae841dbcfe`  |
| 1519   | No file              | `e6ae841dbcfe`  |
| 1509   | No file              | `e6ae841dbcfe`  |
| 1506   | No file              | `e6ae841dbcfe`  |
| 1504   | No file              | `e6ae841dbcfe`  |
| 1500   | No file              | `e6ae841dbcfe`  |
| 1493   | No file              | `e6ae841dbcfe`  |
| 1489   | No file              | `e6ae841dbcfe`  |
| 1485   | No file              | `e6ae841dbcfe`  |
| 1481   | No file              | `e6ae841dbcfe`  |
| 1474   | No file              | `e6ae841dbcfe`  |
| 1466   | No file              | `e6ae841dbcfe`  |
| 1462   | No file              | `e6ae841dbcfe`  |
| 1459   | No file              | `e6ae841dbcfe`  |
| 1453   | No file              | `e6ae841dbcfe`  |
| 1450   | No file              | `e6ae841dbcfe`  |
| 1445   | No file              | `e6ae841dbcfe`  |
| 1439   | No file              | `e6ae841dbcfe`  |
| 1433   | No file              | `e6ae841dbcfe`  |
| 1430   | No file              | `e6ae841dbcfe`  |
| 1426   | No file              | `e6ae841dbcfe`  |
| 1421   | No file              | `e6ae841dbcfe`  |
| 1417   | No file              | `e6ae841dbcfe`  |
| 1416   | No file              | `e6ae841dbcfe`  |
| 1409   | No file              | `e6ae841dbcfe`  |
| 1405   | No file              | `e6ae841dbcfe`  |
| 1401   | No file              | `e6ae841dbcfe`  |
| 1396   | No file              | `e6ae841dbcfe`  |
| 1391   | No file              | `e6ae841dbcfe`  |
| 1390   | No file              | `e6ae841dbcfe`  |
| 1386   | No file              | `e6ae841dbcfe`  |
| 1381   | No file              | `e6ae841dbcfe`  |
| 1379   | No file              | `e6ae841dbcfe`  |
| 1372   | No file              | `e6ae841dbcfe`  |
| 1366   | No file              | `e6ae841dbcfe`  |
| 1364   | No file              | `e6ae841dbcfe`  |
| 1363   | No file              | `e6ae841dbcfe`  |
| 1360   | No file              | `e6ae841dbcfe`  |
| 1358   | No file              | `e6ae841dbcfe`  |
| 1355   | No file              | `e6ae841dbcfe`  |
| 1351   | No file              | `e6ae841dbcfe`  |
| 1348   | No file              | `e6ae841dbcfe`  |
| 1346   | No file              | `e6ae841dbcfe`  |
| 1341   | No file              | `e6ae841dbcfe`  |
| 1340   | No file              | `e6ae841dbcfe`  |
| 1338   | No file              | `e6ae841dbcfe`  |
| 1335   | No file              | `e6ae841dbcfe`  |
| 1333   | No file              | `e6ae841dbcfe`  |
| 1329   | No file              | `e6ae841dbcfe`  |
| 1327   | No file              | `e6ae841dbcfe`  |
| 1324   | No file              | `e6ae841dbcfe`  |
| 1321   | No file              | `e6ae841dbcfe`  |
| 1319   | No file              | `e6ae841dbcfe`  |
| 1318   | No file              | `e6ae841dbcfe`  |
| 1316   | No file              | `e6ae841dbcfe`  |
| 1313   | No file              | `e6ae841dbcfe`  |
| 1311   | No file              | `e6ae841dbcfe`  |
| 1309   | No file              | `e6ae841dbcfe`  |
| 1304   | No file              | `e6ae841dbcfe`  |
| 1292   | No file              | `e6ae841dbcfe`  |
| 1286   | No file              | `e6ae841dbcfe`  |
| 1280   | No file              | `e6ae841dbcfe`  |
| 1276   | No file              | `e6ae841dbcfe`  |
| 1267   | No file              | `e6ae841dbcfe`  |
| 1261   | No file              | `e6ae841dbcfe`  |
| 1256   | No file              | `e6ae841dbcfe`  |
| 1250   | No file              | `e6ae841dbcfe`  |
| 1246   | No file              | `e6ae841dbcfe`  |
| 1239   | No file              | `e6ae841dbcfe`  |
| 1230   | No file              | `e6ae841dbcfe`  |
| 1226   | No file              | `e6ae841dbcfe`  |
| 1220   | No file              | `e6ae841dbcfe`  |
| 1217   | No file              | `e6ae841dbcfe`  |
| 1211   | No file              | `e6ae841dbcfe`  |
| 1210   | No file              | `e6ae841dbcfe`  |
| 1208   | No file              | `e6ae841dbcfe`  |
| 1203   | No file              | `e6ae841dbcfe`  |
| 1197   | No file              | `e6ae841dbcfe`  |
| 1194   | No file              | `e6ae841dbcfe`  |
| 1192   | No file              | `e6ae841dbcfe`  |
| 1187   | No file              | `e6ae841dbcfe`  |
| 1183   | No file              | `e6ae841dbcfe`  |
| 1177   | No file              | `e6ae841dbcfe`  |
| 1173   | No file              | `e6ae841dbcfe`  |
| 1167   | No file              | `e6ae841dbcfe`  |
| 1164   | No file              | `e6ae841dbcfe`  |
| 1156   | No file              | `e6ae841dbcfe`  |
| 1149   | No file              | `e6ae841dbcfe`  |
| 1144   | No file              | `e6ae841dbcfe`  |
| 1137   | No file              | `e6ae841dbcfe`  |
| 1132   | No file              | `e6ae841dbcfe`  |
| 1127   | No file              | `e6ae841dbcfe`  |
| 1122   | No file              | `e6ae841dbcfe`  |
| 1118   | No file              | `e6ae841dbcfe`  |
| 1114   | No file              | `e6ae841dbcfe`  |
| 1109   | No file              | `e6ae841dbcfe`  |
| 1102   | No file              | `e6ae841dbcfe`  |
| 1096   | No file              | `e6ae841dbcfe`  |
| 1088   | No file              | `e6ae841dbcfe`  |
| 1081   | No file              | `e6ae841dbcfe`  |
| 1076   | No file              | `e6ae841dbcfe`  |
| 1069   | No file              | `e6ae841dbcfe`  |
| 1064   | No file              | `e6ae841dbcfe`  |
| 1058   | No file              | `e6ae841dbcfe`  |
| 1051   | No file              | `e6ae841dbcfe`  |
| 1044   | No file              | `e6ae841dbcfe`  |
| 1036   | No file              | `e6ae841dbcfe`  |
| 1026   | No file              | `e6ae841dbcfe`  |
| 1016   | No file              | `e6ae841dbcfe`  |
| 1009   | No file              | `e6ae841dbcfe`  |
| 1005   | No file              | `e6ae841dbcfe`  |
| 1000   | No file              | `e6ae841dbcfe`  |
| 998    | No file              | `e6ae841dbcfe`  |
| 990    | No file              | `e6ae841dbcfe`  |
| 979    | No file              | `e6ae841dbcfe`  |
| 972    | No file              | `e6ae841dbcfe`  |
| 963    | No file              | `e6ae841dbcfe`  |
| 955    | No file              | `e6ae841dbcfe`  |
| 946    | No file              | `e6ae841dbcfe`  |
| 938    | No file              | `e6ae841dbcfe`  |
| 927    | No file              | `e6ae841dbcfe`  |
| 911    | No file              | `e6ae841dbcfe`  |
| 904    | No file              | `e6ae841dbcfe`  |
| 899    | No file              | `e6ae841dbcfe`  |
| 894    | No file              | `e6ae841dbcfe`  |
| 885    | No file              | `e6ae841dbcfe`  |
| 879    | No file              | `e6ae841dbcfe`  |
| 872    | No file              | `e6ae841dbcfe`  |
| 864    | No file              | `e6ae841dbcfe`  |
| 855    | No file              | `e6ae841dbcfe`  |
| 853    | No file              | `e6ae841dbcfe`  |
| 845    | No file              | `e6ae841dbcfe`  |
| 837    | No file              | `e6ae841dbcfe`  |
| 829    | No file              | `e6ae841dbcfe`  |
| 822    | No file              | `e6ae841dbcfe`  |
| 814    | No file              | `e6ae841dbcfe`  |
| 805    | No file              | `e6ae841dbcfe`  |
| 794    | No file              | `e6ae841dbcfe`  |
| 787    | No file              | `e6ae841dbcfe`  |
| 780    | No file              | `e6ae841dbcfe`  |
| 771    | No file              | `e6ae841dbcfe`  |
| 760    | No file              | `e6ae841dbcfe`  |
| 748    | No file              | `e6ae841dbcfe`  |
| 741    | No file              | `e6ae841dbcfe`  |
| 736    | No file              | `e6ae841dbcfe`  |
| 731    | No file              | `e6ae841dbcfe`  |
| 723    | No file              | `e6ae841dbcfe`  |
| 711    | No file              | `e6ae841dbcfe`  |
| 707    | No file              | `e6ae841dbcfe`  |
| 697    | No file              | `e6ae841dbcfe`  |
| 689    | No file              | `e6ae841dbcfe`  |
| 683    | No file              | `e6ae841dbcfe`  |
| 678    | No file              | `e6ae841dbcfe`  |
| 670    | No file              | `e6ae841dbcfe`  |
| 661    | No file              | `e6ae841dbcfe`  |
| 656    | No file              | `e6ae841dbcfe`  |
| 652    | No file              | `e6ae841dbcfe`  |
| 643    | No file              | `e6ae841dbcfe`  |
| 637    | No file              | `e6ae841dbcfe`  |
| 630    | No file              | `e6ae841dbcfe`  |
| 627    | No file              | `e6ae841dbcfe`  |
| 621    | No file              | `e6ae841dbcfe`  |
| 617    | No file              | `e6ae841dbcfe`  |
| 615    | No file              | `e6ae841dbcfe`  |
| 606    | No file              | `e6ae841dbcfe`  |
| 599    | No file              | `e6ae841dbcfe`  |
| 592    | No file              | `e6ae841dbcfe`  |
| 586    | No file              | `e6ae841dbcfe`  |
| 577    | No file              | `e6ae841dbcfe`  |
| 569    | No file              | `e6ae841dbcfe`  |
| 561    | No file              | `e6ae841dbcfe`  |
| 554    | No file              | `e6ae841dbcfe`  |
| 542    | No file              | `e6ae841dbcfe`  |
| 532    | No file              | `e6ae841dbcfe`  |
| 531    | No file              | `e6ae841dbcfe`  |
| 526    | No file              | `e6ae841dbcfe`  |
| 521    | No file              | `e6ae841dbcfe`  |
| 517    | No file              | `e6ae841dbcfe`  |
| 510    | No file              | `e6ae841dbcfe`  |
| 508    | No file              | `e6ae841dbcfe`  |
| 504    | No file              | `e6ae841dbcfe`  |
| 497    | No file              | `e6ae841dbcfe`  |
| 491    | No file              | `e6ae841dbcfe`  |
| 485    | No file              | `e6ae841dbcfe`  |
| 478    | No file              | `e6ae841dbcfe`  |
| 472    | No file              | `e6ae841dbcfe`  |
| 466    | No file              | `e6ae841dbcfe`  |
| 457    | No file              | `e6ae841dbcfe`  |
| 452    | No file              | `e6ae841dbcfe`  |
| 449    | No file              | `e6ae841dbcfe`  |
| 435    | No file              | `e6ae841dbcfe`  |

<!-- versions:end -->

## Companion Files

| File                                | Required | Role                                                                     |
| ----------------------------------- | -------- | ------------------------------------------------------------------------ |
| `restrictcontentsregionoffset.dbss` | Optional | `region_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`               | Optional | Region names (LOC type 17)                                               |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (13 bytes)

| Offset  | Type | Field                | Notes                                                        |
| ------- | ---- | -------------------- | ------------------------------------------------------------ |
| `+0x00` | u16  | region_key           | A `regioninfo.bss` region; LOC type 17 names every key of client 3474 |
| `+0x02` | u16  | region_key_dup       | Equal to `region_key`; the offset file points here           |
| `+0x04` | u8   | ban_maid             | `1`: no maid here; `0` on every row of client 3474            |
| `+0x05` | u8   | ban_world_map        | `1`: no world map                                            |
| `+0x06` | u8   | ban_character_change | `1`: no character change                                     |
| `+0x07` | u8   | ban_muster           | `1`: no muster                                               |
| `+0x08` | u8   | ban_camp             | `1`: no camp; `0` on every row of clients 1784 and 3474       |
| `+0x09` | u8   | ban_compass          | `1`: no compass                                              |
| `+0x0A` | u8   | ban_item_map         | `1`: no item map                                             |
| `+0x0B` | u8   | ban_mini_map         | `1`: no minimap                                              |
| `+0x0C` | u8   | unknown_0c           | `0` on every row of client 3474; not in client 1784           |

The rows are not sorted by key.

### `restrictcontentsregionoffset.dbss`

Bare offset table into `restrictcontentsregion.dbss` (no PABR magic, no
trailer).

| Offset  | Type              | Field | Notes                                         |
| ------- | ----------------- | ----- | --------------------------------------------- |
| `+0x00` | u32               | count | Equals the `restrictcontentsregion.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                                |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                        |
| ------- | ---- | ----------- | ------------------------------------------------------------ |
| `+0x00` | u16  | region_key  | Key of the row it points at                                  |
| `+0x02` | u32  | data_offset | Row start + 2, at `region_key_dup`                           |
| `+0x06` | u32  | data_size   | The row without its leading `region_key`: `11` on client 3474 |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. The index
rows are in another order than the file; on clients 1784 and 3474 every
index row points at the row with its key.

## Layout 1

Client 1784 rows have no `unknown_0c`. The offset rows have the same
layout, with `data_size` `10`.

### Row (12 bytes)

| Offset  | Type | Field                | Notes                                  |
| ------- | ---- | -------------------- | -------------------------------------- |
| `+0x00` | u16  | region_key           |                                        |
| `+0x02` | u16  | region_key_dup       |                                        |
| `+0x04` | u8   | ban_maid             | `1` on every row of client 1784        |
| `+0x05` | u8   | ban_world_map        |                                        |
| `+0x06` | u8   | ban_character_change |                                        |
| `+0x07` | u8   | ban_muster           |                                        |
| `+0x08` | u8   | ban_camp             |                                        |
| `+0x09` | u8   | ban_compass          |                                        |
| `+0x0A` | u8   | ban_item_map         |                                        |
| `+0x0B` | u8   | ban_mini_map         | `1` on `1078` and `1081` only           |

## Field Names

The flags are the `Ban_Function` sheet of a private server's
`DataSheets.bexcel` on client 1784: `RegionGroupKey`, then `Ban_Maid`,
`Ban_WorldMap`, `Ban_CharacterChange`, `Ban_Muster`, `Ban_Camp`,
`Ban_Compass`, `Ban_ItemMap` and `Ban_MiniMap`. Its 24 rows match the
client 1784 file on all 24 keys and all eight flags (an empty `Ban_Camp`
cell is `0`). The client 1784 server dump (`Instance_dumpFull.exe`) reads
the eight columns with its bool reader into consecutive bytes of the row in
this order (loader at VA `0x1408fad80`). Its check messages name the key
`_regionKey` and log "존재하지 않는 지역입니다" ("a region that does not exist")
for an unknown key, so the key is a region key, not a region group key.

Client 3474 keeps the 24 keys of client 1784 and adds 24, and its flags
differ: `ban_maid` is `0` on every row, `ban_world_map` `1` on every row,
and character change, muster, compass and item map are banned together on
7 rows (`1084`, `1542`, `1546` to `1550`). Rows `1078` and `1081`, the two
with `Ban_MiniMap` on client 1784, still ban the minimap (11 rows do),
which places the flags at the same offsets and the new byte at the end.

## Notes

- The Lua names three of the flags: `__eRestrictContentsType_Maid`,
  `__eRestrictContentsType_WorldMap` and `__eRestrictContentsType_MiniMap`
  (`panel_window_maidlist_all_1.luac`, `new_worldmap.luac`,
  `worldminimap.luac`, `radar.luac`). The enum values are set by the
  client, not the Lua.
- `ToClient_RestrictContentsByRegionWithKey` takes a region key as well, and
  the symbol `eErrNoRestrictContentsByRegion` is the message the Lua shows
  when a function is blocked.

## Open Questions

### unknown_0c

Client 3474 added a ninth byte, `0` on all 48 rows. No sheet of client 1784
has a ninth `Ban_*` column, and the Lua names only three
`__eRestrictContentsType_*` values.
