# `cashproduct.dbss` Format

## Purpose

The Pearl Shop product catalog. One variable-length block per cash product,
keyed by product ID through a required offset companion. Each block carries
Korean display text, an inline icon path, and the item ID the product grants.

The stored icon is the Pearl Shop tile for the product, **not** the item's own
icon. 16,620 of the 28,689 products (57.9%) share a tile with another product,
so a whole seasonal collection points at one promotional image and 480 unrelated
products all use `loyalties.dds`. For an item icon, follow the linked item ID
into [itemenchant.dbss](itemenchant_dbss.md) instead.

Product IDs are a separate ID space from items because a purchase is not an
item: one product can grant several items, the same item can be sold by several
products, and the tile is marketing art for the offer.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                     | Bytes      | Records           | Row bytes                      |
| ------ | -------------- | ------------------------ | ---------- | ----------------- | ------------------------------ |
| 1      | 1327 and later | `cashproduct.dbss`       | 30,644,699 | 29,787 Block      | 504 to 1,996, 1,029 on average |
| 1      | 1327 and later | `cashproductoffset.dbss` | 357,448    | 29,787 Offset Row | 12                             |

| Layout | File                     | Known              | Unknown              |
| ------ | ------------------------ | ------------------ | -------------------- |
| 1      | `cashproduct.dbss`       | 1,327,126 B (4.3%) | 29,317,573 B (95.7%) |
| 1      | `cashproductoffset.dbss` | 357,448 B (100.0%) | 0 B (0.0%)           |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `1091996cad2e`  |
| 3482   | Layout 1             | `1091996cad2e`  |
| 3474   | Layout 1             | `1091996cad2e`  |
| 3473   | Layout 1             | `1091996cad2e`  |
| 3464   | Layout 1             | `1091996cad2e`  |
| 3458   | Layout 1             | `1091996cad2e`  |
| 3454   | Layout 1             | `1091996cad2e`  |
| 3444   | Layout 1             | `1091996cad2e`  |
| 3435   | Layout 1             | `1091996cad2e`  |
| 3426   | Layout 1             | `1091996cad2e`  |
| 3418   | Layout 1             | `1091996cad2e`  |
| 3412   | Layout 1             | `1091996cad2e`  |
| 3402   | Layout 1             | `1091996cad2e`  |
| 3396   | Layout 1             | `1091996cad2e`  |
| 3387   | Layout 1             | `1091996cad2e`  |
| 3381   | Layout 1             | `1091996cad2e`  |
| 3373   | Layout 1             | `1091996cad2e`  |
| 3364   | Layout 1             | `1091996cad2e`  |
| 3356   | Layout 1             | `1091996cad2e`  |
| 3349   | Layout 1             | `1091996cad2e`  |
| 3342   | Layout 1             | `1091996cad2e`  |
| 3335   | Layout 1             | `1091996cad2e`  |
| 3326   | Layout 1             | `1091996cad2e`  |
| 3321   | Layout 1             | `1091996cad2e`  |
| 3314   | Layout 1             | `1091996cad2e`  |
| 3303   | Layout 1             | `1091996cad2e`  |
| 3302   | Layout 1             | `1091996cad2e`  |
| 3293   | Layout 1             | `1091996cad2e`  |
| 3283   | Layout 1             | `1091996cad2e`  |
| 3275   | Layout 1             | `1091996cad2e`  |
| 3267   | Layout 1             | `1091996cad2e`  |
| 3258   | Layout 1             | `1091996cad2e`  |
| 3251   | Layout 1             | `1091996cad2e`  |
| 3242   | Layout 1             | `1091996cad2e`  |
| 3235   | Layout 1             | `1091996cad2e`  |
| 3229   | Layout 1             | `1091996cad2e`  |
| 3212   | Layout 1             | `1091996cad2e`  |
| 3203   | Layout 1             | `1091996cad2e`  |
| 3193   | Layout 1             | `1091996cad2e`  |
| 3186   | Layout 1             | `1091996cad2e`  |
| 3177   | Layout 1             | `1091996cad2e`  |
| 3169   | Layout 1             | `1091996cad2e`  |
| 3158   | Layout 1             | `1091996cad2e`  |
| 3151   | Layout 1             | `1091996cad2e`  |
| 3144   | Layout 1             | `1091996cad2e`  |
| 3133   | Layout 1             | `1091996cad2e`  |
| 3125   | Layout 1             | `1091996cad2e`  |
| 3118   | Layout 1             | `1091996cad2e`  |
| 3111   | Layout 1             | `1091996cad2e`  |
| 3103   | Layout 1             | `1091996cad2e`  |
| 3095   | Layout 1             | `1091996cad2e`  |
| 3086   | Layout 1             | `1091996cad2e`  |
| 3072   | Layout 1             | `1091996cad2e`  |
| 3062   | Layout 1             | `1091996cad2e`  |
| 3052   | Layout 1             | `1091996cad2e`  |
| 3045   | Layout 1             | `1091996cad2e`  |
| 3037   | Layout 1             | `1091996cad2e`  |
| 3030   | Layout 1             | `1091996cad2e`  |
| 3021   | Layout 1             | `1091996cad2e`  |
| 3012   | Layout 1             | `1091996cad2e`  |
| 3002   | Layout 1             | `1091996cad2e`  |
| 2995   | Layout 1             | `1091996cad2e`  |
| 2987   | Layout 1             | `1091996cad2e`  |
| 2978   | Layout 1             | `1091996cad2e`  |
| 2970   | Layout 1             | `1091996cad2e`  |
| 2959   | Layout 1             | `1091996cad2e`  |
| 2951   | Layout 1             | `1091996cad2e`  |
| 2942   | Layout 1             | `1091996cad2e`  |
| 2935   | Layout 1             | `1091996cad2e`  |
| 2932   | Layout 1             | `1091996cad2e`  |
| 2923   | Layout 1             | `1091996cad2e`  |
| 2919   | Layout 1             | `1091996cad2e`  |
| 2907   | Layout 1             | `1091996cad2e`  |
| 2900   | Layout 1             | `1091996cad2e`  |
| 2891   | Layout 1             | `1091996cad2e`  |
| 2882   | Layout 1             | `1091996cad2e`  |
| 2872   | Layout 1             | `1091996cad2e`  |
| 2863   | Layout 1             | `1091996cad2e`  |
| 2855   | Layout 1             | `1091996cad2e`  |
| 2849   | Layout 1             | `1091996cad2e`  |
| 2844   | Layout 1             | `1091996cad2e`  |
| 2834   | Layout 1             | `1091996cad2e`  |
| 2825   | Layout 1             | `1091996cad2e`  |
| 2819   | Layout 1             | `1091996cad2e`  |
| 2811   | Layout 1             | `1091996cad2e`  |
| 2803   | Layout 1             | `1091996cad2e`  |
| 2794   | Layout 1             | `1091996cad2e`  |
| 2783   | Layout 1             | `1091996cad2e`  |
| 2774   | Layout 1             | `1091996cad2e`  |
| 2765   | Layout 1             | `1091996cad2e`  |
| 2756   | Layout 1             | `1091996cad2e`  |
| 2750   | Layout 1             | `1091996cad2e`  |
| 2743   | Layout 1             | `1091996cad2e`  |
| 2736   | Layout 1             | `1091996cad2e`  |
| 2726   | Layout 1             | `1091996cad2e`  |
| 2717   | Layout 1             | `1091996cad2e`  |
| 2709   | Layout 1             | `1091996cad2e`  |
| 2703   | Layout 1             | `1091996cad2e`  |
| 2695   | Layout 1             | `1091996cad2e`  |
| 2684   | Layout 1             | `1091996cad2e`  |
| 2672   | Layout 1             | `1091996cad2e`  |
| 2665   | Layout 1             | `1091996cad2e`  |
| 2657   | Layout 1             | `1091996cad2e`  |
| 2649   | Layout 1             | `1091996cad2e`  |
| 2644   | Layout 1             | `1091996cad2e`  |
| 2637   | Layout 1             | `1091996cad2e`  |
| 2629   | Layout 1             | `1091996cad2e`  |
| 2619   | Layout 1             | `1091996cad2e`  |
| 2612   | Layout 1             | `1091996cad2e`  |
| 2606   | Layout 1             | `1091996cad2e`  |
| 2602   | Layout 1             | `1091996cad2e`  |
| 2601   | Layout 1             | `1091996cad2e`  |
| 2592   | Layout 1             | `1091996cad2e`  |
| 2583   | Layout 1             | `1091996cad2e`  |
| 2575   | Layout 1             | `1091996cad2e`  |
| 2567   | Layout 1             | `1091996cad2e`  |
| 2560   | Layout 1             | `1091996cad2e`  |
| 2553   | Layout 1             | `1091996cad2e`  |
| 2545   | Layout 1             | `1091996cad2e`  |
| 2538   | Layout 1             | `1091996cad2e`  |
| 2529   | Layout 1             | `1091996cad2e`  |
| 2519   | Layout 1             | `1091996cad2e`  |
| 2513   | Layout 1             | `1091996cad2e`  |
| 2510   | Layout 1             | `1091996cad2e`  |
| 2507   | Layout 1             | `1091996cad2e`  |
| 2503   | Layout 1             | `1091996cad2e`  |
| 2498   | Layout 1             | `1091996cad2e`  |
| 2492   | Layout 1             | `1091996cad2e`  |
| 2487   | Layout 1             | `1091996cad2e`  |
| 2480   | Layout 1             | `1091996cad2e`  |
| 2474   | Layout 1             | `1091996cad2e`  |
| 2468   | Layout 1             | `1091996cad2e`  |
| 2460   | Layout 1             | `1091996cad2e`  |
| 2453   | Layout 1             | `1091996cad2e`  |
| 2444   | Layout 1             | `1091996cad2e`  |
| 2438   | Layout 1             | `1091996cad2e`  |
| 2434   | Layout 1             | `1091996cad2e`  |
| 2429   | Layout 1             | `1091996cad2e`  |
| 2421   | Layout 1             | `1091996cad2e`  |
| 2414   | Layout 1             | `1091996cad2e`  |
| 2407   | Layout 1             | `1091996cad2e`  |
| 2401   | Layout 1             | `1091996cad2e`  |
| 2397   | Layout 1             | `1091996cad2e`  |
| 2393   | Layout 1             | `1091996cad2e`  |
| 2384   | Layout 1             | `1091996cad2e`  |
| 2378   | Layout 1             | `1091996cad2e`  |
| 2372   | Layout 1             | `1091996cad2e`  |
| 2358   | Layout 1             | `1091996cad2e`  |
| 2352   | Layout 1             | `1091996cad2e`  |
| 2347   | Layout 1             | `1091996cad2e`  |
| 2343   | Layout 1             | `1091996cad2e`  |
| 2335   | Layout 1             | `1091996cad2e`  |
| 2327   | Layout 1             | `1091996cad2e`  |
| 2324   | Layout 1             | `1091996cad2e`  |
| 2319   | Layout 1             | `1091996cad2e`  |
| 2313   | Layout 1             | `1091996cad2e`  |
| 2308   | Layout 1             | `1091996cad2e`  |
| 2302   | Layout 1             | `1091996cad2e`  |
| 2295   | Layout 1             | `1091996cad2e`  |
| 2290   | Layout 1             | `1091996cad2e`  |
| 2284   | Layout 1             | `1091996cad2e`  |
| 2276   | Layout 1             | `1091996cad2e`  |
| 2269   | Layout 1             | `1091996cad2e`  |
| 2259   | Layout 1             | `1091996cad2e`  |
| 2250   | Layout 1             | `1091996cad2e`  |
| 2243   | Layout 1             | `1091996cad2e`  |
| 2235   | Layout 1             | `1091996cad2e`  |
| 2229   | Layout 1             | `1091996cad2e`  |
| 2224   | Layout 1             | `1091996cad2e`  |
| 2218   | Layout 1             | `1091996cad2e`  |
| 2215   | Layout 1             | `1091996cad2e`  |
| 2207   | Layout 1             | `1091996cad2e`  |
| 2203   | Layout 1             | `1091996cad2e`  |
| 2196   | Layout 1             | `1091996cad2e`  |
| 2192   | Layout 1             | `1091996cad2e`  |
| 2189   | Layout 1             | `1091996cad2e`  |
| 2183   | Layout 1             | `1091996cad2e`  |
| 2179   | Layout 1             | `1091996cad2e`  |
| 2171   | Layout 1             | `1091996cad2e`  |
| 2163   | Layout 1             | `1091996cad2e`  |
| 2156   | Layout 1             | `1091996cad2e`  |
| 2151   | Layout 1             | `1091996cad2e`  |
| 2147   | Layout 1             | `1091996cad2e`  |
| 2142   | Layout 1             | `1091996cad2e`  |
| 2138   | Layout 1             | `1091996cad2e`  |
| 2134   | Layout 1             | `1091996cad2e`  |
| 2130   | Layout 1             | `1091996cad2e`  |
| 2122   | Layout 1             | `1091996cad2e`  |
| 2107   | Layout 1             | `1091996cad2e`  |
| 2098   | Layout 1             | `1091996cad2e`  |
| 2089   | Layout 1             | `1091996cad2e`  |
| 2081   | Layout 1             | `1091996cad2e`  |
| 2073   | Layout 1             | `1091996cad2e`  |
| 2067   | Layout 1             | `1091996cad2e`  |
| 2063   | Layout 1             | `1091996cad2e`  |
| 2059   | Layout 1             | `1091996cad2e`  |
| 2052   | Layout 1             | `1091996cad2e`  |
| 2044   | Layout 1             | `1091996cad2e`  |
| 2039   | Layout 1             | `1091996cad2e`  |
| 2032   | Layout 1             | `1091996cad2e`  |
| 2025   | Layout 1             | `1091996cad2e`  |
| 2011   | Layout 1             | `1091996cad2e`  |
| 2005   | Layout 1             | `1091996cad2e`  |
| 2000   | Layout 1             | `1091996cad2e`  |
| 1996   | Layout 1             | `1091996cad2e`  |
| 1991   | Layout 1             | `1091996cad2e`  |
| 1985   | Layout 1             | `1091996cad2e`  |
| 1980   | Layout 1             | `1091996cad2e`  |
| 1969   | Layout 1             | `1091996cad2e`  |
| 1964   | Layout 1             | `1091996cad2e`  |
| 1958   | Layout 1             | `1091996cad2e`  |
| 1950   | Layout 1             | `1091996cad2e`  |
| 1945   | Layout 1             | `1091996cad2e`  |
| 1937   | Layout 1             | `1091996cad2e`  |
| 1933   | Layout 1             | `1091996cad2e`  |
| 1927   | Layout 1             | `1091996cad2e`  |
| 1921   | Layout 1             | `1091996cad2e`  |
| 1914   | Layout 1             | `1091996cad2e`  |
| 1908   | Layout 1             | `1091996cad2e`  |
| 1897   | Layout 1             | `1091996cad2e`  |
| 1892   | Layout 1             | `1091996cad2e`  |
| 1886   | Layout 1             | `1091996cad2e`  |
| 1881   | Layout 1             | `1091996cad2e`  |
| 1871   | Layout 1             | `1091996cad2e`  |
| 1866   | Layout 1             | `1091996cad2e`  |
| 1862   | Layout 1             | `1091996cad2e`  |
| 1854   | Layout 1             | `1091996cad2e`  |
| 1846   | Layout 1             | `1091996cad2e`  |
| 1838   | Layout 1             | `1091996cad2e`  |
| 1832   | Layout 1             | `1091996cad2e`  |
| 1826   | Layout 1             | `1091996cad2e`  |
| 1822   | Layout 1             | `1091996cad2e`  |
| 1818   | Layout 1             | `1091996cad2e`  |
| 1804   | Layout 1             | `1091996cad2e`  |
| 1794   | Layout 1             | `1091996cad2e`  |
| 1790   | Layout 1             | `1091996cad2e`  |
| 1784   | Layout 1             | `1091996cad2e`  |
| 1774   | Layout 1             | `1091996cad2e`  |
| 1771   | Layout 1             | `1091996cad2e`  |
| 1762   | Layout 1             | `1091996cad2e`  |
| 1759   | Layout 1             | `1091996cad2e`  |
| 1754   | Layout 1             | `1091996cad2e`  |
| 1749   | Layout 1             | `1091996cad2e`  |
| 1743   | Layout 1             | `1091996cad2e`  |
| 1737   | Layout 1             | `1091996cad2e`  |
| 1731   | Layout 1             | `1091996cad2e`  |
| 1725   | Layout 1             | `1091996cad2e`  |
| 1717   | Layout 1             | `1091996cad2e`  |
| 1710   | Layout 1             | `1091996cad2e`  |
| 1704   | Layout 1             | `1091996cad2e`  |
| 1698   | Layout 1             | `1091996cad2e`  |
| 1690   | Layout 1             | `1091996cad2e`  |
| 1685   | Layout 1             | `1091996cad2e`  |
| 1680   | Layout 1             | `1091996cad2e`  |
| 1674   | Layout 1             | `1091996cad2e`  |
| 1668   | Layout 1             | `1091996cad2e`  |
| 1659   | Layout 1             | `1091996cad2e`  |
| 1649   | Layout 1             | `1091996cad2e`  |
| 1642   | Layout 1             | `1091996cad2e`  |
| 1636   | Layout 1             | `1091996cad2e`  |
| 1628   | Layout 1             | `1091996cad2e`  |
| 1622   | Layout 1             | `1091996cad2e`  |
| 1614   | Layout 1             | `1091996cad2e`  |
| 1608   | Layout 1             | `1091996cad2e`  |
| 1602   | Layout 1             | `1091996cad2e`  |
| 1598   | Layout 1             | `1091996cad2e`  |
| 1594   | Layout 1             | `1091996cad2e`  |
| 1590   | Layout 1             | `1091996cad2e`  |
| 1587   | Layout 1             | `1091996cad2e`  |
| 1584   | Layout 1             | `1091996cad2e`  |
| 1579   | Layout 1             | `1091996cad2e`  |
| 1572   | Layout 1             | `1091996cad2e`  |
| 1565   | Layout 1             | `1091996cad2e`  |
| 1559   | Layout 1             | `1091996cad2e`  |
| 1554   | Layout 1             | `1091996cad2e`  |
| 1547   | Layout 1             | `1091996cad2e`  |
| 1537   | Layout 1             | `1091996cad2e`  |
| 1529   | Layout 1             | `1091996cad2e`  |
| 1524   | Layout 1             | `1091996cad2e`  |
| 1519   | Layout 1             | `1091996cad2e`  |
| 1509   | Layout 1             | `1091996cad2e`  |
| 1506   | Layout 1             | `1091996cad2e`  |
| 1504   | Layout 1             | `1091996cad2e`  |
| 1500   | Layout 1             | `1091996cad2e`  |
| 1493   | Layout 1             | `1091996cad2e`  |
| 1489   | Layout 1             | `1091996cad2e`  |
| 1485   | Layout 1             | `1091996cad2e`  |
| 1481   | Layout 1             | `1091996cad2e`  |
| 1474   | Layout 1             | `1091996cad2e`  |
| 1466   | Layout 1             | `1091996cad2e`  |
| 1462   | Layout 1             | `1091996cad2e`  |
| 1459   | Layout 1             | `1091996cad2e`  |
| 1453   | Layout 1             | `1091996cad2e`  |
| 1450   | Layout 1             | `1091996cad2e`  |
| 1445   | Layout 1             | `1091996cad2e`  |
| 1439   | Layout 1             | `1091996cad2e`  |
| 1433   | Layout 1             | `1091996cad2e`  |
| 1430   | Layout 1             | `1091996cad2e`  |
| 1426   | Layout 1             | `1091996cad2e`  |
| 1421   | Layout 1             | `1091996cad2e`  |
| 1417   | Layout 1             | `1091996cad2e`  |
| 1416   | Layout 1             | `1091996cad2e`  |
| 1409   | Layout 1             | `1091996cad2e`  |
| 1405   | Layout 1             | `1091996cad2e`  |
| 1401   | Layout 1             | `1091996cad2e`  |
| 1396   | Layout 1             | `1091996cad2e`  |
| 1391   | Layout 1             | `1091996cad2e`  |
| 1390   | Layout 1             | `1091996cad2e`  |
| 1386   | Layout 1             | `1091996cad2e`  |
| 1381   | Layout 1             | `1091996cad2e`  |
| 1379   | Layout 1             | `1091996cad2e`  |
| 1372   | Layout 1             | `1091996cad2e`  |
| 1366   | Layout 1             | `1091996cad2e`  |
| 1364   | Layout 1             | `1091996cad2e`  |
| 1363   | Layout 1             | `1091996cad2e`  |
| 1360   | Layout 1             | `1091996cad2e`  |
| 1358   | Layout 1             | `1091996cad2e`  |
| 1355   | Layout 1             | `1091996cad2e`  |
| 1351   | Layout 1             | `1091996cad2e`  |
| 1348   | Layout 1             | `1091996cad2e`  |
| 1346   | Layout 1             | `1091996cad2e`  |
| 1341   | Layout 1             | `1091996cad2e`  |
| 1340   | Layout 1             | `1091996cad2e`  |
| 1338   | Layout 1             | `1091996cad2e`  |
| 1335   | Layout 1             | `1091996cad2e`  |
| 1333   | Layout 1             | `1091996cad2e`  |
| 1329   | Layout 1             | `1091996cad2e`  |
| 1327   | Layout 1             | `1091996cad2e`  |
| 1324   | No documented layout | `1091996cad2e`  |
| 1321   | No documented layout | `1091996cad2e`  |
| 1319   | No documented layout | `1091996cad2e`  |
| 1318   | No documented layout | `1091996cad2e`  |
| 1316   | No documented layout | `1091996cad2e`  |
| 1313   | No documented layout | `1091996cad2e`  |
| 1311   | No documented layout | `1091996cad2e`  |
| 1309   | No documented layout | `1091996cad2e`  |
| 1304   | No documented layout | `1091996cad2e`  |
| 1292   | No documented layout | `1091996cad2e`  |
| 1286   | No documented layout | `1091996cad2e`  |
| 1280   | No file              | `1091996cad2e`  |
| 1276   | No file              | `1091996cad2e`  |
| 1267   | No file              | `1091996cad2e`  |
| 1261   | No file              | `1091996cad2e`  |
| 1256   | No file              | `1091996cad2e`  |
| 1250   | No file              | `1091996cad2e`  |
| 1246   | No file              | `1091996cad2e`  |
| 1239   | No file              | `1091996cad2e`  |
| 1230   | No file              | `1091996cad2e`  |
| 1226   | No file              | `1091996cad2e`  |
| 1220   | No file              | `1091996cad2e`  |
| 1217   | No file              | `1091996cad2e`  |
| 1211   | No file              | `1091996cad2e`  |
| 1210   | No file              | `1091996cad2e`  |
| 1208   | No file              | `1091996cad2e`  |
| 1203   | No file              | `1091996cad2e`  |
| 1197   | No file              | `1091996cad2e`  |
| 1194   | No file              | `1091996cad2e`  |
| 1192   | No file              | `1091996cad2e`  |
| 1187   | No file              | `1091996cad2e`  |
| 1183   | No file              | `1091996cad2e`  |
| 1177   | No file              | `1091996cad2e`  |
| 1173   | No file              | `1091996cad2e`  |
| 1167   | No file              | `1091996cad2e`  |
| 1164   | No file              | `1091996cad2e`  |
| 1156   | No file              | `1091996cad2e`  |
| 1149   | No file              | `1091996cad2e`  |
| 1144   | No file              | `1091996cad2e`  |
| 1137   | No file              | `1091996cad2e`  |
| 1132   | No file              | `1091996cad2e`  |
| 1127   | No file              | `1091996cad2e`  |
| 1122   | No file              | `1091996cad2e`  |
| 1118   | No file              | `1091996cad2e`  |
| 1114   | No file              | `1091996cad2e`  |
| 1109   | No file              | `1091996cad2e`  |
| 1102   | No file              | `1091996cad2e`  |
| 1096   | No file              | `1091996cad2e`  |
| 1088   | No file              | `1091996cad2e`  |
| 1081   | No file              | `1091996cad2e`  |
| 1076   | No file              | `1091996cad2e`  |
| 1069   | No file              | `1091996cad2e`  |
| 1064   | No file              | `1091996cad2e`  |
| 1058   | No file              | `1091996cad2e`  |
| 1051   | No file              | `1091996cad2e`  |
| 1044   | No file              | `1091996cad2e`  |
| 1036   | No file              | `1091996cad2e`  |
| 1026   | No file              | `1091996cad2e`  |
| 1016   | No file              | `1091996cad2e`  |
| 1009   | No file              | `1091996cad2e`  |
| 1005   | No file              | `1091996cad2e`  |
| 1000   | No file              | `1091996cad2e`  |
| 998    | No file              | `1091996cad2e`  |
| 990    | No file              | `1091996cad2e`  |
| 979    | No file              | `1091996cad2e`  |
| 972    | No file              | `1091996cad2e`  |
| 963    | No file              | `1091996cad2e`  |
| 955    | No file              | `1091996cad2e`  |
| 946    | No file              | `1091996cad2e`  |
| 938    | No file              | `1091996cad2e`  |
| 927    | No file              | `1091996cad2e`  |
| 911    | No file              | `1091996cad2e`  |
| 904    | No file              | `1091996cad2e`  |
| 899    | No file              | `1091996cad2e`  |
| 894    | No file              | `1091996cad2e`  |
| 885    | No file              | `1091996cad2e`  |
| 879    | No file              | `1091996cad2e`  |
| 872    | No file              | `1091996cad2e`  |
| 864    | No file              | `1091996cad2e`  |
| 855    | No file              | `1091996cad2e`  |
| 853    | No file              | `1091996cad2e`  |
| 845    | No file              | `1091996cad2e`  |
| 837    | No file              | `1091996cad2e`  |
| 829    | No file              | `1091996cad2e`  |
| 822    | No file              | `1091996cad2e`  |
| 814    | No file              | `1091996cad2e`  |
| 805    | No file              | `1091996cad2e`  |
| 794    | No file              | `1091996cad2e`  |
| 787    | No file              | `1091996cad2e`  |
| 780    | No file              | `1091996cad2e`  |
| 771    | No file              | `1091996cad2e`  |
| 760    | No file              | `1091996cad2e`  |
| 748    | No file              | `1091996cad2e`  |
| 741    | No file              | `1091996cad2e`  |
| 736    | No file              | `1091996cad2e`  |
| 731    | No file              | `1091996cad2e`  |
| 723    | No file              | `1091996cad2e`  |
| 711    | No file              | `1091996cad2e`  |
| 707    | No file              | `1091996cad2e`  |
| 697    | No file              | `1091996cad2e`  |
| 689    | No file              | `1091996cad2e`  |
| 683    | No file              | `1091996cad2e`  |
| 678    | No file              | `1091996cad2e`  |
| 670    | No file              | `1091996cad2e`  |
| 661    | No file              | `1091996cad2e`  |
| 656    | No file              | `1091996cad2e`  |
| 652    | No file              | `1091996cad2e`  |
| 643    | No file              | `1091996cad2e`  |
| 637    | No file              | `1091996cad2e`  |
| 630    | No file              | `1091996cad2e`  |
| 627    | No file              | `1091996cad2e`  |
| 621    | No file              | `1091996cad2e`  |
| 617    | No file              | `1091996cad2e`  |
| 615    | No file              | `1091996cad2e`  |
| 606    | No file              | `1091996cad2e`  |
| 599    | No file              | `1091996cad2e`  |
| 592    | No file              | `1091996cad2e`  |
| 586    | No file              | `1091996cad2e`  |
| 577    | No file              | `1091996cad2e`  |
| 569    | No file              | `1091996cad2e`  |
| 561    | No file              | `1091996cad2e`  |
| 554    | No file              | `1091996cad2e`  |
| 542    | No file              | `1091996cad2e`  |
| 532    | No file              | `1091996cad2e`  |
| 531    | No file              | `1091996cad2e`  |
| 526    | No file              | `1091996cad2e`  |
| 521    | No file              | `1091996cad2e`  |
| 517    | No file              | `1091996cad2e`  |
| 510    | No file              | `1091996cad2e`  |
| 508    | No file              | `1091996cad2e`  |
| 504    | No file              | `1091996cad2e`  |
| 497    | No file              | `1091996cad2e`  |
| 491    | No file              | `1091996cad2e`  |
| 485    | No file              | `1091996cad2e`  |
| 478    | No file              | `1091996cad2e`  |
| 472    | No file              | `1091996cad2e`  |
| 466    | No file              | `1091996cad2e`  |
| 457    | No file              | `1091996cad2e`  |
| 452    | No file              | `1091996cad2e`  |
| 449    | No file              | `1091996cad2e`  |
| 435    | No file              | `1091996cad2e`  |

<!-- versions:end -->

## Companion Files

| File                     | Required | Role                                           |
| ------------------------ | -------- | ---------------------------------------------- |
| `cashproductoffset.dbss` | Required | Maps product ID to a block offset and size     |
| `languagedata_en.loc`    | Optional | Product name and description (`str_type=50`), name of the linked item (`str_type=0`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type         | Field  | Notes                                      |
| ------- | ------------ | ------ | ------------------------------------------ |
| `+0x00` | u32          | count  | Block count; see below                     |
| `+0x04` | Block[count] | blocks | Variable-length blocks, contiguous         |

The first block starts at byte `4` and the last ends exactly at end of file
(29,500,854 bytes observed), so the block stream is gap-free.

Observed blocks: 28,689 in the pre-2026-09-27 test fixture, 28,945 in the
2026-09-27 client (29,769,307 bytes, also gap-free). The other counts in this
doc are from the fixture.

### Block (variable: 12 bytes, size from `cashproductoffset.dbss`)

Only the product ID and the name sit at fixed offsets. The rest of the block
holds further strings and numeric data that a parser finds by scanning, see
Block Strings and Icon Path and Linked Item.

| Offset      | Type        | Field              | Notes                                      |
| ----------- | ----------- | ------------------ | ------------------------------------------ |
| `+0x00`     | u32         | product_id         | Matches the companion key in every sample  |
| `+0x04`     | str16       | name               | UTF-16LE Korean product name. The u64 count is the u32 `name_length`, the character count of the name that follows, and a u32 that is always 0 |
| `name+0x00` | bytes[rest] | unknown_after_name | Further strings and undecoded numeric data. The parser finds the icon path by scanning for the `(length, 0, text)` shape of an ASCII string, and reads `item_id` as a u32 16 bytes after the end of the icon text, see Icon Path and Linked Item |

### `cashproductoffset.dbss`

Unlike most offset companions this file has no `PABR` magic and no trailer: a 4-byte count followed by rows, ending exactly at `4 + count × 12`
(344,272 bytes observed).

| Offset  | Type              | Field | Notes                                               |
| ------- | ----------------- | ----- | --------------------------------------------------- |
| `+0x00` | u32               | count | Number of rows; equals the `cashproduct.dbss` count |
| `+0x04` | Offset Row[count] | rows  | `count` × 12-byte rows                              |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                          |
| ------- | ---- | ----------- | ---------------------------------------------- |
| `+0x00` | u32  | product_id  | Cash product ID; repeated at the block start   |
| `+0x04` | u32  | data_offset | Byte offset of the block in `cashproduct.dbss` |
| `+0x08` | u32  | data_size   | Block length in bytes                          |

Rows are contiguous: `data_offset + data_size` equals the next row's
`data_offset`.

## Block Strings

Both text encodings share one 8-byte prefix, the u64 count of `str16` and
`str8`: a u32 `length`, which counts **characters** in UTF-16 strings and
bytes in ASCII ones, and a u32 that is always 0 in observed data. The text
after it is UTF-16LE or ASCII and not null-terminated.

Strings sit at no fixed offset, so a parser scans for the
`(length, 0, text)` shape rather than seeking a constant. A block holds one to
five strings: the Korean name and its variants, an optional description
carrying `<PAColor…>` tags, and the ASCII icon path.

## Icon Path and Linked Item

The icon path is the block's only ASCII string, and a `u32` item ID follows
16 bytes after the end of that string:

| Element    | Position                          | Observed                    |
| ---------- | --------------------------------- | --------------------------- |
| icon path  | length-prefixed ASCII string      | 100% of blocks              |
| item_id    | `u32` at icon end + 16            | 96.8% of blocks             |

Stored paths always begin with `Icon/`, so the PAZ path is the stored value
prefixed with `ui_texture/`, matched case-insensitively:

```text
Icon/New_Icon/09_Cash/03_Product/00105099.dds
  -> ui_texture/icon/new_icon/09_cash/03_product/00105099.dds
```

This differs from [itemenchant.dbss](itemenchant_dbss.md), whose paths
start at `New_Icon/` and take the prefix `ui_texture/icon/`.

## Icon Coverage

| Measure                                     | Value            |
| ------------------------------------------- | ---------------- |
| Blocks carrying an icon path                 | 28,689 (100%)    |
| Icon paths resolving to a real PAZ file      | 28,613 (99.7%)   |
| Length prefix matching the string length     | 1,435 / 1,435    |
| Blocks with an item ID 16 bytes after the icon | 96.8%          |

## Notes

- Product IDs and item IDs are separate ID spaces. Product 117722 grants item
  340916 and uses icon `00105099`, three unrelated numbers. Only this file ties
  them together.
- The block's display text is Korean only. LOC type 50 holds the product's
  own name and description, keyed by `product_id` and a service code in
  `str_id3` (see `languagedata_loc.md`, Type 50). The product name differs
  from the linked item's name on about a third of the products: `Premium
  Pearl Box - 10,000+1,500` grants `Pearl Box - 10,000+1,500`, and
  `Polar Bear (Tier 3)` grants `[Pet] Polar Bear (Tier 3)`.
- Descriptions embed `<PAColor0xFFE9BD23>` and `<PAOldColor>` markup, the same
  tags as LOC text.
- `cashproductoffset.dbss` has no `PABR` magic and no trailer: a u32 count,
  then u32-keyed rows (`parse_bare_u32_offset_rows()`).
- 17 `gamecommondata` tables store inline icon paths. This file is second by
  volume with 14,750 unique paths, behind `itemenchant.dbss` with 21,768.

## Open Questions

### Remaining Numeric Fields

Everything other than the product ID, the strings, and the linked item ID is
undecoded. Price in Pearls, sale flags, category links and availability dates
are all plausible and none is confirmed.

### Blocks Without a Linked Item

3.2% of blocks have no LOC item ID at the expected position. Whether those
products grant several items, grant none directly, reference an unreleased item,
or simply store the ID elsewhere in the block is unresolved.

### Multiple Granted Items

Only the first item ID after the icon was searched for. Bundle products
plausibly list several, but no block was confirmed to carry more than one, so
the field may be a single link or the head of a list.

### String Roles

Blocks carry between one and five strings. The first is the product name and one
is the icon path, but whether the others are display variants, a subtitle, or a
description is not established.
