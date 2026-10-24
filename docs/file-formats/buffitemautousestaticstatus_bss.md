# `buffitemautousestaticstatus.bss` Format

## Purpose

The items the auto-use of buff items (a Fairy skill) can use: one 9-byte
row per item with its category. The categories are the rows of
[`autousebuffitemcategoryinfo.bss`](autousebuffitemcategoryinfo_bss.md). The auto-use window
(`panel_window_autousebuffitem_1.luac`) walks
`ToClient_getAutoUseBuffItemCategoryCount()` and
`ToClient_getAutoUseBuffItemCategoryKey(index)`, names each category with
`ToClient_getAutoUseBuffItemCategoryStaticStatusWrapper(categoryKey):getCategoryName()`
and lists its items with
`ToClient_getAutoUseBuffItemElement(categoryKey, buffCategory, index)`,
whose `getItemKey()` is the item.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                              | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------------------------- | ----- | ------- | --------- |
| 2      | 2583 and later | 3483    | `buffitemautousestaticstatus.bss` | 8,228 | 912 Row | 9         |
| 1      | 1969 to 2575   | 2575    | `buffitemautousestaticstatus.bss` | 4,980 | 620 Row | 8         |

| Layout | File                              | Known            | Unknown       |
| ------ | --------------------------------- | ---------------- | ------------- |
| 2      | `buffitemautousestaticstatus.bss` | 7,316 B (88.9%)  | 912 B (11.1%) |
| 1      | `buffitemautousestaticstatus.bss` | 4,980 B (100.0%) | 0 B (0.0%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `23a2fafb947d`  |
| 3482   | Layout 2             | `23a2fafb947d`  |
| 3474   | Layout 2             | `23a2fafb947d`  |
| 3473   | Layout 2             | `23a2fafb947d`  |
| 3464   | Layout 2             | `23a2fafb947d`  |
| 3458   | Layout 2             | `23a2fafb947d`  |
| 3454   | Layout 2             | `23a2fafb947d`  |
| 3444   | Layout 2             | `23a2fafb947d`  |
| 3435   | Layout 2             | `23a2fafb947d`  |
| 3426   | Layout 2             | `23a2fafb947d`  |
| 3418   | Layout 2             | `23a2fafb947d`  |
| 3412   | Layout 2             | `23a2fafb947d`  |
| 3402   | Layout 2             | `23a2fafb947d`  |
| 3396   | Layout 2             | `23a2fafb947d`  |
| 3387   | Layout 2             | `23a2fafb947d`  |
| 3381   | Layout 2             | `23a2fafb947d`  |
| 3373   | Layout 2             | `23a2fafb947d`  |
| 3364   | Layout 2             | `23a2fafb947d`  |
| 3356   | Layout 2             | `23a2fafb947d`  |
| 3349   | Layout 2             | `23a2fafb947d`  |
| 3342   | Layout 2             | `23a2fafb947d`  |
| 3335   | Layout 2             | `23a2fafb947d`  |
| 3326   | Layout 2             | `23a2fafb947d`  |
| 3321   | Layout 2             | `23a2fafb947d`  |
| 3314   | Layout 2             | `23a2fafb947d`  |
| 3303   | Layout 2             | `23a2fafb947d`  |
| 3302   | Layout 2             | `23a2fafb947d`  |
| 3293   | Layout 2             | `23a2fafb947d`  |
| 3283   | Layout 2             | `23a2fafb947d`  |
| 3275   | Layout 2             | `23a2fafb947d`  |
| 3267   | Layout 2             | `23a2fafb947d`  |
| 3258   | Layout 2             | `23a2fafb947d`  |
| 3251   | Layout 2             | `23a2fafb947d`  |
| 3242   | Layout 2             | `23a2fafb947d`  |
| 3235   | Layout 2             | `23a2fafb947d`  |
| 3229   | Layout 2             | `23a2fafb947d`  |
| 3212   | Layout 2             | `23a2fafb947d`  |
| 3203   | Layout 2             | `23a2fafb947d`  |
| 3193   | Layout 2             | `23a2fafb947d`  |
| 3186   | Layout 2             | `23a2fafb947d`  |
| 3177   | Layout 2             | `23a2fafb947d`  |
| 3169   | Layout 2             | `23a2fafb947d`  |
| 3158   | Layout 2             | `23a2fafb947d`  |
| 3151   | Layout 2             | `23a2fafb947d`  |
| 3144   | Layout 2             | `23a2fafb947d`  |
| 3133   | Layout 2             | `23a2fafb947d`  |
| 3125   | Layout 2             | `23a2fafb947d`  |
| 3118   | Layout 2             | `23a2fafb947d`  |
| 3111   | Layout 2             | `23a2fafb947d`  |
| 3103   | Layout 2             | `23a2fafb947d`  |
| 3095   | Layout 2             | `23a2fafb947d`  |
| 3086   | Layout 2             | `23a2fafb947d`  |
| 3072   | Layout 2             | `23a2fafb947d`  |
| 3062   | Layout 2             | `23a2fafb947d`  |
| 3052   | Layout 2             | `23a2fafb947d`  |
| 3045   | Layout 2             | `23a2fafb947d`  |
| 3037   | Layout 2             | `23a2fafb947d`  |
| 3030   | Layout 2             | `23a2fafb947d`  |
| 3021   | Layout 2             | `23a2fafb947d`  |
| 3012   | Layout 2             | `23a2fafb947d`  |
| 3002   | Layout 2             | `23a2fafb947d`  |
| 2995   | Layout 2             | `23a2fafb947d`  |
| 2987   | Layout 2             | `23a2fafb947d`  |
| 2978   | Layout 2             | `23a2fafb947d`  |
| 2970   | Layout 2             | `23a2fafb947d`  |
| 2959   | Layout 2             | `23a2fafb947d`  |
| 2951   | Layout 2             | `23a2fafb947d`  |
| 2942   | Layout 2             | `23a2fafb947d`  |
| 2935   | Layout 2             | `23a2fafb947d`  |
| 2932   | Layout 2             | `23a2fafb947d`  |
| 2923   | Layout 2             | `23a2fafb947d`  |
| 2919   | Layout 2             | `23a2fafb947d`  |
| 2907   | Layout 2             | `23a2fafb947d`  |
| 2900   | Layout 2             | `23a2fafb947d`  |
| 2891   | Layout 2             | `23a2fafb947d`  |
| 2882   | Layout 2             | `23a2fafb947d`  |
| 2872   | Layout 2             | `23a2fafb947d`  |
| 2863   | Layout 2             | `23a2fafb947d`  |
| 2855   | Layout 2             | `23a2fafb947d`  |
| 2849   | Layout 2             | `23a2fafb947d`  |
| 2844   | Layout 2             | `23a2fafb947d`  |
| 2834   | Layout 2             | `23a2fafb947d`  |
| 2825   | Layout 2             | `23a2fafb947d`  |
| 2819   | Layout 2             | `23a2fafb947d`  |
| 2811   | Layout 2             | `23a2fafb947d`  |
| 2803   | Layout 2             | `23a2fafb947d`  |
| 2794   | Layout 2             | `23a2fafb947d`  |
| 2783   | Layout 2             | `23a2fafb947d`  |
| 2774   | Layout 2             | `23a2fafb947d`  |
| 2765   | Layout 2             | `23a2fafb947d`  |
| 2756   | Layout 2             | `23a2fafb947d`  |
| 2750   | Layout 2             | `23a2fafb947d`  |
| 2743   | Layout 2             | `23a2fafb947d`  |
| 2736   | Layout 2             | `23a2fafb947d`  |
| 2726   | Layout 2             | `23a2fafb947d`  |
| 2717   | Layout 2             | `23a2fafb947d`  |
| 2709   | Layout 2             | `23a2fafb947d`  |
| 2703   | Layout 2             | `23a2fafb947d`  |
| 2695   | Layout 2             | `23a2fafb947d`  |
| 2684   | Layout 2             | `23a2fafb947d`  |
| 2672   | Layout 2             | `23a2fafb947d`  |
| 2665   | Layout 2             | `23a2fafb947d`  |
| 2657   | Layout 2             | `23a2fafb947d`  |
| 2649   | Layout 2             | `23a2fafb947d`  |
| 2644   | Layout 2             | `23a2fafb947d`  |
| 2637   | Layout 2             | `23a2fafb947d`  |
| 2629   | Layout 2             | `23a2fafb947d`  |
| 2619   | Layout 2             | `23a2fafb947d`  |
| 2612   | Layout 2             | `23a2fafb947d`  |
| 2606   | Layout 2             | `23a2fafb947d`  |
| 2602   | Layout 2             | `23a2fafb947d`  |
| 2601   | Layout 2             | `23a2fafb947d`  |
| 2592   | Layout 2             | `23a2fafb947d`  |
| 2583   | Layout 2             | `23a2fafb947d`  |
| 2575   | Layout 1             | `23a2fafb947d`  |
| 2567   | Layout 1             | `23a2fafb947d`  |
| 2560   | Layout 1             | `23a2fafb947d`  |
| 2553   | Layout 1             | `23a2fafb947d`  |
| 2545   | Layout 1             | `23a2fafb947d`  |
| 2538   | Layout 1             | `23a2fafb947d`  |
| 2529   | Layout 1             | `23a2fafb947d`  |
| 2519   | Layout 1             | `23a2fafb947d`  |
| 2513   | Layout 1             | `23a2fafb947d`  |
| 2510   | Layout 1             | `23a2fafb947d`  |
| 2507   | Layout 1             | `23a2fafb947d`  |
| 2503   | Layout 1             | `23a2fafb947d`  |
| 2498   | Layout 1             | `23a2fafb947d`  |
| 2492   | Layout 1             | `23a2fafb947d`  |
| 2487   | Layout 1             | `23a2fafb947d`  |
| 2480   | Layout 1             | `23a2fafb947d`  |
| 2474   | Layout 1             | `23a2fafb947d`  |
| 2468   | Layout 1             | `23a2fafb947d`  |
| 2460   | Layout 1             | `23a2fafb947d`  |
| 2453   | Layout 1             | `23a2fafb947d`  |
| 2444   | Layout 1             | `23a2fafb947d`  |
| 2438   | Layout 1             | `23a2fafb947d`  |
| 2434   | Layout 1             | `23a2fafb947d`  |
| 2429   | Layout 1             | `23a2fafb947d`  |
| 2421   | Layout 1             | `23a2fafb947d`  |
| 2414   | Layout 1             | `23a2fafb947d`  |
| 2407   | Layout 1             | `23a2fafb947d`  |
| 2401   | Layout 1             | `23a2fafb947d`  |
| 2397   | Layout 1             | `23a2fafb947d`  |
| 2393   | Layout 1             | `23a2fafb947d`  |
| 2384   | Layout 1             | `23a2fafb947d`  |
| 2378   | Layout 1             | `23a2fafb947d`  |
| 2372   | Layout 1             | `23a2fafb947d`  |
| 2358   | Layout 1             | `23a2fafb947d`  |
| 2352   | Layout 1             | `23a2fafb947d`  |
| 2347   | Layout 1             | `23a2fafb947d`  |
| 2343   | Layout 1             | `23a2fafb947d`  |
| 2335   | Layout 1             | `23a2fafb947d`  |
| 2327   | Layout 1             | `23a2fafb947d`  |
| 2324   | Layout 1             | `23a2fafb947d`  |
| 2319   | Layout 1             | `23a2fafb947d`  |
| 2313   | Layout 1             | `23a2fafb947d`  |
| 2308   | Layout 1             | `23a2fafb947d`  |
| 2302   | Layout 1             | `23a2fafb947d`  |
| 2295   | Layout 1             | `23a2fafb947d`  |
| 2290   | Layout 1             | `23a2fafb947d`  |
| 2284   | Layout 1             | `23a2fafb947d`  |
| 2276   | Layout 1             | `23a2fafb947d`  |
| 2269   | Layout 1             | `23a2fafb947d`  |
| 2259   | Layout 1             | `23a2fafb947d`  |
| 2250   | Layout 1             | `23a2fafb947d`  |
| 2243   | Layout 1             | `23a2fafb947d`  |
| 2235   | Layout 1             | `23a2fafb947d`  |
| 2229   | Layout 1             | `23a2fafb947d`  |
| 2224   | Layout 1             | `23a2fafb947d`  |
| 2218   | Layout 1             | `23a2fafb947d`  |
| 2215   | Layout 1             | `23a2fafb947d`  |
| 2207   | Layout 1             | `23a2fafb947d`  |
| 2203   | Layout 1             | `23a2fafb947d`  |
| 2196   | Layout 1             | `23a2fafb947d`  |
| 2192   | Layout 1             | `23a2fafb947d`  |
| 2189   | Layout 1             | `23a2fafb947d`  |
| 2183   | Layout 1             | `23a2fafb947d`  |
| 2179   | Layout 1             | `23a2fafb947d`  |
| 2171   | Layout 1             | `23a2fafb947d`  |
| 2163   | Layout 1             | `23a2fafb947d`  |
| 2156   | Layout 1             | `23a2fafb947d`  |
| 2151   | Layout 1             | `23a2fafb947d`  |
| 2147   | Layout 1             | `23a2fafb947d`  |
| 2142   | Layout 1             | `23a2fafb947d`  |
| 2138   | Layout 1             | `23a2fafb947d`  |
| 2134   | Layout 1             | `23a2fafb947d`  |
| 2130   | Layout 1             | `23a2fafb947d`  |
| 2122   | Layout 1             | `23a2fafb947d`  |
| 2107   | Layout 1             | `23a2fafb947d`  |
| 2098   | Layout 1             | `23a2fafb947d`  |
| 2089   | Layout 1             | `23a2fafb947d`  |
| 2081   | Layout 1             | `23a2fafb947d`  |
| 2073   | Layout 1             | `23a2fafb947d`  |
| 2067   | Layout 1             | `23a2fafb947d`  |
| 2063   | Layout 1             | `23a2fafb947d`  |
| 2059   | Layout 1             | `23a2fafb947d`  |
| 2052   | Layout 1             | `23a2fafb947d`  |
| 2044   | Layout 1             | `23a2fafb947d`  |
| 2039   | Layout 1             | `23a2fafb947d`  |
| 2032   | Layout 1             | `23a2fafb947d`  |
| 2025   | Layout 1             | `23a2fafb947d`  |
| 2011   | Layout 1             | `23a2fafb947d`  |
| 2005   | Layout 1             | `23a2fafb947d`  |
| 2000   | Layout 1             | `23a2fafb947d`  |
| 1996   | Layout 1             | `23a2fafb947d`  |
| 1991   | Layout 1             | `23a2fafb947d`  |
| 1985   | Layout 1             | `23a2fafb947d`  |
| 1980   | Layout 1             | `23a2fafb947d`  |
| 1969   | Layout 1             | `23a2fafb947d`  |
| 1964   | No file              | `23a2fafb947d`  |
| 1958   | No file              | `23a2fafb947d`  |
| 1950   | No file              | `23a2fafb947d`  |
| 1945   | No documented layout | `23a2fafb947d`  |
| 1937   | No file              | `23a2fafb947d`  |
| 1933   | No file              | `23a2fafb947d`  |
| 1927   | No file              | `23a2fafb947d`  |
| 1921   | No file              | `23a2fafb947d`  |
| 1914   | No file              | `23a2fafb947d`  |
| 1908   | No file              | `23a2fafb947d`  |
| 1897   | No file              | `23a2fafb947d`  |
| 1892   | No file              | `23a2fafb947d`  |
| 1886   | No file              | `23a2fafb947d`  |
| 1881   | No file              | `23a2fafb947d`  |
| 1871   | No file              | `23a2fafb947d`  |
| 1866   | No file              | `23a2fafb947d`  |
| 1862   | No file              | `23a2fafb947d`  |
| 1854   | No file              | `23a2fafb947d`  |
| 1846   | No file              | `23a2fafb947d`  |
| 1838   | No file              | `23a2fafb947d`  |
| 1832   | No file              | `23a2fafb947d`  |
| 1826   | No file              | `23a2fafb947d`  |
| 1822   | No file              | `23a2fafb947d`  |
| 1818   | No file              | `23a2fafb947d`  |
| 1804   | No file              | `23a2fafb947d`  |
| 1794   | No file              | `23a2fafb947d`  |
| 1790   | No file              | `23a2fafb947d`  |
| 1784   | No file              | `23a2fafb947d`  |
| 1774   | No file              | `23a2fafb947d`  |
| 1771   | No file              | `23a2fafb947d`  |
| 1762   | No file              | `23a2fafb947d`  |
| 1759   | No file              | `23a2fafb947d`  |
| 1754   | No file              | `23a2fafb947d`  |
| 1749   | No file              | `23a2fafb947d`  |
| 1743   | No file              | `23a2fafb947d`  |
| 1737   | No file              | `23a2fafb947d`  |
| 1731   | No file              | `23a2fafb947d`  |
| 1725   | No file              | `23a2fafb947d`  |
| 1717   | No file              | `23a2fafb947d`  |
| 1710   | No file              | `23a2fafb947d`  |
| 1704   | No file              | `23a2fafb947d`  |
| 1698   | No file              | `23a2fafb947d`  |
| 1690   | No file              | `23a2fafb947d`  |
| 1685   | No file              | `23a2fafb947d`  |
| 1680   | No file              | `23a2fafb947d`  |
| 1674   | No file              | `23a2fafb947d`  |
| 1668   | No file              | `23a2fafb947d`  |
| 1659   | No file              | `23a2fafb947d`  |
| 1649   | No file              | `23a2fafb947d`  |
| 1642   | No file              | `23a2fafb947d`  |
| 1636   | No file              | `23a2fafb947d`  |
| 1628   | No file              | `23a2fafb947d`  |
| 1622   | No file              | `23a2fafb947d`  |
| 1614   | No file              | `23a2fafb947d`  |
| 1608   | No file              | `23a2fafb947d`  |
| 1602   | No file              | `23a2fafb947d`  |
| 1598   | No file              | `23a2fafb947d`  |
| 1594   | No file              | `23a2fafb947d`  |
| 1590   | No file              | `23a2fafb947d`  |
| 1587   | No file              | `23a2fafb947d`  |
| 1584   | No file              | `23a2fafb947d`  |
| 1579   | No file              | `23a2fafb947d`  |
| 1572   | No file              | `23a2fafb947d`  |
| 1565   | No file              | `23a2fafb947d`  |
| 1559   | No file              | `23a2fafb947d`  |
| 1554   | No file              | `23a2fafb947d`  |
| 1547   | No file              | `23a2fafb947d`  |
| 1537   | No file              | `23a2fafb947d`  |
| 1529   | No file              | `23a2fafb947d`  |
| 1524   | No file              | `23a2fafb947d`  |
| 1519   | No file              | `23a2fafb947d`  |
| 1509   | No file              | `23a2fafb947d`  |
| 1506   | No file              | `23a2fafb947d`  |
| 1504   | No file              | `23a2fafb947d`  |
| 1500   | No file              | `23a2fafb947d`  |
| 1493   | No file              | `23a2fafb947d`  |
| 1489   | No file              | `23a2fafb947d`  |
| 1485   | No file              | `23a2fafb947d`  |
| 1481   | No file              | `23a2fafb947d`  |
| 1474   | No file              | `23a2fafb947d`  |
| 1466   | No file              | `23a2fafb947d`  |
| 1462   | No file              | `23a2fafb947d`  |
| 1459   | No file              | `23a2fafb947d`  |
| 1453   | No file              | `23a2fafb947d`  |
| 1450   | No file              | `23a2fafb947d`  |
| 1445   | No file              | `23a2fafb947d`  |
| 1439   | No file              | `23a2fafb947d`  |
| 1433   | No file              | `23a2fafb947d`  |
| 1430   | No file              | `23a2fafb947d`  |
| 1426   | No file              | `23a2fafb947d`  |
| 1421   | No file              | `23a2fafb947d`  |
| 1417   | No file              | `23a2fafb947d`  |
| 1416   | No file              | `23a2fafb947d`  |
| 1409   | No file              | `23a2fafb947d`  |
| 1405   | No file              | `23a2fafb947d`  |
| 1401   | No file              | `23a2fafb947d`  |
| 1396   | No file              | `23a2fafb947d`  |
| 1391   | No file              | `23a2fafb947d`  |
| 1390   | No file              | `23a2fafb947d`  |
| 1386   | No file              | `23a2fafb947d`  |
| 1381   | No file              | `23a2fafb947d`  |
| 1379   | No file              | `23a2fafb947d`  |
| 1372   | No file              | `23a2fafb947d`  |
| 1366   | No file              | `23a2fafb947d`  |
| 1364   | No file              | `23a2fafb947d`  |
| 1363   | No file              | `23a2fafb947d`  |
| 1360   | No file              | `23a2fafb947d`  |
| 1358   | No file              | `23a2fafb947d`  |
| 1355   | No file              | `23a2fafb947d`  |
| 1351   | No file              | `23a2fafb947d`  |
| 1348   | No file              | `23a2fafb947d`  |
| 1346   | No file              | `23a2fafb947d`  |
| 1341   | No file              | `23a2fafb947d`  |
| 1340   | No file              | `23a2fafb947d`  |
| 1338   | No file              | `23a2fafb947d`  |
| 1335   | No file              | `23a2fafb947d`  |
| 1333   | No file              | `23a2fafb947d`  |
| 1329   | No file              | `23a2fafb947d`  |
| 1327   | No file              | `23a2fafb947d`  |
| 1324   | No file              | `23a2fafb947d`  |
| 1321   | No file              | `23a2fafb947d`  |
| 1319   | No file              | `23a2fafb947d`  |
| 1318   | No file              | `23a2fafb947d`  |
| 1316   | No file              | `23a2fafb947d`  |
| 1313   | No file              | `23a2fafb947d`  |
| 1311   | No file              | `23a2fafb947d`  |
| 1309   | No file              | `23a2fafb947d`  |
| 1304   | No file              | `23a2fafb947d`  |
| 1292   | No file              | `23a2fafb947d`  |
| 1286   | No file              | `23a2fafb947d`  |
| 1280   | No file              | `23a2fafb947d`  |
| 1276   | No file              | `23a2fafb947d`  |
| 1267   | No file              | `23a2fafb947d`  |
| 1261   | No file              | `23a2fafb947d`  |
| 1256   | No file              | `23a2fafb947d`  |
| 1250   | No file              | `23a2fafb947d`  |
| 1246   | No file              | `23a2fafb947d`  |
| 1239   | No file              | `23a2fafb947d`  |
| 1230   | No file              | `23a2fafb947d`  |
| 1226   | No file              | `23a2fafb947d`  |
| 1220   | No file              | `23a2fafb947d`  |
| 1217   | No file              | `23a2fafb947d`  |
| 1211   | No file              | `23a2fafb947d`  |
| 1210   | No file              | `23a2fafb947d`  |
| 1208   | No file              | `23a2fafb947d`  |
| 1203   | No file              | `23a2fafb947d`  |
| 1197   | No file              | `23a2fafb947d`  |
| 1194   | No file              | `23a2fafb947d`  |
| 1192   | No file              | `23a2fafb947d`  |
| 1187   | No file              | `23a2fafb947d`  |
| 1183   | No file              | `23a2fafb947d`  |
| 1177   | No file              | `23a2fafb947d`  |
| 1173   | No file              | `23a2fafb947d`  |
| 1167   | No file              | `23a2fafb947d`  |
| 1164   | No file              | `23a2fafb947d`  |
| 1156   | No file              | `23a2fafb947d`  |
| 1149   | No file              | `23a2fafb947d`  |
| 1144   | No file              | `23a2fafb947d`  |
| 1137   | No file              | `23a2fafb947d`  |
| 1132   | No file              | `23a2fafb947d`  |
| 1127   | No file              | `23a2fafb947d`  |
| 1122   | No file              | `23a2fafb947d`  |
| 1118   | No file              | `23a2fafb947d`  |
| 1114   | No file              | `23a2fafb947d`  |
| 1109   | No file              | `23a2fafb947d`  |
| 1102   | No file              | `23a2fafb947d`  |
| 1096   | No file              | `23a2fafb947d`  |
| 1088   | No file              | `23a2fafb947d`  |
| 1081   | No file              | `23a2fafb947d`  |
| 1076   | No file              | `23a2fafb947d`  |
| 1069   | No file              | `23a2fafb947d`  |
| 1064   | No file              | `23a2fafb947d`  |
| 1058   | No file              | `23a2fafb947d`  |
| 1051   | No file              | `23a2fafb947d`  |
| 1044   | No file              | `23a2fafb947d`  |
| 1036   | No file              | `23a2fafb947d`  |
| 1026   | No file              | `23a2fafb947d`  |
| 1016   | No file              | `23a2fafb947d`  |
| 1009   | No file              | `23a2fafb947d`  |
| 1005   | No file              | `23a2fafb947d`  |
| 1000   | No file              | `23a2fafb947d`  |
| 998    | No file              | `23a2fafb947d`  |
| 990    | No file              | `23a2fafb947d`  |
| 979    | No file              | `23a2fafb947d`  |
| 972    | No file              | `23a2fafb947d`  |
| 963    | No file              | `23a2fafb947d`  |
| 955    | No file              | `23a2fafb947d`  |
| 946    | No file              | `23a2fafb947d`  |
| 938    | No file              | `23a2fafb947d`  |
| 927    | No file              | `23a2fafb947d`  |
| 911    | No file              | `23a2fafb947d`  |
| 904    | No file              | `23a2fafb947d`  |
| 899    | No file              | `23a2fafb947d`  |
| 894    | No file              | `23a2fafb947d`  |
| 885    | No file              | `23a2fafb947d`  |
| 879    | No file              | `23a2fafb947d`  |
| 872    | No file              | `23a2fafb947d`  |
| 864    | No file              | `23a2fafb947d`  |
| 855    | No file              | `23a2fafb947d`  |
| 853    | No file              | `23a2fafb947d`  |
| 845    | No file              | `23a2fafb947d`  |
| 837    | No file              | `23a2fafb947d`  |
| 829    | No file              | `23a2fafb947d`  |
| 822    | No file              | `23a2fafb947d`  |
| 814    | No file              | `23a2fafb947d`  |
| 805    | No file              | `23a2fafb947d`  |
| 794    | No file              | `23a2fafb947d`  |
| 787    | No file              | `23a2fafb947d`  |
| 780    | No file              | `23a2fafb947d`  |
| 771    | No file              | `23a2fafb947d`  |
| 760    | No file              | `23a2fafb947d`  |
| 748    | No file              | `23a2fafb947d`  |
| 741    | No file              | `23a2fafb947d`  |
| 736    | No file              | `23a2fafb947d`  |
| 731    | No file              | `23a2fafb947d`  |
| 723    | No file              | `23a2fafb947d`  |
| 711    | No file              | `23a2fafb947d`  |
| 707    | No file              | `23a2fafb947d`  |
| 697    | No file              | `23a2fafb947d`  |
| 689    | No file              | `23a2fafb947d`  |
| 683    | No file              | `23a2fafb947d`  |
| 678    | No file              | `23a2fafb947d`  |
| 670    | No file              | `23a2fafb947d`  |
| 661    | No file              | `23a2fafb947d`  |
| 656    | No file              | `23a2fafb947d`  |
| 652    | No file              | `23a2fafb947d`  |
| 643    | No file              | `23a2fafb947d`  |
| 637    | No file              | `23a2fafb947d`  |
| 630    | No file              | `23a2fafb947d`  |
| 627    | No file              | `23a2fafb947d`  |
| 621    | No file              | `23a2fafb947d`  |
| 617    | No file              | `23a2fafb947d`  |
| 615    | No file              | `23a2fafb947d`  |
| 606    | No file              | `23a2fafb947d`  |
| 599    | No file              | `23a2fafb947d`  |
| 592    | No file              | `23a2fafb947d`  |
| 586    | No file              | `23a2fafb947d`  |
| 577    | No file              | `23a2fafb947d`  |
| 569    | No file              | `23a2fafb947d`  |
| 561    | No file              | `23a2fafb947d`  |
| 554    | No file              | `23a2fafb947d`  |
| 542    | No file              | `23a2fafb947d`  |
| 532    | No file              | `23a2fafb947d`  |
| 531    | No file              | `23a2fafb947d`  |
| 526    | No file              | `23a2fafb947d`  |
| 521    | No file              | `23a2fafb947d`  |
| 517    | No file              | `23a2fafb947d`  |
| 510    | No file              | `23a2fafb947d`  |
| 508    | No file              | `23a2fafb947d`  |
| 504    | No file              | `23a2fafb947d`  |
| 497    | No file              | `23a2fafb947d`  |
| 491    | No file              | `23a2fafb947d`  |
| 485    | No file              | `23a2fafb947d`  |
| 478    | No file              | `23a2fafb947d`  |
| 472    | No file              | `23a2fafb947d`  |
| 466    | No file              | `23a2fafb947d`  |
| 457    | No file              | `23a2fafb947d`  |
| 452    | No file              | `23a2fafb947d`  |
| 449    | No file              | `23a2fafb947d`  |
| 435    | No file              | `23a2fafb947d`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                |
| --------------------- | -------- | ------------------- |
| `languagedata_en.loc` | Optional | Item names (type 0) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of items                               |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed, in no key order         |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (9 bytes)

| Offset  | Type | Field        | Notes                                                                      |
| ------- | ---- | ------------ | -------------------------------------------------------------------------- |
| `+0x00` | u32  | category_key | The `autousebuffitemcategoryinfo.bss` category; see Categories             |
| `+0x04` | u32  | item_key     | The item (LOC type 0 name); unique per row, top byte `0` on every row      |
| `+0x08` | u8   | unknown_08   | `1` on 892 of 912 rows (client 3482); see Open Questions                   |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                              |
| ------- | ------------------ | ------------ | ---------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on client 3482 |
| `+0x04` | pstr[string_count] | strings      | Empty                              |

## Layout 1

No `unknown_08`: a row is 8 bytes. Only the Row differs from Layout 2.

### Row (8 bytes)

| Offset  | Type | Field        | Notes |
| ------- | ---- | ------------ | ----- |
| `+0x00` | u32  | category_key |       |
| `+0x04` | u32  | item_key     |       |

## Categories

`autousebuffitemcategoryinfo.bss` holds the nine category keys `1` to `9`,
each with a Korean name in its string table and an English name in LOC
type 118. Every `category_key` of this file is one of them, and the items
of each key fit its name. Counts are from client 3482.

| `category_key` | Korean name (`autousebuffitemcategoryinfo.bss`) | Items | Examples                                       |
| -------------- | ----------------------------------------------- | ----- | ---------------------------------------------- |
| 1              | `크론 정식 /음식` (Cron Meal / food)            | 270   | Crispy Stir-Fried Vegetables, Savory Sungnyung |
| 2              | `영약 / 비약` (draughts / elixirs)              | 263   | [Party] Merciless Sky Elixir                   |
| 3              | `향수` (perfumes)                               | 36    | Perfume of Charm                               |
| 4              | `별채 주문서` (annex scrolls)                   | 2     | [Scroll] Turning Gates, [Scroll] Body Enhancement |
| 5              | `모험의 가호 주문서` (adventure boon scroll)    | 1     | [Scroll] Adventure's Boon                      |
| 6              | `영물의 축복` (mystic beast blessings)          | 6     | Blessing of Mystic Beasts - All AP             |
| 7              | `황금 축복` (golden blessings)                  | 8     | [Event] Golden Blessing of Agris               |
| 8              | `주문서` (scrolls)                              | 107   | Max HP Increase Scroll, Mercenary's Skill (60 min) |
| 9              | `기타` (other)                                  | 219   | [Event] Pineapple Skewer                       |

## Open Questions

### What `unknown_08` Holds

`unknown_08` is `1` on 892 rows, `15` on the ten Harmony Draughts (item
keys `1399` to `1408`) and `4` on the ten Draughts `1389` to `1398`
(Fury, Adaptation, Potential, Corruption, Berserk and their Immortal
versions) on client 3482. The window groups each category's items by a
`buffCategory` (`ToClient_getAutoUseBuffItemBuffCategory(categoryKey,
groupIndex)`), which could be this byte or come from the item's buff.
