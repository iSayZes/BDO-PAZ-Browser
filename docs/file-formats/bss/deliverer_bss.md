# `deliverer.bss` Format

## Purpose

The wagons and ships that carry goods between towns for the Transport
window and drive along their routes on the world map: one row per carrier
character with its route number, load, fee, world map model, the names of
up to 20 route waypoints and its `CppEnums.DelivererType`. The world map
Lua (`new_worldmap_actortooltip.luac`) reads the type from a carrier icon
through `FromClient_getDelivererType()` and opens no cargo window for a
`WagonForPerson` or `OfferingCarrier`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File            | Bytes | Records | Row bytes |
| ------ | -------------- | --------------- | ----- | ------- | --------- |
| 2      | 2429 and later | `deliverer.bss` | 7,497 | 27 Row  | 106       |
| 1      | 805 to 2421    | `deliverer.bss` | 6,718 | 24 Row  | 104       |

| Layout | File            | Known            | Unknown     |
| ------ | --------------- | ---------------- | ----------- |
| 2      | `deliverer.bss` | 7,470 B (99.6%)  | 27 B (0.4%) |
| 1      | `deliverer.bss` | 6,718 B (100.0%) | 0 B (0.0%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `e4b2ae8c696e`  |
| 3482   | Layout 2             | `e4b2ae8c696e`  |
| 3474   | Layout 2             | `e4b2ae8c696e`  |
| 3473   | Layout 2             | `e4b2ae8c696e`  |
| 3464   | Layout 2             | `e4b2ae8c696e`  |
| 3458   | Layout 2             | `e4b2ae8c696e`  |
| 3454   | Layout 2             | `e4b2ae8c696e`  |
| 3444   | Layout 2             | `e4b2ae8c696e`  |
| 3435   | Layout 2             | `e4b2ae8c696e`  |
| 3426   | Layout 2             | `e4b2ae8c696e`  |
| 3418   | Layout 2             | `e4b2ae8c696e`  |
| 3412   | Layout 2             | `e4b2ae8c696e`  |
| 3402   | Layout 2             | `e4b2ae8c696e`  |
| 3396   | Layout 2             | `e4b2ae8c696e`  |
| 3387   | Layout 2             | `e4b2ae8c696e`  |
| 3381   | Layout 2             | `e4b2ae8c696e`  |
| 3373   | Layout 2             | `e4b2ae8c696e`  |
| 3364   | Layout 2             | `e4b2ae8c696e`  |
| 3356   | Layout 2             | `e4b2ae8c696e`  |
| 3349   | Layout 2             | `e4b2ae8c696e`  |
| 3342   | Layout 2             | `e4b2ae8c696e`  |
| 3335   | Layout 2             | `e4b2ae8c696e`  |
| 3326   | Layout 2             | `e4b2ae8c696e`  |
| 3321   | Layout 2             | `e4b2ae8c696e`  |
| 3314   | Layout 2             | `e4b2ae8c696e`  |
| 3303   | Layout 2             | `e4b2ae8c696e`  |
| 3302   | Layout 2             | `e4b2ae8c696e`  |
| 3293   | Layout 2             | `e4b2ae8c696e`  |
| 3283   | Layout 2             | `e4b2ae8c696e`  |
| 3275   | Layout 2             | `e4b2ae8c696e`  |
| 3267   | Layout 2             | `e4b2ae8c696e`  |
| 3258   | Layout 2             | `e4b2ae8c696e`  |
| 3251   | Layout 2             | `e4b2ae8c696e`  |
| 3242   | Layout 2             | `e4b2ae8c696e`  |
| 3235   | Layout 2             | `e4b2ae8c696e`  |
| 3229   | Layout 2             | `e4b2ae8c696e`  |
| 3212   | Layout 2             | `e4b2ae8c696e`  |
| 3203   | Layout 2             | `e4b2ae8c696e`  |
| 3193   | Layout 2             | `e4b2ae8c696e`  |
| 3186   | Layout 2             | `e4b2ae8c696e`  |
| 3177   | Layout 2             | `e4b2ae8c696e`  |
| 3169   | Layout 2             | `e4b2ae8c696e`  |
| 3158   | Layout 2             | `e4b2ae8c696e`  |
| 3151   | Layout 2             | `e4b2ae8c696e`  |
| 3144   | Layout 2             | `e4b2ae8c696e`  |
| 3133   | Layout 2             | `e4b2ae8c696e`  |
| 3125   | Layout 2             | `e4b2ae8c696e`  |
| 3118   | Layout 2             | `e4b2ae8c696e`  |
| 3111   | Layout 2             | `e4b2ae8c696e`  |
| 3103   | Layout 2             | `e4b2ae8c696e`  |
| 3095   | Layout 2             | `e4b2ae8c696e`  |
| 3086   | Layout 2             | `e4b2ae8c696e`  |
| 3072   | Layout 2             | `e4b2ae8c696e`  |
| 3062   | Layout 2             | `e4b2ae8c696e`  |
| 3052   | Layout 2             | `e4b2ae8c696e`  |
| 3045   | Layout 2             | `e4b2ae8c696e`  |
| 3037   | Layout 2             | `e4b2ae8c696e`  |
| 3030   | Layout 2             | `e4b2ae8c696e`  |
| 3021   | Layout 2             | `e4b2ae8c696e`  |
| 3012   | Layout 2             | `e4b2ae8c696e`  |
| 3002   | Layout 2             | `e4b2ae8c696e`  |
| 2995   | Layout 2             | `e4b2ae8c696e`  |
| 2987   | Layout 2             | `e4b2ae8c696e`  |
| 2978   | Layout 2             | `e4b2ae8c696e`  |
| 2970   | Layout 2             | `e4b2ae8c696e`  |
| 2959   | Layout 2             | `e4b2ae8c696e`  |
| 2951   | Layout 2             | `e4b2ae8c696e`  |
| 2942   | Layout 2             | `e4b2ae8c696e`  |
| 2935   | Layout 2             | `e4b2ae8c696e`  |
| 2932   | Layout 2             | `e4b2ae8c696e`  |
| 2923   | Layout 2             | `e4b2ae8c696e`  |
| 2919   | Layout 2             | `e4b2ae8c696e`  |
| 2907   | Layout 2             | `e4b2ae8c696e`  |
| 2900   | Layout 2             | `e4b2ae8c696e`  |
| 2891   | Layout 2             | `e4b2ae8c696e`  |
| 2882   | Layout 2             | `e4b2ae8c696e`  |
| 2872   | Layout 2             | `e4b2ae8c696e`  |
| 2863   | Layout 2             | `e4b2ae8c696e`  |
| 2855   | Layout 2             | `e4b2ae8c696e`  |
| 2849   | Layout 2             | `e4b2ae8c696e`  |
| 2844   | Layout 2             | `e4b2ae8c696e`  |
| 2834   | Layout 2             | `e4b2ae8c696e`  |
| 2825   | Layout 2             | `e4b2ae8c696e`  |
| 2819   | Layout 2             | `e4b2ae8c696e`  |
| 2811   | Layout 2             | `e4b2ae8c696e`  |
| 2803   | Layout 2             | `e4b2ae8c696e`  |
| 2794   | Layout 2             | `e4b2ae8c696e`  |
| 2783   | Layout 2             | `e4b2ae8c696e`  |
| 2774   | Layout 2             | `e4b2ae8c696e`  |
| 2765   | Layout 2             | `e4b2ae8c696e`  |
| 2756   | Layout 2             | `e4b2ae8c696e`  |
| 2750   | Layout 2             | `e4b2ae8c696e`  |
| 2743   | Layout 2             | `e4b2ae8c696e`  |
| 2736   | Layout 2             | `e4b2ae8c696e`  |
| 2726   | Layout 2             | `e4b2ae8c696e`  |
| 2717   | Layout 2             | `e4b2ae8c696e`  |
| 2709   | Layout 2             | `e4b2ae8c696e`  |
| 2703   | Layout 2             | `e4b2ae8c696e`  |
| 2695   | Layout 2             | `e4b2ae8c696e`  |
| 2684   | Layout 2             | `e4b2ae8c696e`  |
| 2672   | Layout 2             | `e4b2ae8c696e`  |
| 2665   | Layout 2             | `e4b2ae8c696e`  |
| 2657   | Layout 2             | `e4b2ae8c696e`  |
| 2649   | Layout 2             | `e4b2ae8c696e`  |
| 2644   | Layout 2             | `e4b2ae8c696e`  |
| 2637   | Layout 2             | `e4b2ae8c696e`  |
| 2629   | Layout 2             | `e4b2ae8c696e`  |
| 2619   | Layout 2             | `e4b2ae8c696e`  |
| 2612   | Layout 2             | `e4b2ae8c696e`  |
| 2606   | Layout 2             | `e4b2ae8c696e`  |
| 2602   | Layout 2             | `e4b2ae8c696e`  |
| 2601   | Layout 2             | `e4b2ae8c696e`  |
| 2592   | Layout 2             | `e4b2ae8c696e`  |
| 2583   | Layout 2             | `e4b2ae8c696e`  |
| 2575   | Layout 2             | `e4b2ae8c696e`  |
| 2567   | Layout 2             | `e4b2ae8c696e`  |
| 2560   | Layout 2             | `e4b2ae8c696e`  |
| 2553   | Layout 2             | `e4b2ae8c696e`  |
| 2545   | Layout 2             | `e4b2ae8c696e`  |
| 2538   | Layout 2             | `e4b2ae8c696e`  |
| 2529   | Layout 2             | `e4b2ae8c696e`  |
| 2519   | Layout 2             | `e4b2ae8c696e`  |
| 2513   | Layout 2             | `e4b2ae8c696e`  |
| 2510   | Layout 2             | `e4b2ae8c696e`  |
| 2507   | Layout 2             | `e4b2ae8c696e`  |
| 2503   | Layout 2             | `e4b2ae8c696e`  |
| 2498   | Layout 2             | `e4b2ae8c696e`  |
| 2492   | Layout 2             | `e4b2ae8c696e`  |
| 2487   | Layout 2             | `e4b2ae8c696e`  |
| 2480   | Layout 2             | `e4b2ae8c696e`  |
| 2474   | Layout 2             | `e4b2ae8c696e`  |
| 2468   | Layout 2             | `e4b2ae8c696e`  |
| 2460   | Layout 2             | `e4b2ae8c696e`  |
| 2453   | Layout 2             | `e4b2ae8c696e`  |
| 2444   | Layout 2             | `e4b2ae8c696e`  |
| 2438   | Layout 2             | `e4b2ae8c696e`  |
| 2434   | Layout 2             | `e4b2ae8c696e`  |
| 2429   | Layout 2             | `e4b2ae8c696e`  |
| 2421   | Layout 1             | `e4b2ae8c696e`  |
| 2414   | Layout 1             | `e4b2ae8c696e`  |
| 2407   | Layout 1             | `e4b2ae8c696e`  |
| 2401   | Layout 1             | `e4b2ae8c696e`  |
| 2397   | Layout 1             | `e4b2ae8c696e`  |
| 2393   | Layout 1             | `e4b2ae8c696e`  |
| 2384   | Layout 1             | `e4b2ae8c696e`  |
| 2378   | Layout 1             | `e4b2ae8c696e`  |
| 2372   | Layout 1             | `e4b2ae8c696e`  |
| 2358   | Layout 1             | `e4b2ae8c696e`  |
| 2352   | Layout 1             | `e4b2ae8c696e`  |
| 2347   | Layout 1             | `e4b2ae8c696e`  |
| 2343   | Layout 1             | `e4b2ae8c696e`  |
| 2335   | Layout 1             | `e4b2ae8c696e`  |
| 2327   | Layout 1             | `e4b2ae8c696e`  |
| 2324   | Layout 1             | `e4b2ae8c696e`  |
| 2319   | Layout 1             | `e4b2ae8c696e`  |
| 2313   | Layout 1             | `e4b2ae8c696e`  |
| 2308   | Layout 1             | `e4b2ae8c696e`  |
| 2302   | Layout 1             | `e4b2ae8c696e`  |
| 2295   | Layout 1             | `e4b2ae8c696e`  |
| 2290   | Layout 1             | `e4b2ae8c696e`  |
| 2284   | Layout 1             | `e4b2ae8c696e`  |
| 2276   | Layout 1             | `e4b2ae8c696e`  |
| 2269   | Layout 1             | `e4b2ae8c696e`  |
| 2259   | Layout 1             | `e4b2ae8c696e`  |
| 2250   | Layout 1             | `e4b2ae8c696e`  |
| 2243   | Layout 1             | `e4b2ae8c696e`  |
| 2235   | Layout 1             | `e4b2ae8c696e`  |
| 2229   | Layout 1             | `e4b2ae8c696e`  |
| 2224   | Layout 1             | `e4b2ae8c696e`  |
| 2218   | Layout 1             | `e4b2ae8c696e`  |
| 2215   | Layout 1             | `e4b2ae8c696e`  |
| 2207   | Layout 1             | `e4b2ae8c696e`  |
| 2203   | Layout 1             | `e4b2ae8c696e`  |
| 2196   | Layout 1             | `e4b2ae8c696e`  |
| 2192   | Layout 1             | `e4b2ae8c696e`  |
| 2189   | Layout 1             | `e4b2ae8c696e`  |
| 2183   | Layout 1             | `e4b2ae8c696e`  |
| 2179   | Layout 1             | `e4b2ae8c696e`  |
| 2171   | Layout 1             | `e4b2ae8c696e`  |
| 2163   | Layout 1             | `e4b2ae8c696e`  |
| 2156   | Layout 1             | `e4b2ae8c696e`  |
| 2151   | Layout 1             | `e4b2ae8c696e`  |
| 2147   | Layout 1             | `e4b2ae8c696e`  |
| 2142   | Layout 1             | `e4b2ae8c696e`  |
| 2138   | Layout 1             | `e4b2ae8c696e`  |
| 2134   | Layout 1             | `e4b2ae8c696e`  |
| 2130   | Layout 1             | `e4b2ae8c696e`  |
| 2122   | Layout 1             | `e4b2ae8c696e`  |
| 2107   | Layout 1             | `e4b2ae8c696e`  |
| 2098   | Layout 1             | `e4b2ae8c696e`  |
| 2089   | Layout 1             | `e4b2ae8c696e`  |
| 2081   | Layout 1             | `e4b2ae8c696e`  |
| 2073   | Layout 1             | `e4b2ae8c696e`  |
| 2067   | Layout 1             | `e4b2ae8c696e`  |
| 2063   | Layout 1             | `e4b2ae8c696e`  |
| 2059   | Layout 1             | `e4b2ae8c696e`  |
| 2052   | Layout 1             | `e4b2ae8c696e`  |
| 2044   | Layout 1             | `e4b2ae8c696e`  |
| 2039   | Layout 1             | `e4b2ae8c696e`  |
| 2032   | Layout 1             | `e4b2ae8c696e`  |
| 2025   | Layout 1             | `e4b2ae8c696e`  |
| 2011   | Layout 1             | `e4b2ae8c696e`  |
| 2005   | Layout 1             | `e4b2ae8c696e`  |
| 2000   | Layout 1             | `e4b2ae8c696e`  |
| 1996   | Layout 1             | `e4b2ae8c696e`  |
| 1991   | Layout 1             | `e4b2ae8c696e`  |
| 1985   | Layout 1             | `e4b2ae8c696e`  |
| 1980   | Layout 1             | `e4b2ae8c696e`  |
| 1969   | Layout 1             | `e4b2ae8c696e`  |
| 1964   | Layout 1             | `e4b2ae8c696e`  |
| 1958   | Layout 1             | `e4b2ae8c696e`  |
| 1950   | Layout 1             | `e4b2ae8c696e`  |
| 1945   | Layout 1             | `e4b2ae8c696e`  |
| 1937   | Layout 1             | `e4b2ae8c696e`  |
| 1933   | Layout 1             | `e4b2ae8c696e`  |
| 1927   | Layout 1             | `e4b2ae8c696e`  |
| 1921   | Layout 1             | `e4b2ae8c696e`  |
| 1914   | Layout 1             | `e4b2ae8c696e`  |
| 1908   | Layout 1             | `e4b2ae8c696e`  |
| 1897   | Layout 1             | `e4b2ae8c696e`  |
| 1892   | Layout 1             | `e4b2ae8c696e`  |
| 1886   | Layout 1             | `e4b2ae8c696e`  |
| 1881   | Layout 1             | `e4b2ae8c696e`  |
| 1871   | Layout 1             | `e4b2ae8c696e`  |
| 1866   | Layout 1             | `e4b2ae8c696e`  |
| 1862   | Layout 1             | `e4b2ae8c696e`  |
| 1854   | Layout 1             | `e4b2ae8c696e`  |
| 1846   | Layout 1             | `e4b2ae8c696e`  |
| 1838   | Layout 1             | `e4b2ae8c696e`  |
| 1832   | Layout 1             | `e4b2ae8c696e`  |
| 1826   | Layout 1             | `e4b2ae8c696e`  |
| 1822   | Layout 1             | `e4b2ae8c696e`  |
| 1818   | Layout 1             | `e4b2ae8c696e`  |
| 1804   | Layout 1             | `e4b2ae8c696e`  |
| 1794   | Layout 1             | `e4b2ae8c696e`  |
| 1790   | Layout 1             | `e4b2ae8c696e`  |
| 1784   | Layout 1             | `e4b2ae8c696e`  |
| 1774   | Layout 1             | `e4b2ae8c696e`  |
| 1771   | Layout 1             | `e4b2ae8c696e`  |
| 1762   | Layout 1             | `e4b2ae8c696e`  |
| 1759   | Layout 1             | `e4b2ae8c696e`  |
| 1754   | Layout 1             | `e4b2ae8c696e`  |
| 1749   | Layout 1             | `e4b2ae8c696e`  |
| 1743   | Layout 1             | `e4b2ae8c696e`  |
| 1737   | Layout 1             | `e4b2ae8c696e`  |
| 1731   | Layout 1             | `e4b2ae8c696e`  |
| 1725   | Layout 1             | `e4b2ae8c696e`  |
| 1717   | Layout 1             | `e4b2ae8c696e`  |
| 1710   | Layout 1             | `e4b2ae8c696e`  |
| 1704   | Layout 1             | `e4b2ae8c696e`  |
| 1698   | Layout 1             | `e4b2ae8c696e`  |
| 1690   | Layout 1             | `e4b2ae8c696e`  |
| 1685   | Layout 1             | `e4b2ae8c696e`  |
| 1680   | Layout 1             | `e4b2ae8c696e`  |
| 1674   | Layout 1             | `e4b2ae8c696e`  |
| 1668   | Layout 1             | `e4b2ae8c696e`  |
| 1659   | Layout 1             | `e4b2ae8c696e`  |
| 1649   | Layout 1             | `e4b2ae8c696e`  |
| 1642   | Layout 1             | `e4b2ae8c696e`  |
| 1636   | Layout 1             | `e4b2ae8c696e`  |
| 1628   | Layout 1             | `e4b2ae8c696e`  |
| 1622   | Layout 1             | `e4b2ae8c696e`  |
| 1614   | Layout 1             | `e4b2ae8c696e`  |
| 1608   | Layout 1             | `e4b2ae8c696e`  |
| 1602   | Layout 1             | `e4b2ae8c696e`  |
| 1598   | Layout 1             | `e4b2ae8c696e`  |
| 1594   | Layout 1             | `e4b2ae8c696e`  |
| 1590   | Layout 1             | `e4b2ae8c696e`  |
| 1587   | Layout 1             | `e4b2ae8c696e`  |
| 1584   | Layout 1             | `e4b2ae8c696e`  |
| 1579   | Layout 1             | `e4b2ae8c696e`  |
| 1572   | Layout 1             | `e4b2ae8c696e`  |
| 1565   | Layout 1             | `e4b2ae8c696e`  |
| 1559   | Layout 1             | `e4b2ae8c696e`  |
| 1554   | Layout 1             | `e4b2ae8c696e`  |
| 1547   | Layout 1             | `e4b2ae8c696e`  |
| 1537   | Layout 1             | `e4b2ae8c696e`  |
| 1529   | Layout 1             | `e4b2ae8c696e`  |
| 1524   | Layout 1             | `e4b2ae8c696e`  |
| 1519   | Layout 1             | `e4b2ae8c696e`  |
| 1509   | Layout 1             | `e4b2ae8c696e`  |
| 1506   | Layout 1             | `e4b2ae8c696e`  |
| 1504   | Layout 1             | `e4b2ae8c696e`  |
| 1500   | Layout 1             | `e4b2ae8c696e`  |
| 1493   | Layout 1             | `e4b2ae8c696e`  |
| 1489   | Layout 1             | `e4b2ae8c696e`  |
| 1485   | Layout 1             | `e4b2ae8c696e`  |
| 1481   | Layout 1             | `e4b2ae8c696e`  |
| 1474   | Layout 1             | `e4b2ae8c696e`  |
| 1466   | Layout 1             | `e4b2ae8c696e`  |
| 1462   | Layout 1             | `e4b2ae8c696e`  |
| 1459   | Layout 1             | `e4b2ae8c696e`  |
| 1453   | Layout 1             | `e4b2ae8c696e`  |
| 1450   | Layout 1             | `e4b2ae8c696e`  |
| 1445   | Layout 1             | `e4b2ae8c696e`  |
| 1439   | Layout 1             | `e4b2ae8c696e`  |
| 1433   | Layout 1             | `e4b2ae8c696e`  |
| 1430   | Layout 1             | `e4b2ae8c696e`  |
| 1426   | Layout 1             | `e4b2ae8c696e`  |
| 1421   | Layout 1             | `e4b2ae8c696e`  |
| 1417   | Layout 1             | `e4b2ae8c696e`  |
| 1416   | Layout 1             | `e4b2ae8c696e`  |
| 1409   | Layout 1             | `e4b2ae8c696e`  |
| 1405   | Layout 1             | `e4b2ae8c696e`  |
| 1401   | Layout 1             | `e4b2ae8c696e`  |
| 1396   | Layout 1             | `e4b2ae8c696e`  |
| 1391   | Layout 1             | `e4b2ae8c696e`  |
| 1390   | Layout 1             | `e4b2ae8c696e`  |
| 1386   | Layout 1             | `e4b2ae8c696e`  |
| 1381   | Layout 1             | `e4b2ae8c696e`  |
| 1379   | Layout 1             | `e4b2ae8c696e`  |
| 1372   | Layout 1             | `e4b2ae8c696e`  |
| 1366   | Layout 1             | `e4b2ae8c696e`  |
| 1364   | Layout 1             | `e4b2ae8c696e`  |
| 1363   | Layout 1             | `e4b2ae8c696e`  |
| 1360   | Layout 1             | `e4b2ae8c696e`  |
| 1358   | Layout 1             | `e4b2ae8c696e`  |
| 1355   | Layout 1             | `e4b2ae8c696e`  |
| 1351   | Layout 1             | `e4b2ae8c696e`  |
| 1348   | Layout 1             | `e4b2ae8c696e`  |
| 1346   | Layout 1             | `e4b2ae8c696e`  |
| 1341   | Layout 1             | `e4b2ae8c696e`  |
| 1340   | Layout 1             | `e4b2ae8c696e`  |
| 1338   | Layout 1             | `e4b2ae8c696e`  |
| 1335   | Layout 1             | `e4b2ae8c696e`  |
| 1333   | Layout 1             | `e4b2ae8c696e`  |
| 1329   | Layout 1             | `e4b2ae8c696e`  |
| 1327   | Layout 1             | `e4b2ae8c696e`  |
| 1324   | Layout 1             | `e4b2ae8c696e`  |
| 1321   | Layout 1             | `e4b2ae8c696e`  |
| 1319   | Layout 1             | `e4b2ae8c696e`  |
| 1318   | Layout 1             | `e4b2ae8c696e`  |
| 1316   | Layout 1             | `e4b2ae8c696e`  |
| 1313   | Layout 1             | `e4b2ae8c696e`  |
| 1311   | Layout 1             | `e4b2ae8c696e`  |
| 1309   | Layout 1             | `e4b2ae8c696e`  |
| 1304   | Layout 1             | `e4b2ae8c696e`  |
| 1292   | Layout 1             | `e4b2ae8c696e`  |
| 1286   | Layout 1             | `e4b2ae8c696e`  |
| 1280   | Layout 1             | `e4b2ae8c696e`  |
| 1276   | Layout 1             | `e4b2ae8c696e`  |
| 1267   | Layout 1             | `e4b2ae8c696e`  |
| 1261   | Layout 1             | `e4b2ae8c696e`  |
| 1256   | Layout 1             | `e4b2ae8c696e`  |
| 1250   | Layout 1             | `e4b2ae8c696e`  |
| 1246   | Layout 1             | `e4b2ae8c696e`  |
| 1239   | Layout 1             | `e4b2ae8c696e`  |
| 1230   | Layout 1             | `e4b2ae8c696e`  |
| 1226   | Layout 1             | `e4b2ae8c696e`  |
| 1220   | Layout 1             | `e4b2ae8c696e`  |
| 1217   | Layout 1             | `e4b2ae8c696e`  |
| 1211   | Layout 1             | `e4b2ae8c696e`  |
| 1210   | Layout 1             | `e4b2ae8c696e`  |
| 1208   | Layout 1             | `e4b2ae8c696e`  |
| 1203   | Layout 1             | `e4b2ae8c696e`  |
| 1197   | Layout 1             | `e4b2ae8c696e`  |
| 1194   | Layout 1             | `e4b2ae8c696e`  |
| 1192   | Layout 1             | `e4b2ae8c696e`  |
| 1187   | Layout 1             | `e4b2ae8c696e`  |
| 1183   | Layout 1             | `e4b2ae8c696e`  |
| 1177   | Layout 1             | `e4b2ae8c696e`  |
| 1173   | Layout 1             | `e4b2ae8c696e`  |
| 1167   | Layout 1             | `e4b2ae8c696e`  |
| 1164   | Layout 1             | `e4b2ae8c696e`  |
| 1156   | Layout 1             | `e4b2ae8c696e`  |
| 1149   | Layout 1             | `e4b2ae8c696e`  |
| 1144   | Layout 1             | `e4b2ae8c696e`  |
| 1137   | Layout 1             | `e4b2ae8c696e`  |
| 1132   | Layout 1             | `e4b2ae8c696e`  |
| 1127   | Layout 1             | `e4b2ae8c696e`  |
| 1122   | Layout 1             | `e4b2ae8c696e`  |
| 1118   | Layout 1             | `e4b2ae8c696e`  |
| 1114   | Layout 1             | `e4b2ae8c696e`  |
| 1109   | Layout 1             | `e4b2ae8c696e`  |
| 1102   | Layout 1             | `e4b2ae8c696e`  |
| 1096   | Layout 1             | `e4b2ae8c696e`  |
| 1088   | Layout 1             | `e4b2ae8c696e`  |
| 1081   | Layout 1             | `e4b2ae8c696e`  |
| 1076   | Layout 1             | `e4b2ae8c696e`  |
| 1069   | Layout 1             | `e4b2ae8c696e`  |
| 1064   | Layout 1             | `e4b2ae8c696e`  |
| 1058   | Layout 1             | `e4b2ae8c696e`  |
| 1051   | Layout 1             | `e4b2ae8c696e`  |
| 1044   | Layout 1             | `e4b2ae8c696e`  |
| 1036   | Layout 1             | `e4b2ae8c696e`  |
| 1026   | Layout 1             | `e4b2ae8c696e`  |
| 1016   | Layout 1             | `e4b2ae8c696e`  |
| 1009   | Layout 1             | `e4b2ae8c696e`  |
| 1005   | Layout 1             | `e4b2ae8c696e`  |
| 1000   | Layout 1             | `e4b2ae8c696e`  |
| 998    | Layout 1             | `e4b2ae8c696e`  |
| 990    | Layout 1             | `e4b2ae8c696e`  |
| 979    | Layout 1             | `e4b2ae8c696e`  |
| 972    | Layout 1             | `e4b2ae8c696e`  |
| 963    | Layout 1             | `e4b2ae8c696e`  |
| 955    | Layout 1             | `e4b2ae8c696e`  |
| 946    | Layout 1             | `e4b2ae8c696e`  |
| 938    | Layout 1             | `e4b2ae8c696e`  |
| 927    | Layout 1             | `e4b2ae8c696e`  |
| 911    | Layout 1             | `e4b2ae8c696e`  |
| 904    | Layout 1             | `e4b2ae8c696e`  |
| 899    | Layout 1             | `e4b2ae8c696e`  |
| 894    | Layout 1             | `e4b2ae8c696e`  |
| 885    | Layout 1             | `e4b2ae8c696e`  |
| 879    | Layout 1             | `e4b2ae8c696e`  |
| 872    | Layout 1             | `e4b2ae8c696e`  |
| 864    | Layout 1             | `e4b2ae8c696e`  |
| 855    | Layout 1             | `e4b2ae8c696e`  |
| 853    | Layout 1             | `e4b2ae8c696e`  |
| 845    | Layout 1             | `e4b2ae8c696e`  |
| 837    | Layout 1             | `e4b2ae8c696e`  |
| 829    | Layout 1             | `e4b2ae8c696e`  |
| 822    | Layout 1             | `e4b2ae8c696e`  |
| 814    | Layout 1             | `e4b2ae8c696e`  |
| 805    | Layout 1             | `e4b2ae8c696e`  |
| 794    | No documented layout | `e4b2ae8c696e`  |
| 787    | No documented layout | `e4b2ae8c696e`  |
| 780    | No documented layout | `e4b2ae8c696e`  |
| 771    | No documented layout | `e4b2ae8c696e`  |
| 760    | No documented layout | `e4b2ae8c696e`  |
| 748    | No documented layout | `e4b2ae8c696e`  |
| 741    | No documented layout | `e4b2ae8c696e`  |
| 736    | No documented layout | `e4b2ae8c696e`  |
| 731    | No documented layout | `e4b2ae8c696e`  |
| 723    | No documented layout | `e4b2ae8c696e`  |
| 711    | No documented layout | `e4b2ae8c696e`  |
| 707    | No documented layout | `e4b2ae8c696e`  |
| 697    | No documented layout | `e4b2ae8c696e`  |
| 689    | No documented layout | `e4b2ae8c696e`  |
| 683    | No documented layout | `e4b2ae8c696e`  |
| 678    | No documented layout | `e4b2ae8c696e`  |
| 670    | No documented layout | `e4b2ae8c696e`  |
| 661    | No documented layout | `e4b2ae8c696e`  |
| 656    | No documented layout | `e4b2ae8c696e`  |
| 652    | No documented layout | `e4b2ae8c696e`  |
| 643    | No documented layout | `e4b2ae8c696e`  |
| 637    | No documented layout | `e4b2ae8c696e`  |
| 630    | No documented layout | `e4b2ae8c696e`  |
| 627    | No documented layout | `e4b2ae8c696e`  |
| 621    | No documented layout | `e4b2ae8c696e`  |
| 617    | No documented layout | `e4b2ae8c696e`  |
| 615    | No documented layout | `e4b2ae8c696e`  |
| 606    | No documented layout | `e4b2ae8c696e`  |
| 599    | No documented layout | `e4b2ae8c696e`  |
| 592    | No documented layout | `e4b2ae8c696e`  |
| 586    | No documented layout | `e4b2ae8c696e`  |
| 577    | No documented layout | `e4b2ae8c696e`  |
| 569    | No documented layout | `e4b2ae8c696e`  |
| 561    | No documented layout | `e4b2ae8c696e`  |
| 554    | No documented layout | `e4b2ae8c696e`  |
| 542    | No documented layout | `e4b2ae8c696e`  |
| 532    | No documented layout | `e4b2ae8c696e`  |
| 531    | No documented layout | `e4b2ae8c696e`  |
| 526    | No documented layout | `e4b2ae8c696e`  |
| 521    | No documented layout | `e4b2ae8c696e`  |
| 517    | No documented layout | `e4b2ae8c696e`  |
| 510    | No documented layout | `e4b2ae8c696e`  |
| 508    | No documented layout | `e4b2ae8c696e`  |
| 504    | No documented layout | `e4b2ae8c696e`  |
| 497    | No documented layout | `e4b2ae8c696e`  |
| 491    | No documented layout | `e4b2ae8c696e`  |
| 485    | No documented layout | `e4b2ae8c696e`  |
| 478    | No documented layout | `e4b2ae8c696e`  |
| 472    | No documented layout | `e4b2ae8c696e`  |
| 466    | No documented layout | `e4b2ae8c696e`  |
| 457    | No documented layout | `e4b2ae8c696e`  |
| 452    | No documented layout | `e4b2ae8c696e`  |
| 449    | No documented layout | `e4b2ae8c696e`  |
| 435    | No documented layout | `e4b2ae8c696e`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                            |
| ---------------------------- | -------- | ------------------------------------------------------------------------------- |
| `characterstaticoffset.dbss` | Optional | The `characterstatic.dbss` keys, so a carrier key without a row shows as plain text |
| `languagedata_en.loc`        | Optional | Carrier names, LOC type 6                                                       |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of carriers                            |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (106 bytes)

| Offset  | Type    | Field                 | Notes                                                                                     |
| ------- | ------- | --------------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u16     | character_key         | Carrier character (LOC type 6 name, `522` Velia Freight Wagon); the rows are in no key order |
| `+0x02` | u16     | character_key_dup     | Equals `character_key` on every row                                                       |
| `+0x04` | u32     | delivery_route        | Route number, `1` to `34` on client 3482; the Altinova (`791`) and O'dyllita (`809`) Freight Wagons share `25` |
| `+0x08` | u32     | load_age              | `30` on every row of clients 1784 and 3482                                                |
| `+0x0C` | i64     | fee                   | `10` on every row of clients 1784 and 3482                                                |
| `+0x14` | u32     | object_file_index     | Index into `strings`: the world map model (`WorldMap/WorldMap_Cart.pam`)                  |
| `+0x18` | u32[20] | waypoint_name_indexes | Indexes into `strings`: waypoint names along the route (`loopline_1`); an unused slot points at an empty string |
| `+0x68` | u8      | deliverer_type        | `CppEnums.DelivererType`; see Deliverer Type                                              |
| `+0x69` | u8      | unknown_69            | `0` on every row of client 3482                                                           |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                                   |
| ------- | ------------------ | ------------ | ----------------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                                                       |
| `+0x04` | pstr[string_count] | strings      | Model paths and waypoint names, UTF-16LE; a string several rows use is stored once |

## Layout 1

No `deliverer_type` and `unknown_69` at the end of the row. Only the Row
differs from Layout 2.

### Row (104 bytes)

| Offset  | Type    | Field                 | Notes |
| ------- | ------- | --------------------- | ----- |
| `+0x00` | u16     | character_key         |       |
| `+0x02` | u16     | character_key_dup     |       |
| `+0x04` | u32     | delivery_route        |       |
| `+0x08` | u32     | load_age              |       |
| `+0x0C` | i64     | fee                   |       |
| `+0x14` | u32     | object_file_index     |       |
| `+0x18` | u32[20] | waypoint_name_indexes |       |

## Deliverer Type

`CppEnums.DelivererType` of the client 3482 Lua
(`global_define_cpp_enum.luac`). Rows on client 3482 in the last column;
the type follows the model on every row but two `WoodenBoat_small` ships.

| Value | Name            | Models (client 3482)                                  | Rows (client 3482) |
| ----- | --------------- | ----------------------------------------------------- | ------------------ |
| 0     | NotDeliverer    |                                                       | 0                  |
| 1     | Wagon           | `WorldMap_Cart.pam`                                   | 13                 |
| 2     | TransportShip   | `WorldMap_WoodenBoat_small.pam`                       | 2                  |
| 3     | TradingShip     | `WorldMap_SailingShip.pam`, `Worldmap_R0001_ShipM.pam`, `WorldMap_WoodenBoat_small.pam` | 10 |
| 4     | WagonForPerson  |                                                       | 0                  |
| 5     | OfferingCarrier | `WorldMap_Cartgold.pam` (the Velia and Heidel Tribute Wagons) | 2          |

## Field Names

The 2016 `gc::DelivererStaticStatus` holds `_characterKey`,
`_deliveryRoute`, `_loadAge`, `_fee`, `_waypointNameList` (20 strings),
`_waypointList` (resolved, not stored) and `_objectFile`; the file stores
the object file before the waypoint names. The `Carriage_Table` sheet of a
private server's `DataSheets.bexcel` on client 1784 has the columns
`CharacterKey`, `Loadage`, `Price`, `MoveSpeed`, `Way Index`,
`WaypointName0` to `WaypointName19`, `Waypoint0` to `Waypoint19`,
`ObjectName` and `ContentsGroupKey`, 23 rows. `MoveSpeed`, the waypoint
numbers and the contents groups have no field.

| Field                 | Column                      | Same value (client 1784) | Same value (client 3482) |
| --------------------- | --------------------------- | ------------------------ | ------------------------ |
| character_key         | `CharacterKey`              | 20 of 20                 | 21 of 21                 |
| delivery_route        | `Way Index`                 | 20 of 20                 | 21 of 21                 |
| load_age              | `Loadage`                   | 20 of 20                 | 21 of 21                 |
| fee                   | `Price`                     | 20 of 20                 | 21 of 21                 |
| object_file_index     | `ObjectName`                | 20 of 20                 | 21 of 21                 |
| waypoint_name_indexes | `WaypointName0` to `19`     | 20 of 20                 | 20 of 21                 |

The string columns compare the strings the indexes point at, the waypoint
names as one list. On client 3482 the Port Ratt Freight Ship (`729`) has
`LotWay_001` and `LotWay_118` where the sheet has `LotWay_0001` and
`LotWay_0153`. Client 3482 adds six carriers the sheet lacks (`730`, `731`,
`50987`, `59898`, `59902`, `62095`); the sheet's `714` and `9106` are not
in either file.

## Notes

- The waypoint names are named waypoints of the world map route graph; the
  wagons and ships move between them on the world map.

## Open Questions

### What the Byte After the Type Holds

`unknown_69` is `0` on every row of client 3482 and has no column or Lua
getter. `deliverer_type` and `unknown_69` may be one u16 field.
