# `selectbox.bss` Format

## Purpose

The contents of the choose-your-item boxes ("Choose Your Ultimate
Enhancement Box"): per box key up to five types, each a list of items with
a count and the texture name of its tab. The select box window
(`panel_window_selectbox_1.luac`) opens for an item whose contents event is
`__eContentsType_SelectBox`, reads the box key from the item's
`getContentsEventParam1()`, and per type `0` to `__eSelectBoxTypeCount - 1`
shows the items with `ToClient_selectBoxItemEnchantKey(key, type, index)`,
`ToClient_selectBoxItemCount(key, type, index)` and the tab with
`ToClient_selectBoxTextureName(key, type)`. The player picks one item of
each type that has items.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File            | Bytes  | Records                               | Row bytes |
| ------ | -------------- | --------------- | ------ | ------------------------------------- | --------- |
| 1      | 1594 and later | `selectbox.bss` | 51,612 | 2,060 Entry, 2,015 Type List, 403 Box | 21        |

| Layout | File            | Known             | Unknown    |
| ------ | --------------- | ----------------- | ---------- |
| 1      | `selectbox.bss` | 51,612 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `0b8af83161ed`  |
| 3482   | Layout 1             | `0b8af83161ed`  |
| 3474   | Layout 1             | `0b8af83161ed`  |
| 3473   | Layout 1             | `0b8af83161ed`  |
| 3464   | Layout 1             | `0b8af83161ed`  |
| 3458   | Layout 1             | `0b8af83161ed`  |
| 3454   | Layout 1             | `0b8af83161ed`  |
| 3444   | Layout 1             | `0b8af83161ed`  |
| 3435   | Layout 1             | `0b8af83161ed`  |
| 3426   | Layout 1             | `0b8af83161ed`  |
| 3418   | Layout 1             | `0b8af83161ed`  |
| 3412   | Layout 1             | `0b8af83161ed`  |
| 3402   | Layout 1             | `0b8af83161ed`  |
| 3396   | Layout 1             | `0b8af83161ed`  |
| 3387   | Layout 1             | `0b8af83161ed`  |
| 3381   | Layout 1             | `0b8af83161ed`  |
| 3373   | Layout 1             | `0b8af83161ed`  |
| 3364   | Layout 1             | `0b8af83161ed`  |
| 3356   | Layout 1             | `0b8af83161ed`  |
| 3349   | Layout 1             | `0b8af83161ed`  |
| 3342   | Layout 1             | `0b8af83161ed`  |
| 3335   | Layout 1             | `0b8af83161ed`  |
| 3326   | Layout 1             | `0b8af83161ed`  |
| 3321   | Layout 1             | `0b8af83161ed`  |
| 3314   | Layout 1             | `0b8af83161ed`  |
| 3303   | Layout 1             | `0b8af83161ed`  |
| 3302   | Layout 1             | `0b8af83161ed`  |
| 3293   | Layout 1             | `0b8af83161ed`  |
| 3283   | Layout 1             | `0b8af83161ed`  |
| 3275   | Layout 1             | `0b8af83161ed`  |
| 3267   | Layout 1             | `0b8af83161ed`  |
| 3258   | Layout 1             | `0b8af83161ed`  |
| 3251   | Layout 1             | `0b8af83161ed`  |
| 3242   | Layout 1             | `0b8af83161ed`  |
| 3235   | Layout 1             | `0b8af83161ed`  |
| 3229   | Layout 1             | `0b8af83161ed`  |
| 3212   | Layout 1             | `0b8af83161ed`  |
| 3203   | Layout 1             | `0b8af83161ed`  |
| 3193   | Layout 1             | `0b8af83161ed`  |
| 3186   | Layout 1             | `0b8af83161ed`  |
| 3177   | Layout 1             | `0b8af83161ed`  |
| 3169   | Layout 1             | `0b8af83161ed`  |
| 3158   | Layout 1             | `0b8af83161ed`  |
| 3151   | Layout 1             | `0b8af83161ed`  |
| 3144   | Layout 1             | `0b8af83161ed`  |
| 3133   | Layout 1             | `0b8af83161ed`  |
| 3125   | Layout 1             | `0b8af83161ed`  |
| 3118   | Layout 1             | `0b8af83161ed`  |
| 3111   | Layout 1             | `0b8af83161ed`  |
| 3103   | Layout 1             | `0b8af83161ed`  |
| 3095   | Layout 1             | `0b8af83161ed`  |
| 3086   | Layout 1             | `0b8af83161ed`  |
| 3072   | Layout 1             | `0b8af83161ed`  |
| 3062   | Layout 1             | `0b8af83161ed`  |
| 3052   | Layout 1             | `0b8af83161ed`  |
| 3045   | Layout 1             | `0b8af83161ed`  |
| 3037   | Layout 1             | `0b8af83161ed`  |
| 3030   | Layout 1             | `0b8af83161ed`  |
| 3021   | Layout 1             | `0b8af83161ed`  |
| 3012   | Layout 1             | `0b8af83161ed`  |
| 3002   | Layout 1             | `0b8af83161ed`  |
| 2995   | Layout 1             | `0b8af83161ed`  |
| 2987   | Layout 1             | `0b8af83161ed`  |
| 2978   | Layout 1             | `0b8af83161ed`  |
| 2970   | Layout 1             | `0b8af83161ed`  |
| 2959   | Layout 1             | `0b8af83161ed`  |
| 2951   | Layout 1             | `0b8af83161ed`  |
| 2942   | Layout 1             | `0b8af83161ed`  |
| 2935   | Layout 1             | `0b8af83161ed`  |
| 2932   | Layout 1             | `0b8af83161ed`  |
| 2923   | Layout 1             | `0b8af83161ed`  |
| 2919   | Layout 1             | `0b8af83161ed`  |
| 2907   | Layout 1             | `0b8af83161ed`  |
| 2900   | Layout 1             | `0b8af83161ed`  |
| 2891   | Layout 1             | `0b8af83161ed`  |
| 2882   | Layout 1             | `0b8af83161ed`  |
| 2872   | Layout 1             | `0b8af83161ed`  |
| 2863   | Layout 1             | `0b8af83161ed`  |
| 2855   | Layout 1             | `0b8af83161ed`  |
| 2849   | Layout 1             | `0b8af83161ed`  |
| 2844   | Layout 1             | `0b8af83161ed`  |
| 2834   | Layout 1             | `0b8af83161ed`  |
| 2825   | Layout 1             | `0b8af83161ed`  |
| 2819   | Layout 1             | `0b8af83161ed`  |
| 2811   | Layout 1             | `0b8af83161ed`  |
| 2803   | Layout 1             | `0b8af83161ed`  |
| 2794   | Layout 1             | `0b8af83161ed`  |
| 2783   | Layout 1             | `0b8af83161ed`  |
| 2774   | Layout 1             | `0b8af83161ed`  |
| 2765   | Layout 1             | `0b8af83161ed`  |
| 2756   | Layout 1             | `0b8af83161ed`  |
| 2750   | Layout 1             | `0b8af83161ed`  |
| 2743   | Layout 1             | `0b8af83161ed`  |
| 2736   | Layout 1             | `0b8af83161ed`  |
| 2726   | Layout 1             | `0b8af83161ed`  |
| 2717   | Layout 1             | `0b8af83161ed`  |
| 2709   | Layout 1             | `0b8af83161ed`  |
| 2703   | Layout 1             | `0b8af83161ed`  |
| 2695   | Layout 1             | `0b8af83161ed`  |
| 2684   | Layout 1             | `0b8af83161ed`  |
| 2672   | Layout 1             | `0b8af83161ed`  |
| 2665   | Layout 1             | `0b8af83161ed`  |
| 2657   | Layout 1             | `0b8af83161ed`  |
| 2649   | Layout 1             | `0b8af83161ed`  |
| 2644   | Layout 1             | `0b8af83161ed`  |
| 2637   | Layout 1             | `0b8af83161ed`  |
| 2629   | Layout 1             | `0b8af83161ed`  |
| 2619   | Layout 1             | `0b8af83161ed`  |
| 2612   | Layout 1             | `0b8af83161ed`  |
| 2606   | Layout 1             | `0b8af83161ed`  |
| 2602   | Layout 1             | `0b8af83161ed`  |
| 2601   | Layout 1             | `0b8af83161ed`  |
| 2592   | Layout 1             | `0b8af83161ed`  |
| 2583   | Layout 1             | `0b8af83161ed`  |
| 2575   | Layout 1             | `0b8af83161ed`  |
| 2567   | Layout 1             | `0b8af83161ed`  |
| 2560   | Layout 1             | `0b8af83161ed`  |
| 2553   | Layout 1             | `0b8af83161ed`  |
| 2545   | Layout 1             | `0b8af83161ed`  |
| 2538   | Layout 1             | `0b8af83161ed`  |
| 2529   | Layout 1             | `0b8af83161ed`  |
| 2519   | Layout 1             | `0b8af83161ed`  |
| 2513   | Layout 1             | `0b8af83161ed`  |
| 2510   | Layout 1             | `0b8af83161ed`  |
| 2507   | Layout 1             | `0b8af83161ed`  |
| 2503   | Layout 1             | `0b8af83161ed`  |
| 2498   | Layout 1             | `0b8af83161ed`  |
| 2492   | Layout 1             | `0b8af83161ed`  |
| 2487   | Layout 1             | `0b8af83161ed`  |
| 2480   | Layout 1             | `0b8af83161ed`  |
| 2474   | Layout 1             | `0b8af83161ed`  |
| 2468   | Layout 1             | `0b8af83161ed`  |
| 2460   | Layout 1             | `0b8af83161ed`  |
| 2453   | Layout 1             | `0b8af83161ed`  |
| 2444   | Layout 1             | `0b8af83161ed`  |
| 2438   | Layout 1             | `0b8af83161ed`  |
| 2434   | Layout 1             | `0b8af83161ed`  |
| 2429   | Layout 1             | `0b8af83161ed`  |
| 2421   | Layout 1             | `0b8af83161ed`  |
| 2414   | Layout 1             | `0b8af83161ed`  |
| 2407   | Layout 1             | `0b8af83161ed`  |
| 2401   | Layout 1             | `0b8af83161ed`  |
| 2397   | Layout 1             | `0b8af83161ed`  |
| 2393   | Layout 1             | `0b8af83161ed`  |
| 2384   | Layout 1             | `0b8af83161ed`  |
| 2378   | Layout 1             | `0b8af83161ed`  |
| 2372   | Layout 1             | `0b8af83161ed`  |
| 2358   | Layout 1             | `0b8af83161ed`  |
| 2352   | Layout 1             | `0b8af83161ed`  |
| 2347   | Layout 1             | `0b8af83161ed`  |
| 2343   | Layout 1             | `0b8af83161ed`  |
| 2335   | Layout 1             | `0b8af83161ed`  |
| 2327   | Layout 1             | `0b8af83161ed`  |
| 2324   | Layout 1             | `0b8af83161ed`  |
| 2319   | Layout 1             | `0b8af83161ed`  |
| 2313   | Layout 1             | `0b8af83161ed`  |
| 2308   | Layout 1             | `0b8af83161ed`  |
| 2302   | Layout 1             | `0b8af83161ed`  |
| 2295   | Layout 1             | `0b8af83161ed`  |
| 2290   | Layout 1             | `0b8af83161ed`  |
| 2284   | Layout 1             | `0b8af83161ed`  |
| 2276   | Layout 1             | `0b8af83161ed`  |
| 2269   | Layout 1             | `0b8af83161ed`  |
| 2259   | Layout 1             | `0b8af83161ed`  |
| 2250   | Layout 1             | `0b8af83161ed`  |
| 2243   | Layout 1             | `0b8af83161ed`  |
| 2235   | Layout 1             | `0b8af83161ed`  |
| 2229   | Layout 1             | `0b8af83161ed`  |
| 2224   | Layout 1             | `0b8af83161ed`  |
| 2218   | Layout 1             | `0b8af83161ed`  |
| 2215   | Layout 1             | `0b8af83161ed`  |
| 2207   | Layout 1             | `0b8af83161ed`  |
| 2203   | Layout 1             | `0b8af83161ed`  |
| 2196   | Layout 1             | `0b8af83161ed`  |
| 2192   | Layout 1             | `0b8af83161ed`  |
| 2189   | Layout 1             | `0b8af83161ed`  |
| 2183   | Layout 1             | `0b8af83161ed`  |
| 2179   | Layout 1             | `0b8af83161ed`  |
| 2171   | Layout 1             | `0b8af83161ed`  |
| 2163   | Layout 1             | `0b8af83161ed`  |
| 2156   | Layout 1             | `0b8af83161ed`  |
| 2151   | Layout 1             | `0b8af83161ed`  |
| 2147   | Layout 1             | `0b8af83161ed`  |
| 2142   | Layout 1             | `0b8af83161ed`  |
| 2138   | Layout 1             | `0b8af83161ed`  |
| 2134   | Layout 1             | `0b8af83161ed`  |
| 2130   | Layout 1             | `0b8af83161ed`  |
| 2122   | Layout 1             | `0b8af83161ed`  |
| 2107   | Layout 1             | `0b8af83161ed`  |
| 2098   | Layout 1             | `0b8af83161ed`  |
| 2089   | Layout 1             | `0b8af83161ed`  |
| 2081   | Layout 1             | `0b8af83161ed`  |
| 2073   | Layout 1             | `0b8af83161ed`  |
| 2067   | Layout 1             | `0b8af83161ed`  |
| 2063   | Layout 1             | `0b8af83161ed`  |
| 2059   | Layout 1             | `0b8af83161ed`  |
| 2052   | Layout 1             | `0b8af83161ed`  |
| 2044   | Layout 1             | `0b8af83161ed`  |
| 2039   | Layout 1             | `0b8af83161ed`  |
| 2032   | Layout 1             | `0b8af83161ed`  |
| 2025   | Layout 1             | `0b8af83161ed`  |
| 2011   | Layout 1             | `0b8af83161ed`  |
| 2005   | Layout 1             | `0b8af83161ed`  |
| 2000   | Layout 1             | `0b8af83161ed`  |
| 1996   | Layout 1             | `0b8af83161ed`  |
| 1991   | Layout 1             | `0b8af83161ed`  |
| 1985   | Layout 1             | `0b8af83161ed`  |
| 1980   | Layout 1             | `0b8af83161ed`  |
| 1969   | Layout 1             | `0b8af83161ed`  |
| 1964   | Layout 1             | `0b8af83161ed`  |
| 1958   | Layout 1             | `0b8af83161ed`  |
| 1950   | Layout 1             | `0b8af83161ed`  |
| 1945   | Layout 1             | `0b8af83161ed`  |
| 1937   | Layout 1             | `0b8af83161ed`  |
| 1933   | Layout 1             | `0b8af83161ed`  |
| 1927   | Layout 1             | `0b8af83161ed`  |
| 1921   | Layout 1             | `0b8af83161ed`  |
| 1914   | Layout 1             | `0b8af83161ed`  |
| 1908   | Layout 1             | `0b8af83161ed`  |
| 1897   | Layout 1             | `0b8af83161ed`  |
| 1892   | Layout 1             | `0b8af83161ed`  |
| 1886   | Layout 1             | `0b8af83161ed`  |
| 1881   | Layout 1             | `0b8af83161ed`  |
| 1871   | Layout 1             | `0b8af83161ed`  |
| 1866   | Layout 1             | `0b8af83161ed`  |
| 1862   | Layout 1             | `0b8af83161ed`  |
| 1854   | Layout 1             | `0b8af83161ed`  |
| 1846   | Layout 1             | `0b8af83161ed`  |
| 1838   | Layout 1             | `0b8af83161ed`  |
| 1832   | Layout 1             | `0b8af83161ed`  |
| 1826   | Layout 1             | `0b8af83161ed`  |
| 1822   | Layout 1             | `0b8af83161ed`  |
| 1818   | Layout 1             | `0b8af83161ed`  |
| 1804   | Layout 1             | `0b8af83161ed`  |
| 1794   | Layout 1             | `0b8af83161ed`  |
| 1790   | Layout 1             | `0b8af83161ed`  |
| 1784   | Layout 1             | `0b8af83161ed`  |
| 1774   | Layout 1             | `0b8af83161ed`  |
| 1771   | Layout 1             | `0b8af83161ed`  |
| 1762   | Layout 1             | `0b8af83161ed`  |
| 1759   | Layout 1             | `0b8af83161ed`  |
| 1754   | Layout 1             | `0b8af83161ed`  |
| 1749   | Layout 1             | `0b8af83161ed`  |
| 1743   | Layout 1             | `0b8af83161ed`  |
| 1737   | Layout 1             | `0b8af83161ed`  |
| 1731   | Layout 1             | `0b8af83161ed`  |
| 1725   | Layout 1             | `0b8af83161ed`  |
| 1717   | Layout 1             | `0b8af83161ed`  |
| 1710   | Layout 1             | `0b8af83161ed`  |
| 1704   | Layout 1             | `0b8af83161ed`  |
| 1698   | Layout 1             | `0b8af83161ed`  |
| 1690   | Layout 1             | `0b8af83161ed`  |
| 1685   | Layout 1             | `0b8af83161ed`  |
| 1680   | Layout 1             | `0b8af83161ed`  |
| 1674   | Layout 1             | `0b8af83161ed`  |
| 1668   | Layout 1             | `0b8af83161ed`  |
| 1659   | Layout 1             | `0b8af83161ed`  |
| 1649   | Layout 1             | `0b8af83161ed`  |
| 1642   | Layout 1             | `0b8af83161ed`  |
| 1636   | Layout 1             | `0b8af83161ed`  |
| 1628   | Layout 1             | `0b8af83161ed`  |
| 1622   | Layout 1             | `0b8af83161ed`  |
| 1614   | Layout 1             | `0b8af83161ed`  |
| 1608   | Layout 1             | `0b8af83161ed`  |
| 1602   | Layout 1             | `0b8af83161ed`  |
| 1598   | Layout 1             | `0b8af83161ed`  |
| 1594   | Layout 1             | `0b8af83161ed`  |
| 1590   | No documented layout | `0b8af83161ed`  |
| 1587   | No file              | `0b8af83161ed`  |
| 1584   | No file              | `0b8af83161ed`  |
| 1579   | No file              | `0b8af83161ed`  |
| 1572   | No file              | `0b8af83161ed`  |
| 1565   | No file              | `0b8af83161ed`  |
| 1559   | No file              | `0b8af83161ed`  |
| 1554   | No file              | `0b8af83161ed`  |
| 1547   | No file              | `0b8af83161ed`  |
| 1537   | No file              | `0b8af83161ed`  |
| 1529   | No file              | `0b8af83161ed`  |
| 1524   | No file              | `0b8af83161ed`  |
| 1519   | No file              | `0b8af83161ed`  |
| 1509   | No file              | `0b8af83161ed`  |
| 1506   | No file              | `0b8af83161ed`  |
| 1504   | No file              | `0b8af83161ed`  |
| 1500   | No file              | `0b8af83161ed`  |
| 1493   | No file              | `0b8af83161ed`  |
| 1489   | No file              | `0b8af83161ed`  |
| 1485   | No file              | `0b8af83161ed`  |
| 1481   | No file              | `0b8af83161ed`  |
| 1474   | No file              | `0b8af83161ed`  |
| 1466   | No file              | `0b8af83161ed`  |
| 1462   | No file              | `0b8af83161ed`  |
| 1459   | No file              | `0b8af83161ed`  |
| 1453   | No file              | `0b8af83161ed`  |
| 1450   | No file              | `0b8af83161ed`  |
| 1445   | No file              | `0b8af83161ed`  |
| 1439   | No file              | `0b8af83161ed`  |
| 1433   | No file              | `0b8af83161ed`  |
| 1430   | No file              | `0b8af83161ed`  |
| 1426   | No file              | `0b8af83161ed`  |
| 1421   | No file              | `0b8af83161ed`  |
| 1417   | No file              | `0b8af83161ed`  |
| 1416   | No file              | `0b8af83161ed`  |
| 1409   | No file              | `0b8af83161ed`  |
| 1405   | No file              | `0b8af83161ed`  |
| 1401   | No file              | `0b8af83161ed`  |
| 1396   | No file              | `0b8af83161ed`  |
| 1391   | No file              | `0b8af83161ed`  |
| 1390   | No file              | `0b8af83161ed`  |
| 1386   | No file              | `0b8af83161ed`  |
| 1381   | No file              | `0b8af83161ed`  |
| 1379   | No file              | `0b8af83161ed`  |
| 1372   | No file              | `0b8af83161ed`  |
| 1366   | No file              | `0b8af83161ed`  |
| 1364   | No file              | `0b8af83161ed`  |
| 1363   | No file              | `0b8af83161ed`  |
| 1360   | No file              | `0b8af83161ed`  |
| 1358   | No file              | `0b8af83161ed`  |
| 1355   | No file              | `0b8af83161ed`  |
| 1351   | No file              | `0b8af83161ed`  |
| 1348   | No file              | `0b8af83161ed`  |
| 1346   | No file              | `0b8af83161ed`  |
| 1341   | No file              | `0b8af83161ed`  |
| 1340   | No file              | `0b8af83161ed`  |
| 1338   | No file              | `0b8af83161ed`  |
| 1335   | No file              | `0b8af83161ed`  |
| 1333   | No file              | `0b8af83161ed`  |
| 1329   | No file              | `0b8af83161ed`  |
| 1327   | No file              | `0b8af83161ed`  |
| 1324   | No file              | `0b8af83161ed`  |
| 1321   | No file              | `0b8af83161ed`  |
| 1319   | No file              | `0b8af83161ed`  |
| 1318   | No file              | `0b8af83161ed`  |
| 1316   | No file              | `0b8af83161ed`  |
| 1313   | No file              | `0b8af83161ed`  |
| 1311   | No file              | `0b8af83161ed`  |
| 1309   | No file              | `0b8af83161ed`  |
| 1304   | No file              | `0b8af83161ed`  |
| 1292   | No file              | `0b8af83161ed`  |
| 1286   | No file              | `0b8af83161ed`  |
| 1280   | No file              | `0b8af83161ed`  |
| 1276   | No file              | `0b8af83161ed`  |
| 1267   | No file              | `0b8af83161ed`  |
| 1261   | No file              | `0b8af83161ed`  |
| 1256   | No file              | `0b8af83161ed`  |
| 1250   | No file              | `0b8af83161ed`  |
| 1246   | No file              | `0b8af83161ed`  |
| 1239   | No file              | `0b8af83161ed`  |
| 1230   | No file              | `0b8af83161ed`  |
| 1226   | No file              | `0b8af83161ed`  |
| 1220   | No file              | `0b8af83161ed`  |
| 1217   | No file              | `0b8af83161ed`  |
| 1211   | No file              | `0b8af83161ed`  |
| 1210   | No file              | `0b8af83161ed`  |
| 1208   | No file              | `0b8af83161ed`  |
| 1203   | No file              | `0b8af83161ed`  |
| 1197   | No file              | `0b8af83161ed`  |
| 1194   | No file              | `0b8af83161ed`  |
| 1192   | No file              | `0b8af83161ed`  |
| 1187   | No file              | `0b8af83161ed`  |
| 1183   | No file              | `0b8af83161ed`  |
| 1177   | No file              | `0b8af83161ed`  |
| 1173   | No file              | `0b8af83161ed`  |
| 1167   | No file              | `0b8af83161ed`  |
| 1164   | No file              | `0b8af83161ed`  |
| 1156   | No file              | `0b8af83161ed`  |
| 1149   | No file              | `0b8af83161ed`  |
| 1144   | No file              | `0b8af83161ed`  |
| 1137   | No file              | `0b8af83161ed`  |
| 1132   | No file              | `0b8af83161ed`  |
| 1127   | No file              | `0b8af83161ed`  |
| 1122   | No file              | `0b8af83161ed`  |
| 1118   | No file              | `0b8af83161ed`  |
| 1114   | No file              | `0b8af83161ed`  |
| 1109   | No file              | `0b8af83161ed`  |
| 1102   | No file              | `0b8af83161ed`  |
| 1096   | No file              | `0b8af83161ed`  |
| 1088   | No file              | `0b8af83161ed`  |
| 1081   | No file              | `0b8af83161ed`  |
| 1076   | No file              | `0b8af83161ed`  |
| 1069   | No file              | `0b8af83161ed`  |
| 1064   | No file              | `0b8af83161ed`  |
| 1058   | No file              | `0b8af83161ed`  |
| 1051   | No file              | `0b8af83161ed`  |
| 1044   | No file              | `0b8af83161ed`  |
| 1036   | No file              | `0b8af83161ed`  |
| 1026   | No file              | `0b8af83161ed`  |
| 1016   | No file              | `0b8af83161ed`  |
| 1009   | No file              | `0b8af83161ed`  |
| 1005   | No file              | `0b8af83161ed`  |
| 1000   | No file              | `0b8af83161ed`  |
| 998    | No file              | `0b8af83161ed`  |
| 990    | No file              | `0b8af83161ed`  |
| 979    | No file              | `0b8af83161ed`  |
| 972    | No file              | `0b8af83161ed`  |
| 963    | No file              | `0b8af83161ed`  |
| 955    | No file              | `0b8af83161ed`  |
| 946    | No file              | `0b8af83161ed`  |
| 938    | No file              | `0b8af83161ed`  |
| 927    | No file              | `0b8af83161ed`  |
| 911    | No file              | `0b8af83161ed`  |
| 904    | No file              | `0b8af83161ed`  |
| 899    | No file              | `0b8af83161ed`  |
| 894    | No file              | `0b8af83161ed`  |
| 885    | No file              | `0b8af83161ed`  |
| 879    | No file              | `0b8af83161ed`  |
| 872    | No file              | `0b8af83161ed`  |
| 864    | No file              | `0b8af83161ed`  |
| 855    | No file              | `0b8af83161ed`  |
| 853    | No file              | `0b8af83161ed`  |
| 845    | No file              | `0b8af83161ed`  |
| 837    | No file              | `0b8af83161ed`  |
| 829    | No file              | `0b8af83161ed`  |
| 822    | No file              | `0b8af83161ed`  |
| 814    | No file              | `0b8af83161ed`  |
| 805    | No file              | `0b8af83161ed`  |
| 794    | No file              | `0b8af83161ed`  |
| 787    | No file              | `0b8af83161ed`  |
| 780    | No file              | `0b8af83161ed`  |
| 771    | No file              | `0b8af83161ed`  |
| 760    | No file              | `0b8af83161ed`  |
| 748    | No file              | `0b8af83161ed`  |
| 741    | No file              | `0b8af83161ed`  |
| 736    | No file              | `0b8af83161ed`  |
| 731    | No file              | `0b8af83161ed`  |
| 723    | No file              | `0b8af83161ed`  |
| 711    | No file              | `0b8af83161ed`  |
| 707    | No file              | `0b8af83161ed`  |
| 697    | No file              | `0b8af83161ed`  |
| 689    | No file              | `0b8af83161ed`  |
| 683    | No file              | `0b8af83161ed`  |
| 678    | No file              | `0b8af83161ed`  |
| 670    | No file              | `0b8af83161ed`  |
| 661    | No file              | `0b8af83161ed`  |
| 656    | No file              | `0b8af83161ed`  |
| 652    | No file              | `0b8af83161ed`  |
| 643    | No file              | `0b8af83161ed`  |
| 637    | No file              | `0b8af83161ed`  |
| 630    | No file              | `0b8af83161ed`  |
| 627    | No file              | `0b8af83161ed`  |
| 621    | No file              | `0b8af83161ed`  |
| 617    | No file              | `0b8af83161ed`  |
| 615    | No file              | `0b8af83161ed`  |
| 606    | No file              | `0b8af83161ed`  |
| 599    | No file              | `0b8af83161ed`  |
| 592    | No file              | `0b8af83161ed`  |
| 586    | No file              | `0b8af83161ed`  |
| 577    | No file              | `0b8af83161ed`  |
| 569    | No file              | `0b8af83161ed`  |
| 561    | No file              | `0b8af83161ed`  |
| 554    | No file              | `0b8af83161ed`  |
| 542    | No file              | `0b8af83161ed`  |
| 532    | No file              | `0b8af83161ed`  |
| 531    | No file              | `0b8af83161ed`  |
| 526    | No file              | `0b8af83161ed`  |
| 521    | No file              | `0b8af83161ed`  |
| 517    | No file              | `0b8af83161ed`  |
| 510    | No file              | `0b8af83161ed`  |
| 508    | No file              | `0b8af83161ed`  |
| 504    | No file              | `0b8af83161ed`  |
| 497    | No file              | `0b8af83161ed`  |
| 491    | No file              | `0b8af83161ed`  |
| 485    | No file              | `0b8af83161ed`  |
| 478    | No file              | `0b8af83161ed`  |
| 472    | No file              | `0b8af83161ed`  |
| 466    | No file              | `0b8af83161ed`  |
| 457    | No file              | `0b8af83161ed`  |
| 452    | No file              | `0b8af83161ed`  |
| 449    | No file              | `0b8af83161ed`  |
| 435    | No file              | `0b8af83161ed`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                    |
| --------------------- | -------- | ----------------------- |
| `languagedata_en.loc` | Optional | Item names (LOC type 0) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type                 | Field        | Notes                                         |
| ------------------- | -------------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]              | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32                  | box_count    | Number of boxes                               |
| `+0x08`             | Box[box_count]       | boxes        | See Box; in no key order                      |
| `boxes+0x00`        | String Table         | string_table | See String Table                              |
| `string_table+0x00` | u32                  | table_start  | Offset of the string table, where `boxes` ends |
| `string_table+0x04` | u32                  | zero         | Always `0`                                    |

### Box (variable: 0 bytes + five type lists)

The box stores no key of its own; every entry repeats it.

| Offset  | Type         | Field      | Notes                                                                 |
| ------- | ------------ | ---------- | --------------------------------------------------------------------- |
| `+0x00` | Type List[5] | type_lists | Type `0` to `4` in order (`__eSelectBoxTypeCount`); see Type List      |

### Type List (variable: 4 bytes + entries)

| Offset  | Type               | Field       | Notes                                                    |
| ------- | ------------------ | ----------- | -------------------------------------------------------- |
| `+0x00` | u32                | entry_count | Number of `entries`; `0` for a type the box does not use |
| `+0x04` | Entry[entry_count] | entries     | See Entry; the index the Lua passes is the place in this list |

### Entry (21 bytes)

| Offset  | Type | Field        | Notes                                                                                          |
| ------- | ---- | ------------ | ---------------------------------------------------------------------------------------------- |
| `+0x00` | u32  | key          | Box key, the same in every entry of a box; the `contents_event_param1` of the box item          |
| `+0x04` | u8   | type         | The type list the entry is in, `0` to `4`                                                       |
| `+0x05` | u32  | item_key     | Item the entry gives, a packed item key (`enchant_level << 24 \| item_id`); levels up to `20` on client 3482 |
| `+0x09` | u64  | item_count   | How many of the item                                                                            |
| `+0x11` | u32  | texture_name | Index into `strings`: the tab texture (`Combine_Tab_Icon_Daily`)                                |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                 |
| ------- | ------------------ | ------------ | --------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; 10 on client 3482                                  |
| `+0x04` | pstr[string_count] | strings      | The tab texture names, UTF-8, each once (`Combine_Tab_Icon_Dark`, `Combine_Tab_Icon_Hunt`) |

## Field Names

The `Item_SelectBox` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `Key`, `TextureName`, `Type`, `ItemKey`,
`ItemCount` and `ContentsGroupKey`, one sheet row per entry. All 214
entries of the client 1784 file equal a sheet row on `Key`, `ItemKey`,
`ItemCount` and the string `TextureName` points at, with `type` one less
than the sheet's `Type` (`1` to `4`). The sheet has 232 rows; the 18 the file
lacks are the rows of keys 42 and 48 to 50. `ContentsGroupKey` has no field,
and the sheet's `Type` gives the name of `type`.

On client 3482, 216 of the 2,060 entries equal a sheet row; the file has 403
boxes against the sheet's 43 keys.

## Notes

- On clients 1784 and 3482 the entries of a box share one key, each type
  list holds only entries of its own type, and no box has all five lists
  empty. Client 3482 has 354 boxes with one used type, 23 with two, 13 with
  three, 11 with four and 2 with five; the longest list has 10 entries.
- On client 3482, two type lists hold entries with different textures; the
  Lua asks for one texture per type.
- An item whose `contents_event_type` is `114` names a box in
  `contents_event_param1`: on client 3482 the 386 such items name 379
  boxes, every one a key of the file ("Choose Your Ultimate Enhancement
  Box", item 860344, names `403`).
- The handler (`_bss/selectbox/`) shows one row per box with the items of
  each type and the tab textures.

## Open Questions

### Which Boxes No Item Opens

On client 3482, 24 box keys (14, 30, 38, 48, 56, 97, 151, 265, 297 and
more) are named by no item with contents event `114`. They may be boxes of
removed events, or boxes another contents event opens.
