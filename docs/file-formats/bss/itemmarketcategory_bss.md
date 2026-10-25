# `itemmarketcategory.bss` Format

## Purpose

The Central Market category tree: one row per main category (Main Weapon,
Sub-weapon, Awakening, Armor and on to Artifact/Lightstone) with its
sub-categories, the entries of the market's category list, and two filter
lists per main category. Filter 1 holds the enhancement levels on gear rows,
the stone tiers on Alchemy Stone, the classes on Pearl Item and the colours
on Dye; filter 2 holds the grade colours on Main Weapon and Alchemy Stone.
The market sends the main and sub category numbers to the server as they
stand here (`ToClient_requestListByWorldMarket(__eWorldMarketKeyType_Item,
mainCategoryValue:getCategoryNo(), subCategoryValue:getCategoryNo())` in
`panel_window_marketplace_itemmarket_renew.luac`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                     | Bytes | Records                    | Row bytes |
| ------ | -------------- | ------------------------ | ----- | -------------------------- | --------- |
| 1      | 1280 and later | `itemmarketcategory.bss` | 5,999 | 420 Category Value, 18 Row | 5         |

| Layout | File                     | Known           | Unknown     |
| ------ | ------------------------ | --------------- | ----------- |
| 1      | `itemmarketcategory.bss` | 5,927 B (98.8%) | 72 B (1.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `bb5357b4fa7b`  |
| 3482   | Layout 1             | `bb5357b4fa7b`  |
| 3474   | Layout 1             | `bb5357b4fa7b`  |
| 3473   | Layout 1             | `bb5357b4fa7b`  |
| 3464   | Layout 1             | `bb5357b4fa7b`  |
| 3458   | Layout 1             | `bb5357b4fa7b`  |
| 3454   | Layout 1             | `bb5357b4fa7b`  |
| 3444   | Layout 1             | `bb5357b4fa7b`  |
| 3435   | Layout 1             | `bb5357b4fa7b`  |
| 3426   | Layout 1             | `bb5357b4fa7b`  |
| 3418   | Layout 1             | `bb5357b4fa7b`  |
| 3412   | Layout 1             | `bb5357b4fa7b`  |
| 3402   | Layout 1             | `bb5357b4fa7b`  |
| 3396   | Layout 1             | `bb5357b4fa7b`  |
| 3387   | Layout 1             | `bb5357b4fa7b`  |
| 3381   | Layout 1             | `bb5357b4fa7b`  |
| 3373   | Layout 1             | `bb5357b4fa7b`  |
| 3364   | Layout 1             | `bb5357b4fa7b`  |
| 3356   | Layout 1             | `bb5357b4fa7b`  |
| 3349   | Layout 1             | `bb5357b4fa7b`  |
| 3342   | Layout 1             | `bb5357b4fa7b`  |
| 3335   | Layout 1             | `bb5357b4fa7b`  |
| 3326   | Layout 1             | `bb5357b4fa7b`  |
| 3321   | Layout 1             | `bb5357b4fa7b`  |
| 3314   | Layout 1             | `bb5357b4fa7b`  |
| 3303   | Layout 1             | `bb5357b4fa7b`  |
| 3302   | Layout 1             | `bb5357b4fa7b`  |
| 3293   | Layout 1             | `bb5357b4fa7b`  |
| 3283   | Layout 1             | `bb5357b4fa7b`  |
| 3275   | Layout 1             | `bb5357b4fa7b`  |
| 3267   | Layout 1             | `bb5357b4fa7b`  |
| 3258   | Layout 1             | `bb5357b4fa7b`  |
| 3251   | Layout 1             | `bb5357b4fa7b`  |
| 3242   | Layout 1             | `bb5357b4fa7b`  |
| 3235   | Layout 1             | `bb5357b4fa7b`  |
| 3229   | Layout 1             | `bb5357b4fa7b`  |
| 3212   | Layout 1             | `bb5357b4fa7b`  |
| 3203   | Layout 1             | `bb5357b4fa7b`  |
| 3193   | Layout 1             | `bb5357b4fa7b`  |
| 3186   | Layout 1             | `bb5357b4fa7b`  |
| 3177   | Layout 1             | `bb5357b4fa7b`  |
| 3169   | Layout 1             | `bb5357b4fa7b`  |
| 3158   | Layout 1             | `bb5357b4fa7b`  |
| 3151   | Layout 1             | `bb5357b4fa7b`  |
| 3144   | Layout 1             | `bb5357b4fa7b`  |
| 3133   | Layout 1             | `bb5357b4fa7b`  |
| 3125   | Layout 1             | `bb5357b4fa7b`  |
| 3118   | Layout 1             | `bb5357b4fa7b`  |
| 3111   | Layout 1             | `bb5357b4fa7b`  |
| 3103   | Layout 1             | `bb5357b4fa7b`  |
| 3095   | Layout 1             | `bb5357b4fa7b`  |
| 3086   | Layout 1             | `bb5357b4fa7b`  |
| 3072   | Layout 1             | `bb5357b4fa7b`  |
| 3062   | Layout 1             | `bb5357b4fa7b`  |
| 3052   | Layout 1             | `bb5357b4fa7b`  |
| 3045   | Layout 1             | `bb5357b4fa7b`  |
| 3037   | Layout 1             | `bb5357b4fa7b`  |
| 3030   | Layout 1             | `bb5357b4fa7b`  |
| 3021   | Layout 1             | `bb5357b4fa7b`  |
| 3012   | Layout 1             | `bb5357b4fa7b`  |
| 3002   | Layout 1             | `bb5357b4fa7b`  |
| 2995   | Layout 1             | `bb5357b4fa7b`  |
| 2987   | Layout 1             | `bb5357b4fa7b`  |
| 2978   | Layout 1             | `bb5357b4fa7b`  |
| 2970   | Layout 1             | `bb5357b4fa7b`  |
| 2959   | Layout 1             | `bb5357b4fa7b`  |
| 2951   | Layout 1             | `bb5357b4fa7b`  |
| 2942   | Layout 1             | `bb5357b4fa7b`  |
| 2935   | Layout 1             | `bb5357b4fa7b`  |
| 2932   | Layout 1             | `bb5357b4fa7b`  |
| 2923   | Layout 1             | `bb5357b4fa7b`  |
| 2919   | Layout 1             | `bb5357b4fa7b`  |
| 2907   | Layout 1             | `bb5357b4fa7b`  |
| 2900   | Layout 1             | `bb5357b4fa7b`  |
| 2891   | Layout 1             | `bb5357b4fa7b`  |
| 2882   | Layout 1             | `bb5357b4fa7b`  |
| 2872   | Layout 1             | `bb5357b4fa7b`  |
| 2863   | Layout 1             | `bb5357b4fa7b`  |
| 2855   | Layout 1             | `bb5357b4fa7b`  |
| 2849   | Layout 1             | `bb5357b4fa7b`  |
| 2844   | Layout 1             | `bb5357b4fa7b`  |
| 2834   | Layout 1             | `bb5357b4fa7b`  |
| 2825   | Layout 1             | `bb5357b4fa7b`  |
| 2819   | Layout 1             | `bb5357b4fa7b`  |
| 2811   | Layout 1             | `bb5357b4fa7b`  |
| 2803   | Layout 1             | `bb5357b4fa7b`  |
| 2794   | Layout 1             | `bb5357b4fa7b`  |
| 2783   | Layout 1             | `bb5357b4fa7b`  |
| 2774   | Layout 1             | `bb5357b4fa7b`  |
| 2765   | Layout 1             | `bb5357b4fa7b`  |
| 2756   | Layout 1             | `bb5357b4fa7b`  |
| 2750   | Layout 1             | `bb5357b4fa7b`  |
| 2743   | Layout 1             | `bb5357b4fa7b`  |
| 2736   | Layout 1             | `bb5357b4fa7b`  |
| 2726   | Layout 1             | `bb5357b4fa7b`  |
| 2717   | Layout 1             | `bb5357b4fa7b`  |
| 2709   | Layout 1             | `bb5357b4fa7b`  |
| 2703   | Layout 1             | `bb5357b4fa7b`  |
| 2695   | Layout 1             | `bb5357b4fa7b`  |
| 2684   | Layout 1             | `bb5357b4fa7b`  |
| 2672   | Layout 1             | `bb5357b4fa7b`  |
| 2665   | Layout 1             | `bb5357b4fa7b`  |
| 2657   | Layout 1             | `bb5357b4fa7b`  |
| 2649   | Layout 1             | `bb5357b4fa7b`  |
| 2644   | Layout 1             | `bb5357b4fa7b`  |
| 2637   | Layout 1             | `bb5357b4fa7b`  |
| 2629   | Layout 1             | `bb5357b4fa7b`  |
| 2619   | Layout 1             | `bb5357b4fa7b`  |
| 2612   | Layout 1             | `bb5357b4fa7b`  |
| 2606   | Layout 1             | `bb5357b4fa7b`  |
| 2602   | Layout 1             | `bb5357b4fa7b`  |
| 2601   | Layout 1             | `bb5357b4fa7b`  |
| 2592   | Layout 1             | `bb5357b4fa7b`  |
| 2583   | Layout 1             | `bb5357b4fa7b`  |
| 2575   | Layout 1             | `bb5357b4fa7b`  |
| 2567   | Layout 1             | `bb5357b4fa7b`  |
| 2560   | Layout 1             | `bb5357b4fa7b`  |
| 2553   | Layout 1             | `bb5357b4fa7b`  |
| 2545   | Layout 1             | `bb5357b4fa7b`  |
| 2538   | Layout 1             | `bb5357b4fa7b`  |
| 2529   | Layout 1             | `bb5357b4fa7b`  |
| 2519   | Layout 1             | `bb5357b4fa7b`  |
| 2513   | Layout 1             | `bb5357b4fa7b`  |
| 2510   | Layout 1             | `bb5357b4fa7b`  |
| 2507   | Layout 1             | `bb5357b4fa7b`  |
| 2503   | Layout 1             | `bb5357b4fa7b`  |
| 2498   | Layout 1             | `bb5357b4fa7b`  |
| 2492   | Layout 1             | `bb5357b4fa7b`  |
| 2487   | Layout 1             | `bb5357b4fa7b`  |
| 2480   | Layout 1             | `bb5357b4fa7b`  |
| 2474   | Layout 1             | `bb5357b4fa7b`  |
| 2468   | Layout 1             | `bb5357b4fa7b`  |
| 2460   | Layout 1             | `bb5357b4fa7b`  |
| 2453   | Layout 1             | `bb5357b4fa7b`  |
| 2444   | Layout 1             | `bb5357b4fa7b`  |
| 2438   | Layout 1             | `bb5357b4fa7b`  |
| 2434   | Layout 1             | `bb5357b4fa7b`  |
| 2429   | Layout 1             | `bb5357b4fa7b`  |
| 2421   | Layout 1             | `bb5357b4fa7b`  |
| 2414   | Layout 1             | `bb5357b4fa7b`  |
| 2407   | Layout 1             | `bb5357b4fa7b`  |
| 2401   | Layout 1             | `bb5357b4fa7b`  |
| 2397   | Layout 1             | `bb5357b4fa7b`  |
| 2393   | Layout 1             | `bb5357b4fa7b`  |
| 2384   | Layout 1             | `bb5357b4fa7b`  |
| 2378   | Layout 1             | `bb5357b4fa7b`  |
| 2372   | Layout 1             | `bb5357b4fa7b`  |
| 2358   | Layout 1             | `bb5357b4fa7b`  |
| 2352   | Layout 1             | `bb5357b4fa7b`  |
| 2347   | Layout 1             | `bb5357b4fa7b`  |
| 2343   | Layout 1             | `bb5357b4fa7b`  |
| 2335   | Layout 1             | `bb5357b4fa7b`  |
| 2327   | Layout 1             | `bb5357b4fa7b`  |
| 2324   | Layout 1             | `bb5357b4fa7b`  |
| 2319   | Layout 1             | `bb5357b4fa7b`  |
| 2313   | Layout 1             | `bb5357b4fa7b`  |
| 2308   | Layout 1             | `bb5357b4fa7b`  |
| 2302   | Layout 1             | `bb5357b4fa7b`  |
| 2295   | Layout 1             | `bb5357b4fa7b`  |
| 2290   | Layout 1             | `bb5357b4fa7b`  |
| 2284   | Layout 1             | `bb5357b4fa7b`  |
| 2276   | Layout 1             | `bb5357b4fa7b`  |
| 2269   | Layout 1             | `bb5357b4fa7b`  |
| 2259   | Layout 1             | `bb5357b4fa7b`  |
| 2250   | Layout 1             | `bb5357b4fa7b`  |
| 2243   | Layout 1             | `bb5357b4fa7b`  |
| 2235   | Layout 1             | `bb5357b4fa7b`  |
| 2229   | Layout 1             | `bb5357b4fa7b`  |
| 2224   | Layout 1             | `bb5357b4fa7b`  |
| 2218   | Layout 1             | `bb5357b4fa7b`  |
| 2215   | Layout 1             | `bb5357b4fa7b`  |
| 2207   | Layout 1             | `bb5357b4fa7b`  |
| 2203   | Layout 1             | `bb5357b4fa7b`  |
| 2196   | Layout 1             | `bb5357b4fa7b`  |
| 2192   | Layout 1             | `bb5357b4fa7b`  |
| 2189   | Layout 1             | `bb5357b4fa7b`  |
| 2183   | Layout 1             | `bb5357b4fa7b`  |
| 2179   | Layout 1             | `bb5357b4fa7b`  |
| 2171   | Layout 1             | `bb5357b4fa7b`  |
| 2163   | Layout 1             | `bb5357b4fa7b`  |
| 2156   | Layout 1             | `bb5357b4fa7b`  |
| 2151   | Layout 1             | `bb5357b4fa7b`  |
| 2147   | Layout 1             | `bb5357b4fa7b`  |
| 2142   | Layout 1             | `bb5357b4fa7b`  |
| 2138   | Layout 1             | `bb5357b4fa7b`  |
| 2134   | Layout 1             | `bb5357b4fa7b`  |
| 2130   | Layout 1             | `bb5357b4fa7b`  |
| 2122   | Layout 1             | `bb5357b4fa7b`  |
| 2107   | Layout 1             | `bb5357b4fa7b`  |
| 2098   | Layout 1             | `bb5357b4fa7b`  |
| 2089   | Layout 1             | `bb5357b4fa7b`  |
| 2081   | Layout 1             | `bb5357b4fa7b`  |
| 2073   | Layout 1             | `bb5357b4fa7b`  |
| 2067   | Layout 1             | `bb5357b4fa7b`  |
| 2063   | Layout 1             | `bb5357b4fa7b`  |
| 2059   | Layout 1             | `bb5357b4fa7b`  |
| 2052   | Layout 1             | `bb5357b4fa7b`  |
| 2044   | Layout 1             | `bb5357b4fa7b`  |
| 2039   | Layout 1             | `bb5357b4fa7b`  |
| 2032   | Layout 1             | `bb5357b4fa7b`  |
| 2025   | Layout 1             | `bb5357b4fa7b`  |
| 2011   | Layout 1             | `bb5357b4fa7b`  |
| 2005   | Layout 1             | `bb5357b4fa7b`  |
| 2000   | Layout 1             | `bb5357b4fa7b`  |
| 1996   | Layout 1             | `bb5357b4fa7b`  |
| 1991   | Layout 1             | `bb5357b4fa7b`  |
| 1985   | Layout 1             | `bb5357b4fa7b`  |
| 1980   | Layout 1             | `bb5357b4fa7b`  |
| 1969   | Layout 1             | `bb5357b4fa7b`  |
| 1964   | Layout 1             | `bb5357b4fa7b`  |
| 1958   | Layout 1             | `bb5357b4fa7b`  |
| 1950   | Layout 1             | `bb5357b4fa7b`  |
| 1945   | Layout 1             | `bb5357b4fa7b`  |
| 1937   | Layout 1             | `bb5357b4fa7b`  |
| 1933   | Layout 1             | `bb5357b4fa7b`  |
| 1927   | Layout 1             | `bb5357b4fa7b`  |
| 1921   | Layout 1             | `bb5357b4fa7b`  |
| 1914   | Layout 1             | `bb5357b4fa7b`  |
| 1908   | Layout 1             | `bb5357b4fa7b`  |
| 1897   | Layout 1             | `bb5357b4fa7b`  |
| 1892   | Layout 1             | `bb5357b4fa7b`  |
| 1886   | Layout 1             | `bb5357b4fa7b`  |
| 1881   | Layout 1             | `bb5357b4fa7b`  |
| 1871   | Layout 1             | `bb5357b4fa7b`  |
| 1866   | Layout 1             | `bb5357b4fa7b`  |
| 1862   | Layout 1             | `bb5357b4fa7b`  |
| 1854   | Layout 1             | `bb5357b4fa7b`  |
| 1846   | Layout 1             | `bb5357b4fa7b`  |
| 1838   | Layout 1             | `bb5357b4fa7b`  |
| 1832   | Layout 1             | `bb5357b4fa7b`  |
| 1826   | Layout 1             | `bb5357b4fa7b`  |
| 1822   | Layout 1             | `bb5357b4fa7b`  |
| 1818   | Layout 1             | `bb5357b4fa7b`  |
| 1804   | Layout 1             | `bb5357b4fa7b`  |
| 1794   | Layout 1             | `bb5357b4fa7b`  |
| 1790   | Layout 1             | `bb5357b4fa7b`  |
| 1784   | Layout 1             | `bb5357b4fa7b`  |
| 1774   | Layout 1             | `bb5357b4fa7b`  |
| 1771   | Layout 1             | `bb5357b4fa7b`  |
| 1762   | Layout 1             | `bb5357b4fa7b`  |
| 1759   | Layout 1             | `bb5357b4fa7b`  |
| 1754   | Layout 1             | `bb5357b4fa7b`  |
| 1749   | Layout 1             | `bb5357b4fa7b`  |
| 1743   | Layout 1             | `bb5357b4fa7b`  |
| 1737   | Layout 1             | `bb5357b4fa7b`  |
| 1731   | Layout 1             | `bb5357b4fa7b`  |
| 1725   | Layout 1             | `bb5357b4fa7b`  |
| 1717   | Layout 1             | `bb5357b4fa7b`  |
| 1710   | Layout 1             | `bb5357b4fa7b`  |
| 1704   | Layout 1             | `bb5357b4fa7b`  |
| 1698   | Layout 1             | `bb5357b4fa7b`  |
| 1690   | Layout 1             | `bb5357b4fa7b`  |
| 1685   | Layout 1             | `bb5357b4fa7b`  |
| 1680   | Layout 1             | `bb5357b4fa7b`  |
| 1674   | Layout 1             | `bb5357b4fa7b`  |
| 1668   | Layout 1             | `bb5357b4fa7b`  |
| 1659   | Layout 1             | `bb5357b4fa7b`  |
| 1649   | Layout 1             | `bb5357b4fa7b`  |
| 1642   | Layout 1             | `bb5357b4fa7b`  |
| 1636   | Layout 1             | `bb5357b4fa7b`  |
| 1628   | Layout 1             | `bb5357b4fa7b`  |
| 1622   | Layout 1             | `bb5357b4fa7b`  |
| 1614   | Layout 1             | `bb5357b4fa7b`  |
| 1608   | Layout 1             | `bb5357b4fa7b`  |
| 1602   | Layout 1             | `bb5357b4fa7b`  |
| 1598   | Layout 1             | `bb5357b4fa7b`  |
| 1594   | Layout 1             | `bb5357b4fa7b`  |
| 1590   | Layout 1             | `bb5357b4fa7b`  |
| 1587   | Layout 1             | `bb5357b4fa7b`  |
| 1584   | Layout 1             | `bb5357b4fa7b`  |
| 1579   | Layout 1             | `bb5357b4fa7b`  |
| 1572   | Layout 1             | `bb5357b4fa7b`  |
| 1565   | Layout 1             | `bb5357b4fa7b`  |
| 1559   | Layout 1             | `bb5357b4fa7b`  |
| 1554   | Layout 1             | `bb5357b4fa7b`  |
| 1547   | Layout 1             | `bb5357b4fa7b`  |
| 1537   | Layout 1             | `bb5357b4fa7b`  |
| 1529   | Layout 1             | `bb5357b4fa7b`  |
| 1524   | Layout 1             | `bb5357b4fa7b`  |
| 1519   | Layout 1             | `bb5357b4fa7b`  |
| 1509   | Layout 1             | `bb5357b4fa7b`  |
| 1506   | Layout 1             | `bb5357b4fa7b`  |
| 1504   | Layout 1             | `bb5357b4fa7b`  |
| 1500   | Layout 1             | `bb5357b4fa7b`  |
| 1493   | Layout 1             | `bb5357b4fa7b`  |
| 1489   | Layout 1             | `bb5357b4fa7b`  |
| 1485   | Layout 1             | `bb5357b4fa7b`  |
| 1481   | Layout 1             | `bb5357b4fa7b`  |
| 1474   | Layout 1             | `bb5357b4fa7b`  |
| 1466   | Layout 1             | `bb5357b4fa7b`  |
| 1462   | Layout 1             | `bb5357b4fa7b`  |
| 1459   | Layout 1             | `bb5357b4fa7b`  |
| 1453   | Layout 1             | `bb5357b4fa7b`  |
| 1450   | Layout 1             | `bb5357b4fa7b`  |
| 1445   | Layout 1             | `bb5357b4fa7b`  |
| 1439   | Layout 1             | `bb5357b4fa7b`  |
| 1433   | Layout 1             | `bb5357b4fa7b`  |
| 1430   | Layout 1             | `bb5357b4fa7b`  |
| 1426   | Layout 1             | `bb5357b4fa7b`  |
| 1421   | Layout 1             | `bb5357b4fa7b`  |
| 1417   | Layout 1             | `bb5357b4fa7b`  |
| 1416   | Layout 1             | `bb5357b4fa7b`  |
| 1409   | Layout 1             | `bb5357b4fa7b`  |
| 1405   | Layout 1             | `bb5357b4fa7b`  |
| 1401   | Layout 1             | `bb5357b4fa7b`  |
| 1396   | Layout 1             | `bb5357b4fa7b`  |
| 1391   | Layout 1             | `bb5357b4fa7b`  |
| 1390   | Layout 1             | `bb5357b4fa7b`  |
| 1386   | Layout 1             | `bb5357b4fa7b`  |
| 1381   | Layout 1             | `bb5357b4fa7b`  |
| 1379   | Layout 1             | `bb5357b4fa7b`  |
| 1372   | Layout 1             | `bb5357b4fa7b`  |
| 1366   | Layout 1             | `bb5357b4fa7b`  |
| 1364   | Layout 1             | `bb5357b4fa7b`  |
| 1363   | Layout 1             | `bb5357b4fa7b`  |
| 1360   | Layout 1             | `bb5357b4fa7b`  |
| 1358   | Layout 1             | `bb5357b4fa7b`  |
| 1355   | Layout 1             | `bb5357b4fa7b`  |
| 1351   | Layout 1             | `bb5357b4fa7b`  |
| 1348   | Layout 1             | `bb5357b4fa7b`  |
| 1346   | Layout 1             | `bb5357b4fa7b`  |
| 1341   | Layout 1             | `bb5357b4fa7b`  |
| 1340   | Layout 1             | `bb5357b4fa7b`  |
| 1338   | Layout 1             | `bb5357b4fa7b`  |
| 1335   | Layout 1             | `bb5357b4fa7b`  |
| 1333   | Layout 1             | `bb5357b4fa7b`  |
| 1329   | Layout 1             | `bb5357b4fa7b`  |
| 1327   | Layout 1             | `bb5357b4fa7b`  |
| 1324   | Layout 1             | `bb5357b4fa7b`  |
| 1321   | Layout 1             | `bb5357b4fa7b`  |
| 1319   | Layout 1             | `bb5357b4fa7b`  |
| 1318   | Layout 1             | `bb5357b4fa7b`  |
| 1316   | Layout 1             | `bb5357b4fa7b`  |
| 1313   | Layout 1             | `bb5357b4fa7b`  |
| 1311   | Layout 1             | `bb5357b4fa7b`  |
| 1309   | Layout 1             | `bb5357b4fa7b`  |
| 1304   | Layout 1             | `bb5357b4fa7b`  |
| 1292   | Layout 1             | `bb5357b4fa7b`  |
| 1286   | Layout 1             | `bb5357b4fa7b`  |
| 1280   | Layout 1             | `bb5357b4fa7b`  |
| 1276   | No documented layout | `bb5357b4fa7b`  |
| 1267   | No documented layout | `bb5357b4fa7b`  |
| 1261   | No documented layout | `bb5357b4fa7b`  |
| 1256   | No documented layout | `bb5357b4fa7b`  |
| 1250   | No documented layout | `bb5357b4fa7b`  |
| 1246   | No documented layout | `bb5357b4fa7b`  |
| 1239   | No documented layout | `bb5357b4fa7b`  |
| 1230   | No documented layout | `bb5357b4fa7b`  |
| 1226   | No documented layout | `bb5357b4fa7b`  |
| 1220   | No documented layout | `bb5357b4fa7b`  |
| 1217   | No documented layout | `bb5357b4fa7b`  |
| 1211   | No documented layout | `bb5357b4fa7b`  |
| 1210   | No documented layout | `bb5357b4fa7b`  |
| 1208   | No documented layout | `bb5357b4fa7b`  |
| 1203   | No documented layout | `bb5357b4fa7b`  |
| 1197   | No documented layout | `bb5357b4fa7b`  |
| 1194   | No documented layout | `bb5357b4fa7b`  |
| 1192   | No documented layout | `bb5357b4fa7b`  |
| 1187   | No documented layout | `bb5357b4fa7b`  |
| 1183   | No documented layout | `bb5357b4fa7b`  |
| 1177   | No documented layout | `bb5357b4fa7b`  |
| 1173   | No documented layout | `bb5357b4fa7b`  |
| 1167   | No documented layout | `bb5357b4fa7b`  |
| 1164   | No documented layout | `bb5357b4fa7b`  |
| 1156   | No documented layout | `bb5357b4fa7b`  |
| 1149   | No documented layout | `bb5357b4fa7b`  |
| 1144   | No documented layout | `bb5357b4fa7b`  |
| 1137   | No documented layout | `bb5357b4fa7b`  |
| 1132   | No documented layout | `bb5357b4fa7b`  |
| 1127   | No documented layout | `bb5357b4fa7b`  |
| 1122   | No documented layout | `bb5357b4fa7b`  |
| 1118   | No documented layout | `bb5357b4fa7b`  |
| 1114   | No documented layout | `bb5357b4fa7b`  |
| 1109   | No documented layout | `bb5357b4fa7b`  |
| 1102   | No documented layout | `bb5357b4fa7b`  |
| 1096   | No documented layout | `bb5357b4fa7b`  |
| 1088   | No documented layout | `bb5357b4fa7b`  |
| 1081   | No documented layout | `bb5357b4fa7b`  |
| 1076   | No documented layout | `bb5357b4fa7b`  |
| 1069   | No documented layout | `bb5357b4fa7b`  |
| 1064   | No documented layout | `bb5357b4fa7b`  |
| 1058   | No documented layout | `bb5357b4fa7b`  |
| 1051   | No documented layout | `bb5357b4fa7b`  |
| 1044   | No documented layout | `bb5357b4fa7b`  |
| 1036   | No documented layout | `bb5357b4fa7b`  |
| 1026   | No documented layout | `bb5357b4fa7b`  |
| 1016   | No documented layout | `bb5357b4fa7b`  |
| 1009   | No documented layout | `bb5357b4fa7b`  |
| 1005   | No documented layout | `bb5357b4fa7b`  |
| 1000   | No documented layout | `bb5357b4fa7b`  |
| 998    | No documented layout | `bb5357b4fa7b`  |
| 990    | No documented layout | `bb5357b4fa7b`  |
| 979    | No documented layout | `bb5357b4fa7b`  |
| 972    | No documented layout | `bb5357b4fa7b`  |
| 963    | No documented layout | `bb5357b4fa7b`  |
| 955    | No documented layout | `bb5357b4fa7b`  |
| 946    | No documented layout | `bb5357b4fa7b`  |
| 938    | No documented layout | `bb5357b4fa7b`  |
| 927    | No documented layout | `bb5357b4fa7b`  |
| 911    | No documented layout | `bb5357b4fa7b`  |
| 904    | No documented layout | `bb5357b4fa7b`  |
| 899    | No documented layout | `bb5357b4fa7b`  |
| 894    | No documented layout | `bb5357b4fa7b`  |
| 885    | No documented layout | `bb5357b4fa7b`  |
| 879    | No documented layout | `bb5357b4fa7b`  |
| 872    | No documented layout | `bb5357b4fa7b`  |
| 864    | No documented layout | `bb5357b4fa7b`  |
| 855    | No documented layout | `bb5357b4fa7b`  |
| 853    | No documented layout | `bb5357b4fa7b`  |
| 845    | No documented layout | `bb5357b4fa7b`  |
| 837    | No documented layout | `bb5357b4fa7b`  |
| 829    | No documented layout | `bb5357b4fa7b`  |
| 822    | No documented layout | `bb5357b4fa7b`  |
| 814    | No documented layout | `bb5357b4fa7b`  |
| 805    | No documented layout | `bb5357b4fa7b`  |
| 794    | No documented layout | `bb5357b4fa7b`  |
| 787    | No documented layout | `bb5357b4fa7b`  |
| 780    | No documented layout | `bb5357b4fa7b`  |
| 771    | No documented layout | `bb5357b4fa7b`  |
| 760    | No documented layout | `bb5357b4fa7b`  |
| 748    | No documented layout | `bb5357b4fa7b`  |
| 741    | No documented layout | `bb5357b4fa7b`  |
| 736    | No documented layout | `bb5357b4fa7b`  |
| 731    | No documented layout | `bb5357b4fa7b`  |
| 723    | No documented layout | `bb5357b4fa7b`  |
| 711    | No documented layout | `bb5357b4fa7b`  |
| 707    | No documented layout | `bb5357b4fa7b`  |
| 697    | No documented layout | `bb5357b4fa7b`  |
| 689    | No documented layout | `bb5357b4fa7b`  |
| 683    | No documented layout | `bb5357b4fa7b`  |
| 678    | No documented layout | `bb5357b4fa7b`  |
| 670    | No documented layout | `bb5357b4fa7b`  |
| 661    | No documented layout | `bb5357b4fa7b`  |
| 656    | No documented layout | `bb5357b4fa7b`  |
| 652    | No documented layout | `bb5357b4fa7b`  |
| 643    | No documented layout | `bb5357b4fa7b`  |
| 637    | No documented layout | `bb5357b4fa7b`  |
| 630    | No documented layout | `bb5357b4fa7b`  |
| 627    | No documented layout | `bb5357b4fa7b`  |
| 621    | No documented layout | `bb5357b4fa7b`  |
| 617    | No documented layout | `bb5357b4fa7b`  |
| 615    | No documented layout | `bb5357b4fa7b`  |
| 606    | No documented layout | `bb5357b4fa7b`  |
| 599    | No documented layout | `bb5357b4fa7b`  |
| 592    | No documented layout | `bb5357b4fa7b`  |
| 586    | No documented layout | `bb5357b4fa7b`  |
| 577    | No documented layout | `bb5357b4fa7b`  |
| 569    | No documented layout | `bb5357b4fa7b`  |
| 561    | No documented layout | `bb5357b4fa7b`  |
| 554    | No documented layout | `bb5357b4fa7b`  |
| 542    | No documented layout | `bb5357b4fa7b`  |
| 532    | No documented layout | `bb5357b4fa7b`  |
| 531    | No documented layout | `bb5357b4fa7b`  |
| 526    | No documented layout | `bb5357b4fa7b`  |
| 521    | No documented layout | `bb5357b4fa7b`  |
| 517    | No documented layout | `bb5357b4fa7b`  |
| 510    | No documented layout | `bb5357b4fa7b`  |
| 508    | No documented layout | `bb5357b4fa7b`  |
| 504    | No documented layout | `bb5357b4fa7b`  |
| 497    | No documented layout | `bb5357b4fa7b`  |
| 491    | No documented layout | `bb5357b4fa7b`  |
| 485    | No documented layout | `bb5357b4fa7b`  |
| 478    | No documented layout | `bb5357b4fa7b`  |
| 472    | No documented layout | `bb5357b4fa7b`  |
| 466    | No documented layout | `bb5357b4fa7b`  |
| 457    | No documented layout | `bb5357b4fa7b`  |
| 452    | No documented layout | `bb5357b4fa7b`  |
| 449    | No documented layout | `bb5357b4fa7b`  |
| 435    | No documented layout | `bb5357b4fa7b`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                 |
| --------------------- | -------- | -------------------------------------------------------------------- |
| `languagedata_en.loc` | Optional | Category names, type 44 keyed (main, sub, filter 1, filter 2); see Notes |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type            | Field              | Notes                                                   |
| ------------------- | --------------- | ------------------ | ------------------------------------------------------- |
| `+0x00`             | char[4]         | magic              | ASCII `PABR`                                            |
| `+0x04`             | u32             | row_count          | Number of main categories; `18` on client 3474          |
| `+0x08`             | Row[row_count]  | rows               | See Row; sorted by `key`                                |
| `rows+0x00`         | String Table    | string_table       | The Korean category names                               |
| `string_table+0x00` | u32             | string_table_start | Absolute offset of `string_count` (`0x96E` on client 3474) |
| `string_table+0x04` | u32             | zero               | Always `0`                                              |

### Row (variable: 22 bytes + lists)

A list is a u32 count followed by that many Category Values.

| Offset                  | Type                               | Field                     | Notes                                                                 |
| ----------------------- | ---------------------------------- | ------------------------- | --------------------------------------------------------------------- |
| `+0x00`                 | u8                                 | key                       | Main category number; equals `main_category.category_no` on every row (clients 1784 and 3474) |
| `+0x01`                 | Category Value                     | main_category             | `getMainCategoryValue()`; `1`, then `5` to `85` in steps of 5       |
| `+0x06`                 | u32                                | sub_category_count        | Number of `sub_categories`; `getSubCategoryListCount()`               |
| `+0x0A`                 | Category Value[sub_category_count] | sub_categories            | `getSubCategoryAt(i)`; the entries of the market's category list      |
| `sub_categories+0x00`   | u32                                | filter1_count             | Number of `filter1_values`; `0` on 6 of 18 rows (client 3474)         |
| `sub_categories+0x04`   | Category Value[filter1_count]      | filter1_values            | Enhancement levels (`+ 0` to `PEN (V)`), stone tiers, classes or dye colours |
| `filter1_values+0x00`   | u32                                | filter2_count             | Number of `filter2_values`; only Main Weapon (3) and Alchemy Stone (4) have any |
| `filter1_values+0x04`   | Category Value[filter2_count]      | filter2_values            | Grade colours: `2` green, `3` blue, `4` yellow, and `1` white on Alchemy Stone |
| `filter2_values+0x00`   | u32                                | unknown_filter2_values_00 | `7` on 10 of 18 rows (client 3474); see Open Questions                |

### Category Value (5 bytes)

| Offset  | Type | Field       | Notes                                                                  |
| ------- | ---- | ----------- | ---------------------------------------------------------------------- |
| `+0x00` | u8   | category_no | `getCategoryNo()`; unique within its list, from 1 with gaps            |
| `+0x01` | u32  | name_ref    | String table index of the Korean name (`getCategoryName()` text in the Korean client) |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                    |
| ------- | ------------------ | ------------ | -------------------------------------------------------- |
| `+0x00` | u32                | string_count | `291` on client 3474                                     |
| `+0x04` | pstr[string_count] | strings      | All wide; `name_ref` indexes them, each string once      |

## Field Names

The names are the `MarketCategoryNameTag` sheet of a private server's
`DataSheets.bexcel` on client 1784, with the columns `MarketCategory1`,
`MarketCategory2`, `MarketFilter1`, `MarketFilter2` and `NameTag`. A sheet
row with only `MarketCategory1` set is a `main_category`, one with
`MarketCategory2` set a `sub_categories` entry, and one with `MarketFilter1`
or `MarketFilter2` set a `filter1_values` or `filter2_values` entry; its
`NameTag` is the string `name_ref` points at.

| Keys compared                          | Same name (client 1784) | Same name (client 3474) |
| -------------------------------------- | ----------------------- | ----------------------- |
| (category, sub-category, filter 1, filter 2) | 359 of 359        | 328 of 344              |

The sheet has 360 rows; its one row with no entry in the file is
`MarketCategory1` 10, `MarketCategory2` 18 (`악기`), and both clients skip
sub-category 18 under Awakening. The 16 misses on client 3474 are lists
that were re-sorted after client 1784: Material, Enhancement, Consumables
and Magic Crystal (Magic Crystal's sub-categories were gear slots on
client 1784 and are crystal types on client 3474).

## Notes

- LOC type 44 holds the English names, keyed `str_id1` main category,
  `str_id2` sub-category, `str_id3` filter 1 and `str_id4` filter 2, with
  `0` for the parts a row does not have: (1, 0, 0, 0) is `Main Weapon`,
  (10, 17, 0, 0) `Greatbow`, (1, 0, 17, 0) `PRI (I)`. On client 3474 it
  covers 413 of the 420 keys of the file; the 7 others are the
  `filter2_values` grade colours, which have no LOC text. LOC also keeps 8
  keys the file no longer has (Magic Crystal's old gear-slot entries and
  Dye filter 1 `Real Red`).
- The market lists the categories through
  `PaGlobalFunc_getItemMarketCategoryListAndSetUI` in
  `global_util_itemacquirehelper.luac`, in file order: each row, then its
  `sub_categories`. The Lua reads `getFilterListCount(0)` in two places and
  uses the result nowhere; no Lua reads a filter entry.
- The sheet `MarketCategoryOrder` of the same client 1784 source has a
  `ContentsGroupKey` per (`MarketCategory1`, `MarketCategory2`); the file
  holds no such column.

## Open Questions

### `unknown_filter2_values_00`

The u32 after the lists is `7` on 10 of 18 rows on client 3474 and on 13
of 17 rows on client 1784 (`0` on 3 more there). The other rows hold values
whose bytes read as UTF-16 text fragments (`72 00 71 00` is `rq`, `75 00 65
00` is `ue`), which points at memory the build did not clear. No Lua call
returns it.
