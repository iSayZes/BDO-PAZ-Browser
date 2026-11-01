# `cashproduct_grouplist.bss` Format

## Purpose

The Pearl Shop offer groups: per offer group the
[`cashproduct.dbss`](../dbss/cashproduct_dbss.md) products that share it, such as
the pieces of one outfit set or the stack sizes of one item. The Pearl Shop
Lua (`panel_ingamecashshop.luac`, `panel_pearlshop.luac`) reads a
product's group with `cashProduct:getOfferGroup()`, then the members with
`getCashProductStaticStatusGroupListCount(offerGroup)` and
`getCashProductStaticStatusGroupByIndex(offerGroup, index)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                        | Bytes  | Records   | Row bytes                |
| ------ | -------------- | --------------------------- | ------ | --------- | ------------------------ |
| 1      | 1327 and later | `cashproduct_grouplist.bss` | 89,704 | 3,007 Row | 12 to 128, 30 on average |

| Layout | File                        | Known             | Unknown    |
| ------ | --------------------------- | ----------------- | ---------- |
| 1      | `cashproduct_grouplist.bss` | 89,704 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `489c9951e390`  |
| 3482   | Layout 1             | `489c9951e390`  |
| 3474   | Layout 1             | `489c9951e390`  |
| 3473   | Layout 1             | `489c9951e390`  |
| 3464   | Layout 1             | `489c9951e390`  |
| 3458   | Layout 1             | `489c9951e390`  |
| 3454   | Layout 1             | `489c9951e390`  |
| 3444   | Layout 1             | `489c9951e390`  |
| 3435   | Layout 1             | `489c9951e390`  |
| 3426   | Layout 1             | `489c9951e390`  |
| 3418   | Layout 1             | `489c9951e390`  |
| 3412   | Layout 1             | `489c9951e390`  |
| 3402   | Layout 1             | `489c9951e390`  |
| 3396   | Layout 1             | `489c9951e390`  |
| 3387   | Layout 1             | `489c9951e390`  |
| 3381   | Layout 1             | `489c9951e390`  |
| 3373   | Layout 1             | `489c9951e390`  |
| 3364   | Layout 1             | `489c9951e390`  |
| 3356   | Layout 1             | `489c9951e390`  |
| 3349   | Layout 1             | `489c9951e390`  |
| 3342   | Layout 1             | `489c9951e390`  |
| 3335   | Layout 1             | `489c9951e390`  |
| 3326   | Layout 1             | `489c9951e390`  |
| 3321   | Layout 1             | `489c9951e390`  |
| 3314   | Layout 1             | `489c9951e390`  |
| 3303   | Layout 1             | `489c9951e390`  |
| 3302   | Layout 1             | `489c9951e390`  |
| 3293   | Layout 1             | `489c9951e390`  |
| 3283   | Layout 1             | `489c9951e390`  |
| 3275   | Layout 1             | `489c9951e390`  |
| 3267   | Layout 1             | `489c9951e390`  |
| 3258   | Layout 1             | `489c9951e390`  |
| 3251   | Layout 1             | `489c9951e390`  |
| 3242   | Layout 1             | `489c9951e390`  |
| 3235   | Layout 1             | `489c9951e390`  |
| 3229   | Layout 1             | `489c9951e390`  |
| 3212   | Layout 1             | `489c9951e390`  |
| 3203   | Layout 1             | `489c9951e390`  |
| 3193   | Layout 1             | `489c9951e390`  |
| 3186   | Layout 1             | `489c9951e390`  |
| 3177   | Layout 1             | `489c9951e390`  |
| 3169   | Layout 1             | `489c9951e390`  |
| 3158   | Layout 1             | `489c9951e390`  |
| 3151   | Layout 1             | `489c9951e390`  |
| 3144   | Layout 1             | `489c9951e390`  |
| 3133   | Layout 1             | `489c9951e390`  |
| 3125   | Layout 1             | `489c9951e390`  |
| 3118   | Layout 1             | `489c9951e390`  |
| 3111   | Layout 1             | `489c9951e390`  |
| 3103   | Layout 1             | `489c9951e390`  |
| 3095   | Layout 1             | `489c9951e390`  |
| 3086   | Layout 1             | `489c9951e390`  |
| 3072   | Layout 1             | `489c9951e390`  |
| 3062   | Layout 1             | `489c9951e390`  |
| 3052   | Layout 1             | `489c9951e390`  |
| 3045   | Layout 1             | `489c9951e390`  |
| 3037   | Layout 1             | `489c9951e390`  |
| 3030   | Layout 1             | `489c9951e390`  |
| 3021   | Layout 1             | `489c9951e390`  |
| 3012   | Layout 1             | `489c9951e390`  |
| 3002   | Layout 1             | `489c9951e390`  |
| 2995   | Layout 1             | `489c9951e390`  |
| 2987   | Layout 1             | `489c9951e390`  |
| 2978   | Layout 1             | `489c9951e390`  |
| 2970   | Layout 1             | `489c9951e390`  |
| 2959   | Layout 1             | `489c9951e390`  |
| 2951   | Layout 1             | `489c9951e390`  |
| 2942   | Layout 1             | `489c9951e390`  |
| 2935   | Layout 1             | `489c9951e390`  |
| 2932   | Layout 1             | `489c9951e390`  |
| 2923   | Layout 1             | `489c9951e390`  |
| 2919   | Layout 1             | `489c9951e390`  |
| 2907   | Layout 1             | `489c9951e390`  |
| 2900   | Layout 1             | `489c9951e390`  |
| 2891   | Layout 1             | `489c9951e390`  |
| 2882   | Layout 1             | `489c9951e390`  |
| 2872   | Layout 1             | `489c9951e390`  |
| 2863   | Layout 1             | `489c9951e390`  |
| 2855   | Layout 1             | `489c9951e390`  |
| 2849   | Layout 1             | `489c9951e390`  |
| 2844   | Layout 1             | `489c9951e390`  |
| 2834   | Layout 1             | `489c9951e390`  |
| 2825   | Layout 1             | `489c9951e390`  |
| 2819   | Layout 1             | `489c9951e390`  |
| 2811   | Layout 1             | `489c9951e390`  |
| 2803   | Layout 1             | `489c9951e390`  |
| 2794   | Layout 1             | `489c9951e390`  |
| 2783   | Layout 1             | `489c9951e390`  |
| 2774   | Layout 1             | `489c9951e390`  |
| 2765   | Layout 1             | `489c9951e390`  |
| 2756   | Layout 1             | `489c9951e390`  |
| 2750   | Layout 1             | `489c9951e390`  |
| 2743   | Layout 1             | `489c9951e390`  |
| 2736   | Layout 1             | `489c9951e390`  |
| 2726   | Layout 1             | `489c9951e390`  |
| 2717   | Layout 1             | `489c9951e390`  |
| 2709   | Layout 1             | `489c9951e390`  |
| 2703   | Layout 1             | `489c9951e390`  |
| 2695   | Layout 1             | `489c9951e390`  |
| 2684   | Layout 1             | `489c9951e390`  |
| 2672   | Layout 1             | `489c9951e390`  |
| 2665   | Layout 1             | `489c9951e390`  |
| 2657   | Layout 1             | `489c9951e390`  |
| 2649   | Layout 1             | `489c9951e390`  |
| 2644   | Layout 1             | `489c9951e390`  |
| 2637   | Layout 1             | `489c9951e390`  |
| 2629   | Layout 1             | `489c9951e390`  |
| 2619   | Layout 1             | `489c9951e390`  |
| 2612   | Layout 1             | `489c9951e390`  |
| 2606   | Layout 1             | `489c9951e390`  |
| 2602   | Layout 1             | `489c9951e390`  |
| 2601   | Layout 1             | `489c9951e390`  |
| 2592   | Layout 1             | `489c9951e390`  |
| 2583   | Layout 1             | `489c9951e390`  |
| 2575   | Layout 1             | `489c9951e390`  |
| 2567   | Layout 1             | `489c9951e390`  |
| 2560   | Layout 1             | `489c9951e390`  |
| 2553   | Layout 1             | `489c9951e390`  |
| 2545   | Layout 1             | `489c9951e390`  |
| 2538   | Layout 1             | `489c9951e390`  |
| 2529   | Layout 1             | `489c9951e390`  |
| 2519   | Layout 1             | `489c9951e390`  |
| 2513   | Layout 1             | `489c9951e390`  |
| 2510   | Layout 1             | `489c9951e390`  |
| 2507   | Layout 1             | `489c9951e390`  |
| 2503   | Layout 1             | `489c9951e390`  |
| 2498   | Layout 1             | `489c9951e390`  |
| 2492   | Layout 1             | `489c9951e390`  |
| 2487   | Layout 1             | `489c9951e390`  |
| 2480   | Layout 1             | `489c9951e390`  |
| 2474   | Layout 1             | `489c9951e390`  |
| 2468   | Layout 1             | `489c9951e390`  |
| 2460   | Layout 1             | `489c9951e390`  |
| 2453   | Layout 1             | `489c9951e390`  |
| 2444   | Layout 1             | `489c9951e390`  |
| 2438   | Layout 1             | `489c9951e390`  |
| 2434   | Layout 1             | `489c9951e390`  |
| 2429   | Layout 1             | `489c9951e390`  |
| 2421   | Layout 1             | `489c9951e390`  |
| 2414   | Layout 1             | `489c9951e390`  |
| 2407   | Layout 1             | `489c9951e390`  |
| 2401   | Layout 1             | `489c9951e390`  |
| 2397   | Layout 1             | `489c9951e390`  |
| 2393   | Layout 1             | `489c9951e390`  |
| 2384   | Layout 1             | `489c9951e390`  |
| 2378   | Layout 1             | `489c9951e390`  |
| 2372   | Layout 1             | `489c9951e390`  |
| 2358   | Layout 1             | `489c9951e390`  |
| 2352   | Layout 1             | `489c9951e390`  |
| 2347   | Layout 1             | `489c9951e390`  |
| 2343   | Layout 1             | `489c9951e390`  |
| 2335   | Layout 1             | `489c9951e390`  |
| 2327   | Layout 1             | `489c9951e390`  |
| 2324   | Layout 1             | `489c9951e390`  |
| 2319   | Layout 1             | `489c9951e390`  |
| 2313   | Layout 1             | `489c9951e390`  |
| 2308   | Layout 1             | `489c9951e390`  |
| 2302   | Layout 1             | `489c9951e390`  |
| 2295   | Layout 1             | `489c9951e390`  |
| 2290   | Layout 1             | `489c9951e390`  |
| 2284   | Layout 1             | `489c9951e390`  |
| 2276   | Layout 1             | `489c9951e390`  |
| 2269   | Layout 1             | `489c9951e390`  |
| 2259   | Layout 1             | `489c9951e390`  |
| 2250   | Layout 1             | `489c9951e390`  |
| 2243   | Layout 1             | `489c9951e390`  |
| 2235   | Layout 1             | `489c9951e390`  |
| 2229   | Layout 1             | `489c9951e390`  |
| 2224   | Layout 1             | `489c9951e390`  |
| 2218   | Layout 1             | `489c9951e390`  |
| 2215   | Layout 1             | `489c9951e390`  |
| 2207   | Layout 1             | `489c9951e390`  |
| 2203   | Layout 1             | `489c9951e390`  |
| 2196   | Layout 1             | `489c9951e390`  |
| 2192   | Layout 1             | `489c9951e390`  |
| 2189   | Layout 1             | `489c9951e390`  |
| 2183   | Layout 1             | `489c9951e390`  |
| 2179   | Layout 1             | `489c9951e390`  |
| 2171   | Layout 1             | `489c9951e390`  |
| 2163   | Layout 1             | `489c9951e390`  |
| 2156   | Layout 1             | `489c9951e390`  |
| 2151   | Layout 1             | `489c9951e390`  |
| 2147   | Layout 1             | `489c9951e390`  |
| 2142   | Layout 1             | `489c9951e390`  |
| 2138   | Layout 1             | `489c9951e390`  |
| 2134   | Layout 1             | `489c9951e390`  |
| 2130   | Layout 1             | `489c9951e390`  |
| 2122   | Layout 1             | `489c9951e390`  |
| 2107   | Layout 1             | `489c9951e390`  |
| 2098   | Layout 1             | `489c9951e390`  |
| 2089   | Layout 1             | `489c9951e390`  |
| 2081   | Layout 1             | `489c9951e390`  |
| 2073   | Layout 1             | `489c9951e390`  |
| 2067   | Layout 1             | `489c9951e390`  |
| 2063   | Layout 1             | `489c9951e390`  |
| 2059   | Layout 1             | `489c9951e390`  |
| 2052   | Layout 1             | `489c9951e390`  |
| 2044   | Layout 1             | `489c9951e390`  |
| 2039   | Layout 1             | `489c9951e390`  |
| 2032   | Layout 1             | `489c9951e390`  |
| 2025   | Layout 1             | `489c9951e390`  |
| 2011   | Layout 1             | `489c9951e390`  |
| 2005   | Layout 1             | `489c9951e390`  |
| 2000   | Layout 1             | `489c9951e390`  |
| 1996   | Layout 1             | `489c9951e390`  |
| 1991   | Layout 1             | `489c9951e390`  |
| 1985   | Layout 1             | `489c9951e390`  |
| 1980   | Layout 1             | `489c9951e390`  |
| 1969   | Layout 1             | `489c9951e390`  |
| 1964   | Layout 1             | `489c9951e390`  |
| 1958   | Layout 1             | `489c9951e390`  |
| 1950   | Layout 1             | `489c9951e390`  |
| 1945   | Layout 1             | `489c9951e390`  |
| 1937   | Layout 1             | `489c9951e390`  |
| 1933   | Layout 1             | `489c9951e390`  |
| 1927   | Layout 1             | `489c9951e390`  |
| 1921   | Layout 1             | `489c9951e390`  |
| 1914   | Layout 1             | `489c9951e390`  |
| 1908   | Layout 1             | `489c9951e390`  |
| 1897   | Layout 1             | `489c9951e390`  |
| 1892   | Layout 1             | `489c9951e390`  |
| 1886   | Layout 1             | `489c9951e390`  |
| 1881   | Layout 1             | `489c9951e390`  |
| 1871   | Layout 1             | `489c9951e390`  |
| 1866   | Layout 1             | `489c9951e390`  |
| 1862   | Layout 1             | `489c9951e390`  |
| 1854   | Layout 1             | `489c9951e390`  |
| 1846   | Layout 1             | `489c9951e390`  |
| 1838   | Layout 1             | `489c9951e390`  |
| 1832   | Layout 1             | `489c9951e390`  |
| 1826   | Layout 1             | `489c9951e390`  |
| 1822   | Layout 1             | `489c9951e390`  |
| 1818   | Layout 1             | `489c9951e390`  |
| 1804   | Layout 1             | `489c9951e390`  |
| 1794   | Layout 1             | `489c9951e390`  |
| 1790   | Layout 1             | `489c9951e390`  |
| 1784   | Layout 1             | `489c9951e390`  |
| 1774   | Layout 1             | `489c9951e390`  |
| 1771   | Layout 1             | `489c9951e390`  |
| 1762   | Layout 1             | `489c9951e390`  |
| 1759   | Layout 1             | `489c9951e390`  |
| 1754   | Layout 1             | `489c9951e390`  |
| 1749   | Layout 1             | `489c9951e390`  |
| 1743   | Layout 1             | `489c9951e390`  |
| 1737   | Layout 1             | `489c9951e390`  |
| 1731   | Layout 1             | `489c9951e390`  |
| 1725   | Layout 1             | `489c9951e390`  |
| 1717   | Layout 1             | `489c9951e390`  |
| 1710   | Layout 1             | `489c9951e390`  |
| 1704   | Layout 1             | `489c9951e390`  |
| 1698   | Layout 1             | `489c9951e390`  |
| 1690   | Layout 1             | `489c9951e390`  |
| 1685   | Layout 1             | `489c9951e390`  |
| 1680   | Layout 1             | `489c9951e390`  |
| 1674   | Layout 1             | `489c9951e390`  |
| 1668   | Layout 1             | `489c9951e390`  |
| 1659   | Layout 1             | `489c9951e390`  |
| 1649   | Layout 1             | `489c9951e390`  |
| 1642   | Layout 1             | `489c9951e390`  |
| 1636   | Layout 1             | `489c9951e390`  |
| 1628   | Layout 1             | `489c9951e390`  |
| 1622   | Layout 1             | `489c9951e390`  |
| 1614   | Layout 1             | `489c9951e390`  |
| 1608   | Layout 1             | `489c9951e390`  |
| 1602   | Layout 1             | `489c9951e390`  |
| 1598   | Layout 1             | `489c9951e390`  |
| 1594   | Layout 1             | `489c9951e390`  |
| 1590   | Layout 1             | `489c9951e390`  |
| 1587   | Layout 1             | `489c9951e390`  |
| 1584   | Layout 1             | `489c9951e390`  |
| 1579   | Layout 1             | `489c9951e390`  |
| 1572   | Layout 1             | `489c9951e390`  |
| 1565   | Layout 1             | `489c9951e390`  |
| 1559   | Layout 1             | `489c9951e390`  |
| 1554   | Layout 1             | `489c9951e390`  |
| 1547   | Layout 1             | `489c9951e390`  |
| 1537   | Layout 1             | `489c9951e390`  |
| 1529   | Layout 1             | `489c9951e390`  |
| 1524   | Layout 1             | `489c9951e390`  |
| 1519   | Layout 1             | `489c9951e390`  |
| 1509   | Layout 1             | `489c9951e390`  |
| 1506   | Layout 1             | `489c9951e390`  |
| 1504   | Layout 1             | `489c9951e390`  |
| 1500   | Layout 1             | `489c9951e390`  |
| 1493   | Layout 1             | `489c9951e390`  |
| 1489   | Layout 1             | `489c9951e390`  |
| 1485   | Layout 1             | `489c9951e390`  |
| 1481   | Layout 1             | `489c9951e390`  |
| 1474   | Layout 1             | `489c9951e390`  |
| 1466   | Layout 1             | `489c9951e390`  |
| 1462   | Layout 1             | `489c9951e390`  |
| 1459   | Layout 1             | `489c9951e390`  |
| 1453   | Layout 1             | `489c9951e390`  |
| 1450   | Layout 1             | `489c9951e390`  |
| 1445   | Layout 1             | `489c9951e390`  |
| 1439   | Layout 1             | `489c9951e390`  |
| 1433   | Layout 1             | `489c9951e390`  |
| 1430   | Layout 1             | `489c9951e390`  |
| 1426   | Layout 1             | `489c9951e390`  |
| 1421   | Layout 1             | `489c9951e390`  |
| 1417   | Layout 1             | `489c9951e390`  |
| 1416   | Layout 1             | `489c9951e390`  |
| 1409   | Layout 1             | `489c9951e390`  |
| 1405   | Layout 1             | `489c9951e390`  |
| 1401   | Layout 1             | `489c9951e390`  |
| 1396   | Layout 1             | `489c9951e390`  |
| 1391   | Layout 1             | `489c9951e390`  |
| 1390   | Layout 1             | `489c9951e390`  |
| 1386   | Layout 1             | `489c9951e390`  |
| 1381   | Layout 1             | `489c9951e390`  |
| 1379   | Layout 1             | `489c9951e390`  |
| 1372   | Layout 1             | `489c9951e390`  |
| 1366   | Layout 1             | `489c9951e390`  |
| 1364   | Layout 1             | `489c9951e390`  |
| 1363   | Layout 1             | `489c9951e390`  |
| 1360   | Layout 1             | `489c9951e390`  |
| 1358   | Layout 1             | `489c9951e390`  |
| 1355   | Layout 1             | `489c9951e390`  |
| 1351   | Layout 1             | `489c9951e390`  |
| 1348   | Layout 1             | `489c9951e390`  |
| 1346   | Layout 1             | `489c9951e390`  |
| 1341   | Layout 1             | `489c9951e390`  |
| 1340   | Layout 1             | `489c9951e390`  |
| 1338   | Layout 1             | `489c9951e390`  |
| 1335   | Layout 1             | `489c9951e390`  |
| 1333   | Layout 1             | `489c9951e390`  |
| 1329   | Layout 1             | `489c9951e390`  |
| 1327   | Layout 1             | `489c9951e390`  |
| 1324   | No documented layout | `489c9951e390`  |
| 1321   | No documented layout | `489c9951e390`  |
| 1319   | No documented layout | `489c9951e390`  |
| 1318   | No documented layout | `489c9951e390`  |
| 1316   | No documented layout | `489c9951e390`  |
| 1313   | No documented layout | `489c9951e390`  |
| 1311   | No documented layout | `489c9951e390`  |
| 1309   | No documented layout | `489c9951e390`  |
| 1304   | No documented layout | `489c9951e390`  |
| 1292   | No documented layout | `489c9951e390`  |
| 1286   | No documented layout | `489c9951e390`  |
| 1280   | No documented layout | `489c9951e390`  |
| 1276   | No documented layout | `489c9951e390`  |
| 1267   | No documented layout | `489c9951e390`  |
| 1261   | No documented layout | `489c9951e390`  |
| 1256   | No documented layout | `489c9951e390`  |
| 1250   | No documented layout | `489c9951e390`  |
| 1246   | No documented layout | `489c9951e390`  |
| 1239   | No documented layout | `489c9951e390`  |
| 1230   | No documented layout | `489c9951e390`  |
| 1226   | No documented layout | `489c9951e390`  |
| 1220   | No documented layout | `489c9951e390`  |
| 1217   | No documented layout | `489c9951e390`  |
| 1211   | No documented layout | `489c9951e390`  |
| 1210   | No documented layout | `489c9951e390`  |
| 1208   | No documented layout | `489c9951e390`  |
| 1203   | No documented layout | `489c9951e390`  |
| 1197   | No documented layout | `489c9951e390`  |
| 1194   | No documented layout | `489c9951e390`  |
| 1192   | No documented layout | `489c9951e390`  |
| 1187   | No documented layout | `489c9951e390`  |
| 1183   | No documented layout | `489c9951e390`  |
| 1177   | No documented layout | `489c9951e390`  |
| 1173   | No documented layout | `489c9951e390`  |
| 1167   | No documented layout | `489c9951e390`  |
| 1164   | No documented layout | `489c9951e390`  |
| 1156   | No documented layout | `489c9951e390`  |
| 1149   | No documented layout | `489c9951e390`  |
| 1144   | No documented layout | `489c9951e390`  |
| 1137   | No documented layout | `489c9951e390`  |
| 1132   | No documented layout | `489c9951e390`  |
| 1127   | No documented layout | `489c9951e390`  |
| 1122   | No documented layout | `489c9951e390`  |
| 1118   | No documented layout | `489c9951e390`  |
| 1114   | No documented layout | `489c9951e390`  |
| 1109   | No documented layout | `489c9951e390`  |
| 1102   | No documented layout | `489c9951e390`  |
| 1096   | No documented layout | `489c9951e390`  |
| 1088   | No documented layout | `489c9951e390`  |
| 1081   | No documented layout | `489c9951e390`  |
| 1076   | No documented layout | `489c9951e390`  |
| 1069   | No documented layout | `489c9951e390`  |
| 1064   | No documented layout | `489c9951e390`  |
| 1058   | No documented layout | `489c9951e390`  |
| 1051   | No documented layout | `489c9951e390`  |
| 1044   | No documented layout | `489c9951e390`  |
| 1036   | No documented layout | `489c9951e390`  |
| 1026   | No documented layout | `489c9951e390`  |
| 1016   | No documented layout | `489c9951e390`  |
| 1009   | No documented layout | `489c9951e390`  |
| 1005   | No documented layout | `489c9951e390`  |
| 1000   | No documented layout | `489c9951e390`  |
| 998    | No documented layout | `489c9951e390`  |
| 990    | No documented layout | `489c9951e390`  |
| 979    | No documented layout | `489c9951e390`  |
| 972    | No documented layout | `489c9951e390`  |
| 963    | No documented layout | `489c9951e390`  |
| 955    | No documented layout | `489c9951e390`  |
| 946    | No documented layout | `489c9951e390`  |
| 938    | No documented layout | `489c9951e390`  |
| 927    | No documented layout | `489c9951e390`  |
| 911    | No documented layout | `489c9951e390`  |
| 904    | No documented layout | `489c9951e390`  |
| 899    | No file              | `489c9951e390`  |
| 894    | No file              | `489c9951e390`  |
| 885    | No file              | `489c9951e390`  |
| 879    | No file              | `489c9951e390`  |
| 872    | No file              | `489c9951e390`  |
| 864    | No file              | `489c9951e390`  |
| 855    | No file              | `489c9951e390`  |
| 853    | No file              | `489c9951e390`  |
| 845    | No file              | `489c9951e390`  |
| 837    | No file              | `489c9951e390`  |
| 829    | No file              | `489c9951e390`  |
| 822    | No file              | `489c9951e390`  |
| 814    | No file              | `489c9951e390`  |
| 805    | No file              | `489c9951e390`  |
| 794    | No file              | `489c9951e390`  |
| 787    | No file              | `489c9951e390`  |
| 780    | No file              | `489c9951e390`  |
| 771    | No file              | `489c9951e390`  |
| 760    | No file              | `489c9951e390`  |
| 748    | No file              | `489c9951e390`  |
| 741    | No file              | `489c9951e390`  |
| 736    | No file              | `489c9951e390`  |
| 731    | No file              | `489c9951e390`  |
| 723    | No file              | `489c9951e390`  |
| 711    | No file              | `489c9951e390`  |
| 707    | No file              | `489c9951e390`  |
| 697    | No file              | `489c9951e390`  |
| 689    | No file              | `489c9951e390`  |
| 683    | No file              | `489c9951e390`  |
| 678    | No file              | `489c9951e390`  |
| 670    | No file              | `489c9951e390`  |
| 661    | No file              | `489c9951e390`  |
| 656    | No file              | `489c9951e390`  |
| 652    | No file              | `489c9951e390`  |
| 643    | No file              | `489c9951e390`  |
| 637    | No file              | `489c9951e390`  |
| 630    | No file              | `489c9951e390`  |
| 627    | No file              | `489c9951e390`  |
| 621    | No file              | `489c9951e390`  |
| 617    | No file              | `489c9951e390`  |
| 615    | No file              | `489c9951e390`  |
| 606    | No file              | `489c9951e390`  |
| 599    | No file              | `489c9951e390`  |
| 592    | No file              | `489c9951e390`  |
| 586    | No file              | `489c9951e390`  |
| 577    | No file              | `489c9951e390`  |
| 569    | No file              | `489c9951e390`  |
| 561    | No file              | `489c9951e390`  |
| 554    | No file              | `489c9951e390`  |
| 542    | No file              | `489c9951e390`  |
| 532    | No file              | `489c9951e390`  |
| 531    | No file              | `489c9951e390`  |
| 526    | No file              | `489c9951e390`  |
| 521    | No file              | `489c9951e390`  |
| 517    | No file              | `489c9951e390`  |
| 510    | No file              | `489c9951e390`  |
| 508    | No file              | `489c9951e390`  |
| 504    | No file              | `489c9951e390`  |
| 497    | No file              | `489c9951e390`  |
| 491    | No file              | `489c9951e390`  |
| 485    | No file              | `489c9951e390`  |
| 478    | No file              | `489c9951e390`  |
| 472    | No file              | `489c9951e390`  |
| 466    | No file              | `489c9951e390`  |
| 457    | No file              | `489c9951e390`  |
| 452    | No file              | `489c9951e390`  |
| 449    | No file              | `489c9951e390`  |
| 435    | No file              | `489c9951e390`  |

<!-- versions:end -->

## Companion Files

None. The handler names each product from LOC type 50, as
[`cashproduct.dbss`](../dbss/cashproduct_dbss.md) does, and links it to its
`cashproduct.dbss` row.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                       |
| ------------------- | -------------- | ------------ | ------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                |
| `+0x04`             | u32            | row_count    | Number of offer groups, `3007` on client 3482 |
| `+0x08`             | Row[row_count] | rows         | See Row                                     |
| `rows+0x00`         | String Table   | string_table | See String Table                            |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                  |

### Row (variable: 8 bytes + products)

| Offset  | Type                | Field         | Notes                                                                                    |
| ------- | ------------------- | ------------- | ---------------------------------------------------------------------------------------- |
| `+0x00` | u32                 | product_count | Number of `product_nos`, `1` to `30` on client 3482                                      |
| `+0x04` | u32                 | offer_group   | The group the products share; a product number of the group on 2,832 of 3,007 rows (client 3482) |
| `+0x08` | u32[product_count]  | product_nos   | `cashproduct.dbss` product IDs; all 16,407 of client 3482 have a row there               |

The offer groups are unique and in no key order.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                        |
| ------- | ------------------ | ------------ | ---------------------------- |
| `+0x00` | u32                | string_count | `0` on clients 1784 and 3482 |
| `+0x04` | pstr[string_count] | strings      | None                         |

## Field Names

The `CashProduct_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 gives each product an `OfferGroup`. Each of the 939 rows of the
client 1784 file is an `OfferGroup` of the sheet with the products that
name it:

| Field       | Sheet                                    | Same value (client 1784) |
| ----------- | ---------------------------------------- | ------------------------ |
| offer_group | `OfferGroup`                             | 939 of 939               |
| product_nos | `ProductNo` of the rows with that group  | 872 of 939 as a set      |

On the other 67 groups the file lists a subset of the sheet's products; 458
groups keep the sheet's row order. 359 sheet groups have no row in the
file.

## Open Questions

### Which Products Drop Out of a Group

On client 1784 the file leaves out some sheet products of 67 groups and 359
whole groups. Sale periods (`SalesStartPeriod`, `SalesEndPeriod`) or
`IsMallDisplay` may decide it; `cashproduct.dbss` does not yet expose them
to compare.
