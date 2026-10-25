# `eventcategory.dbss` Format

## Purpose

The discount events of the pearl shop's event cart
(`panel_ingamecashshop_eventcart.luac`): per event index the cash shop
category, the discount period as text, up to ten discount steps (spend at
least `discount_ceiling` pearls, get `discount_price` off), the largest
discount and the event type. The Lua reads a row with
`ToClient_GetEventCategoryStaticStatusWrapperByKeyRaw(key)` and its
`getEventSize()`, `getEventlDiscountCelling(i)`,
`getEventlDiscountPrice(i)`, `getDiscountType()`, `isSellinPeriod()` and
`isDiscountPeriod()`. On client 3474 the file holds 4 events from
2018-04-13 to 2021-08-11. Companion `eventcategoryoffset.dbss` lists where
every row sits.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                       | Bytes | Records                 | Row bytes |
| ------ | -------------- | -------------------------- | ----- | ----------------------- | --------- |
| 1      | 1286 and later | `eventcategory.dbss`       | 1,040 | 40 Discount Step, 4 Row | 16        |
| 1      | 1286 and later | `eventcategoryoffset.dbss` | 44    | 4 Offset Row            | 10        |

| Layout | File                       | Known           | Unknown    |
| ------ | -------------------------- | --------------- | ---------- |
| 1      | `eventcategory.dbss`       | 1,032 B (99.2%) | 8 B (0.8%) |
| 1      | `eventcategoryoffset.dbss` | 44 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `de8b3a59ef8f`  |
| 3482   | Layout 1 | `de8b3a59ef8f`  |
| 3474   | Layout 1 | `de8b3a59ef8f`  |
| 3473   | Layout 1 | `de8b3a59ef8f`  |
| 3464   | Layout 1 | `de8b3a59ef8f`  |
| 3458   | Layout 1 | `de8b3a59ef8f`  |
| 3454   | Layout 1 | `de8b3a59ef8f`  |
| 3444   | Layout 1 | `de8b3a59ef8f`  |
| 3435   | Layout 1 | `de8b3a59ef8f`  |
| 3426   | Layout 1 | `de8b3a59ef8f`  |
| 3418   | Layout 1 | `de8b3a59ef8f`  |
| 3412   | Layout 1 | `de8b3a59ef8f`  |
| 3402   | Layout 1 | `de8b3a59ef8f`  |
| 3396   | Layout 1 | `de8b3a59ef8f`  |
| 3387   | Layout 1 | `de8b3a59ef8f`  |
| 3381   | Layout 1 | `de8b3a59ef8f`  |
| 3373   | Layout 1 | `de8b3a59ef8f`  |
| 3364   | Layout 1 | `de8b3a59ef8f`  |
| 3356   | Layout 1 | `de8b3a59ef8f`  |
| 3349   | Layout 1 | `de8b3a59ef8f`  |
| 3342   | Layout 1 | `de8b3a59ef8f`  |
| 3335   | Layout 1 | `de8b3a59ef8f`  |
| 3326   | Layout 1 | `de8b3a59ef8f`  |
| 3321   | Layout 1 | `de8b3a59ef8f`  |
| 3314   | Layout 1 | `de8b3a59ef8f`  |
| 3303   | Layout 1 | `de8b3a59ef8f`  |
| 3302   | Layout 1 | `de8b3a59ef8f`  |
| 3293   | Layout 1 | `de8b3a59ef8f`  |
| 3283   | Layout 1 | `de8b3a59ef8f`  |
| 3275   | Layout 1 | `de8b3a59ef8f`  |
| 3267   | Layout 1 | `de8b3a59ef8f`  |
| 3258   | Layout 1 | `de8b3a59ef8f`  |
| 3251   | Layout 1 | `de8b3a59ef8f`  |
| 3242   | Layout 1 | `de8b3a59ef8f`  |
| 3235   | Layout 1 | `de8b3a59ef8f`  |
| 3229   | Layout 1 | `de8b3a59ef8f`  |
| 3212   | Layout 1 | `de8b3a59ef8f`  |
| 3203   | Layout 1 | `de8b3a59ef8f`  |
| 3193   | Layout 1 | `de8b3a59ef8f`  |
| 3186   | Layout 1 | `de8b3a59ef8f`  |
| 3177   | Layout 1 | `de8b3a59ef8f`  |
| 3169   | Layout 1 | `de8b3a59ef8f`  |
| 3158   | Layout 1 | `de8b3a59ef8f`  |
| 3151   | Layout 1 | `de8b3a59ef8f`  |
| 3144   | Layout 1 | `de8b3a59ef8f`  |
| 3133   | Layout 1 | `de8b3a59ef8f`  |
| 3125   | Layout 1 | `de8b3a59ef8f`  |
| 3118   | Layout 1 | `de8b3a59ef8f`  |
| 3111   | Layout 1 | `de8b3a59ef8f`  |
| 3103   | Layout 1 | `de8b3a59ef8f`  |
| 3095   | Layout 1 | `de8b3a59ef8f`  |
| 3086   | Layout 1 | `de8b3a59ef8f`  |
| 3072   | Layout 1 | `de8b3a59ef8f`  |
| 3062   | Layout 1 | `de8b3a59ef8f`  |
| 3052   | Layout 1 | `de8b3a59ef8f`  |
| 3045   | Layout 1 | `de8b3a59ef8f`  |
| 3037   | Layout 1 | `de8b3a59ef8f`  |
| 3030   | Layout 1 | `de8b3a59ef8f`  |
| 3021   | Layout 1 | `de8b3a59ef8f`  |
| 3012   | Layout 1 | `de8b3a59ef8f`  |
| 3002   | Layout 1 | `de8b3a59ef8f`  |
| 2995   | Layout 1 | `de8b3a59ef8f`  |
| 2987   | Layout 1 | `de8b3a59ef8f`  |
| 2978   | Layout 1 | `de8b3a59ef8f`  |
| 2970   | Layout 1 | `de8b3a59ef8f`  |
| 2959   | Layout 1 | `de8b3a59ef8f`  |
| 2951   | Layout 1 | `de8b3a59ef8f`  |
| 2942   | Layout 1 | `de8b3a59ef8f`  |
| 2935   | Layout 1 | `de8b3a59ef8f`  |
| 2932   | Layout 1 | `de8b3a59ef8f`  |
| 2923   | Layout 1 | `de8b3a59ef8f`  |
| 2919   | Layout 1 | `de8b3a59ef8f`  |
| 2907   | Layout 1 | `de8b3a59ef8f`  |
| 2900   | Layout 1 | `de8b3a59ef8f`  |
| 2891   | Layout 1 | `de8b3a59ef8f`  |
| 2882   | Layout 1 | `de8b3a59ef8f`  |
| 2872   | Layout 1 | `de8b3a59ef8f`  |
| 2863   | Layout 1 | `de8b3a59ef8f`  |
| 2855   | Layout 1 | `de8b3a59ef8f`  |
| 2849   | Layout 1 | `de8b3a59ef8f`  |
| 2844   | Layout 1 | `de8b3a59ef8f`  |
| 2834   | Layout 1 | `de8b3a59ef8f`  |
| 2825   | Layout 1 | `de8b3a59ef8f`  |
| 2819   | Layout 1 | `de8b3a59ef8f`  |
| 2811   | Layout 1 | `de8b3a59ef8f`  |
| 2803   | Layout 1 | `de8b3a59ef8f`  |
| 2794   | Layout 1 | `de8b3a59ef8f`  |
| 2783   | Layout 1 | `de8b3a59ef8f`  |
| 2774   | Layout 1 | `de8b3a59ef8f`  |
| 2765   | Layout 1 | `de8b3a59ef8f`  |
| 2756   | Layout 1 | `de8b3a59ef8f`  |
| 2750   | Layout 1 | `de8b3a59ef8f`  |
| 2743   | Layout 1 | `de8b3a59ef8f`  |
| 2736   | Layout 1 | `de8b3a59ef8f`  |
| 2726   | Layout 1 | `de8b3a59ef8f`  |
| 2717   | Layout 1 | `de8b3a59ef8f`  |
| 2709   | Layout 1 | `de8b3a59ef8f`  |
| 2703   | Layout 1 | `de8b3a59ef8f`  |
| 2695   | Layout 1 | `de8b3a59ef8f`  |
| 2684   | Layout 1 | `de8b3a59ef8f`  |
| 2672   | Layout 1 | `de8b3a59ef8f`  |
| 2665   | Layout 1 | `de8b3a59ef8f`  |
| 2657   | Layout 1 | `de8b3a59ef8f`  |
| 2649   | Layout 1 | `de8b3a59ef8f`  |
| 2644   | Layout 1 | `de8b3a59ef8f`  |
| 2637   | Layout 1 | `de8b3a59ef8f`  |
| 2629   | Layout 1 | `de8b3a59ef8f`  |
| 2619   | Layout 1 | `de8b3a59ef8f`  |
| 2612   | Layout 1 | `de8b3a59ef8f`  |
| 2606   | Layout 1 | `de8b3a59ef8f`  |
| 2602   | Layout 1 | `de8b3a59ef8f`  |
| 2601   | Layout 1 | `de8b3a59ef8f`  |
| 2592   | Layout 1 | `de8b3a59ef8f`  |
| 2583   | Layout 1 | `de8b3a59ef8f`  |
| 2575   | Layout 1 | `de8b3a59ef8f`  |
| 2567   | Layout 1 | `de8b3a59ef8f`  |
| 2560   | Layout 1 | `de8b3a59ef8f`  |
| 2553   | Layout 1 | `de8b3a59ef8f`  |
| 2545   | Layout 1 | `de8b3a59ef8f`  |
| 2538   | Layout 1 | `de8b3a59ef8f`  |
| 2529   | Layout 1 | `de8b3a59ef8f`  |
| 2519   | Layout 1 | `de8b3a59ef8f`  |
| 2513   | Layout 1 | `de8b3a59ef8f`  |
| 2510   | Layout 1 | `de8b3a59ef8f`  |
| 2507   | Layout 1 | `de8b3a59ef8f`  |
| 2503   | Layout 1 | `de8b3a59ef8f`  |
| 2498   | Layout 1 | `de8b3a59ef8f`  |
| 2492   | Layout 1 | `de8b3a59ef8f`  |
| 2487   | Layout 1 | `de8b3a59ef8f`  |
| 2480   | Layout 1 | `de8b3a59ef8f`  |
| 2474   | Layout 1 | `de8b3a59ef8f`  |
| 2468   | Layout 1 | `de8b3a59ef8f`  |
| 2460   | Layout 1 | `de8b3a59ef8f`  |
| 2453   | Layout 1 | `de8b3a59ef8f`  |
| 2444   | Layout 1 | `de8b3a59ef8f`  |
| 2438   | Layout 1 | `de8b3a59ef8f`  |
| 2434   | Layout 1 | `de8b3a59ef8f`  |
| 2429   | Layout 1 | `de8b3a59ef8f`  |
| 2421   | Layout 1 | `de8b3a59ef8f`  |
| 2414   | Layout 1 | `de8b3a59ef8f`  |
| 2407   | Layout 1 | `de8b3a59ef8f`  |
| 2401   | Layout 1 | `de8b3a59ef8f`  |
| 2397   | Layout 1 | `de8b3a59ef8f`  |
| 2393   | Layout 1 | `de8b3a59ef8f`  |
| 2384   | Layout 1 | `de8b3a59ef8f`  |
| 2378   | Layout 1 | `de8b3a59ef8f`  |
| 2372   | Layout 1 | `de8b3a59ef8f`  |
| 2358   | Layout 1 | `de8b3a59ef8f`  |
| 2352   | Layout 1 | `de8b3a59ef8f`  |
| 2347   | Layout 1 | `de8b3a59ef8f`  |
| 2343   | Layout 1 | `de8b3a59ef8f`  |
| 2335   | Layout 1 | `de8b3a59ef8f`  |
| 2327   | Layout 1 | `de8b3a59ef8f`  |
| 2324   | Layout 1 | `de8b3a59ef8f`  |
| 2319   | Layout 1 | `de8b3a59ef8f`  |
| 2313   | Layout 1 | `de8b3a59ef8f`  |
| 2308   | Layout 1 | `de8b3a59ef8f`  |
| 2302   | Layout 1 | `de8b3a59ef8f`  |
| 2295   | Layout 1 | `de8b3a59ef8f`  |
| 2290   | Layout 1 | `de8b3a59ef8f`  |
| 2284   | Layout 1 | `de8b3a59ef8f`  |
| 2276   | Layout 1 | `de8b3a59ef8f`  |
| 2269   | Layout 1 | `de8b3a59ef8f`  |
| 2259   | Layout 1 | `de8b3a59ef8f`  |
| 2250   | Layout 1 | `de8b3a59ef8f`  |
| 2243   | Layout 1 | `de8b3a59ef8f`  |
| 2235   | Layout 1 | `de8b3a59ef8f`  |
| 2229   | Layout 1 | `de8b3a59ef8f`  |
| 2224   | Layout 1 | `de8b3a59ef8f`  |
| 2218   | Layout 1 | `de8b3a59ef8f`  |
| 2215   | Layout 1 | `de8b3a59ef8f`  |
| 2207   | Layout 1 | `de8b3a59ef8f`  |
| 2203   | Layout 1 | `de8b3a59ef8f`  |
| 2196   | Layout 1 | `de8b3a59ef8f`  |
| 2192   | Layout 1 | `de8b3a59ef8f`  |
| 2189   | Layout 1 | `de8b3a59ef8f`  |
| 2183   | Layout 1 | `de8b3a59ef8f`  |
| 2179   | Layout 1 | `de8b3a59ef8f`  |
| 2171   | Layout 1 | `de8b3a59ef8f`  |
| 2163   | Layout 1 | `de8b3a59ef8f`  |
| 2156   | Layout 1 | `de8b3a59ef8f`  |
| 2151   | Layout 1 | `de8b3a59ef8f`  |
| 2147   | Layout 1 | `de8b3a59ef8f`  |
| 2142   | Layout 1 | `de8b3a59ef8f`  |
| 2138   | Layout 1 | `de8b3a59ef8f`  |
| 2134   | Layout 1 | `de8b3a59ef8f`  |
| 2130   | Layout 1 | `de8b3a59ef8f`  |
| 2122   | Layout 1 | `de8b3a59ef8f`  |
| 2107   | Layout 1 | `de8b3a59ef8f`  |
| 2098   | Layout 1 | `de8b3a59ef8f`  |
| 2089   | Layout 1 | `de8b3a59ef8f`  |
| 2081   | Layout 1 | `de8b3a59ef8f`  |
| 2073   | Layout 1 | `de8b3a59ef8f`  |
| 2067   | Layout 1 | `de8b3a59ef8f`  |
| 2063   | Layout 1 | `de8b3a59ef8f`  |
| 2059   | Layout 1 | `de8b3a59ef8f`  |
| 2052   | Layout 1 | `de8b3a59ef8f`  |
| 2044   | Layout 1 | `de8b3a59ef8f`  |
| 2039   | Layout 1 | `de8b3a59ef8f`  |
| 2032   | Layout 1 | `de8b3a59ef8f`  |
| 2025   | Layout 1 | `de8b3a59ef8f`  |
| 2011   | Layout 1 | `de8b3a59ef8f`  |
| 2005   | Layout 1 | `de8b3a59ef8f`  |
| 2000   | Layout 1 | `de8b3a59ef8f`  |
| 1996   | Layout 1 | `de8b3a59ef8f`  |
| 1991   | Layout 1 | `de8b3a59ef8f`  |
| 1985   | Layout 1 | `de8b3a59ef8f`  |
| 1980   | Layout 1 | `de8b3a59ef8f`  |
| 1969   | Layout 1 | `de8b3a59ef8f`  |
| 1964   | Layout 1 | `de8b3a59ef8f`  |
| 1958   | Layout 1 | `de8b3a59ef8f`  |
| 1950   | Layout 1 | `de8b3a59ef8f`  |
| 1945   | Layout 1 | `de8b3a59ef8f`  |
| 1937   | Layout 1 | `de8b3a59ef8f`  |
| 1933   | Layout 1 | `de8b3a59ef8f`  |
| 1927   | Layout 1 | `de8b3a59ef8f`  |
| 1921   | Layout 1 | `de8b3a59ef8f`  |
| 1914   | Layout 1 | `de8b3a59ef8f`  |
| 1908   | Layout 1 | `de8b3a59ef8f`  |
| 1897   | Layout 1 | `de8b3a59ef8f`  |
| 1892   | Layout 1 | `de8b3a59ef8f`  |
| 1886   | Layout 1 | `de8b3a59ef8f`  |
| 1881   | Layout 1 | `de8b3a59ef8f`  |
| 1871   | Layout 1 | `de8b3a59ef8f`  |
| 1866   | Layout 1 | `de8b3a59ef8f`  |
| 1862   | Layout 1 | `de8b3a59ef8f`  |
| 1854   | Layout 1 | `de8b3a59ef8f`  |
| 1846   | Layout 1 | `de8b3a59ef8f`  |
| 1838   | Layout 1 | `de8b3a59ef8f`  |
| 1832   | Layout 1 | `de8b3a59ef8f`  |
| 1826   | Layout 1 | `de8b3a59ef8f`  |
| 1822   | Layout 1 | `de8b3a59ef8f`  |
| 1818   | Layout 1 | `de8b3a59ef8f`  |
| 1804   | Layout 1 | `de8b3a59ef8f`  |
| 1794   | Layout 1 | `de8b3a59ef8f`  |
| 1790   | Layout 1 | `de8b3a59ef8f`  |
| 1784   | Layout 1 | `de8b3a59ef8f`  |
| 1774   | Layout 1 | `de8b3a59ef8f`  |
| 1771   | Layout 1 | `de8b3a59ef8f`  |
| 1762   | Layout 1 | `de8b3a59ef8f`  |
| 1759   | Layout 1 | `de8b3a59ef8f`  |
| 1754   | Layout 1 | `de8b3a59ef8f`  |
| 1749   | Layout 1 | `de8b3a59ef8f`  |
| 1743   | Layout 1 | `de8b3a59ef8f`  |
| 1737   | Layout 1 | `de8b3a59ef8f`  |
| 1731   | Layout 1 | `de8b3a59ef8f`  |
| 1725   | Layout 1 | `de8b3a59ef8f`  |
| 1717   | Layout 1 | `de8b3a59ef8f`  |
| 1710   | Layout 1 | `de8b3a59ef8f`  |
| 1704   | Layout 1 | `de8b3a59ef8f`  |
| 1698   | Layout 1 | `de8b3a59ef8f`  |
| 1690   | Layout 1 | `de8b3a59ef8f`  |
| 1685   | Layout 1 | `de8b3a59ef8f`  |
| 1680   | Layout 1 | `de8b3a59ef8f`  |
| 1674   | Layout 1 | `de8b3a59ef8f`  |
| 1668   | Layout 1 | `de8b3a59ef8f`  |
| 1659   | Layout 1 | `de8b3a59ef8f`  |
| 1649   | Layout 1 | `de8b3a59ef8f`  |
| 1642   | Layout 1 | `de8b3a59ef8f`  |
| 1636   | Layout 1 | `de8b3a59ef8f`  |
| 1628   | Layout 1 | `de8b3a59ef8f`  |
| 1622   | Layout 1 | `de8b3a59ef8f`  |
| 1614   | Layout 1 | `de8b3a59ef8f`  |
| 1608   | Layout 1 | `de8b3a59ef8f`  |
| 1602   | Layout 1 | `de8b3a59ef8f`  |
| 1598   | Layout 1 | `de8b3a59ef8f`  |
| 1594   | Layout 1 | `de8b3a59ef8f`  |
| 1590   | Layout 1 | `de8b3a59ef8f`  |
| 1587   | Layout 1 | `de8b3a59ef8f`  |
| 1584   | Layout 1 | `de8b3a59ef8f`  |
| 1579   | Layout 1 | `de8b3a59ef8f`  |
| 1572   | Layout 1 | `de8b3a59ef8f`  |
| 1565   | Layout 1 | `de8b3a59ef8f`  |
| 1559   | Layout 1 | `de8b3a59ef8f`  |
| 1554   | Layout 1 | `de8b3a59ef8f`  |
| 1547   | Layout 1 | `de8b3a59ef8f`  |
| 1537   | Layout 1 | `de8b3a59ef8f`  |
| 1529   | Layout 1 | `de8b3a59ef8f`  |
| 1524   | Layout 1 | `de8b3a59ef8f`  |
| 1519   | Layout 1 | `de8b3a59ef8f`  |
| 1509   | Layout 1 | `de8b3a59ef8f`  |
| 1506   | Layout 1 | `de8b3a59ef8f`  |
| 1504   | Layout 1 | `de8b3a59ef8f`  |
| 1500   | Layout 1 | `de8b3a59ef8f`  |
| 1493   | Layout 1 | `de8b3a59ef8f`  |
| 1489   | Layout 1 | `de8b3a59ef8f`  |
| 1485   | Layout 1 | `de8b3a59ef8f`  |
| 1481   | Layout 1 | `de8b3a59ef8f`  |
| 1474   | Layout 1 | `de8b3a59ef8f`  |
| 1466   | Layout 1 | `de8b3a59ef8f`  |
| 1462   | Layout 1 | `de8b3a59ef8f`  |
| 1459   | Layout 1 | `de8b3a59ef8f`  |
| 1453   | Layout 1 | `de8b3a59ef8f`  |
| 1450   | Layout 1 | `de8b3a59ef8f`  |
| 1445   | Layout 1 | `de8b3a59ef8f`  |
| 1439   | Layout 1 | `de8b3a59ef8f`  |
| 1433   | Layout 1 | `de8b3a59ef8f`  |
| 1430   | Layout 1 | `de8b3a59ef8f`  |
| 1426   | Layout 1 | `de8b3a59ef8f`  |
| 1421   | Layout 1 | `de8b3a59ef8f`  |
| 1417   | Layout 1 | `de8b3a59ef8f`  |
| 1416   | Layout 1 | `de8b3a59ef8f`  |
| 1409   | Layout 1 | `de8b3a59ef8f`  |
| 1405   | Layout 1 | `de8b3a59ef8f`  |
| 1401   | Layout 1 | `de8b3a59ef8f`  |
| 1396   | Layout 1 | `de8b3a59ef8f`  |
| 1391   | Layout 1 | `de8b3a59ef8f`  |
| 1390   | Layout 1 | `de8b3a59ef8f`  |
| 1386   | Layout 1 | `de8b3a59ef8f`  |
| 1381   | Layout 1 | `de8b3a59ef8f`  |
| 1379   | Layout 1 | `de8b3a59ef8f`  |
| 1372   | Layout 1 | `de8b3a59ef8f`  |
| 1366   | Layout 1 | `de8b3a59ef8f`  |
| 1364   | Layout 1 | `de8b3a59ef8f`  |
| 1363   | Layout 1 | `de8b3a59ef8f`  |
| 1360   | Layout 1 | `de8b3a59ef8f`  |
| 1358   | Layout 1 | `de8b3a59ef8f`  |
| 1355   | Layout 1 | `de8b3a59ef8f`  |
| 1351   | Layout 1 | `de8b3a59ef8f`  |
| 1348   | Layout 1 | `de8b3a59ef8f`  |
| 1346   | Layout 1 | `de8b3a59ef8f`  |
| 1341   | Layout 1 | `de8b3a59ef8f`  |
| 1340   | Layout 1 | `de8b3a59ef8f`  |
| 1338   | Layout 1 | `de8b3a59ef8f`  |
| 1335   | Layout 1 | `de8b3a59ef8f`  |
| 1333   | Layout 1 | `de8b3a59ef8f`  |
| 1329   | Layout 1 | `de8b3a59ef8f`  |
| 1327   | Layout 1 | `de8b3a59ef8f`  |
| 1324   | Layout 1 | `de8b3a59ef8f`  |
| 1321   | Layout 1 | `de8b3a59ef8f`  |
| 1319   | Layout 1 | `de8b3a59ef8f`  |
| 1318   | Layout 1 | `de8b3a59ef8f`  |
| 1316   | Layout 1 | `de8b3a59ef8f`  |
| 1313   | Layout 1 | `de8b3a59ef8f`  |
| 1311   | Layout 1 | `de8b3a59ef8f`  |
| 1309   | Layout 1 | `de8b3a59ef8f`  |
| 1304   | Layout 1 | `de8b3a59ef8f`  |
| 1292   | Layout 1 | `de8b3a59ef8f`  |
| 1286   | Layout 1 | `de8b3a59ef8f`  |
| 1280   | No file  | `de8b3a59ef8f`  |
| 1276   | No file  | `de8b3a59ef8f`  |
| 1267   | No file  | `de8b3a59ef8f`  |
| 1261   | No file  | `de8b3a59ef8f`  |
| 1256   | No file  | `de8b3a59ef8f`  |
| 1250   | No file  | `de8b3a59ef8f`  |
| 1246   | No file  | `de8b3a59ef8f`  |
| 1239   | No file  | `de8b3a59ef8f`  |
| 1230   | No file  | `de8b3a59ef8f`  |
| 1226   | No file  | `de8b3a59ef8f`  |
| 1220   | No file  | `de8b3a59ef8f`  |
| 1217   | No file  | `de8b3a59ef8f`  |
| 1211   | No file  | `de8b3a59ef8f`  |
| 1210   | No file  | `de8b3a59ef8f`  |
| 1208   | No file  | `de8b3a59ef8f`  |
| 1203   | No file  | `de8b3a59ef8f`  |
| 1197   | No file  | `de8b3a59ef8f`  |
| 1194   | No file  | `de8b3a59ef8f`  |
| 1192   | No file  | `de8b3a59ef8f`  |
| 1187   | No file  | `de8b3a59ef8f`  |
| 1183   | No file  | `de8b3a59ef8f`  |
| 1177   | No file  | `de8b3a59ef8f`  |
| 1173   | No file  | `de8b3a59ef8f`  |
| 1167   | No file  | `de8b3a59ef8f`  |
| 1164   | No file  | `de8b3a59ef8f`  |
| 1156   | No file  | `de8b3a59ef8f`  |
| 1149   | No file  | `de8b3a59ef8f`  |
| 1144   | No file  | `de8b3a59ef8f`  |
| 1137   | No file  | `de8b3a59ef8f`  |
| 1132   | No file  | `de8b3a59ef8f`  |
| 1127   | No file  | `de8b3a59ef8f`  |
| 1122   | No file  | `de8b3a59ef8f`  |
| 1118   | No file  | `de8b3a59ef8f`  |
| 1114   | No file  | `de8b3a59ef8f`  |
| 1109   | No file  | `de8b3a59ef8f`  |
| 1102   | No file  | `de8b3a59ef8f`  |
| 1096   | No file  | `de8b3a59ef8f`  |
| 1088   | No file  | `de8b3a59ef8f`  |
| 1081   | No file  | `de8b3a59ef8f`  |
| 1076   | No file  | `de8b3a59ef8f`  |
| 1069   | No file  | `de8b3a59ef8f`  |
| 1064   | No file  | `de8b3a59ef8f`  |
| 1058   | No file  | `de8b3a59ef8f`  |
| 1051   | No file  | `de8b3a59ef8f`  |
| 1044   | No file  | `de8b3a59ef8f`  |
| 1036   | No file  | `de8b3a59ef8f`  |
| 1026   | No file  | `de8b3a59ef8f`  |
| 1016   | No file  | `de8b3a59ef8f`  |
| 1009   | No file  | `de8b3a59ef8f`  |
| 1005   | No file  | `de8b3a59ef8f`  |
| 1000   | No file  | `de8b3a59ef8f`  |
| 998    | No file  | `de8b3a59ef8f`  |
| 990    | No file  | `de8b3a59ef8f`  |
| 979    | No file  | `de8b3a59ef8f`  |
| 972    | No file  | `de8b3a59ef8f`  |
| 963    | No file  | `de8b3a59ef8f`  |
| 955    | No file  | `de8b3a59ef8f`  |
| 946    | No file  | `de8b3a59ef8f`  |
| 938    | No file  | `de8b3a59ef8f`  |
| 927    | No file  | `de8b3a59ef8f`  |
| 911    | No file  | `de8b3a59ef8f`  |
| 904    | No file  | `de8b3a59ef8f`  |
| 899    | No file  | `de8b3a59ef8f`  |
| 894    | No file  | `de8b3a59ef8f`  |
| 885    | No file  | `de8b3a59ef8f`  |
| 879    | No file  | `de8b3a59ef8f`  |
| 872    | No file  | `de8b3a59ef8f`  |
| 864    | No file  | `de8b3a59ef8f`  |
| 855    | No file  | `de8b3a59ef8f`  |
| 853    | No file  | `de8b3a59ef8f`  |
| 845    | No file  | `de8b3a59ef8f`  |
| 837    | No file  | `de8b3a59ef8f`  |
| 829    | No file  | `de8b3a59ef8f`  |
| 822    | No file  | `de8b3a59ef8f`  |
| 814    | No file  | `de8b3a59ef8f`  |
| 805    | No file  | `de8b3a59ef8f`  |
| 794    | No file  | `de8b3a59ef8f`  |
| 787    | No file  | `de8b3a59ef8f`  |
| 780    | No file  | `de8b3a59ef8f`  |
| 771    | No file  | `de8b3a59ef8f`  |
| 760    | No file  | `de8b3a59ef8f`  |
| 748    | No file  | `de8b3a59ef8f`  |
| 741    | No file  | `de8b3a59ef8f`  |
| 736    | No file  | `de8b3a59ef8f`  |
| 731    | No file  | `de8b3a59ef8f`  |
| 723    | No file  | `de8b3a59ef8f`  |
| 711    | No file  | `de8b3a59ef8f`  |
| 707    | No file  | `de8b3a59ef8f`  |
| 697    | No file  | `de8b3a59ef8f`  |
| 689    | No file  | `de8b3a59ef8f`  |
| 683    | No file  | `de8b3a59ef8f`  |
| 678    | No file  | `de8b3a59ef8f`  |
| 670    | No file  | `de8b3a59ef8f`  |
| 661    | No file  | `de8b3a59ef8f`  |
| 656    | No file  | `de8b3a59ef8f`  |
| 652    | No file  | `de8b3a59ef8f`  |
| 643    | No file  | `de8b3a59ef8f`  |
| 637    | No file  | `de8b3a59ef8f`  |
| 630    | No file  | `de8b3a59ef8f`  |
| 627    | No file  | `de8b3a59ef8f`  |
| 621    | No file  | `de8b3a59ef8f`  |
| 617    | No file  | `de8b3a59ef8f`  |
| 615    | No file  | `de8b3a59ef8f`  |
| 606    | No file  | `de8b3a59ef8f`  |
| 599    | No file  | `de8b3a59ef8f`  |
| 592    | No file  | `de8b3a59ef8f`  |
| 586    | No file  | `de8b3a59ef8f`  |
| 577    | No file  | `de8b3a59ef8f`  |
| 569    | No file  | `de8b3a59ef8f`  |
| 561    | No file  | `de8b3a59ef8f`  |
| 554    | No file  | `de8b3a59ef8f`  |
| 542    | No file  | `de8b3a59ef8f`  |
| 532    | No file  | `de8b3a59ef8f`  |
| 531    | No file  | `de8b3a59ef8f`  |
| 526    | No file  | `de8b3a59ef8f`  |
| 521    | No file  | `de8b3a59ef8f`  |
| 517    | No file  | `de8b3a59ef8f`  |
| 510    | No file  | `de8b3a59ef8f`  |
| 508    | No file  | `de8b3a59ef8f`  |
| 504    | No file  | `de8b3a59ef8f`  |
| 497    | No file  | `de8b3a59ef8f`  |
| 491    | No file  | `de8b3a59ef8f`  |
| 485    | No file  | `de8b3a59ef8f`  |
| 478    | No file  | `de8b3a59ef8f`  |
| 472    | No file  | `de8b3a59ef8f`  |
| 466    | No file  | `de8b3a59ef8f`  |
| 457    | No file  | `de8b3a59ef8f`  |
| 452    | No file  | `de8b3a59ef8f`  |
| 449    | No file  | `de8b3a59ef8f`  |
| 435    | No file  | `de8b3a59ef8f`  |

<!-- versions:end -->

## Companion Files

| File                       | Required | Role                                                                 |
| -------------------------- | -------- | -------------------------------------------------------------------- |
| `eventcategoryoffset.dbss` | Optional | `index -> (data_offset, data_size)` of every row; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 195 bytes + period text)

| Offset                          | Type              | Field                       | Notes                                                       |
| ------------------------------- | ----------------- | --------------------------- | ----------------------------------------------------------- |
| `+0x00`                         | u16               | index                       | Row key; the offset file points here                        |
| `+0x02`                         | i16               | cash_coupon_category_main   | `4` on every row of clients 1784 and 3474                   |
| `+0x04`                         | i16               | cash_coupon_category_middle | `-1` (empty) on every row                                   |
| `+0x06`                         | i16               | cash_coupon_category_small  | `-1` (empty) on every row                                   |
| `+0x08`                         | str16             | discount_start_period       | `YYYY-MM-DD HH:MM`, such as `2021-07-21 09:00`              |
| `discount_start_period+0x00`    | str16             | discount_end_period         | Same form                                                   |
| `discount_end_period+0x00`      | u8                | unknown_discount_end_period_00                  | `1` on every row; `DiscountType` or `SellInPeriod`, see Field Names |
| `discount_end_period+0x01`      | Discount Step[10] | discount_steps              | See Discount Step; unused steps are `0`                     |
| `discount_end_period+0xA1`      | u8                | unknown_discount_end_period_a1                  | `1` on every row; `DiscountType` or `SellInPeriod`, see Field Names |
| `discount_end_period+0xA2`      | i64               | max_discount_pearl          | `10000` on every row                                        |
| `discount_end_period+0xAA`      | u8                | event_type                  | `0`, or `1` on index `2`                                    |

Every row of clients 1784 and 3474 has 16 characters in each period, so
the two unknown bytes sit at row offsets `+0x58` and `+0xF9` there.

### Discount Step (16 bytes)

| Offset  | Type | Field            | Notes                                                           |
| ------- | ---- | ---------------- | --------------------------------------------------------------- |
| `+0x00` | i64  | discount_ceiling | Pearls to spend for this step, rising from step to step         |
| `+0x08` | i64  | discount_price   | The discount at this step; pearls off, or a rate for `getDiscountType()` rate events (`/ 10000` in the Lua) |

### `eventcategoryoffset.dbss`

Bare offset table into `eventcategory.dbss` (no PABR magic, no trailer).

| Offset  | Type              | Field | Notes                                 |
| ------- | ----------------- | ----- | ------------------------------------- |
| `+0x00` | u32               | count | Equals the `eventcategory.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row                        |

### Offset Row (10 bytes)

| Offset  | Type | Field       | Notes                                           |
| ------- | ---- | ----------- | ----------------------------------------------- |
| `+0x00` | u16  | index       | Key of the row it points at                     |
| `+0x02` | u32  | data_offset | Row start, at `index`                           |
| `+0x06` | u32  | data_size   | The whole row: `259` on clients 1784 and 3474   |

Read by `parse_bare_offset_rows()` in `_common/pabr_offset.py`. On clients
1784 and 3474 every index row points at the row with its key.

## Field Names

The names follow the `EventCategory_Table` sheet of a private server's
`DataSheets.bexcel` on client 1784: `Index`, `CashCouponCategory_Main`,
`_Middle`, `_Small`, `DiscountStartPeriod`, `DiscountEndPeriod`,
`EventType`, `DiscountType`, `MaxDiscountPearl`, `SellInPeriod` and
`DiscountCelling0` to `9` with `DiscountPrice0` to `9` (`Celling` sic,
also in the Lua getter `getEventlDiscountCelling`). Its 4 rows match the
file on all 4 keys and every value: categories `4`, empty, empty; both
periods; `EventType` `1` only on index `2`; `MaxDiscountPearl` `10000`; the
three or five filled steps. Client 1784 and client 3474 have the same file,
byte for byte.

The client 1784 server dump (`Instance_dumpFull.exe`) reads the sheet in
the function at VA `0x1408cc5d0`: the three categories into u16 members,
`EventType` and `DiscountType` into bytes, `SellInPeriod` into a bool,
`MaxDiscountPearl` widened to an i64 and the ten steps into 20 i64. Its
row order differs from the file's, so it does not tell which of the two
bytes that are `1` on every row (`unknown_discount_end_period_00`, `unknown_discount_end_period_a1`) is
`DiscountType` and which `SellInPeriod`.

## Open Questions

### The Two Bytes After the Periods

`DiscountType` and `SellInPeriod` are both `1` on all 4 rows of the sheet,
and so are the two bytes. A row with a rate discount (the Lua's
`eEventCartDiscountType_Rate`) or one outside its sell period would tell
them apart; neither client has one.
