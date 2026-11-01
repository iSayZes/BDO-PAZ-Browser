# `coupon.dbss` Format

## Purpose

The Pearl Shop discount coupons: per coupon its Korean name, how many days
it stays valid, the discount (a rate, or a Pearl amount off a minimum
price), the cap of a rate discount, the icon and the Pearl Shop category it
applies to. The coupon window Lua (`panel_ingamecashshop_coupon.luac`)
reads a held coupon through `ToClient_GetCouponInfoWrapper(index)` and the
getters `getCouponKey()`, `getCouponName()`, `getCouponDisCountRate()`,
`getCouponDisCountPearl()`, `getCouponMaxDisCountPearl()`,
`getCouponMinProductPearl()` and `getCouponCategoryExpression()`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                | Bytes  | Records        | Row bytes                  |
| ------ | -------------- | ------------------- | ------ | -------------- | -------------------------- |
| 1      | 1256 and later | `coupon.dbss`       | 21,557 | 117 Row        | 155 to 239, 184 on average |
| 1      | 1256 and later | `couponoffset.dbss` | 1,174  | 117 Offset Row | 10                         |

| Layout | File                | Known            | Unknown      |
| ------ | ------------------- | ---------------- | ------------ |
| 1      | `coupon.dbss`       | 20,972 B (97.3%) | 585 B (2.7%) |
| 1      | `couponoffset.dbss` | 1,174 B (100.0%) | 0 B (0.0%)   |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `63fb2daa5b58`  |
| 3482   | Layout 1 | `63fb2daa5b58`  |
| 3474   | Layout 1 | `63fb2daa5b58`  |
| 3473   | Layout 1 | `63fb2daa5b58`  |
| 3464   | Layout 1 | `63fb2daa5b58`  |
| 3458   | Layout 1 | `63fb2daa5b58`  |
| 3454   | Layout 1 | `63fb2daa5b58`  |
| 3444   | Layout 1 | `63fb2daa5b58`  |
| 3435   | Layout 1 | `63fb2daa5b58`  |
| 3426   | Layout 1 | `63fb2daa5b58`  |
| 3418   | Layout 1 | `63fb2daa5b58`  |
| 3412   | Layout 1 | `63fb2daa5b58`  |
| 3402   | Layout 1 | `63fb2daa5b58`  |
| 3396   | Layout 1 | `63fb2daa5b58`  |
| 3387   | Layout 1 | `63fb2daa5b58`  |
| 3381   | Layout 1 | `63fb2daa5b58`  |
| 3373   | Layout 1 | `63fb2daa5b58`  |
| 3364   | Layout 1 | `63fb2daa5b58`  |
| 3356   | Layout 1 | `63fb2daa5b58`  |
| 3349   | Layout 1 | `63fb2daa5b58`  |
| 3342   | Layout 1 | `63fb2daa5b58`  |
| 3335   | Layout 1 | `63fb2daa5b58`  |
| 3326   | Layout 1 | `63fb2daa5b58`  |
| 3321   | Layout 1 | `63fb2daa5b58`  |
| 3314   | Layout 1 | `63fb2daa5b58`  |
| 3303   | Layout 1 | `63fb2daa5b58`  |
| 3302   | Layout 1 | `63fb2daa5b58`  |
| 3293   | Layout 1 | `63fb2daa5b58`  |
| 3283   | Layout 1 | `63fb2daa5b58`  |
| 3275   | Layout 1 | `63fb2daa5b58`  |
| 3267   | Layout 1 | `63fb2daa5b58`  |
| 3258   | Layout 1 | `63fb2daa5b58`  |
| 3251   | Layout 1 | `63fb2daa5b58`  |
| 3242   | Layout 1 | `63fb2daa5b58`  |
| 3235   | Layout 1 | `63fb2daa5b58`  |
| 3229   | Layout 1 | `63fb2daa5b58`  |
| 3212   | Layout 1 | `63fb2daa5b58`  |
| 3203   | Layout 1 | `63fb2daa5b58`  |
| 3193   | Layout 1 | `63fb2daa5b58`  |
| 3186   | Layout 1 | `63fb2daa5b58`  |
| 3177   | Layout 1 | `63fb2daa5b58`  |
| 3169   | Layout 1 | `63fb2daa5b58`  |
| 3158   | Layout 1 | `63fb2daa5b58`  |
| 3151   | Layout 1 | `63fb2daa5b58`  |
| 3144   | Layout 1 | `63fb2daa5b58`  |
| 3133   | Layout 1 | `63fb2daa5b58`  |
| 3125   | Layout 1 | `63fb2daa5b58`  |
| 3118   | Layout 1 | `63fb2daa5b58`  |
| 3111   | Layout 1 | `63fb2daa5b58`  |
| 3103   | Layout 1 | `63fb2daa5b58`  |
| 3095   | Layout 1 | `63fb2daa5b58`  |
| 3086   | Layout 1 | `63fb2daa5b58`  |
| 3072   | Layout 1 | `63fb2daa5b58`  |
| 3062   | Layout 1 | `63fb2daa5b58`  |
| 3052   | Layout 1 | `63fb2daa5b58`  |
| 3045   | Layout 1 | `63fb2daa5b58`  |
| 3037   | Layout 1 | `63fb2daa5b58`  |
| 3030   | Layout 1 | `63fb2daa5b58`  |
| 3021   | Layout 1 | `63fb2daa5b58`  |
| 3012   | Layout 1 | `63fb2daa5b58`  |
| 3002   | Layout 1 | `63fb2daa5b58`  |
| 2995   | Layout 1 | `63fb2daa5b58`  |
| 2987   | Layout 1 | `63fb2daa5b58`  |
| 2978   | Layout 1 | `63fb2daa5b58`  |
| 2970   | Layout 1 | `63fb2daa5b58`  |
| 2959   | Layout 1 | `63fb2daa5b58`  |
| 2951   | Layout 1 | `63fb2daa5b58`  |
| 2942   | Layout 1 | `63fb2daa5b58`  |
| 2935   | Layout 1 | `63fb2daa5b58`  |
| 2932   | Layout 1 | `63fb2daa5b58`  |
| 2923   | Layout 1 | `63fb2daa5b58`  |
| 2919   | Layout 1 | `63fb2daa5b58`  |
| 2907   | Layout 1 | `63fb2daa5b58`  |
| 2900   | Layout 1 | `63fb2daa5b58`  |
| 2891   | Layout 1 | `63fb2daa5b58`  |
| 2882   | Layout 1 | `63fb2daa5b58`  |
| 2872   | Layout 1 | `63fb2daa5b58`  |
| 2863   | Layout 1 | `63fb2daa5b58`  |
| 2855   | Layout 1 | `63fb2daa5b58`  |
| 2849   | Layout 1 | `63fb2daa5b58`  |
| 2844   | Layout 1 | `63fb2daa5b58`  |
| 2834   | Layout 1 | `63fb2daa5b58`  |
| 2825   | Layout 1 | `63fb2daa5b58`  |
| 2819   | Layout 1 | `63fb2daa5b58`  |
| 2811   | Layout 1 | `63fb2daa5b58`  |
| 2803   | Layout 1 | `63fb2daa5b58`  |
| 2794   | Layout 1 | `63fb2daa5b58`  |
| 2783   | Layout 1 | `63fb2daa5b58`  |
| 2774   | Layout 1 | `63fb2daa5b58`  |
| 2765   | Layout 1 | `63fb2daa5b58`  |
| 2756   | Layout 1 | `63fb2daa5b58`  |
| 2750   | Layout 1 | `63fb2daa5b58`  |
| 2743   | Layout 1 | `63fb2daa5b58`  |
| 2736   | Layout 1 | `63fb2daa5b58`  |
| 2726   | Layout 1 | `63fb2daa5b58`  |
| 2717   | Layout 1 | `63fb2daa5b58`  |
| 2709   | Layout 1 | `63fb2daa5b58`  |
| 2703   | Layout 1 | `63fb2daa5b58`  |
| 2695   | Layout 1 | `63fb2daa5b58`  |
| 2684   | Layout 1 | `63fb2daa5b58`  |
| 2672   | Layout 1 | `63fb2daa5b58`  |
| 2665   | Layout 1 | `63fb2daa5b58`  |
| 2657   | Layout 1 | `63fb2daa5b58`  |
| 2649   | Layout 1 | `63fb2daa5b58`  |
| 2644   | Layout 1 | `63fb2daa5b58`  |
| 2637   | Layout 1 | `63fb2daa5b58`  |
| 2629   | Layout 1 | `63fb2daa5b58`  |
| 2619   | Layout 1 | `63fb2daa5b58`  |
| 2612   | Layout 1 | `63fb2daa5b58`  |
| 2606   | Layout 1 | `63fb2daa5b58`  |
| 2602   | Layout 1 | `63fb2daa5b58`  |
| 2601   | Layout 1 | `63fb2daa5b58`  |
| 2592   | Layout 1 | `63fb2daa5b58`  |
| 2583   | Layout 1 | `63fb2daa5b58`  |
| 2575   | Layout 1 | `63fb2daa5b58`  |
| 2567   | Layout 1 | `63fb2daa5b58`  |
| 2560   | Layout 1 | `63fb2daa5b58`  |
| 2553   | Layout 1 | `63fb2daa5b58`  |
| 2545   | Layout 1 | `63fb2daa5b58`  |
| 2538   | Layout 1 | `63fb2daa5b58`  |
| 2529   | Layout 1 | `63fb2daa5b58`  |
| 2519   | Layout 1 | `63fb2daa5b58`  |
| 2513   | Layout 1 | `63fb2daa5b58`  |
| 2510   | Layout 1 | `63fb2daa5b58`  |
| 2507   | Layout 1 | `63fb2daa5b58`  |
| 2503   | Layout 1 | `63fb2daa5b58`  |
| 2498   | Layout 1 | `63fb2daa5b58`  |
| 2492   | Layout 1 | `63fb2daa5b58`  |
| 2487   | Layout 1 | `63fb2daa5b58`  |
| 2480   | Layout 1 | `63fb2daa5b58`  |
| 2474   | Layout 1 | `63fb2daa5b58`  |
| 2468   | Layout 1 | `63fb2daa5b58`  |
| 2460   | Layout 1 | `63fb2daa5b58`  |
| 2453   | Layout 1 | `63fb2daa5b58`  |
| 2444   | Layout 1 | `63fb2daa5b58`  |
| 2438   | Layout 1 | `63fb2daa5b58`  |
| 2434   | Layout 1 | `63fb2daa5b58`  |
| 2429   | Layout 1 | `63fb2daa5b58`  |
| 2421   | Layout 1 | `63fb2daa5b58`  |
| 2414   | Layout 1 | `63fb2daa5b58`  |
| 2407   | Layout 1 | `63fb2daa5b58`  |
| 2401   | Layout 1 | `63fb2daa5b58`  |
| 2397   | Layout 1 | `63fb2daa5b58`  |
| 2393   | Layout 1 | `63fb2daa5b58`  |
| 2384   | Layout 1 | `63fb2daa5b58`  |
| 2378   | Layout 1 | `63fb2daa5b58`  |
| 2372   | Layout 1 | `63fb2daa5b58`  |
| 2358   | Layout 1 | `63fb2daa5b58`  |
| 2352   | Layout 1 | `63fb2daa5b58`  |
| 2347   | Layout 1 | `63fb2daa5b58`  |
| 2343   | Layout 1 | `63fb2daa5b58`  |
| 2335   | Layout 1 | `63fb2daa5b58`  |
| 2327   | Layout 1 | `63fb2daa5b58`  |
| 2324   | Layout 1 | `63fb2daa5b58`  |
| 2319   | Layout 1 | `63fb2daa5b58`  |
| 2313   | Layout 1 | `63fb2daa5b58`  |
| 2308   | Layout 1 | `63fb2daa5b58`  |
| 2302   | Layout 1 | `63fb2daa5b58`  |
| 2295   | Layout 1 | `63fb2daa5b58`  |
| 2290   | Layout 1 | `63fb2daa5b58`  |
| 2284   | Layout 1 | `63fb2daa5b58`  |
| 2276   | Layout 1 | `63fb2daa5b58`  |
| 2269   | Layout 1 | `63fb2daa5b58`  |
| 2259   | Layout 1 | `63fb2daa5b58`  |
| 2250   | Layout 1 | `63fb2daa5b58`  |
| 2243   | Layout 1 | `63fb2daa5b58`  |
| 2235   | Layout 1 | `63fb2daa5b58`  |
| 2229   | Layout 1 | `63fb2daa5b58`  |
| 2224   | Layout 1 | `63fb2daa5b58`  |
| 2218   | Layout 1 | `63fb2daa5b58`  |
| 2215   | Layout 1 | `63fb2daa5b58`  |
| 2207   | Layout 1 | `63fb2daa5b58`  |
| 2203   | Layout 1 | `63fb2daa5b58`  |
| 2196   | Layout 1 | `63fb2daa5b58`  |
| 2192   | Layout 1 | `63fb2daa5b58`  |
| 2189   | Layout 1 | `63fb2daa5b58`  |
| 2183   | Layout 1 | `63fb2daa5b58`  |
| 2179   | Layout 1 | `63fb2daa5b58`  |
| 2171   | Layout 1 | `63fb2daa5b58`  |
| 2163   | Layout 1 | `63fb2daa5b58`  |
| 2156   | Layout 1 | `63fb2daa5b58`  |
| 2151   | Layout 1 | `63fb2daa5b58`  |
| 2147   | Layout 1 | `63fb2daa5b58`  |
| 2142   | Layout 1 | `63fb2daa5b58`  |
| 2138   | Layout 1 | `63fb2daa5b58`  |
| 2134   | Layout 1 | `63fb2daa5b58`  |
| 2130   | Layout 1 | `63fb2daa5b58`  |
| 2122   | Layout 1 | `63fb2daa5b58`  |
| 2107   | Layout 1 | `63fb2daa5b58`  |
| 2098   | Layout 1 | `63fb2daa5b58`  |
| 2089   | Layout 1 | `63fb2daa5b58`  |
| 2081   | Layout 1 | `63fb2daa5b58`  |
| 2073   | Layout 1 | `63fb2daa5b58`  |
| 2067   | Layout 1 | `63fb2daa5b58`  |
| 2063   | Layout 1 | `63fb2daa5b58`  |
| 2059   | Layout 1 | `63fb2daa5b58`  |
| 2052   | Layout 1 | `63fb2daa5b58`  |
| 2044   | Layout 1 | `63fb2daa5b58`  |
| 2039   | Layout 1 | `63fb2daa5b58`  |
| 2032   | Layout 1 | `63fb2daa5b58`  |
| 2025   | Layout 1 | `63fb2daa5b58`  |
| 2011   | Layout 1 | `63fb2daa5b58`  |
| 2005   | Layout 1 | `63fb2daa5b58`  |
| 2000   | Layout 1 | `63fb2daa5b58`  |
| 1996   | Layout 1 | `63fb2daa5b58`  |
| 1991   | Layout 1 | `63fb2daa5b58`  |
| 1985   | Layout 1 | `63fb2daa5b58`  |
| 1980   | Layout 1 | `63fb2daa5b58`  |
| 1969   | Layout 1 | `63fb2daa5b58`  |
| 1964   | Layout 1 | `63fb2daa5b58`  |
| 1958   | Layout 1 | `63fb2daa5b58`  |
| 1950   | Layout 1 | `63fb2daa5b58`  |
| 1945   | Layout 1 | `63fb2daa5b58`  |
| 1937   | Layout 1 | `63fb2daa5b58`  |
| 1933   | Layout 1 | `63fb2daa5b58`  |
| 1927   | Layout 1 | `63fb2daa5b58`  |
| 1921   | Layout 1 | `63fb2daa5b58`  |
| 1914   | Layout 1 | `63fb2daa5b58`  |
| 1908   | Layout 1 | `63fb2daa5b58`  |
| 1897   | Layout 1 | `63fb2daa5b58`  |
| 1892   | Layout 1 | `63fb2daa5b58`  |
| 1886   | Layout 1 | `63fb2daa5b58`  |
| 1881   | Layout 1 | `63fb2daa5b58`  |
| 1871   | Layout 1 | `63fb2daa5b58`  |
| 1866   | Layout 1 | `63fb2daa5b58`  |
| 1862   | Layout 1 | `63fb2daa5b58`  |
| 1854   | Layout 1 | `63fb2daa5b58`  |
| 1846   | Layout 1 | `63fb2daa5b58`  |
| 1838   | Layout 1 | `63fb2daa5b58`  |
| 1832   | Layout 1 | `63fb2daa5b58`  |
| 1826   | Layout 1 | `63fb2daa5b58`  |
| 1822   | Layout 1 | `63fb2daa5b58`  |
| 1818   | Layout 1 | `63fb2daa5b58`  |
| 1804   | Layout 1 | `63fb2daa5b58`  |
| 1794   | Layout 1 | `63fb2daa5b58`  |
| 1790   | Layout 1 | `63fb2daa5b58`  |
| 1784   | Layout 1 | `63fb2daa5b58`  |
| 1774   | Layout 1 | `63fb2daa5b58`  |
| 1771   | Layout 1 | `63fb2daa5b58`  |
| 1762   | Layout 1 | `63fb2daa5b58`  |
| 1759   | Layout 1 | `63fb2daa5b58`  |
| 1754   | Layout 1 | `63fb2daa5b58`  |
| 1749   | Layout 1 | `63fb2daa5b58`  |
| 1743   | Layout 1 | `63fb2daa5b58`  |
| 1737   | Layout 1 | `63fb2daa5b58`  |
| 1731   | Layout 1 | `63fb2daa5b58`  |
| 1725   | Layout 1 | `63fb2daa5b58`  |
| 1717   | Layout 1 | `63fb2daa5b58`  |
| 1710   | Layout 1 | `63fb2daa5b58`  |
| 1704   | Layout 1 | `63fb2daa5b58`  |
| 1698   | Layout 1 | `63fb2daa5b58`  |
| 1690   | Layout 1 | `63fb2daa5b58`  |
| 1685   | Layout 1 | `63fb2daa5b58`  |
| 1680   | Layout 1 | `63fb2daa5b58`  |
| 1674   | Layout 1 | `63fb2daa5b58`  |
| 1668   | Layout 1 | `63fb2daa5b58`  |
| 1659   | Layout 1 | `63fb2daa5b58`  |
| 1649   | Layout 1 | `63fb2daa5b58`  |
| 1642   | Layout 1 | `63fb2daa5b58`  |
| 1636   | Layout 1 | `63fb2daa5b58`  |
| 1628   | Layout 1 | `63fb2daa5b58`  |
| 1622   | Layout 1 | `63fb2daa5b58`  |
| 1614   | Layout 1 | `63fb2daa5b58`  |
| 1608   | Layout 1 | `63fb2daa5b58`  |
| 1602   | Layout 1 | `63fb2daa5b58`  |
| 1598   | Layout 1 | `63fb2daa5b58`  |
| 1594   | Layout 1 | `63fb2daa5b58`  |
| 1590   | Layout 1 | `63fb2daa5b58`  |
| 1587   | Layout 1 | `63fb2daa5b58`  |
| 1584   | Layout 1 | `63fb2daa5b58`  |
| 1579   | Layout 1 | `63fb2daa5b58`  |
| 1572   | Layout 1 | `63fb2daa5b58`  |
| 1565   | Layout 1 | `63fb2daa5b58`  |
| 1559   | Layout 1 | `63fb2daa5b58`  |
| 1554   | Layout 1 | `63fb2daa5b58`  |
| 1547   | Layout 1 | `63fb2daa5b58`  |
| 1537   | Layout 1 | `63fb2daa5b58`  |
| 1529   | Layout 1 | `63fb2daa5b58`  |
| 1524   | Layout 1 | `63fb2daa5b58`  |
| 1519   | Layout 1 | `63fb2daa5b58`  |
| 1509   | Layout 1 | `63fb2daa5b58`  |
| 1506   | Layout 1 | `63fb2daa5b58`  |
| 1504   | Layout 1 | `63fb2daa5b58`  |
| 1500   | Layout 1 | `63fb2daa5b58`  |
| 1493   | Layout 1 | `63fb2daa5b58`  |
| 1489   | Layout 1 | `63fb2daa5b58`  |
| 1485   | Layout 1 | `63fb2daa5b58`  |
| 1481   | Layout 1 | `63fb2daa5b58`  |
| 1474   | Layout 1 | `63fb2daa5b58`  |
| 1466   | Layout 1 | `63fb2daa5b58`  |
| 1462   | Layout 1 | `63fb2daa5b58`  |
| 1459   | Layout 1 | `63fb2daa5b58`  |
| 1453   | Layout 1 | `63fb2daa5b58`  |
| 1450   | Layout 1 | `63fb2daa5b58`  |
| 1445   | Layout 1 | `63fb2daa5b58`  |
| 1439   | Layout 1 | `63fb2daa5b58`  |
| 1433   | Layout 1 | `63fb2daa5b58`  |
| 1430   | Layout 1 | `63fb2daa5b58`  |
| 1426   | Layout 1 | `63fb2daa5b58`  |
| 1421   | Layout 1 | `63fb2daa5b58`  |
| 1417   | Layout 1 | `63fb2daa5b58`  |
| 1416   | Layout 1 | `63fb2daa5b58`  |
| 1409   | Layout 1 | `63fb2daa5b58`  |
| 1405   | Layout 1 | `63fb2daa5b58`  |
| 1401   | Layout 1 | `63fb2daa5b58`  |
| 1396   | Layout 1 | `63fb2daa5b58`  |
| 1391   | Layout 1 | `63fb2daa5b58`  |
| 1390   | Layout 1 | `63fb2daa5b58`  |
| 1386   | Layout 1 | `63fb2daa5b58`  |
| 1381   | Layout 1 | `63fb2daa5b58`  |
| 1379   | Layout 1 | `63fb2daa5b58`  |
| 1372   | Layout 1 | `63fb2daa5b58`  |
| 1366   | Layout 1 | `63fb2daa5b58`  |
| 1364   | Layout 1 | `63fb2daa5b58`  |
| 1363   | Layout 1 | `63fb2daa5b58`  |
| 1360   | Layout 1 | `63fb2daa5b58`  |
| 1358   | Layout 1 | `63fb2daa5b58`  |
| 1355   | Layout 1 | `63fb2daa5b58`  |
| 1351   | Layout 1 | `63fb2daa5b58`  |
| 1348   | Layout 1 | `63fb2daa5b58`  |
| 1346   | Layout 1 | `63fb2daa5b58`  |
| 1341   | Layout 1 | `63fb2daa5b58`  |
| 1340   | Layout 1 | `63fb2daa5b58`  |
| 1338   | Layout 1 | `63fb2daa5b58`  |
| 1335   | Layout 1 | `63fb2daa5b58`  |
| 1333   | Layout 1 | `63fb2daa5b58`  |
| 1329   | Layout 1 | `63fb2daa5b58`  |
| 1327   | Layout 1 | `63fb2daa5b58`  |
| 1324   | Layout 1 | `63fb2daa5b58`  |
| 1321   | Layout 1 | `63fb2daa5b58`  |
| 1319   | Layout 1 | `63fb2daa5b58`  |
| 1318   | Layout 1 | `63fb2daa5b58`  |
| 1316   | Layout 1 | `63fb2daa5b58`  |
| 1313   | Layout 1 | `63fb2daa5b58`  |
| 1311   | Layout 1 | `63fb2daa5b58`  |
| 1309   | Layout 1 | `63fb2daa5b58`  |
| 1304   | Layout 1 | `63fb2daa5b58`  |
| 1292   | Layout 1 | `63fb2daa5b58`  |
| 1286   | Layout 1 | `63fb2daa5b58`  |
| 1280   | Layout 1 | `63fb2daa5b58`  |
| 1276   | Layout 1 | `63fb2daa5b58`  |
| 1267   | Layout 1 | `63fb2daa5b58`  |
| 1261   | Layout 1 | `63fb2daa5b58`  |
| 1256   | Layout 1 | `63fb2daa5b58`  |
| 1250   | No file  | `63fb2daa5b58`  |
| 1246   | No file  | `63fb2daa5b58`  |
| 1239   | No file  | `63fb2daa5b58`  |
| 1230   | No file  | `63fb2daa5b58`  |
| 1226   | No file  | `63fb2daa5b58`  |
| 1220   | No file  | `63fb2daa5b58`  |
| 1217   | No file  | `63fb2daa5b58`  |
| 1211   | No file  | `63fb2daa5b58`  |
| 1210   | No file  | `63fb2daa5b58`  |
| 1208   | No file  | `63fb2daa5b58`  |
| 1203   | No file  | `63fb2daa5b58`  |
| 1197   | No file  | `63fb2daa5b58`  |
| 1194   | No file  | `63fb2daa5b58`  |
| 1192   | No file  | `63fb2daa5b58`  |
| 1187   | No file  | `63fb2daa5b58`  |
| 1183   | No file  | `63fb2daa5b58`  |
| 1177   | No file  | `63fb2daa5b58`  |
| 1173   | No file  | `63fb2daa5b58`  |
| 1167   | No file  | `63fb2daa5b58`  |
| 1164   | No file  | `63fb2daa5b58`  |
| 1156   | No file  | `63fb2daa5b58`  |
| 1149   | No file  | `63fb2daa5b58`  |
| 1144   | No file  | `63fb2daa5b58`  |
| 1137   | No file  | `63fb2daa5b58`  |
| 1132   | No file  | `63fb2daa5b58`  |
| 1127   | No file  | `63fb2daa5b58`  |
| 1122   | No file  | `63fb2daa5b58`  |
| 1118   | No file  | `63fb2daa5b58`  |
| 1114   | No file  | `63fb2daa5b58`  |
| 1109   | No file  | `63fb2daa5b58`  |
| 1102   | No file  | `63fb2daa5b58`  |
| 1096   | No file  | `63fb2daa5b58`  |
| 1088   | No file  | `63fb2daa5b58`  |
| 1081   | No file  | `63fb2daa5b58`  |
| 1076   | No file  | `63fb2daa5b58`  |
| 1069   | No file  | `63fb2daa5b58`  |
| 1064   | No file  | `63fb2daa5b58`  |
| 1058   | No file  | `63fb2daa5b58`  |
| 1051   | No file  | `63fb2daa5b58`  |
| 1044   | No file  | `63fb2daa5b58`  |
| 1036   | No file  | `63fb2daa5b58`  |
| 1026   | No file  | `63fb2daa5b58`  |
| 1016   | No file  | `63fb2daa5b58`  |
| 1009   | No file  | `63fb2daa5b58`  |
| 1005   | No file  | `63fb2daa5b58`  |
| 1000   | No file  | `63fb2daa5b58`  |
| 998    | No file  | `63fb2daa5b58`  |
| 990    | No file  | `63fb2daa5b58`  |
| 979    | No file  | `63fb2daa5b58`  |
| 972    | No file  | `63fb2daa5b58`  |
| 963    | No file  | `63fb2daa5b58`  |
| 955    | No file  | `63fb2daa5b58`  |
| 946    | No file  | `63fb2daa5b58`  |
| 938    | No file  | `63fb2daa5b58`  |
| 927    | No file  | `63fb2daa5b58`  |
| 911    | No file  | `63fb2daa5b58`  |
| 904    | No file  | `63fb2daa5b58`  |
| 899    | No file  | `63fb2daa5b58`  |
| 894    | No file  | `63fb2daa5b58`  |
| 885    | No file  | `63fb2daa5b58`  |
| 879    | No file  | `63fb2daa5b58`  |
| 872    | No file  | `63fb2daa5b58`  |
| 864    | No file  | `63fb2daa5b58`  |
| 855    | No file  | `63fb2daa5b58`  |
| 853    | No file  | `63fb2daa5b58`  |
| 845    | No file  | `63fb2daa5b58`  |
| 837    | No file  | `63fb2daa5b58`  |
| 829    | No file  | `63fb2daa5b58`  |
| 822    | No file  | `63fb2daa5b58`  |
| 814    | No file  | `63fb2daa5b58`  |
| 805    | No file  | `63fb2daa5b58`  |
| 794    | No file  | `63fb2daa5b58`  |
| 787    | No file  | `63fb2daa5b58`  |
| 780    | No file  | `63fb2daa5b58`  |
| 771    | No file  | `63fb2daa5b58`  |
| 760    | No file  | `63fb2daa5b58`  |
| 748    | No file  | `63fb2daa5b58`  |
| 741    | No file  | `63fb2daa5b58`  |
| 736    | No file  | `63fb2daa5b58`  |
| 731    | No file  | `63fb2daa5b58`  |
| 723    | No file  | `63fb2daa5b58`  |
| 711    | No file  | `63fb2daa5b58`  |
| 707    | No file  | `63fb2daa5b58`  |
| 697    | No file  | `63fb2daa5b58`  |
| 689    | No file  | `63fb2daa5b58`  |
| 683    | No file  | `63fb2daa5b58`  |
| 678    | No file  | `63fb2daa5b58`  |
| 670    | No file  | `63fb2daa5b58`  |
| 661    | No file  | `63fb2daa5b58`  |
| 656    | No file  | `63fb2daa5b58`  |
| 652    | No file  | `63fb2daa5b58`  |
| 643    | No file  | `63fb2daa5b58`  |
| 637    | No file  | `63fb2daa5b58`  |
| 630    | No file  | `63fb2daa5b58`  |
| 627    | No file  | `63fb2daa5b58`  |
| 621    | No file  | `63fb2daa5b58`  |
| 617    | No file  | `63fb2daa5b58`  |
| 615    | No file  | `63fb2daa5b58`  |
| 606    | No file  | `63fb2daa5b58`  |
| 599    | No file  | `63fb2daa5b58`  |
| 592    | No file  | `63fb2daa5b58`  |
| 586    | No file  | `63fb2daa5b58`  |
| 577    | No file  | `63fb2daa5b58`  |
| 569    | No file  | `63fb2daa5b58`  |
| 561    | No file  | `63fb2daa5b58`  |
| 554    | No file  | `63fb2daa5b58`  |
| 542    | No file  | `63fb2daa5b58`  |
| 532    | No file  | `63fb2daa5b58`  |
| 531    | No file  | `63fb2daa5b58`  |
| 526    | No file  | `63fb2daa5b58`  |
| 521    | No file  | `63fb2daa5b58`  |
| 517    | No file  | `63fb2daa5b58`  |
| 510    | No file  | `63fb2daa5b58`  |
| 508    | No file  | `63fb2daa5b58`  |
| 504    | No file  | `63fb2daa5b58`  |
| 497    | No file  | `63fb2daa5b58`  |
| 491    | No file  | `63fb2daa5b58`  |
| 485    | No file  | `63fb2daa5b58`  |
| 478    | No file  | `63fb2daa5b58`  |
| 472    | No file  | `63fb2daa5b58`  |
| 466    | No file  | `63fb2daa5b58`  |
| 457    | No file  | `63fb2daa5b58`  |
| 452    | No file  | `63fb2daa5b58`  |
| 449    | No file  | `63fb2daa5b58`  |
| 435    | No file  | `63fb2daa5b58`  |

<!-- versions:end -->

## Companion Files

| File                       | Required | Role                                                                                 |
| -------------------------- | -------- | ------------------------------------------------------------------------------------ |
| `couponoffset.dbss`        | Optional | `coupon_key -> (data_offset, data_size)` of every row; the parser walks the main file without it |
| `languagedata_en.loc`      | Optional | Coupon names (LOC type 47) and the category names (LOC type 51)                      |

The handler names the category in the loaded language from LOC type 51,
the key layout of [`cashproductcategory.dbss`](cashproductcategory_dbss.md).

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes             |
| ------- | ---------- | ----- | ----------------- |
| `+0x00` | u32        | count | Number of coupons |
| `+0x04` | Row[count] | rows  | See Row           |

### Row (variable: 69 bytes + texts)

| Offset                        | Type  | Field                             | Notes                                                                                          |
| ----------------------------- | ----- | --------------------------------- | ---------------------------------------------------------------------------------------------- |
| `+0x00`                       | u16   | coupon_key                        | Row key; LOC type 47 `str_id1` of the name                                                     |
| `+0x02`                       | u8    | unknown_02                        | `2` on every coupon of clients 1784 and 3482                                                   |
| `+0x03`                       | u64   | max_discount_pearl                | Cap of a rate discount in Pearls, `0` for none; `1000` and `2000` on four coupons of client 3482 |
| `+0x0B`                       | u64   | min_product_pearl                 | Lowest product price a Pearl discount applies to, `0` for none                                  |
| `+0x13`                       | str16 | name_kr                           | Korean name                                                                                    |
| `name_kr+0x00`                | u32   | expiration_days                   | Days the coupon stays valid after it is given, `1` to `365` on client 3482                     |
| `name_kr+0x04`                | u32   | discount_rate                     | Discount on the 1,000,000 = 100% scale (`300000` is 30%), `0` on Pearl discount coupons        |
| `name_kr+0x08`                | u64   | discount_pearl                    | Pearls off the price, `0` on rate coupons                                                      |
| `name_kr+0x10`                | str16 | icon_path                         | Icon under `ui_texture/icon/` (`New_Icon/09_Cash/00017718.dds` on all 117 coupons of client 3482) |
| `icon_path+0x00`              | str16 | category_expression_kr            | Korean category text: the category path as `main(middle(small))`, else the all-categories name of `cashproductcategory.dbss` |
| `category_expression_kr+0x00` | u16   | category_main                     | `cashproductcategory.dbss` main key, `65535` for every category                                |
| `category_expression_kr+0x02` | u16   | category_middle                   | Middle key under it, `65535` for none                                                          |
| `category_expression_kr+0x04` | u16   | category_small                    | Small key under that, `65535` for none                                                         |
| `category_expression_kr+0x06` | u32   | unknown_category_expression_kr_06 | `0` on every coupon of clients 1784 and 3482                                                   |

On client 3482 the file holds 117 coupons; 52 apply to every category, 33
to a main category, 28 to a middle and 4 to a small one. Every category
path the coupons name is a category of `cashproductcategory.dbss` on
clients 1784 and 3482.

### `couponoffset.dbss`

Bare offset table into `coupon.dbss` (no PABR magic, no trailer), read by
`parse_bare_offset_rows()` in `_common/pabr_offset.py`.

| Offset  | Type              | Field | Notes                         |
| ------- | ----------------- | ----- | ----------------------------- |
| `+0x00` | u32               | count | Equals the `coupon.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                                  |
| ------- | ---- | ----------- | ------------------------------------------------------ |
| `+0x00` | u16  | coupon_key  | Key of the row it points at                            |
| `+0x02` | u32  | data_offset | Absolute offset of the row in `coupon.dbss`, at `coupon_key` |
| `+0x06` | u32  | data_size   | The whole row                                          |

The index rows are in another order than the file; on clients 1784 and
3482 every index row points at the row with its key.

## Field Names

The `Coupon_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has the columns `CouponKey`, `Name`, `ExpirationDate`,
`DisCountRate`, `MaxDiscountPearl`, `MinProductPearl`, `DiscountPearl`,
`Categorys`, `CouponCategory_Main`, `CouponCategory_Middle`,
`CouponCategory_Small` and `IconPath`, 65 rows. An empty cell compares as
`0`, an empty category as `65535`.

| Field              | Column                  | Same value (client 1784) | Same value (client 3482) |
| ------------------ | ----------------------- | ------------------------ | ------------------------ |
| coupon_key         | `CouponKey`             | 65 of 65                 | 65 of 65                 |
| name_kr            | `Name`                  | 65 of 65                 | 65 of 65                 |
| expiration_days    | `ExpirationDate`        | 65 of 65                 | 65 of 65                 |
| discount_rate      | `DisCountRate`          | 65 of 65                 | 65 of 65                 |
| max_discount_pearl | `MaxDiscountPearl`      | 65 of 65                 | 65 of 65                 |
| min_product_pearl  | `MinProductPearl`       | 65 of 65                 | 65 of 65                 |
| discount_pearl     | `DiscountPearl`         | 65 of 65                 | 65 of 65                 |
| icon_path          | `IconPath`              | 65 of 65                 | 65 of 65                 |
| category_main      | `CouponCategory_Main`   | 65 of 65                 | 65 of 65                 |
| category_middle    | `CouponCategory_Middle` | 65 of 65                 | 65 of 65                 |
| category_small     | `CouponCategory_Small`  | 65 of 65                 | 65 of 65                 |

`Categorys` is empty on all 65 rows; it may be the list that
`unknown_category_expression_kr_06` counts.

## Notes

- LOC type 47 holds the coupon names under `coupon_key`: all 117 coupons of
  client 3482 have an English name (`Mount 30% DC` for `1507`).
- The category text of a coupon for every category is LOC type 51 key
  `(99, 65535, 255)`, `All (Except for Pearl, Loyalty)`; see LOC Names in
  [`cashproductcategory.dbss`](cashproductcategory_dbss.md).

## Open Questions

### What `unknown_02` Holds

The byte after the key is `2` on every coupon of clients 1784 and 3482,
rate and Pearl coupons alike, and no sheet column holds a `2`. The Lua
tells the two kinds apart with `isDisCountPearl()`, which the
`discount_pearl` field answers on its own.

### What the Trailing u32 Counts

`unknown_category_expression_kr_06` is `0` on every coupon. The empty
`Categorys` sheet column suggests a list of further categories; a coupon
with a second category would show whether it is a count.
