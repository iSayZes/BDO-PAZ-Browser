# `bartersubgroup.bss` Format

## Purpose

The barter sub groups of the Great Ocean barters: numbered lists of
exchanges, each an item the player hands over, the item the player gets,
their counts, a cost and the exchange limits. An entry of
[`barter_normal.bss`](barter_normal_bss.md) names a sub group in its
`barter_sub_group` u32, the same field this file keys its entries by.

The file holds two lists of groups. The first is the trade item barter
list (the `BarterSubGroup` sheet of client 1784), the second the material
barter list (the `MaterialBarterSubGroup` sheet). On client 3474 the first
list has 197 groups with 731 entries, the second 5 groups with 85 entries;
on client 1784 125 groups with 443 entries and the same 5 groups with 85.
The same split runs through `barter_normal.bss` (two lists of regions) and
[`barterresetoption.bss`](barterresetoption_bss.md), whose
`MaterialBarter` list prices the ship material refreshes.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                 | Bytes  | Records                            | Row bytes |
| ------ | -------------- | -------------------- | ------ | ---------------------------------- | --------- |
| 3      | 2863 and later | `bartersubgroup.bss` | 59,584 | 816 Exchange, 816 Entry, 202 Group | 56        |
| 2      | 1690 to 2855   | `bartersubgroup.bss` | 36,976 | 528 Exchange, 528 Entry, 130 Group | 56        |
| 1      | 1351 to 1685   | `bartersubgroup.bss` | 36,448 | 528 Exchange, 528 Entry, 130 Group | 56        |

| Layout | File                 | Known             | Unknown    |
| ------ | -------------------- | ----------------- | ---------- |
| 3      | `bartersubgroup.bss` | 59,584 B (100.0%) | 0 B (0.0%) |
| 2      | `bartersubgroup.bss` | 36,976 B (100.0%) | 0 B (0.0%) |
| 1      | `bartersubgroup.bss` | 36,448 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 3             | `07251eefdcc0`  |
| 3482   | Layout 3             | `07251eefdcc0`  |
| 3474   | Layout 3             | `07251eefdcc0`  |
| 3473   | Layout 3             | `07251eefdcc0`  |
| 3464   | Layout 3             | `07251eefdcc0`  |
| 3458   | Layout 3             | `07251eefdcc0`  |
| 3454   | Layout 3             | `07251eefdcc0`  |
| 3444   | Layout 3             | `07251eefdcc0`  |
| 3435   | Layout 3             | `07251eefdcc0`  |
| 3426   | Layout 3             | `07251eefdcc0`  |
| 3418   | Layout 3             | `07251eefdcc0`  |
| 3412   | Layout 3             | `07251eefdcc0`  |
| 3402   | Layout 3             | `07251eefdcc0`  |
| 3396   | Layout 3             | `07251eefdcc0`  |
| 3387   | Layout 3             | `07251eefdcc0`  |
| 3381   | Layout 3             | `07251eefdcc0`  |
| 3373   | Layout 3             | `07251eefdcc0`  |
| 3364   | Layout 3             | `07251eefdcc0`  |
| 3356   | Layout 3             | `07251eefdcc0`  |
| 3349   | Layout 3             | `07251eefdcc0`  |
| 3342   | Layout 3             | `07251eefdcc0`  |
| 3335   | Layout 3             | `07251eefdcc0`  |
| 3326   | Layout 3             | `07251eefdcc0`  |
| 3321   | Layout 3             | `07251eefdcc0`  |
| 3314   | Layout 3             | `07251eefdcc0`  |
| 3303   | Layout 3             | `07251eefdcc0`  |
| 3302   | Layout 3             | `07251eefdcc0`  |
| 3293   | Layout 3             | `07251eefdcc0`  |
| 3283   | Layout 3             | `07251eefdcc0`  |
| 3275   | Layout 3             | `07251eefdcc0`  |
| 3267   | Layout 3             | `07251eefdcc0`  |
| 3258   | Layout 3             | `07251eefdcc0`  |
| 3251   | Layout 3             | `07251eefdcc0`  |
| 3242   | Layout 3             | `07251eefdcc0`  |
| 3235   | Layout 3             | `07251eefdcc0`  |
| 3229   | Layout 3             | `07251eefdcc0`  |
| 3212   | Layout 3             | `07251eefdcc0`  |
| 3203   | Layout 3             | `07251eefdcc0`  |
| 3193   | Layout 3             | `07251eefdcc0`  |
| 3186   | Layout 3             | `07251eefdcc0`  |
| 3177   | Layout 3             | `07251eefdcc0`  |
| 3169   | Layout 3             | `07251eefdcc0`  |
| 3158   | Layout 3             | `07251eefdcc0`  |
| 3151   | Layout 3             | `07251eefdcc0`  |
| 3144   | Layout 3             | `07251eefdcc0`  |
| 3133   | Layout 3             | `07251eefdcc0`  |
| 3125   | Layout 3             | `07251eefdcc0`  |
| 3118   | Layout 3             | `07251eefdcc0`  |
| 3111   | Layout 3             | `07251eefdcc0`  |
| 3103   | Layout 3             | `07251eefdcc0`  |
| 3095   | Layout 3             | `07251eefdcc0`  |
| 3086   | Layout 3             | `07251eefdcc0`  |
| 3072   | Layout 3             | `07251eefdcc0`  |
| 3062   | Layout 3             | `07251eefdcc0`  |
| 3052   | Layout 3             | `07251eefdcc0`  |
| 3045   | Layout 3             | `07251eefdcc0`  |
| 3037   | Layout 3             | `07251eefdcc0`  |
| 3030   | Layout 3             | `07251eefdcc0`  |
| 3021   | Layout 3             | `07251eefdcc0`  |
| 3012   | Layout 3             | `07251eefdcc0`  |
| 3002   | Layout 3             | `07251eefdcc0`  |
| 2995   | Layout 3             | `07251eefdcc0`  |
| 2987   | Layout 3             | `07251eefdcc0`  |
| 2978   | Layout 3             | `07251eefdcc0`  |
| 2970   | Layout 3             | `07251eefdcc0`  |
| 2959   | Layout 3             | `07251eefdcc0`  |
| 2951   | Layout 3             | `07251eefdcc0`  |
| 2942   | Layout 3             | `07251eefdcc0`  |
| 2935   | Layout 3             | `07251eefdcc0`  |
| 2932   | Layout 3             | `07251eefdcc0`  |
| 2923   | Layout 3             | `07251eefdcc0`  |
| 2919   | Layout 3             | `07251eefdcc0`  |
| 2907   | Layout 3             | `07251eefdcc0`  |
| 2900   | Layout 3             | `07251eefdcc0`  |
| 2891   | Layout 3             | `07251eefdcc0`  |
| 2882   | Layout 3             | `07251eefdcc0`  |
| 2872   | Layout 3             | `07251eefdcc0`  |
| 2863   | Layout 3             | `07251eefdcc0`  |
| 2855   | Layout 2             | `07251eefdcc0`  |
| 2849   | Layout 2             | `07251eefdcc0`  |
| 2844   | Layout 2             | `07251eefdcc0`  |
| 2834   | Layout 2             | `07251eefdcc0`  |
| 2825   | Layout 2             | `07251eefdcc0`  |
| 2819   | Layout 2             | `07251eefdcc0`  |
| 2811   | Layout 2             | `07251eefdcc0`  |
| 2803   | Layout 2             | `07251eefdcc0`  |
| 2794   | Layout 2             | `07251eefdcc0`  |
| 2783   | Layout 2             | `07251eefdcc0`  |
| 2774   | Layout 2             | `07251eefdcc0`  |
| 2765   | Layout 2             | `07251eefdcc0`  |
| 2756   | Layout 2             | `07251eefdcc0`  |
| 2750   | Layout 2             | `07251eefdcc0`  |
| 2743   | Layout 2             | `07251eefdcc0`  |
| 2736   | Layout 2             | `07251eefdcc0`  |
| 2726   | Layout 2             | `07251eefdcc0`  |
| 2717   | Layout 2             | `07251eefdcc0`  |
| 2709   | Layout 2             | `07251eefdcc0`  |
| 2703   | Layout 2             | `07251eefdcc0`  |
| 2695   | Layout 2             | `07251eefdcc0`  |
| 2684   | Layout 2             | `07251eefdcc0`  |
| 2672   | Layout 2             | `07251eefdcc0`  |
| 2665   | Layout 2             | `07251eefdcc0`  |
| 2657   | Layout 2             | `07251eefdcc0`  |
| 2649   | Layout 2             | `07251eefdcc0`  |
| 2644   | Layout 2             | `07251eefdcc0`  |
| 2637   | Layout 2             | `07251eefdcc0`  |
| 2629   | Layout 2             | `07251eefdcc0`  |
| 2619   | Layout 2             | `07251eefdcc0`  |
| 2612   | Layout 2             | `07251eefdcc0`  |
| 2606   | Layout 2             | `07251eefdcc0`  |
| 2602   | Layout 2             | `07251eefdcc0`  |
| 2601   | Layout 2             | `07251eefdcc0`  |
| 2592   | Layout 2             | `07251eefdcc0`  |
| 2583   | Layout 2             | `07251eefdcc0`  |
| 2575   | Layout 2             | `07251eefdcc0`  |
| 2567   | Layout 2             | `07251eefdcc0`  |
| 2560   | Layout 2             | `07251eefdcc0`  |
| 2553   | Layout 2             | `07251eefdcc0`  |
| 2545   | Layout 2             | `07251eefdcc0`  |
| 2538   | Layout 2             | `07251eefdcc0`  |
| 2529   | Layout 2             | `07251eefdcc0`  |
| 2519   | Layout 2             | `07251eefdcc0`  |
| 2513   | Layout 2             | `07251eefdcc0`  |
| 2510   | Layout 2             | `07251eefdcc0`  |
| 2507   | Layout 2             | `07251eefdcc0`  |
| 2503   | Layout 2             | `07251eefdcc0`  |
| 2498   | Layout 2             | `07251eefdcc0`  |
| 2492   | Layout 2             | `07251eefdcc0`  |
| 2487   | Layout 2             | `07251eefdcc0`  |
| 2480   | Layout 2             | `07251eefdcc0`  |
| 2474   | Layout 2             | `07251eefdcc0`  |
| 2468   | Layout 2             | `07251eefdcc0`  |
| 2460   | Layout 2             | `07251eefdcc0`  |
| 2453   | Layout 2             | `07251eefdcc0`  |
| 2444   | Layout 2             | `07251eefdcc0`  |
| 2438   | Layout 2             | `07251eefdcc0`  |
| 2434   | Layout 2             | `07251eefdcc0`  |
| 2429   | Layout 2             | `07251eefdcc0`  |
| 2421   | Layout 2             | `07251eefdcc0`  |
| 2414   | Layout 2             | `07251eefdcc0`  |
| 2407   | Layout 2             | `07251eefdcc0`  |
| 2401   | Layout 2             | `07251eefdcc0`  |
| 2397   | Layout 2             | `07251eefdcc0`  |
| 2393   | Layout 2             | `07251eefdcc0`  |
| 2384   | Layout 2             | `07251eefdcc0`  |
| 2378   | Layout 2             | `07251eefdcc0`  |
| 2372   | Layout 2             | `07251eefdcc0`  |
| 2358   | Layout 2             | `07251eefdcc0`  |
| 2352   | Layout 2             | `07251eefdcc0`  |
| 2347   | Layout 2             | `07251eefdcc0`  |
| 2343   | Layout 2             | `07251eefdcc0`  |
| 2335   | Layout 2             | `07251eefdcc0`  |
| 2327   | Layout 2             | `07251eefdcc0`  |
| 2324   | Layout 2             | `07251eefdcc0`  |
| 2319   | Layout 2             | `07251eefdcc0`  |
| 2313   | Layout 2             | `07251eefdcc0`  |
| 2308   | Layout 2             | `07251eefdcc0`  |
| 2302   | Layout 2             | `07251eefdcc0`  |
| 2295   | Layout 2             | `07251eefdcc0`  |
| 2290   | Layout 2             | `07251eefdcc0`  |
| 2284   | Layout 2             | `07251eefdcc0`  |
| 2276   | Layout 2             | `07251eefdcc0`  |
| 2269   | Layout 2             | `07251eefdcc0`  |
| 2259   | Layout 2             | `07251eefdcc0`  |
| 2250   | Layout 2             | `07251eefdcc0`  |
| 2243   | Layout 2             | `07251eefdcc0`  |
| 2235   | Layout 2             | `07251eefdcc0`  |
| 2229   | Layout 2             | `07251eefdcc0`  |
| 2224   | Layout 2             | `07251eefdcc0`  |
| 2218   | Layout 2             | `07251eefdcc0`  |
| 2215   | Layout 2             | `07251eefdcc0`  |
| 2207   | Layout 2             | `07251eefdcc0`  |
| 2203   | Layout 2             | `07251eefdcc0`  |
| 2196   | Layout 2             | `07251eefdcc0`  |
| 2192   | Layout 2             | `07251eefdcc0`  |
| 2189   | Layout 2             | `07251eefdcc0`  |
| 2183   | Layout 2             | `07251eefdcc0`  |
| 2179   | Layout 2             | `07251eefdcc0`  |
| 2171   | Layout 2             | `07251eefdcc0`  |
| 2163   | Layout 2             | `07251eefdcc0`  |
| 2156   | Layout 2             | `07251eefdcc0`  |
| 2151   | Layout 2             | `07251eefdcc0`  |
| 2147   | Layout 2             | `07251eefdcc0`  |
| 2142   | Layout 2             | `07251eefdcc0`  |
| 2138   | Layout 2             | `07251eefdcc0`  |
| 2134   | Layout 2             | `07251eefdcc0`  |
| 2130   | Layout 2             | `07251eefdcc0`  |
| 2122   | Layout 2             | `07251eefdcc0`  |
| 2107   | Layout 2             | `07251eefdcc0`  |
| 2098   | Layout 2             | `07251eefdcc0`  |
| 2089   | Layout 2             | `07251eefdcc0`  |
| 2081   | Layout 2             | `07251eefdcc0`  |
| 2073   | Layout 2             | `07251eefdcc0`  |
| 2067   | Layout 2             | `07251eefdcc0`  |
| 2063   | Layout 2             | `07251eefdcc0`  |
| 2059   | Layout 2             | `07251eefdcc0`  |
| 2052   | Layout 2             | `07251eefdcc0`  |
| 2044   | Layout 2             | `07251eefdcc0`  |
| 2039   | Layout 2             | `07251eefdcc0`  |
| 2032   | Layout 2             | `07251eefdcc0`  |
| 2025   | Layout 2             | `07251eefdcc0`  |
| 2011   | Layout 2             | `07251eefdcc0`  |
| 2005   | Layout 2             | `07251eefdcc0`  |
| 2000   | Layout 2             | `07251eefdcc0`  |
| 1996   | Layout 2             | `07251eefdcc0`  |
| 1991   | Layout 2             | `07251eefdcc0`  |
| 1985   | Layout 2             | `07251eefdcc0`  |
| 1980   | Layout 2             | `07251eefdcc0`  |
| 1969   | Layout 2             | `07251eefdcc0`  |
| 1964   | Layout 2             | `07251eefdcc0`  |
| 1958   | Layout 2             | `07251eefdcc0`  |
| 1950   | Layout 2             | `07251eefdcc0`  |
| 1945   | Layout 2             | `07251eefdcc0`  |
| 1937   | Layout 2             | `07251eefdcc0`  |
| 1933   | Layout 2             | `07251eefdcc0`  |
| 1927   | Layout 2             | `07251eefdcc0`  |
| 1921   | Layout 2             | `07251eefdcc0`  |
| 1914   | Layout 2             | `07251eefdcc0`  |
| 1908   | Layout 2             | `07251eefdcc0`  |
| 1897   | Layout 2             | `07251eefdcc0`  |
| 1892   | Layout 2             | `07251eefdcc0`  |
| 1886   | Layout 2             | `07251eefdcc0`  |
| 1881   | Layout 2             | `07251eefdcc0`  |
| 1871   | Layout 2             | `07251eefdcc0`  |
| 1866   | Layout 2             | `07251eefdcc0`  |
| 1862   | Layout 2             | `07251eefdcc0`  |
| 1854   | Layout 2             | `07251eefdcc0`  |
| 1846   | Layout 2             | `07251eefdcc0`  |
| 1838   | Layout 2             | `07251eefdcc0`  |
| 1832   | Layout 2             | `07251eefdcc0`  |
| 1826   | Layout 2             | `07251eefdcc0`  |
| 1822   | Layout 2             | `07251eefdcc0`  |
| 1818   | Layout 2             | `07251eefdcc0`  |
| 1804   | Layout 2             | `07251eefdcc0`  |
| 1794   | Layout 2             | `07251eefdcc0`  |
| 1790   | Layout 2             | `07251eefdcc0`  |
| 1784   | Layout 2             | `07251eefdcc0`  |
| 1774   | Layout 2             | `07251eefdcc0`  |
| 1771   | Layout 2             | `07251eefdcc0`  |
| 1762   | Layout 2             | `07251eefdcc0`  |
| 1759   | Layout 2             | `07251eefdcc0`  |
| 1754   | Layout 2             | `07251eefdcc0`  |
| 1749   | Layout 2             | `07251eefdcc0`  |
| 1743   | Layout 2             | `07251eefdcc0`  |
| 1737   | Layout 2             | `07251eefdcc0`  |
| 1731   | Layout 2             | `07251eefdcc0`  |
| 1725   | Layout 2             | `07251eefdcc0`  |
| 1717   | Layout 2             | `07251eefdcc0`  |
| 1710   | Layout 2             | `07251eefdcc0`  |
| 1704   | Layout 2             | `07251eefdcc0`  |
| 1698   | Layout 2             | `07251eefdcc0`  |
| 1690   | Layout 2             | `07251eefdcc0`  |
| 1685   | Layout 1             | `07251eefdcc0`  |
| 1680   | Layout 1             | `07251eefdcc0`  |
| 1674   | Layout 1             | `07251eefdcc0`  |
| 1668   | Layout 1             | `07251eefdcc0`  |
| 1659   | Layout 1             | `07251eefdcc0`  |
| 1649   | Layout 1             | `07251eefdcc0`  |
| 1642   | Layout 1             | `07251eefdcc0`  |
| 1636   | Layout 1             | `07251eefdcc0`  |
| 1628   | Layout 1             | `07251eefdcc0`  |
| 1622   | Layout 1             | `07251eefdcc0`  |
| 1614   | Layout 1             | `07251eefdcc0`  |
| 1608   | Layout 1             | `07251eefdcc0`  |
| 1602   | Layout 1             | `07251eefdcc0`  |
| 1598   | Layout 1             | `07251eefdcc0`  |
| 1594   | Layout 1             | `07251eefdcc0`  |
| 1590   | Layout 1             | `07251eefdcc0`  |
| 1587   | Layout 1             | `07251eefdcc0`  |
| 1584   | Layout 1             | `07251eefdcc0`  |
| 1579   | Layout 1             | `07251eefdcc0`  |
| 1572   | Layout 1             | `07251eefdcc0`  |
| 1565   | Layout 1             | `07251eefdcc0`  |
| 1559   | Layout 1             | `07251eefdcc0`  |
| 1554   | Layout 1             | `07251eefdcc0`  |
| 1547   | Layout 1             | `07251eefdcc0`  |
| 1537   | Layout 1             | `07251eefdcc0`  |
| 1529   | Layout 1             | `07251eefdcc0`  |
| 1524   | Layout 1             | `07251eefdcc0`  |
| 1519   | Layout 1             | `07251eefdcc0`  |
| 1509   | Layout 1             | `07251eefdcc0`  |
| 1506   | Layout 1             | `07251eefdcc0`  |
| 1504   | Layout 1             | `07251eefdcc0`  |
| 1500   | Layout 1             | `07251eefdcc0`  |
| 1493   | Layout 1             | `07251eefdcc0`  |
| 1489   | Layout 1             | `07251eefdcc0`  |
| 1485   | Layout 1             | `07251eefdcc0`  |
| 1481   | Layout 1             | `07251eefdcc0`  |
| 1474   | Layout 1             | `07251eefdcc0`  |
| 1466   | Layout 1             | `07251eefdcc0`  |
| 1462   | Layout 1             | `07251eefdcc0`  |
| 1459   | Layout 1             | `07251eefdcc0`  |
| 1453   | Layout 1             | `07251eefdcc0`  |
| 1450   | Layout 1             | `07251eefdcc0`  |
| 1445   | Layout 1             | `07251eefdcc0`  |
| 1439   | Layout 1             | `07251eefdcc0`  |
| 1433   | Layout 1             | `07251eefdcc0`  |
| 1430   | Layout 1             | `07251eefdcc0`  |
| 1426   | Layout 1             | `07251eefdcc0`  |
| 1421   | Layout 1             | `07251eefdcc0`  |
| 1417   | Layout 1             | `07251eefdcc0`  |
| 1416   | Layout 1             | `07251eefdcc0`  |
| 1409   | Layout 1             | `07251eefdcc0`  |
| 1405   | Layout 1             | `07251eefdcc0`  |
| 1401   | Layout 1             | `07251eefdcc0`  |
| 1396   | Layout 1             | `07251eefdcc0`  |
| 1391   | Layout 1             | `07251eefdcc0`  |
| 1390   | Layout 1             | `07251eefdcc0`  |
| 1386   | Layout 1             | `07251eefdcc0`  |
| 1381   | Layout 1             | `07251eefdcc0`  |
| 1379   | Layout 1             | `07251eefdcc0`  |
| 1372   | Layout 1             | `07251eefdcc0`  |
| 1366   | Layout 1             | `07251eefdcc0`  |
| 1364   | Layout 1             | `07251eefdcc0`  |
| 1363   | Layout 1             | `07251eefdcc0`  |
| 1360   | Layout 1             | `07251eefdcc0`  |
| 1358   | Layout 1             | `07251eefdcc0`  |
| 1355   | Layout 1             | `07251eefdcc0`  |
| 1351   | Layout 1             | `07251eefdcc0`  |
| 1348   | No documented layout | `07251eefdcc0`  |
| 1346   | No documented layout | `07251eefdcc0`  |
| 1341   | No documented layout | `07251eefdcc0`  |
| 1340   | No documented layout | `07251eefdcc0`  |
| 1338   | No documented layout | `07251eefdcc0`  |
| 1335   | No documented layout | `07251eefdcc0`  |
| 1333   | No documented layout | `07251eefdcc0`  |
| 1329   | No documented layout | `07251eefdcc0`  |
| 1327   | No documented layout | `07251eefdcc0`  |
| 1324   | No documented layout | `07251eefdcc0`  |
| 1321   | No documented layout | `07251eefdcc0`  |
| 1319   | No documented layout | `07251eefdcc0`  |
| 1318   | No documented layout | `07251eefdcc0`  |
| 1316   | No documented layout | `07251eefdcc0`  |
| 1313   | No documented layout | `07251eefdcc0`  |
| 1311   | No documented layout | `07251eefdcc0`  |
| 1309   | No documented layout | `07251eefdcc0`  |
| 1304   | No documented layout | `07251eefdcc0`  |
| 1292   | No file              | `07251eefdcc0`  |
| 1286   | No file              | `07251eefdcc0`  |
| 1280   | No file              | `07251eefdcc0`  |
| 1276   | No file              | `07251eefdcc0`  |
| 1267   | No file              | `07251eefdcc0`  |
| 1261   | No file              | `07251eefdcc0`  |
| 1256   | No file              | `07251eefdcc0`  |
| 1250   | No file              | `07251eefdcc0`  |
| 1246   | No file              | `07251eefdcc0`  |
| 1239   | No file              | `07251eefdcc0`  |
| 1230   | No file              | `07251eefdcc0`  |
| 1226   | No file              | `07251eefdcc0`  |
| 1220   | No file              | `07251eefdcc0`  |
| 1217   | No file              | `07251eefdcc0`  |
| 1211   | No file              | `07251eefdcc0`  |
| 1210   | No file              | `07251eefdcc0`  |
| 1208   | No file              | `07251eefdcc0`  |
| 1203   | No file              | `07251eefdcc0`  |
| 1197   | No file              | `07251eefdcc0`  |
| 1194   | No file              | `07251eefdcc0`  |
| 1192   | No file              | `07251eefdcc0`  |
| 1187   | No file              | `07251eefdcc0`  |
| 1183   | No file              | `07251eefdcc0`  |
| 1177   | No file              | `07251eefdcc0`  |
| 1173   | No file              | `07251eefdcc0`  |
| 1167   | No file              | `07251eefdcc0`  |
| 1164   | No file              | `07251eefdcc0`  |
| 1156   | No file              | `07251eefdcc0`  |
| 1149   | No file              | `07251eefdcc0`  |
| 1144   | No file              | `07251eefdcc0`  |
| 1137   | No file              | `07251eefdcc0`  |
| 1132   | No file              | `07251eefdcc0`  |
| 1127   | No file              | `07251eefdcc0`  |
| 1122   | No file              | `07251eefdcc0`  |
| 1118   | No file              | `07251eefdcc0`  |
| 1114   | No file              | `07251eefdcc0`  |
| 1109   | No file              | `07251eefdcc0`  |
| 1102   | No file              | `07251eefdcc0`  |
| 1096   | No file              | `07251eefdcc0`  |
| 1088   | No file              | `07251eefdcc0`  |
| 1081   | No file              | `07251eefdcc0`  |
| 1076   | No file              | `07251eefdcc0`  |
| 1069   | No file              | `07251eefdcc0`  |
| 1064   | No file              | `07251eefdcc0`  |
| 1058   | No file              | `07251eefdcc0`  |
| 1051   | No file              | `07251eefdcc0`  |
| 1044   | No file              | `07251eefdcc0`  |
| 1036   | No file              | `07251eefdcc0`  |
| 1026   | No file              | `07251eefdcc0`  |
| 1016   | No file              | `07251eefdcc0`  |
| 1009   | No file              | `07251eefdcc0`  |
| 1005   | No file              | `07251eefdcc0`  |
| 1000   | No file              | `07251eefdcc0`  |
| 998    | No file              | `07251eefdcc0`  |
| 990    | No file              | `07251eefdcc0`  |
| 979    | No file              | `07251eefdcc0`  |
| 972    | No file              | `07251eefdcc0`  |
| 963    | No file              | `07251eefdcc0`  |
| 955    | No file              | `07251eefdcc0`  |
| 946    | No file              | `07251eefdcc0`  |
| 938    | No file              | `07251eefdcc0`  |
| 927    | No file              | `07251eefdcc0`  |
| 911    | No file              | `07251eefdcc0`  |
| 904    | No file              | `07251eefdcc0`  |
| 899    | No file              | `07251eefdcc0`  |
| 894    | No file              | `07251eefdcc0`  |
| 885    | No file              | `07251eefdcc0`  |
| 879    | No file              | `07251eefdcc0`  |
| 872    | No file              | `07251eefdcc0`  |
| 864    | No file              | `07251eefdcc0`  |
| 855    | No file              | `07251eefdcc0`  |
| 853    | No file              | `07251eefdcc0`  |
| 845    | No file              | `07251eefdcc0`  |
| 837    | No file              | `07251eefdcc0`  |
| 829    | No file              | `07251eefdcc0`  |
| 822    | No file              | `07251eefdcc0`  |
| 814    | No file              | `07251eefdcc0`  |
| 805    | No file              | `07251eefdcc0`  |
| 794    | No file              | `07251eefdcc0`  |
| 787    | No file              | `07251eefdcc0`  |
| 780    | No file              | `07251eefdcc0`  |
| 771    | No file              | `07251eefdcc0`  |
| 760    | No file              | `07251eefdcc0`  |
| 748    | No file              | `07251eefdcc0`  |
| 741    | No file              | `07251eefdcc0`  |
| 736    | No file              | `07251eefdcc0`  |
| 731    | No file              | `07251eefdcc0`  |
| 723    | No file              | `07251eefdcc0`  |
| 711    | No file              | `07251eefdcc0`  |
| 707    | No file              | `07251eefdcc0`  |
| 697    | No file              | `07251eefdcc0`  |
| 689    | No file              | `07251eefdcc0`  |
| 683    | No file              | `07251eefdcc0`  |
| 678    | No file              | `07251eefdcc0`  |
| 670    | No file              | `07251eefdcc0`  |
| 661    | No file              | `07251eefdcc0`  |
| 656    | No file              | `07251eefdcc0`  |
| 652    | No file              | `07251eefdcc0`  |
| 643    | No file              | `07251eefdcc0`  |
| 637    | No file              | `07251eefdcc0`  |
| 630    | No file              | `07251eefdcc0`  |
| 627    | No file              | `07251eefdcc0`  |
| 621    | No file              | `07251eefdcc0`  |
| 617    | No file              | `07251eefdcc0`  |
| 615    | No file              | `07251eefdcc0`  |
| 606    | No file              | `07251eefdcc0`  |
| 599    | No file              | `07251eefdcc0`  |
| 592    | No file              | `07251eefdcc0`  |
| 586    | No file              | `07251eefdcc0`  |
| 577    | No file              | `07251eefdcc0`  |
| 569    | No file              | `07251eefdcc0`  |
| 561    | No file              | `07251eefdcc0`  |
| 554    | No file              | `07251eefdcc0`  |
| 542    | No file              | `07251eefdcc0`  |
| 532    | No file              | `07251eefdcc0`  |
| 531    | No file              | `07251eefdcc0`  |
| 526    | No file              | `07251eefdcc0`  |
| 521    | No file              | `07251eefdcc0`  |
| 517    | No file              | `07251eefdcc0`  |
| 510    | No file              | `07251eefdcc0`  |
| 508    | No file              | `07251eefdcc0`  |
| 504    | No file              | `07251eefdcc0`  |
| 497    | No file              | `07251eefdcc0`  |
| 491    | No file              | `07251eefdcc0`  |
| 485    | No file              | `07251eefdcc0`  |
| 478    | No file              | `07251eefdcc0`  |
| 472    | No file              | `07251eefdcc0`  |
| 466    | No file              | `07251eefdcc0`  |
| 457    | No file              | `07251eefdcc0`  |
| 452    | No file              | `07251eefdcc0`  |
| 449    | No file              | `07251eefdcc0`  |
| 435    | No file              | `07251eefdcc0`  |

<!-- versions:end -->

## Companion Files

| File                 | Required | Role                                                 |
| -------------------- | -------- | ---------------------------------------------------- |
| `languagedata_*.loc` | Optional | Item names (type 0) and barter category names (type 37) |

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset                 | Type                         | Field                | Notes                                                          |
| ---------------------- | ---------------------------- | -------------------- | -------------------------------------------------------------- |
| `+0x00`                | char[4]                      | magic                | ASCII `PABR`                                                   |
| `+0x04`                | u32                          | group_count          | Number of `groups`; `197` on client 3474                       |
| `+0x08`                | Group[group_count]           | groups               | The trade item barter sub groups, keys `1` to `group_count` in order |
| `groups+0x00`          | u32                          | material_group_count | Number of `material_groups`; `5` on client 3474                |
| `groups+0x04`          | Group[material_group_count]  | material_groups      | The material barter sub groups, keys `1` to `material_group_count` in order |
| `material_groups+0x00` | String Table                 | string_table         | The PABR string table, present but empty                       |
| `string_table+0x00`    | u32                          | string_table_start   | Absolute offset of `string_count`, where `material_groups` ends |
| `string_table+0x04`    | u32                          | zero                 | Always `0`                                                     |

### Group (variable: 4 bytes + entries)

| Offset  | Type               | Field       | Notes                                                    |
| ------- | ------------------ | ----------- | -------------------------------------------------------- |
| `+0x00` | u32                | entry_count | Number of `entries`; `2` to `60` on client 3474          |
| `+0x04` | Entry[entry_count] | entries     | See Entry; every entry of a group holds the group's key  |

### Entry (72 bytes)

| Offset  | Type     | Field            | Notes                                                                 |
| ------- | -------- | ---------------- | --------------------------------------------------------------------- |
| `+0x00` | u32      | barter_sub_group | The group key: the group's place in its list, from `1`                |
| `+0x04` | u32      | select_rate      | `1000000` on every entry (client 3474)                                |
| `+0x08` | u32      | barter_cost      | `2` to `68` in the trade item list, `15` in the material list (client 3474) |
| `+0x0c` | Exchange | exchange         | See Exchange                                                          |
| `+0x44` | u32      | barter_category  | Bit mask, bit N set for category N of Barter Categories; `0` on every material entry |

### Exchange (56 bytes)

The part every barter row shares: the same 56 bytes sit in the rows of
[`barter_special.bss`](barter_special_bss.md) and the entries of
[`barter_normal.bss`](barter_normal_bss.md).

| Offset  | Type | Field              | Notes                                                                  |
| ------- | ---- | ------------------ | ---------------------------------------------------------------------- |
| `+0x00` | u32  | from_item_key      | The item the player hands over, `enchant_level << 24 \| item_id`       |
| `+0x04` | u64  | from_min_count     | Fewest of `from_item_key` the exchange asks for                        |
| `+0x0c` | u64  | from_max_count     | Most of `from_item_key` the exchange asks for                          |
| `+0x14` | u32  | to_item_key        | The item the player gets, `enchant_level << 24 \| item_id`             |
| `+0x18` | u64  | to_min_count       | Fewest of `to_item_key` the exchange gives                             |
| `+0x20` | u64  | to_max_count       | Most of `to_item_key` the exchange gives                               |
| `+0x28` | u32  | barter_need_point  | `14286` or `21650` in the trade item list, `21650` or `29430` in the material list (client 3474) |
| `+0x2c` | u32  | exchange_max_count | How many times the exchange can be made; `1` to `6` (client 3474)      |
| `+0x30` | u32  | exchange_min       | `0` to `20471` in the trade item list, `0` in the material list (client 3474); see Open Questions |
| `+0x34` | u32  | exchange_max       | `1000000` on every entry (client 3474)                                 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Layout 2

`barter_category` is one byte that holds the category number itself.

### Entry (69 bytes)

| Offset  | Type     | Field            | Notes                                                     |
| ------- | -------- | ---------------- | --------------------------------------------------------- |
| `+0x00` | u32      | barter_sub_group |                                                           |
| `+0x04` | u32      | select_rate      |                                                           |
| `+0x08` | u32      | barter_cost      |                                                           |
| `+0x0c` | Exchange | exchange         |                                                           |
| `+0x44` | u8       | barter_category  | The category number: `5`, `6` or `7` in the trade item list, `8` on every material entry (client 1784) |

## Layout 1

The entry ends after the Exchange: there is no `barter_category`.

### Entry (68 bytes)

| Offset  | Type     | Field            | Notes |
| ------- | -------- | ---------------- | ----- |
| `+0x00` | u32      | barter_sub_group |       |
| `+0x04` | u32      | select_rate      |       |
| `+0x08` | u32      | barter_cost      |       |
| `+0x0c` | Exchange | exchange         |       |

## Barter Categories

The Barter information window (`panel_window_barterinfosearch.luac`,
client 3474) filters by `__eBarterCategory_*`, labelled with the GAME sheet
keys `LUA_BARTER_NEW_FILTER_*`. The Lua names the values but not their
numbers; the numbers below follow from the window and the data:
`getSelectCategoryIndex()` in `panel_window_barterinfosearch_1.luac` returns
the drop-down index plus 1 for the first five entries and maps a pick past
`__eBarterCategory_Ocean` to `__eBarterCategory_Count` when the old list of
eight shows, so Ocean is `8`. The client 3474 masks confirm `5`, `6`, `7` and
`10` by their items: bit 5 entries trade `[Level 4]` items for `[Level 5]`
items, bit 6 entries trade trade items for other items (Tidal Black Stone,
Oquilla's Flower), bit 7 entries give Crow Coins (`10`), and bit 10 entries
trade `[Level 6]` items for `[Level 7]` items. On client 1784 the same
entries hold `5`, `6` and `7` as plain numbers.

| Value | Lua name                            | GAME key                   | English (client 3474) | Entries with the bit (client 3474) |
| ----- | ----------------------------------- | -------------------------- | --------------------- | ---------------------------------- |
| `1`   | `__eBarterCategory_NormalToLevel1`  | `LUA_BARTER_NEW_FILTER_1`  | Normal -> Lv. 1       | 0                                  |
| `2`   | `__eBarterCategory_Level1ToLevel2`  | `LUA_BARTER_NEW_FILTER_2`  | Lv. 1 -> Lv. 2        | 0                                  |
| `3`   | `__eBarterCategory_Level2ToLevel3`  | `LUA_BARTER_NEW_FILTER_3`  | Lv. 2 -> Lv. 3        | 0                                  |
| `4`   | `__eBarterCategory_Level3ToLevel4`  | `LUA_BARTER_NEW_FILTER_4`  | Lv. 3 -> Lv. 4        | 0                                  |
| `5`   | `__eBarterCategory_Level4ToLevel5`  | `LUA_BARTER_NEW_FILTER_5`  | Lv. 4 -> Lv. 5        | 120                                |
| `6`   | `__eBarterCategory_NormalBarter`    | `LUA_BARTER_NEW_FILTER_6`  | Normal Barter         | 197                                |
| `7`   | `__eBarterCategory_CrowCoin`        | `LUA_BARTER_NEW_FILTER_7`  | Crow Coin             | 126                                |
| `8`   | `__eBarterCategory_Ocean`           | `LUA_BARTER_NEW_FILTER_9`  | Ocean Barter          | 0                                  |
| `9`   | `__eBarterCategory_Level5ToLevel6`  | `LUA_BARTER_NEW_FILTER_10` | Lv. 5 -> Lv. 6        | 0                                  |
| `10`  | `__eBarterCategory_Level6ToLevel7`  | `LUA_BARTER_NEW_FILTER_11` | Lv. 6 -> Lv. 7        | 288                                |

`__eBarterCategory_Count` is the "All Barters" pick (`LUA_BARTER_NEW_FILTER_8`).
Every trade item entry of client 3474 has exactly one bit set.

## Field Names

The entry is the `BarterSubGroup` sheet of a private server's
`DataSheets.bexcel` on client 1784, and the material list its
`MaterialBarterSubGroup` sheet. The client 1784 file holds the 443 and 85
sheet rows in sheet order, and every column matches on all of them:
`BarterSubGroup`, `SelectRate`, `BarterCost`, `GivedItemKey` with
`GivedEnchantLevel` (one packed key), `GivedMinCount`, `GivedMaxCount`,
`TakedItemKey` with `TakedEnchantLevel`, `TakedMinCount`, `TakedMaxCount`,
`BarterNeedPoint`, `ExchangeMaxCount`, `ExchangeMin`, `ExchangeMax` and, in
the trade item list, `BarterCategory`. The material sheet has no
`BarterCategory` column; its entries hold `8` on client 1784 and `0` on
client 3474. The sheet columns `ContentsGroup`, `TradeEmployeeExp` and
`BarterTradeExp` are not in the file.

`SelectRate` and `ExchangeMax` are `1000000` on every row of the sheet, so
the sheet alone does not tell them apart. The `SpecialBarterData` sheet
does: there `SelectRate` is `0` and `ExchangeMax` holds two values, and they
match the u32 before the Exchange and the last u32 of the Exchange of
[`barter_special.bss`](barter_special_bss.md) on 148 of 148 rows.

On client 3474 the sheet rows that share a group key and place in the group
match as follows (443 rows of the first list, 85 of the second):

| Field              | Column             | Trade item list | Material list |
| ------------------ | ------------------ | --------------- | ------------- |
| barter_sub_group   | `BarterSubGroup`   | 443             | 85            |
| select_rate        | `SelectRate`       | 443             | 85            |
| barter_cost        | `BarterCost`       | 406             | 85            |
| from_item_key      | `GivedItemKey`     | 400             | 12            |
| from_min_count     | `GivedMinCount`    | 435             | 85            |
| from_max_count     | `GivedMaxCount`    | 435             | 85            |
| to_item_key        | `TakedItemKey`     | 392             | 85            |
| to_min_count       | `TakedMinCount`    | 392             | 12            |
| to_max_count       | `TakedMaxCount`    | 392             | 12            |
| barter_need_point  | `BarterNeedPoint`  | 443             | 18            |
| exchange_max_count | `ExchangeMaxCount` | 273             | 85            |
| exchange_min       | `ExchangeMin`      | 427             | 85            |
| exchange_max       | `ExchangeMax`      | 443             | 85            |

The material list has the sheet's group sizes, `10, 20, 15, 20, 20`, and
holds other items: client 3474 asks for `[Level 4]` items (Marine Knights'
Helm `800043` onwards) where the sheet asks for `[Level 5]` ones (`800057`
onwards), for 360 to 440 Crow Coins in place of 120 to 145.

`from_*` and `to_*` follow the client Lua: the barter windows read the
exchange with `getFromItemEnchantKey()`, `getFromItemCount()`,
`getToItemEnchantKey()` and `getToItemCount()`, and
`panel_window_barterinfosearch_special_1.luac` shows the from item under
`Static_MyItemBG` (the player's item) and the to item under
`Static_TakeItemBG`. The sheet's `Gived` is the from item and `Taked` the
to item: the 1784 special barter row `1` hands over Gold Bar 1,000G (`5`)
for item `45505`. `exchange_max_count` is the
`getExchangeMaxCount()` of the same wrappers.

## Notes

- The keys of the first list run `1` to `197` and those of the second `1`
  to `5` on client 3474; the entries of `barter_normal.bss` name keys `1`
  to `197` in its trade item list and `1` to `5` in its material list (see
  its [Sub Group Entries](barter_normal_bss.md#sub-group-entries)).
- Item keys pack the enhancement level like
  [`itemenchant.dbss`](itemenchant_dbss.md); the from items are level `0`
  on every entry (client 3474).
- The handler (`_bss/bartersubgroup/`) shows one row per entry, with a
  Material flag on the entries of the second list. It reads the Exchange
  and walks the two lists with the shared barter reader in `_bss/barter/`,
  which `barter_special.bss` and `barter_normal.bss` use too, and names the
  categories with their LOC type 37 GAME text. Each entry carries
  `sub_group_ref` (`trade:12`, `material:3`), the field the
  `barter_normal.bss` sub group links open it by.

## Open Questions

### Exchange Min and Max

`exchange_min` and `exchange_max` are the sheet's `ExchangeMin` and
`ExchangeMax`. `exchange_max` is `1000000` on every entry. On client 3474
220 of the 731 trade item entries hold an `exchange_min` of 10 times a
power of 2 less 9 (`11`, `31`, `71`, ... `2551`, `5111`, `10231`,
`20471`), 203 a round number (`6`, `10`, `20`, `100`, `3000`, `5000`,
`8000`, `10000`, `20000`) and 308 `0`. The doubling steps look like the
parley a barter costs, but the Lua
reads the parley through `getExchangeCountForTime()` and nothing in the
barter windows reads a minimum or maximum. What the two bound is not in the
client data read so far.

### Barter Need Point and Select Rate

`barter_need_point` (`14286`, `21650` or `29430`) and `select_rate`
(`1000000`) are read by no Lua function of the barter windows. A lead for
`select_rate`: a weight in millionths for picking one entry of the group,
as `CppDefine.e1Percent` is `10000` and `1000000` is then 100%.
