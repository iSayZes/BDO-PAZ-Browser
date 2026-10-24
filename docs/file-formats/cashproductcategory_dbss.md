# `cashproductcategory.dbss` Format

## Purpose

The Pearl Shop category tree: the main categories (the shop tabs), their
middle categories and the small categories under those, each with its
Korean name, price type, tag and the unique number coupons and products
point at. The Pearl Shop Lua (`panel_pearlshop_category.luac`,
`panel_ingamecashshop.luac`) reads a main category through
`ToClient_GetMainCategoryStaticStatusWrapperByKeyRaw(key)` and the names
through `getCashCategoryName(main, middle)`; the main keys are
`CppEnums.CashProductCategory` (`1` Pearl, `2` Mileage, `3` Normal, `4`
Costumes, `5` Furniture, `6` Servant, `7` Pet, `8` Beauty, `9` HotNew, `15`
StepUp). [`coupon.dbss`](coupon_dbss.md) names its category by these keys.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                             | Bytes | Records       | Row bytes                   |
| ------ | -------------- | ------- | -------------------------------- | ----- | ------------- | --------------------------- |
| 1      | 1286 and later | 3483    | `cashproductcategory.dbss`       | 6,579 | 135 Category  | 34 to 1,976, 118 on average |
| 1      | 1286 and later | 3483    | `cashproductcategoryoffset.dbss` | 170   | 15 Offset Row | 10                          |

| Layout | File                             | Known           | Unknown         |
| ------ | -------------------------------- | --------------- | --------------- |
| 1      | `cashproductcategory.dbss`       | 5,359 B (81.5%) | 1,220 B (18.5%) |
| 1      | `cashproductcategoryoffset.dbss` | 170 B (100.0%)  | 0 B (0.0%)      |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `8edbdde6d7be`  |
| 3482   | Layout 1 | `8edbdde6d7be`  |
| 3474   | Layout 1 | `8edbdde6d7be`  |
| 3473   | Layout 1 | `8edbdde6d7be`  |
| 3464   | Layout 1 | `8edbdde6d7be`  |
| 3458   | Layout 1 | `8edbdde6d7be`  |
| 3454   | Layout 1 | `8edbdde6d7be`  |
| 3444   | Layout 1 | `8edbdde6d7be`  |
| 3435   | Layout 1 | `8edbdde6d7be`  |
| 3426   | Layout 1 | `8edbdde6d7be`  |
| 3418   | Layout 1 | `8edbdde6d7be`  |
| 3412   | Layout 1 | `8edbdde6d7be`  |
| 3402   | Layout 1 | `8edbdde6d7be`  |
| 3396   | Layout 1 | `8edbdde6d7be`  |
| 3387   | Layout 1 | `8edbdde6d7be`  |
| 3381   | Layout 1 | `8edbdde6d7be`  |
| 3373   | Layout 1 | `8edbdde6d7be`  |
| 3364   | Layout 1 | `8edbdde6d7be`  |
| 3356   | Layout 1 | `8edbdde6d7be`  |
| 3349   | Layout 1 | `8edbdde6d7be`  |
| 3342   | Layout 1 | `8edbdde6d7be`  |
| 3335   | Layout 1 | `8edbdde6d7be`  |
| 3326   | Layout 1 | `8edbdde6d7be`  |
| 3321   | Layout 1 | `8edbdde6d7be`  |
| 3314   | Layout 1 | `8edbdde6d7be`  |
| 3303   | Layout 1 | `8edbdde6d7be`  |
| 3302   | Layout 1 | `8edbdde6d7be`  |
| 3293   | Layout 1 | `8edbdde6d7be`  |
| 3283   | Layout 1 | `8edbdde6d7be`  |
| 3275   | Layout 1 | `8edbdde6d7be`  |
| 3267   | Layout 1 | `8edbdde6d7be`  |
| 3258   | Layout 1 | `8edbdde6d7be`  |
| 3251   | Layout 1 | `8edbdde6d7be`  |
| 3242   | Layout 1 | `8edbdde6d7be`  |
| 3235   | Layout 1 | `8edbdde6d7be`  |
| 3229   | Layout 1 | `8edbdde6d7be`  |
| 3212   | Layout 1 | `8edbdde6d7be`  |
| 3203   | Layout 1 | `8edbdde6d7be`  |
| 3193   | Layout 1 | `8edbdde6d7be`  |
| 3186   | Layout 1 | `8edbdde6d7be`  |
| 3177   | Layout 1 | `8edbdde6d7be`  |
| 3169   | Layout 1 | `8edbdde6d7be`  |
| 3158   | Layout 1 | `8edbdde6d7be`  |
| 3151   | Layout 1 | `8edbdde6d7be`  |
| 3144   | Layout 1 | `8edbdde6d7be`  |
| 3133   | Layout 1 | `8edbdde6d7be`  |
| 3125   | Layout 1 | `8edbdde6d7be`  |
| 3118   | Layout 1 | `8edbdde6d7be`  |
| 3111   | Layout 1 | `8edbdde6d7be`  |
| 3103   | Layout 1 | `8edbdde6d7be`  |
| 3095   | Layout 1 | `8edbdde6d7be`  |
| 3086   | Layout 1 | `8edbdde6d7be`  |
| 3072   | Layout 1 | `8edbdde6d7be`  |
| 3062   | Layout 1 | `8edbdde6d7be`  |
| 3052   | Layout 1 | `8edbdde6d7be`  |
| 3045   | Layout 1 | `8edbdde6d7be`  |
| 3037   | Layout 1 | `8edbdde6d7be`  |
| 3030   | Layout 1 | `8edbdde6d7be`  |
| 3021   | Layout 1 | `8edbdde6d7be`  |
| 3012   | Layout 1 | `8edbdde6d7be`  |
| 3002   | Layout 1 | `8edbdde6d7be`  |
| 2995   | Layout 1 | `8edbdde6d7be`  |
| 2987   | Layout 1 | `8edbdde6d7be`  |
| 2978   | Layout 1 | `8edbdde6d7be`  |
| 2970   | Layout 1 | `8edbdde6d7be`  |
| 2959   | Layout 1 | `8edbdde6d7be`  |
| 2951   | Layout 1 | `8edbdde6d7be`  |
| 2942   | Layout 1 | `8edbdde6d7be`  |
| 2935   | Layout 1 | `8edbdde6d7be`  |
| 2932   | Layout 1 | `8edbdde6d7be`  |
| 2923   | Layout 1 | `8edbdde6d7be`  |
| 2919   | Layout 1 | `8edbdde6d7be`  |
| 2907   | Layout 1 | `8edbdde6d7be`  |
| 2900   | Layout 1 | `8edbdde6d7be`  |
| 2891   | Layout 1 | `8edbdde6d7be`  |
| 2882   | Layout 1 | `8edbdde6d7be`  |
| 2872   | Layout 1 | `8edbdde6d7be`  |
| 2863   | Layout 1 | `8edbdde6d7be`  |
| 2855   | Layout 1 | `8edbdde6d7be`  |
| 2849   | Layout 1 | `8edbdde6d7be`  |
| 2844   | Layout 1 | `8edbdde6d7be`  |
| 2834   | Layout 1 | `8edbdde6d7be`  |
| 2825   | Layout 1 | `8edbdde6d7be`  |
| 2819   | Layout 1 | `8edbdde6d7be`  |
| 2811   | Layout 1 | `8edbdde6d7be`  |
| 2803   | Layout 1 | `8edbdde6d7be`  |
| 2794   | Layout 1 | `8edbdde6d7be`  |
| 2783   | Layout 1 | `8edbdde6d7be`  |
| 2774   | Layout 1 | `8edbdde6d7be`  |
| 2765   | Layout 1 | `8edbdde6d7be`  |
| 2756   | Layout 1 | `8edbdde6d7be`  |
| 2750   | Layout 1 | `8edbdde6d7be`  |
| 2743   | Layout 1 | `8edbdde6d7be`  |
| 2736   | Layout 1 | `8edbdde6d7be`  |
| 2726   | Layout 1 | `8edbdde6d7be`  |
| 2717   | Layout 1 | `8edbdde6d7be`  |
| 2709   | Layout 1 | `8edbdde6d7be`  |
| 2703   | Layout 1 | `8edbdde6d7be`  |
| 2695   | Layout 1 | `8edbdde6d7be`  |
| 2684   | Layout 1 | `8edbdde6d7be`  |
| 2672   | Layout 1 | `8edbdde6d7be`  |
| 2665   | Layout 1 | `8edbdde6d7be`  |
| 2657   | Layout 1 | `8edbdde6d7be`  |
| 2649   | Layout 1 | `8edbdde6d7be`  |
| 2644   | Layout 1 | `8edbdde6d7be`  |
| 2637   | Layout 1 | `8edbdde6d7be`  |
| 2629   | Layout 1 | `8edbdde6d7be`  |
| 2619   | Layout 1 | `8edbdde6d7be`  |
| 2612   | Layout 1 | `8edbdde6d7be`  |
| 2606   | Layout 1 | `8edbdde6d7be`  |
| 2602   | Layout 1 | `8edbdde6d7be`  |
| 2601   | Layout 1 | `8edbdde6d7be`  |
| 2592   | Layout 1 | `8edbdde6d7be`  |
| 2583   | Layout 1 | `8edbdde6d7be`  |
| 2575   | Layout 1 | `8edbdde6d7be`  |
| 2567   | Layout 1 | `8edbdde6d7be`  |
| 2560   | Layout 1 | `8edbdde6d7be`  |
| 2553   | Layout 1 | `8edbdde6d7be`  |
| 2545   | Layout 1 | `8edbdde6d7be`  |
| 2538   | Layout 1 | `8edbdde6d7be`  |
| 2529   | Layout 1 | `8edbdde6d7be`  |
| 2519   | Layout 1 | `8edbdde6d7be`  |
| 2513   | Layout 1 | `8edbdde6d7be`  |
| 2510   | Layout 1 | `8edbdde6d7be`  |
| 2507   | Layout 1 | `8edbdde6d7be`  |
| 2503   | Layout 1 | `8edbdde6d7be`  |
| 2498   | Layout 1 | `8edbdde6d7be`  |
| 2492   | Layout 1 | `8edbdde6d7be`  |
| 2487   | Layout 1 | `8edbdde6d7be`  |
| 2480   | Layout 1 | `8edbdde6d7be`  |
| 2474   | Layout 1 | `8edbdde6d7be`  |
| 2468   | Layout 1 | `8edbdde6d7be`  |
| 2460   | Layout 1 | `8edbdde6d7be`  |
| 2453   | Layout 1 | `8edbdde6d7be`  |
| 2444   | Layout 1 | `8edbdde6d7be`  |
| 2438   | Layout 1 | `8edbdde6d7be`  |
| 2434   | Layout 1 | `8edbdde6d7be`  |
| 2429   | Layout 1 | `8edbdde6d7be`  |
| 2421   | Layout 1 | `8edbdde6d7be`  |
| 2414   | Layout 1 | `8edbdde6d7be`  |
| 2407   | Layout 1 | `8edbdde6d7be`  |
| 2401   | Layout 1 | `8edbdde6d7be`  |
| 2397   | Layout 1 | `8edbdde6d7be`  |
| 2393   | Layout 1 | `8edbdde6d7be`  |
| 2384   | Layout 1 | `8edbdde6d7be`  |
| 2378   | Layout 1 | `8edbdde6d7be`  |
| 2372   | Layout 1 | `8edbdde6d7be`  |
| 2358   | Layout 1 | `8edbdde6d7be`  |
| 2352   | Layout 1 | `8edbdde6d7be`  |
| 2347   | Layout 1 | `8edbdde6d7be`  |
| 2343   | Layout 1 | `8edbdde6d7be`  |
| 2335   | Layout 1 | `8edbdde6d7be`  |
| 2327   | Layout 1 | `8edbdde6d7be`  |
| 2324   | Layout 1 | `8edbdde6d7be`  |
| 2319   | Layout 1 | `8edbdde6d7be`  |
| 2313   | Layout 1 | `8edbdde6d7be`  |
| 2308   | Layout 1 | `8edbdde6d7be`  |
| 2302   | Layout 1 | `8edbdde6d7be`  |
| 2295   | Layout 1 | `8edbdde6d7be`  |
| 2290   | Layout 1 | `8edbdde6d7be`  |
| 2284   | Layout 1 | `8edbdde6d7be`  |
| 2276   | Layout 1 | `8edbdde6d7be`  |
| 2269   | Layout 1 | `8edbdde6d7be`  |
| 2259   | Layout 1 | `8edbdde6d7be`  |
| 2250   | Layout 1 | `8edbdde6d7be`  |
| 2243   | Layout 1 | `8edbdde6d7be`  |
| 2235   | Layout 1 | `8edbdde6d7be`  |
| 2229   | Layout 1 | `8edbdde6d7be`  |
| 2224   | Layout 1 | `8edbdde6d7be`  |
| 2218   | Layout 1 | `8edbdde6d7be`  |
| 2215   | Layout 1 | `8edbdde6d7be`  |
| 2207   | Layout 1 | `8edbdde6d7be`  |
| 2203   | Layout 1 | `8edbdde6d7be`  |
| 2196   | Layout 1 | `8edbdde6d7be`  |
| 2192   | Layout 1 | `8edbdde6d7be`  |
| 2189   | Layout 1 | `8edbdde6d7be`  |
| 2183   | Layout 1 | `8edbdde6d7be`  |
| 2179   | Layout 1 | `8edbdde6d7be`  |
| 2171   | Layout 1 | `8edbdde6d7be`  |
| 2163   | Layout 1 | `8edbdde6d7be`  |
| 2156   | Layout 1 | `8edbdde6d7be`  |
| 2151   | Layout 1 | `8edbdde6d7be`  |
| 2147   | Layout 1 | `8edbdde6d7be`  |
| 2142   | Layout 1 | `8edbdde6d7be`  |
| 2138   | Layout 1 | `8edbdde6d7be`  |
| 2134   | Layout 1 | `8edbdde6d7be`  |
| 2130   | Layout 1 | `8edbdde6d7be`  |
| 2122   | Layout 1 | `8edbdde6d7be`  |
| 2107   | Layout 1 | `8edbdde6d7be`  |
| 2098   | Layout 1 | `8edbdde6d7be`  |
| 2089   | Layout 1 | `8edbdde6d7be`  |
| 2081   | Layout 1 | `8edbdde6d7be`  |
| 2073   | Layout 1 | `8edbdde6d7be`  |
| 2067   | Layout 1 | `8edbdde6d7be`  |
| 2063   | Layout 1 | `8edbdde6d7be`  |
| 2059   | Layout 1 | `8edbdde6d7be`  |
| 2052   | Layout 1 | `8edbdde6d7be`  |
| 2044   | Layout 1 | `8edbdde6d7be`  |
| 2039   | Layout 1 | `8edbdde6d7be`  |
| 2032   | Layout 1 | `8edbdde6d7be`  |
| 2025   | Layout 1 | `8edbdde6d7be`  |
| 2011   | Layout 1 | `8edbdde6d7be`  |
| 2005   | Layout 1 | `8edbdde6d7be`  |
| 2000   | Layout 1 | `8edbdde6d7be`  |
| 1996   | Layout 1 | `8edbdde6d7be`  |
| 1991   | Layout 1 | `8edbdde6d7be`  |
| 1985   | Layout 1 | `8edbdde6d7be`  |
| 1980   | Layout 1 | `8edbdde6d7be`  |
| 1969   | Layout 1 | `8edbdde6d7be`  |
| 1964   | Layout 1 | `8edbdde6d7be`  |
| 1958   | Layout 1 | `8edbdde6d7be`  |
| 1950   | Layout 1 | `8edbdde6d7be`  |
| 1945   | Layout 1 | `8edbdde6d7be`  |
| 1937   | Layout 1 | `8edbdde6d7be`  |
| 1933   | Layout 1 | `8edbdde6d7be`  |
| 1927   | Layout 1 | `8edbdde6d7be`  |
| 1921   | Layout 1 | `8edbdde6d7be`  |
| 1914   | Layout 1 | `8edbdde6d7be`  |
| 1908   | Layout 1 | `8edbdde6d7be`  |
| 1897   | Layout 1 | `8edbdde6d7be`  |
| 1892   | Layout 1 | `8edbdde6d7be`  |
| 1886   | Layout 1 | `8edbdde6d7be`  |
| 1881   | Layout 1 | `8edbdde6d7be`  |
| 1871   | Layout 1 | `8edbdde6d7be`  |
| 1866   | Layout 1 | `8edbdde6d7be`  |
| 1862   | Layout 1 | `8edbdde6d7be`  |
| 1854   | Layout 1 | `8edbdde6d7be`  |
| 1846   | Layout 1 | `8edbdde6d7be`  |
| 1838   | Layout 1 | `8edbdde6d7be`  |
| 1832   | Layout 1 | `8edbdde6d7be`  |
| 1826   | Layout 1 | `8edbdde6d7be`  |
| 1822   | Layout 1 | `8edbdde6d7be`  |
| 1818   | Layout 1 | `8edbdde6d7be`  |
| 1804   | Layout 1 | `8edbdde6d7be`  |
| 1794   | Layout 1 | `8edbdde6d7be`  |
| 1790   | Layout 1 | `8edbdde6d7be`  |
| 1784   | Layout 1 | `8edbdde6d7be`  |
| 1774   | Layout 1 | `8edbdde6d7be`  |
| 1771   | Layout 1 | `8edbdde6d7be`  |
| 1762   | Layout 1 | `8edbdde6d7be`  |
| 1759   | Layout 1 | `8edbdde6d7be`  |
| 1754   | Layout 1 | `8edbdde6d7be`  |
| 1749   | Layout 1 | `8edbdde6d7be`  |
| 1743   | Layout 1 | `8edbdde6d7be`  |
| 1737   | Layout 1 | `8edbdde6d7be`  |
| 1731   | Layout 1 | `8edbdde6d7be`  |
| 1725   | Layout 1 | `8edbdde6d7be`  |
| 1717   | Layout 1 | `8edbdde6d7be`  |
| 1710   | Layout 1 | `8edbdde6d7be`  |
| 1704   | Layout 1 | `8edbdde6d7be`  |
| 1698   | Layout 1 | `8edbdde6d7be`  |
| 1690   | Layout 1 | `8edbdde6d7be`  |
| 1685   | Layout 1 | `8edbdde6d7be`  |
| 1680   | Layout 1 | `8edbdde6d7be`  |
| 1674   | Layout 1 | `8edbdde6d7be`  |
| 1668   | Layout 1 | `8edbdde6d7be`  |
| 1659   | Layout 1 | `8edbdde6d7be`  |
| 1649   | Layout 1 | `8edbdde6d7be`  |
| 1642   | Layout 1 | `8edbdde6d7be`  |
| 1636   | Layout 1 | `8edbdde6d7be`  |
| 1628   | Layout 1 | `8edbdde6d7be`  |
| 1622   | Layout 1 | `8edbdde6d7be`  |
| 1614   | Layout 1 | `8edbdde6d7be`  |
| 1608   | Layout 1 | `8edbdde6d7be`  |
| 1602   | Layout 1 | `8edbdde6d7be`  |
| 1598   | Layout 1 | `8edbdde6d7be`  |
| 1594   | Layout 1 | `8edbdde6d7be`  |
| 1590   | Layout 1 | `8edbdde6d7be`  |
| 1587   | Layout 1 | `8edbdde6d7be`  |
| 1584   | Layout 1 | `8edbdde6d7be`  |
| 1579   | Layout 1 | `8edbdde6d7be`  |
| 1572   | Layout 1 | `8edbdde6d7be`  |
| 1565   | Layout 1 | `8edbdde6d7be`  |
| 1559   | Layout 1 | `8edbdde6d7be`  |
| 1554   | Layout 1 | `8edbdde6d7be`  |
| 1547   | Layout 1 | `8edbdde6d7be`  |
| 1537   | Layout 1 | `8edbdde6d7be`  |
| 1529   | Layout 1 | `8edbdde6d7be`  |
| 1524   | Layout 1 | `8edbdde6d7be`  |
| 1519   | Layout 1 | `8edbdde6d7be`  |
| 1509   | Layout 1 | `8edbdde6d7be`  |
| 1506   | Layout 1 | `8edbdde6d7be`  |
| 1504   | Layout 1 | `8edbdde6d7be`  |
| 1500   | Layout 1 | `8edbdde6d7be`  |
| 1493   | Layout 1 | `8edbdde6d7be`  |
| 1489   | Layout 1 | `8edbdde6d7be`  |
| 1485   | Layout 1 | `8edbdde6d7be`  |
| 1481   | Layout 1 | `8edbdde6d7be`  |
| 1474   | Layout 1 | `8edbdde6d7be`  |
| 1466   | Layout 1 | `8edbdde6d7be`  |
| 1462   | Layout 1 | `8edbdde6d7be`  |
| 1459   | Layout 1 | `8edbdde6d7be`  |
| 1453   | Layout 1 | `8edbdde6d7be`  |
| 1450   | Layout 1 | `8edbdde6d7be`  |
| 1445   | Layout 1 | `8edbdde6d7be`  |
| 1439   | Layout 1 | `8edbdde6d7be`  |
| 1433   | Layout 1 | `8edbdde6d7be`  |
| 1430   | Layout 1 | `8edbdde6d7be`  |
| 1426   | Layout 1 | `8edbdde6d7be`  |
| 1421   | Layout 1 | `8edbdde6d7be`  |
| 1417   | Layout 1 | `8edbdde6d7be`  |
| 1416   | Layout 1 | `8edbdde6d7be`  |
| 1409   | Layout 1 | `8edbdde6d7be`  |
| 1405   | Layout 1 | `8edbdde6d7be`  |
| 1401   | Layout 1 | `8edbdde6d7be`  |
| 1396   | Layout 1 | `8edbdde6d7be`  |
| 1391   | Layout 1 | `8edbdde6d7be`  |
| 1390   | Layout 1 | `8edbdde6d7be`  |
| 1386   | Layout 1 | `8edbdde6d7be`  |
| 1381   | Layout 1 | `8edbdde6d7be`  |
| 1379   | Layout 1 | `8edbdde6d7be`  |
| 1372   | Layout 1 | `8edbdde6d7be`  |
| 1366   | Layout 1 | `8edbdde6d7be`  |
| 1364   | Layout 1 | `8edbdde6d7be`  |
| 1363   | Layout 1 | `8edbdde6d7be`  |
| 1360   | Layout 1 | `8edbdde6d7be`  |
| 1358   | Layout 1 | `8edbdde6d7be`  |
| 1355   | Layout 1 | `8edbdde6d7be`  |
| 1351   | Layout 1 | `8edbdde6d7be`  |
| 1348   | Layout 1 | `8edbdde6d7be`  |
| 1346   | Layout 1 | `8edbdde6d7be`  |
| 1341   | Layout 1 | `8edbdde6d7be`  |
| 1340   | Layout 1 | `8edbdde6d7be`  |
| 1338   | Layout 1 | `8edbdde6d7be`  |
| 1335   | Layout 1 | `8edbdde6d7be`  |
| 1333   | Layout 1 | `8edbdde6d7be`  |
| 1329   | Layout 1 | `8edbdde6d7be`  |
| 1327   | Layout 1 | `8edbdde6d7be`  |
| 1324   | Layout 1 | `8edbdde6d7be`  |
| 1321   | Layout 1 | `8edbdde6d7be`  |
| 1319   | Layout 1 | `8edbdde6d7be`  |
| 1318   | Layout 1 | `8edbdde6d7be`  |
| 1316   | Layout 1 | `8edbdde6d7be`  |
| 1313   | Layout 1 | `8edbdde6d7be`  |
| 1311   | Layout 1 | `8edbdde6d7be`  |
| 1309   | Layout 1 | `8edbdde6d7be`  |
| 1304   | Layout 1 | `8edbdde6d7be`  |
| 1292   | Layout 1 | `8edbdde6d7be`  |
| 1286   | Layout 1 | `8edbdde6d7be`  |
| 1280   | No file  | `8edbdde6d7be`  |
| 1276   | No file  | `8edbdde6d7be`  |
| 1267   | No file  | `8edbdde6d7be`  |
| 1261   | No file  | `8edbdde6d7be`  |
| 1256   | No file  | `8edbdde6d7be`  |
| 1250   | No file  | `8edbdde6d7be`  |
| 1246   | No file  | `8edbdde6d7be`  |
| 1239   | No file  | `8edbdde6d7be`  |
| 1230   | No file  | `8edbdde6d7be`  |
| 1226   | No file  | `8edbdde6d7be`  |
| 1220   | No file  | `8edbdde6d7be`  |
| 1217   | No file  | `8edbdde6d7be`  |
| 1211   | No file  | `8edbdde6d7be`  |
| 1210   | No file  | `8edbdde6d7be`  |
| 1208   | No file  | `8edbdde6d7be`  |
| 1203   | No file  | `8edbdde6d7be`  |
| 1197   | No file  | `8edbdde6d7be`  |
| 1194   | No file  | `8edbdde6d7be`  |
| 1192   | No file  | `8edbdde6d7be`  |
| 1187   | No file  | `8edbdde6d7be`  |
| 1183   | No file  | `8edbdde6d7be`  |
| 1177   | No file  | `8edbdde6d7be`  |
| 1173   | No file  | `8edbdde6d7be`  |
| 1167   | No file  | `8edbdde6d7be`  |
| 1164   | No file  | `8edbdde6d7be`  |
| 1156   | No file  | `8edbdde6d7be`  |
| 1149   | No file  | `8edbdde6d7be`  |
| 1144   | No file  | `8edbdde6d7be`  |
| 1137   | No file  | `8edbdde6d7be`  |
| 1132   | No file  | `8edbdde6d7be`  |
| 1127   | No file  | `8edbdde6d7be`  |
| 1122   | No file  | `8edbdde6d7be`  |
| 1118   | No file  | `8edbdde6d7be`  |
| 1114   | No file  | `8edbdde6d7be`  |
| 1109   | No file  | `8edbdde6d7be`  |
| 1102   | No file  | `8edbdde6d7be`  |
| 1096   | No file  | `8edbdde6d7be`  |
| 1088   | No file  | `8edbdde6d7be`  |
| 1081   | No file  | `8edbdde6d7be`  |
| 1076   | No file  | `8edbdde6d7be`  |
| 1069   | No file  | `8edbdde6d7be`  |
| 1064   | No file  | `8edbdde6d7be`  |
| 1058   | No file  | `8edbdde6d7be`  |
| 1051   | No file  | `8edbdde6d7be`  |
| 1044   | No file  | `8edbdde6d7be`  |
| 1036   | No file  | `8edbdde6d7be`  |
| 1026   | No file  | `8edbdde6d7be`  |
| 1016   | No file  | `8edbdde6d7be`  |
| 1009   | No file  | `8edbdde6d7be`  |
| 1005   | No file  | `8edbdde6d7be`  |
| 1000   | No file  | `8edbdde6d7be`  |
| 998    | No file  | `8edbdde6d7be`  |
| 990    | No file  | `8edbdde6d7be`  |
| 979    | No file  | `8edbdde6d7be`  |
| 972    | No file  | `8edbdde6d7be`  |
| 963    | No file  | `8edbdde6d7be`  |
| 955    | No file  | `8edbdde6d7be`  |
| 946    | No file  | `8edbdde6d7be`  |
| 938    | No file  | `8edbdde6d7be`  |
| 927    | No file  | `8edbdde6d7be`  |
| 911    | No file  | `8edbdde6d7be`  |
| 904    | No file  | `8edbdde6d7be`  |
| 899    | No file  | `8edbdde6d7be`  |
| 894    | No file  | `8edbdde6d7be`  |
| 885    | No file  | `8edbdde6d7be`  |
| 879    | No file  | `8edbdde6d7be`  |
| 872    | No file  | `8edbdde6d7be`  |
| 864    | No file  | `8edbdde6d7be`  |
| 855    | No file  | `8edbdde6d7be`  |
| 853    | No file  | `8edbdde6d7be`  |
| 845    | No file  | `8edbdde6d7be`  |
| 837    | No file  | `8edbdde6d7be`  |
| 829    | No file  | `8edbdde6d7be`  |
| 822    | No file  | `8edbdde6d7be`  |
| 814    | No file  | `8edbdde6d7be`  |
| 805    | No file  | `8edbdde6d7be`  |
| 794    | No file  | `8edbdde6d7be`  |
| 787    | No file  | `8edbdde6d7be`  |
| 780    | No file  | `8edbdde6d7be`  |
| 771    | No file  | `8edbdde6d7be`  |
| 760    | No file  | `8edbdde6d7be`  |
| 748    | No file  | `8edbdde6d7be`  |
| 741    | No file  | `8edbdde6d7be`  |
| 736    | No file  | `8edbdde6d7be`  |
| 731    | No file  | `8edbdde6d7be`  |
| 723    | No file  | `8edbdde6d7be`  |
| 711    | No file  | `8edbdde6d7be`  |
| 707    | No file  | `8edbdde6d7be`  |
| 697    | No file  | `8edbdde6d7be`  |
| 689    | No file  | `8edbdde6d7be`  |
| 683    | No file  | `8edbdde6d7be`  |
| 678    | No file  | `8edbdde6d7be`  |
| 670    | No file  | `8edbdde6d7be`  |
| 661    | No file  | `8edbdde6d7be`  |
| 656    | No file  | `8edbdde6d7be`  |
| 652    | No file  | `8edbdde6d7be`  |
| 643    | No file  | `8edbdde6d7be`  |
| 637    | No file  | `8edbdde6d7be`  |
| 630    | No file  | `8edbdde6d7be`  |
| 627    | No file  | `8edbdde6d7be`  |
| 621    | No file  | `8edbdde6d7be`  |
| 617    | No file  | `8edbdde6d7be`  |
| 615    | No file  | `8edbdde6d7be`  |
| 606    | No file  | `8edbdde6d7be`  |
| 599    | No file  | `8edbdde6d7be`  |
| 592    | No file  | `8edbdde6d7be`  |
| 586    | No file  | `8edbdde6d7be`  |
| 577    | No file  | `8edbdde6d7be`  |
| 569    | No file  | `8edbdde6d7be`  |
| 561    | No file  | `8edbdde6d7be`  |
| 554    | No file  | `8edbdde6d7be`  |
| 542    | No file  | `8edbdde6d7be`  |
| 532    | No file  | `8edbdde6d7be`  |
| 531    | No file  | `8edbdde6d7be`  |
| 526    | No file  | `8edbdde6d7be`  |
| 521    | No file  | `8edbdde6d7be`  |
| 517    | No file  | `8edbdde6d7be`  |
| 510    | No file  | `8edbdde6d7be`  |
| 508    | No file  | `8edbdde6d7be`  |
| 504    | No file  | `8edbdde6d7be`  |
| 497    | No file  | `8edbdde6d7be`  |
| 491    | No file  | `8edbdde6d7be`  |
| 485    | No file  | `8edbdde6d7be`  |
| 478    | No file  | `8edbdde6d7be`  |
| 472    | No file  | `8edbdde6d7be`  |
| 466    | No file  | `8edbdde6d7be`  |
| 457    | No file  | `8edbdde6d7be`  |
| 452    | No file  | `8edbdde6d7be`  |
| 449    | No file  | `8edbdde6d7be`  |
| 435    | No file  | `8edbdde6d7be`  |

<!-- versions:end -->

## Companion Files

| File                             | Required | Role                                                                                      |
| -------------------------------- | -------- | ----------------------------------------------------------------------------------------- |
| `cashproductcategoryoffset.dbss` | Optional | `main_key -> (data_offset, data_size)` of every main category; the parser walks the main file without it |
| `languagedata_en.loc`            | Optional | Category names, LOC type 51                                                               |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic. The name of the all-categories entry, then the main
categories, each followed by its children.

| Offset             | Type            | Field                  | Notes                                                                  |
| ------------------ | --------------- | ---------------------- | ---------------------------------------------------------------------- |
| `+0x00`            | str16           | all_name_kr            | `전체(펄 상자, 마일리지 제외)` (all, Pearl Box and Mileage excluded); see Notes |
| `all_name_kr+0x00` | u32             | unknown_all_name_kr_00 | `0` on clients 1784 and 3482                                           |
| `all_name_kr+0x04` | u8              | unknown_all_name_kr_04 | `1` on clients 1784 and 3482                                           |
| `all_name_kr+0x05` | u32             | count                  | Number of main categories, `15` on client 3482                         |
| `all_name_kr+0x09` | Category[count] | categories             | See Category                                                           |

### Category (variable: 32 bytes + name and children)

One category; its children follow inside it. A main category's children
are middle categories, theirs small categories; no small category of
clients 1784 and 3482 has children.

| Offset          | Type                  | Field                 | Notes                                                                                        |
| --------------- | --------------------- | --------------------- | -------------------------------------------------------------------------------------------- |
| `+0x00`         | u16                   | category_key          | Main key (`CppEnums.CashProductCategory`), else the key under the parent, from `1`          |
| `+0x02`         | str16                 | name_kr               | Korean name; main names start with a space, `\n` (two characters) breaks a line              |
| `name_kr+0x00`  | u8                    | is_useable            | `0` on main categories `1` and `13` of client 3482, `1` on the other 133 categories          |
| `name_kr+0x01`  | u8                    | price_type            | See Price Types                                                                              |
| `name_kr+0x02`  | u8                    | special_category_type | `2` on main 5 (Furniture) and its seven children and on Step Up 1 to 10, `3` on the appearance change coupons (8, 2), `1` on Hot&New Special (9, 7), else `0` (client 3482) |
| `name_kr+0x03`  | u8                    | tag_type              | Hot&New tag: `1` New, `2` Hot, `3` Event, `4` Sale, `5` Best, `7` Special, `8` to `17` Step Up 1 to 10; `0` elsewhere |
| `name_kr+0x04`  | u8                    | tag_order             | Order of the tag, `1` to `7`; `0` where `tag_type` is `0`                                    |
| `name_kr+0x05`  | bytes[3]              | unknown_name_kr_05    | `0` on every category of clients 1784 and 3482                                               |
| `name_kr+0x08`  | u32                   | unique_no             | Unique number of the category, `1` to `999` on client 3482                                   |
| `name_kr+0x0C`  | u32                   | child_count           | Number of `children`                                                                         |
| `name_kr+0x10`  | Category[child_count] | children              | The categories one level down                                                                |
| `children+0x00` | u16                   | unknown_children_00   | `65535` on every category of clients 1784 and 3482                                           |
| `children+0x02` | u32                   | unknown_children_02   | `0` on every category                                                                        |

On client 3482 the file holds 15 main, 54 middle and 66 small categories.

### `cashproductcategoryoffset.dbss`

The `PABR` index layout of `characterstaticoffset.dbss`, read by
`parse_pabr_offset_rows()` in `_common/pabr_offset.py`.

| Offset      | Type              | Field        | Notes                                          |
| ----------- | ----------------- | ------------ | ---------------------------------------------- |
| `+0x00`     | char[4]           | magic        | `PABR`                                         |
| `+0x04`     | u32               | count        | Equals the main category count                 |
| `+0x08`     | Offset Row[count] | rows         | See Offset Row                                 |
| `rows+0x00` | u32               | string_count | `0`: the empty PABR string table               |
| `rows+0x04` | u32               | table_start  | End of the rows (`8 + 10 * count`)             |
| `rows+0x08` | u32               | zero         | Always `0`                                     |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                       |
| ------- | ---- | ----------- | ----------------------------------------------------------- |
| `+0x00` | u16  | main_key    | `category_key` of the main category it points at            |
| `+0x02` | u32  | data_offset | Absolute offset of that main category, at its `category_key` |
| `+0x06` | u32  | data_size   | The main category with all its children                     |

On clients 1784 and 3482 the index rows follow the file order and every
one points at the main category with its key.

## Price Types

`price_type` against the `PriceType` text of the client 1784 sheet (see
Field Names), 88 of 88 categories. The Lua knows the same four as
`__ePriceType_Cash`, `__ePriceType_Pearl`, `__ePriceType_Mileage` and
`__ePriceType_Sliver`.

| Value | Sheet `PriceType` | Categories (client 3482)                      |
| ----- | ----------------- | --------------------------------------------- |
| 0     | `Silver`          | Silver Event Items (main 2, middle 2)          |
| 1     | `Cash`            | Pearl Box (main 1)                             |
| 2     | `Pearl`           | The other 132                                  |
| 3     | `Mileage`         | Loyalties (main 2, middle 1)                   |

## LOC Names

LOC type 51 holds each category's name under `(main, middle, small)`: a
main category writes middle `65535` and small `255`, a middle category
small `255`. All 135 categories of client 3482 have an English name. The
key `(99, 65535, 255)` names the all-categories entry of the file head
(`All (Except for Pearl, Loyalty)`). Older rows with middle or small `0`
(`(1, 0, 0)` `Pearl Box`) are not used by the file.

## Field Names

The `CouponCategory_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `CashCouponCategory_Main`, `_Middle` and
`_Small` (the path), `IsUseable`, `MoneyType`, `PriceType`, `TagType`,
`TagOrder`, `specialCategoryType`, `CashCouponCategory_Name`, `UniqueNo` and
`IsHighLightCategory`, 89 rows. 88 of them are the categories of the client
1784 file; row `99` (`UniqueNo` 70) has the text of `all_name_kr`.

| Field                 | Column                    | Same value (client 1784) | Same value (client 3482) |
| --------------------- | ------------------------- | ------------------------ | ------------------------ |
| category_key          | the path columns          | 88 of 88                 | 83 of 88                 |
| name_kr               | `CashCouponCategory_Name` | 88 of 88                 | 71 of 83                 |
| is_useable            | `IsUseable`               | 88 of 88                 | 82 of 83                 |
| price_type            | `PriceType`               | 88 of 88                 | 82 of 83                 |
| special_category_type | `specialCategoryType`     | 88 of 88                 | 82 of 83                 |
| tag_type              | `TagType`                 | 88 of 88                 | 83 of 83                 |
| tag_order             | `TagOrder`                | 88 of 88                 | 79 of 83                 |
| unique_no             | `UniqueNo`                | 88 of 88                 | 83 of 83                 |

Client 3482 renames 12 of the 83 shared categories, turns main 2 into
`마일리지/\n 은화 상품` with two middle categories (Mileage and the Silver
event items, which the sheet keeps under main 10) and moves the Hot&New
tag orders up by one for Step Up. `MoneyType` (`0` Cash, `1` Pearl, `2`
Mileage, `3` Silver) names the same four in another order, so
`price_type` matches it as well; no other byte holds it.

## Notes

- The name of the all-categories entry is the coupon category text of a
  coupon valid in every category: [`coupon.dbss`](coupon_dbss.md) stores it
  as `category_expression_kr` of 52 of its 117 coupons on client 3482.

## Open Questions

### What the Zero and 65535 Fields Hold

`unknown_name_kr_05` is `0` on every category of clients 1784 and 3482,
`unknown_children_00` `65535` and `unknown_children_02` `0`. The sheet's
`IsHighLightCategory` is `0` on all 89 rows, so it may be one of the zero
bytes; no value differs to confirm it.

### What the Head Fields Hold

`unknown_all_name_kr_00` (`0`) and `unknown_all_name_kr_04` (`1`) follow
the all-categories name on clients 1784 and 3482. They may be the
`is_useable` and other flags of that entry in another order, which a
client with other values would show.
