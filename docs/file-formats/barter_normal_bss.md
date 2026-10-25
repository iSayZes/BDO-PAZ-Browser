# `barter_normal.bss` Format

## Purpose

The barter slots of the Great Ocean barters, per barter region (the
island, port or ship of a [`barter_npclist.bss`](barter_npclist_bss.md)
row). The file holds two lists of regions: the trade item barters (the
`BarterData` sheet of client 1784) and the material barters (the
`MaterialBarterData` sheet). Every region of the first list has 40 slots
and every region of the second 41 (clients 1485 to 3474).

A slot is either an exchange of its own (the item the player hands over,
the item the player gets, their counts and the exchange limits) or a
reference to a sub group of [`bartersubgroup.bss`](bartersubgroup_bss.md)
in the same list, with its own exchange left zero. On client 3474 the two
lists hold 91 regions each, 3,640 and 3,731 slots; 511 trade item slots and
10 material slots name a sub group.

The barter windows read a region's exchanges at run time through
`ToClient_barterWrapper(RegionKey(regionKey))`
(`panel_window_barterinfosearch_2.luac`); see Open Questions.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                | Bytes   | Records                                 | Row bytes |
| ------ | -------------- | ------------------- | ------- | --------------------------------------- | --------- |
| 3      | 2863 and later | `barter_normal.bss` | 517,086 | 7,371 Exchange, 7,371 Entry, 182 Region | 56        |
| 2      | 1690 to 2855   | `barter_normal.bss` | 440,583 | 6,561 Exchange, 6,561 Entry, 162 Region | 56        |
| 1      | 1351 to 1685   | `barter_normal.bss` | 434,022 | 6,561 Exchange, 6,561 Entry, 162 Region | 56        |

| Layout | File                | Known              | Unknown    |
| ------ | ------------------- | ------------------ | ---------- |
| 3      | `barter_normal.bss` | 517,086 B (100.0%) | 0 B (0.0%) |
| 2      | `barter_normal.bss` | 440,583 B (100.0%) | 0 B (0.0%) |
| 1      | `barter_normal.bss` | 434,022 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 3             | `2ef58a4cde3e`  |
| 3482   | Layout 3             | `2ef58a4cde3e`  |
| 3474   | Layout 3             | `2ef58a4cde3e`  |
| 3473   | Layout 3             | `2ef58a4cde3e`  |
| 3464   | Layout 3             | `2ef58a4cde3e`  |
| 3458   | Layout 3             | `2ef58a4cde3e`  |
| 3454   | Layout 3             | `2ef58a4cde3e`  |
| 3444   | Layout 3             | `2ef58a4cde3e`  |
| 3435   | Layout 3             | `2ef58a4cde3e`  |
| 3426   | Layout 3             | `2ef58a4cde3e`  |
| 3418   | Layout 3             | `2ef58a4cde3e`  |
| 3412   | Layout 3             | `2ef58a4cde3e`  |
| 3402   | Layout 3             | `2ef58a4cde3e`  |
| 3396   | Layout 3             | `2ef58a4cde3e`  |
| 3387   | Layout 3             | `2ef58a4cde3e`  |
| 3381   | Layout 3             | `2ef58a4cde3e`  |
| 3373   | Layout 3             | `2ef58a4cde3e`  |
| 3364   | Layout 3             | `2ef58a4cde3e`  |
| 3356   | Layout 3             | `2ef58a4cde3e`  |
| 3349   | Layout 3             | `2ef58a4cde3e`  |
| 3342   | Layout 3             | `2ef58a4cde3e`  |
| 3335   | Layout 3             | `2ef58a4cde3e`  |
| 3326   | Layout 3             | `2ef58a4cde3e`  |
| 3321   | Layout 3             | `2ef58a4cde3e`  |
| 3314   | Layout 3             | `2ef58a4cde3e`  |
| 3303   | Layout 3             | `2ef58a4cde3e`  |
| 3302   | Layout 3             | `2ef58a4cde3e`  |
| 3293   | Layout 3             | `2ef58a4cde3e`  |
| 3283   | Layout 3             | `2ef58a4cde3e`  |
| 3275   | Layout 3             | `2ef58a4cde3e`  |
| 3267   | Layout 3             | `2ef58a4cde3e`  |
| 3258   | Layout 3             | `2ef58a4cde3e`  |
| 3251   | Layout 3             | `2ef58a4cde3e`  |
| 3242   | Layout 3             | `2ef58a4cde3e`  |
| 3235   | Layout 3             | `2ef58a4cde3e`  |
| 3229   | Layout 3             | `2ef58a4cde3e`  |
| 3212   | Layout 3             | `2ef58a4cde3e`  |
| 3203   | Layout 3             | `2ef58a4cde3e`  |
| 3193   | Layout 3             | `2ef58a4cde3e`  |
| 3186   | Layout 3             | `2ef58a4cde3e`  |
| 3177   | Layout 3             | `2ef58a4cde3e`  |
| 3169   | Layout 3             | `2ef58a4cde3e`  |
| 3158   | Layout 3             | `2ef58a4cde3e`  |
| 3151   | Layout 3             | `2ef58a4cde3e`  |
| 3144   | Layout 3             | `2ef58a4cde3e`  |
| 3133   | Layout 3             | `2ef58a4cde3e`  |
| 3125   | Layout 3             | `2ef58a4cde3e`  |
| 3118   | Layout 3             | `2ef58a4cde3e`  |
| 3111   | Layout 3             | `2ef58a4cde3e`  |
| 3103   | Layout 3             | `2ef58a4cde3e`  |
| 3095   | Layout 3             | `2ef58a4cde3e`  |
| 3086   | Layout 3             | `2ef58a4cde3e`  |
| 3072   | Layout 3             | `2ef58a4cde3e`  |
| 3062   | Layout 3             | `2ef58a4cde3e`  |
| 3052   | Layout 3             | `2ef58a4cde3e`  |
| 3045   | Layout 3             | `2ef58a4cde3e`  |
| 3037   | Layout 3             | `2ef58a4cde3e`  |
| 3030   | Layout 3             | `2ef58a4cde3e`  |
| 3021   | Layout 3             | `2ef58a4cde3e`  |
| 3012   | Layout 3             | `2ef58a4cde3e`  |
| 3002   | Layout 3             | `2ef58a4cde3e`  |
| 2995   | Layout 3             | `2ef58a4cde3e`  |
| 2987   | Layout 3             | `2ef58a4cde3e`  |
| 2978   | Layout 3             | `2ef58a4cde3e`  |
| 2970   | Layout 3             | `2ef58a4cde3e`  |
| 2959   | Layout 3             | `2ef58a4cde3e`  |
| 2951   | Layout 3             | `2ef58a4cde3e`  |
| 2942   | Layout 3             | `2ef58a4cde3e`  |
| 2935   | Layout 3             | `2ef58a4cde3e`  |
| 2932   | Layout 3             | `2ef58a4cde3e`  |
| 2923   | Layout 3             | `2ef58a4cde3e`  |
| 2919   | Layout 3             | `2ef58a4cde3e`  |
| 2907   | Layout 3             | `2ef58a4cde3e`  |
| 2900   | Layout 3             | `2ef58a4cde3e`  |
| 2891   | Layout 3             | `2ef58a4cde3e`  |
| 2882   | Layout 3             | `2ef58a4cde3e`  |
| 2872   | Layout 3             | `2ef58a4cde3e`  |
| 2863   | Layout 3             | `2ef58a4cde3e`  |
| 2855   | Layout 2             | `2ef58a4cde3e`  |
| 2849   | Layout 2             | `2ef58a4cde3e`  |
| 2844   | Layout 2             | `2ef58a4cde3e`  |
| 2834   | Layout 2             | `2ef58a4cde3e`  |
| 2825   | Layout 2             | `2ef58a4cde3e`  |
| 2819   | Layout 2             | `2ef58a4cde3e`  |
| 2811   | Layout 2             | `2ef58a4cde3e`  |
| 2803   | Layout 2             | `2ef58a4cde3e`  |
| 2794   | Layout 2             | `2ef58a4cde3e`  |
| 2783   | Layout 2             | `2ef58a4cde3e`  |
| 2774   | Layout 2             | `2ef58a4cde3e`  |
| 2765   | Layout 2             | `2ef58a4cde3e`  |
| 2756   | Layout 2             | `2ef58a4cde3e`  |
| 2750   | Layout 2             | `2ef58a4cde3e`  |
| 2743   | Layout 2             | `2ef58a4cde3e`  |
| 2736   | Layout 2             | `2ef58a4cde3e`  |
| 2726   | Layout 2             | `2ef58a4cde3e`  |
| 2717   | Layout 2             | `2ef58a4cde3e`  |
| 2709   | Layout 2             | `2ef58a4cde3e`  |
| 2703   | Layout 2             | `2ef58a4cde3e`  |
| 2695   | Layout 2             | `2ef58a4cde3e`  |
| 2684   | Layout 2             | `2ef58a4cde3e`  |
| 2672   | Layout 2             | `2ef58a4cde3e`  |
| 2665   | Layout 2             | `2ef58a4cde3e`  |
| 2657   | Layout 2             | `2ef58a4cde3e`  |
| 2649   | Layout 2             | `2ef58a4cde3e`  |
| 2644   | Layout 2             | `2ef58a4cde3e`  |
| 2637   | Layout 2             | `2ef58a4cde3e`  |
| 2629   | Layout 2             | `2ef58a4cde3e`  |
| 2619   | Layout 2             | `2ef58a4cde3e`  |
| 2612   | Layout 2             | `2ef58a4cde3e`  |
| 2606   | Layout 2             | `2ef58a4cde3e`  |
| 2602   | Layout 2             | `2ef58a4cde3e`  |
| 2601   | Layout 2             | `2ef58a4cde3e`  |
| 2592   | Layout 2             | `2ef58a4cde3e`  |
| 2583   | Layout 2             | `2ef58a4cde3e`  |
| 2575   | Layout 2             | `2ef58a4cde3e`  |
| 2567   | Layout 2             | `2ef58a4cde3e`  |
| 2560   | Layout 2             | `2ef58a4cde3e`  |
| 2553   | Layout 2             | `2ef58a4cde3e`  |
| 2545   | Layout 2             | `2ef58a4cde3e`  |
| 2538   | Layout 2             | `2ef58a4cde3e`  |
| 2529   | Layout 2             | `2ef58a4cde3e`  |
| 2519   | Layout 2             | `2ef58a4cde3e`  |
| 2513   | Layout 2             | `2ef58a4cde3e`  |
| 2510   | Layout 2             | `2ef58a4cde3e`  |
| 2507   | Layout 2             | `2ef58a4cde3e`  |
| 2503   | Layout 2             | `2ef58a4cde3e`  |
| 2498   | Layout 2             | `2ef58a4cde3e`  |
| 2492   | Layout 2             | `2ef58a4cde3e`  |
| 2487   | Layout 2             | `2ef58a4cde3e`  |
| 2480   | Layout 2             | `2ef58a4cde3e`  |
| 2474   | Layout 2             | `2ef58a4cde3e`  |
| 2468   | Layout 2             | `2ef58a4cde3e`  |
| 2460   | Layout 2             | `2ef58a4cde3e`  |
| 2453   | Layout 2             | `2ef58a4cde3e`  |
| 2444   | Layout 2             | `2ef58a4cde3e`  |
| 2438   | Layout 2             | `2ef58a4cde3e`  |
| 2434   | Layout 2             | `2ef58a4cde3e`  |
| 2429   | Layout 2             | `2ef58a4cde3e`  |
| 2421   | Layout 2             | `2ef58a4cde3e`  |
| 2414   | Layout 2             | `2ef58a4cde3e`  |
| 2407   | Layout 2             | `2ef58a4cde3e`  |
| 2401   | Layout 2             | `2ef58a4cde3e`  |
| 2397   | Layout 2             | `2ef58a4cde3e`  |
| 2393   | Layout 2             | `2ef58a4cde3e`  |
| 2384   | Layout 2             | `2ef58a4cde3e`  |
| 2378   | Layout 2             | `2ef58a4cde3e`  |
| 2372   | Layout 2             | `2ef58a4cde3e`  |
| 2358   | Layout 2             | `2ef58a4cde3e`  |
| 2352   | Layout 2             | `2ef58a4cde3e`  |
| 2347   | Layout 2             | `2ef58a4cde3e`  |
| 2343   | Layout 2             | `2ef58a4cde3e`  |
| 2335   | Layout 2             | `2ef58a4cde3e`  |
| 2327   | Layout 2             | `2ef58a4cde3e`  |
| 2324   | Layout 2             | `2ef58a4cde3e`  |
| 2319   | Layout 2             | `2ef58a4cde3e`  |
| 2313   | Layout 2             | `2ef58a4cde3e`  |
| 2308   | Layout 2             | `2ef58a4cde3e`  |
| 2302   | Layout 2             | `2ef58a4cde3e`  |
| 2295   | Layout 2             | `2ef58a4cde3e`  |
| 2290   | Layout 2             | `2ef58a4cde3e`  |
| 2284   | Layout 2             | `2ef58a4cde3e`  |
| 2276   | Layout 2             | `2ef58a4cde3e`  |
| 2269   | Layout 2             | `2ef58a4cde3e`  |
| 2259   | Layout 2             | `2ef58a4cde3e`  |
| 2250   | Layout 2             | `2ef58a4cde3e`  |
| 2243   | Layout 2             | `2ef58a4cde3e`  |
| 2235   | Layout 2             | `2ef58a4cde3e`  |
| 2229   | Layout 2             | `2ef58a4cde3e`  |
| 2224   | Layout 2             | `2ef58a4cde3e`  |
| 2218   | Layout 2             | `2ef58a4cde3e`  |
| 2215   | Layout 2             | `2ef58a4cde3e`  |
| 2207   | Layout 2             | `2ef58a4cde3e`  |
| 2203   | Layout 2             | `2ef58a4cde3e`  |
| 2196   | Layout 2             | `2ef58a4cde3e`  |
| 2192   | Layout 2             | `2ef58a4cde3e`  |
| 2189   | Layout 2             | `2ef58a4cde3e`  |
| 2183   | Layout 2             | `2ef58a4cde3e`  |
| 2179   | Layout 2             | `2ef58a4cde3e`  |
| 2171   | Layout 2             | `2ef58a4cde3e`  |
| 2163   | Layout 2             | `2ef58a4cde3e`  |
| 2156   | Layout 2             | `2ef58a4cde3e`  |
| 2151   | Layout 2             | `2ef58a4cde3e`  |
| 2147   | Layout 2             | `2ef58a4cde3e`  |
| 2142   | Layout 2             | `2ef58a4cde3e`  |
| 2138   | Layout 2             | `2ef58a4cde3e`  |
| 2134   | Layout 2             | `2ef58a4cde3e`  |
| 2130   | Layout 2             | `2ef58a4cde3e`  |
| 2122   | Layout 2             | `2ef58a4cde3e`  |
| 2107   | Layout 2             | `2ef58a4cde3e`  |
| 2098   | Layout 2             | `2ef58a4cde3e`  |
| 2089   | Layout 2             | `2ef58a4cde3e`  |
| 2081   | Layout 2             | `2ef58a4cde3e`  |
| 2073   | Layout 2             | `2ef58a4cde3e`  |
| 2067   | Layout 2             | `2ef58a4cde3e`  |
| 2063   | Layout 2             | `2ef58a4cde3e`  |
| 2059   | Layout 2             | `2ef58a4cde3e`  |
| 2052   | Layout 2             | `2ef58a4cde3e`  |
| 2044   | Layout 2             | `2ef58a4cde3e`  |
| 2039   | Layout 2             | `2ef58a4cde3e`  |
| 2032   | Layout 2             | `2ef58a4cde3e`  |
| 2025   | Layout 2             | `2ef58a4cde3e`  |
| 2011   | Layout 2             | `2ef58a4cde3e`  |
| 2005   | Layout 2             | `2ef58a4cde3e`  |
| 2000   | Layout 2             | `2ef58a4cde3e`  |
| 1996   | Layout 2             | `2ef58a4cde3e`  |
| 1991   | Layout 2             | `2ef58a4cde3e`  |
| 1985   | Layout 2             | `2ef58a4cde3e`  |
| 1980   | Layout 2             | `2ef58a4cde3e`  |
| 1969   | Layout 2             | `2ef58a4cde3e`  |
| 1964   | Layout 2             | `2ef58a4cde3e`  |
| 1958   | Layout 2             | `2ef58a4cde3e`  |
| 1950   | Layout 2             | `2ef58a4cde3e`  |
| 1945   | Layout 2             | `2ef58a4cde3e`  |
| 1937   | Layout 2             | `2ef58a4cde3e`  |
| 1933   | Layout 2             | `2ef58a4cde3e`  |
| 1927   | Layout 2             | `2ef58a4cde3e`  |
| 1921   | Layout 2             | `2ef58a4cde3e`  |
| 1914   | Layout 2             | `2ef58a4cde3e`  |
| 1908   | Layout 2             | `2ef58a4cde3e`  |
| 1897   | Layout 2             | `2ef58a4cde3e`  |
| 1892   | Layout 2             | `2ef58a4cde3e`  |
| 1886   | Layout 2             | `2ef58a4cde3e`  |
| 1881   | Layout 2             | `2ef58a4cde3e`  |
| 1871   | Layout 2             | `2ef58a4cde3e`  |
| 1866   | Layout 2             | `2ef58a4cde3e`  |
| 1862   | Layout 2             | `2ef58a4cde3e`  |
| 1854   | Layout 2             | `2ef58a4cde3e`  |
| 1846   | Layout 2             | `2ef58a4cde3e`  |
| 1838   | Layout 2             | `2ef58a4cde3e`  |
| 1832   | Layout 2             | `2ef58a4cde3e`  |
| 1826   | Layout 2             | `2ef58a4cde3e`  |
| 1822   | Layout 2             | `2ef58a4cde3e`  |
| 1818   | Layout 2             | `2ef58a4cde3e`  |
| 1804   | Layout 2             | `2ef58a4cde3e`  |
| 1794   | Layout 2             | `2ef58a4cde3e`  |
| 1790   | Layout 2             | `2ef58a4cde3e`  |
| 1784   | Layout 2             | `2ef58a4cde3e`  |
| 1774   | Layout 2             | `2ef58a4cde3e`  |
| 1771   | Layout 2             | `2ef58a4cde3e`  |
| 1762   | Layout 2             | `2ef58a4cde3e`  |
| 1759   | Layout 2             | `2ef58a4cde3e`  |
| 1754   | Layout 2             | `2ef58a4cde3e`  |
| 1749   | Layout 2             | `2ef58a4cde3e`  |
| 1743   | Layout 2             | `2ef58a4cde3e`  |
| 1737   | Layout 2             | `2ef58a4cde3e`  |
| 1731   | Layout 2             | `2ef58a4cde3e`  |
| 1725   | Layout 2             | `2ef58a4cde3e`  |
| 1717   | Layout 2             | `2ef58a4cde3e`  |
| 1710   | Layout 2             | `2ef58a4cde3e`  |
| 1704   | Layout 2             | `2ef58a4cde3e`  |
| 1698   | Layout 2             | `2ef58a4cde3e`  |
| 1690   | Layout 2             | `2ef58a4cde3e`  |
| 1685   | Layout 1             | `2ef58a4cde3e`  |
| 1680   | Layout 1             | `2ef58a4cde3e`  |
| 1674   | Layout 1             | `2ef58a4cde3e`  |
| 1668   | Layout 1             | `2ef58a4cde3e`  |
| 1659   | Layout 1             | `2ef58a4cde3e`  |
| 1649   | Layout 1             | `2ef58a4cde3e`  |
| 1642   | Layout 1             | `2ef58a4cde3e`  |
| 1636   | Layout 1             | `2ef58a4cde3e`  |
| 1628   | Layout 1             | `2ef58a4cde3e`  |
| 1622   | Layout 1             | `2ef58a4cde3e`  |
| 1614   | Layout 1             | `2ef58a4cde3e`  |
| 1608   | Layout 1             | `2ef58a4cde3e`  |
| 1602   | Layout 1             | `2ef58a4cde3e`  |
| 1598   | Layout 1             | `2ef58a4cde3e`  |
| 1594   | Layout 1             | `2ef58a4cde3e`  |
| 1590   | Layout 1             | `2ef58a4cde3e`  |
| 1587   | Layout 1             | `2ef58a4cde3e`  |
| 1584   | Layout 1             | `2ef58a4cde3e`  |
| 1579   | Layout 1             | `2ef58a4cde3e`  |
| 1572   | Layout 1             | `2ef58a4cde3e`  |
| 1565   | Layout 1             | `2ef58a4cde3e`  |
| 1559   | Layout 1             | `2ef58a4cde3e`  |
| 1554   | Layout 1             | `2ef58a4cde3e`  |
| 1547   | Layout 1             | `2ef58a4cde3e`  |
| 1537   | Layout 1             | `2ef58a4cde3e`  |
| 1529   | Layout 1             | `2ef58a4cde3e`  |
| 1524   | Layout 1             | `2ef58a4cde3e`  |
| 1519   | Layout 1             | `2ef58a4cde3e`  |
| 1509   | Layout 1             | `2ef58a4cde3e`  |
| 1506   | Layout 1             | `2ef58a4cde3e`  |
| 1504   | Layout 1             | `2ef58a4cde3e`  |
| 1500   | Layout 1             | `2ef58a4cde3e`  |
| 1493   | Layout 1             | `2ef58a4cde3e`  |
| 1489   | Layout 1             | `2ef58a4cde3e`  |
| 1485   | Layout 1             | `2ef58a4cde3e`  |
| 1481   | Layout 1             | `2ef58a4cde3e`  |
| 1474   | Layout 1             | `2ef58a4cde3e`  |
| 1466   | Layout 1             | `2ef58a4cde3e`  |
| 1462   | Layout 1             | `2ef58a4cde3e`  |
| 1459   | Layout 1             | `2ef58a4cde3e`  |
| 1453   | Layout 1             | `2ef58a4cde3e`  |
| 1450   | Layout 1             | `2ef58a4cde3e`  |
| 1445   | Layout 1             | `2ef58a4cde3e`  |
| 1439   | Layout 1             | `2ef58a4cde3e`  |
| 1433   | Layout 1             | `2ef58a4cde3e`  |
| 1430   | Layout 1             | `2ef58a4cde3e`  |
| 1426   | Layout 1             | `2ef58a4cde3e`  |
| 1421   | Layout 1             | `2ef58a4cde3e`  |
| 1417   | Layout 1             | `2ef58a4cde3e`  |
| 1416   | Layout 1             | `2ef58a4cde3e`  |
| 1409   | Layout 1             | `2ef58a4cde3e`  |
| 1405   | Layout 1             | `2ef58a4cde3e`  |
| 1401   | Layout 1             | `2ef58a4cde3e`  |
| 1396   | Layout 1             | `2ef58a4cde3e`  |
| 1391   | Layout 1             | `2ef58a4cde3e`  |
| 1390   | Layout 1             | `2ef58a4cde3e`  |
| 1386   | Layout 1             | `2ef58a4cde3e`  |
| 1381   | Layout 1             | `2ef58a4cde3e`  |
| 1379   | Layout 1             | `2ef58a4cde3e`  |
| 1372   | Layout 1             | `2ef58a4cde3e`  |
| 1366   | Layout 1             | `2ef58a4cde3e`  |
| 1364   | Layout 1             | `2ef58a4cde3e`  |
| 1363   | Layout 1             | `2ef58a4cde3e`  |
| 1360   | Layout 1             | `2ef58a4cde3e`  |
| 1358   | Layout 1             | `2ef58a4cde3e`  |
| 1355   | Layout 1             | `2ef58a4cde3e`  |
| 1351   | Layout 1             | `2ef58a4cde3e`  |
| 1348   | No documented layout | `2ef58a4cde3e`  |
| 1346   | No documented layout | `2ef58a4cde3e`  |
| 1341   | No documented layout | `2ef58a4cde3e`  |
| 1340   | No documented layout | `2ef58a4cde3e`  |
| 1338   | No documented layout | `2ef58a4cde3e`  |
| 1335   | No documented layout | `2ef58a4cde3e`  |
| 1333   | No documented layout | `2ef58a4cde3e`  |
| 1329   | No documented layout | `2ef58a4cde3e`  |
| 1327   | No documented layout | `2ef58a4cde3e`  |
| 1324   | No documented layout | `2ef58a4cde3e`  |
| 1321   | No documented layout | `2ef58a4cde3e`  |
| 1319   | No documented layout | `2ef58a4cde3e`  |
| 1318   | No documented layout | `2ef58a4cde3e`  |
| 1316   | No documented layout | `2ef58a4cde3e`  |
| 1313   | No documented layout | `2ef58a4cde3e`  |
| 1311   | No documented layout | `2ef58a4cde3e`  |
| 1309   | No documented layout | `2ef58a4cde3e`  |
| 1304   | No documented layout | `2ef58a4cde3e`  |
| 1292   | No documented layout | `2ef58a4cde3e`  |
| 1286   | No documented layout | `2ef58a4cde3e`  |
| 1280   | No documented layout | `2ef58a4cde3e`  |
| 1276   | No documented layout | `2ef58a4cde3e`  |
| 1267   | No documented layout | `2ef58a4cde3e`  |
| 1261   | No documented layout | `2ef58a4cde3e`  |
| 1256   | No documented layout | `2ef58a4cde3e`  |
| 1250   | No documented layout | `2ef58a4cde3e`  |
| 1246   | No documented layout | `2ef58a4cde3e`  |
| 1239   | No documented layout | `2ef58a4cde3e`  |
| 1230   | No file              | `2ef58a4cde3e`  |
| 1226   | No file              | `2ef58a4cde3e`  |
| 1220   | No file              | `2ef58a4cde3e`  |
| 1217   | No file              | `2ef58a4cde3e`  |
| 1211   | No file              | `2ef58a4cde3e`  |
| 1210   | No file              | `2ef58a4cde3e`  |
| 1208   | No file              | `2ef58a4cde3e`  |
| 1203   | No file              | `2ef58a4cde3e`  |
| 1197   | No file              | `2ef58a4cde3e`  |
| 1194   | No file              | `2ef58a4cde3e`  |
| 1192   | No file              | `2ef58a4cde3e`  |
| 1187   | No file              | `2ef58a4cde3e`  |
| 1183   | No file              | `2ef58a4cde3e`  |
| 1177   | No file              | `2ef58a4cde3e`  |
| 1173   | No file              | `2ef58a4cde3e`  |
| 1167   | No file              | `2ef58a4cde3e`  |
| 1164   | No file              | `2ef58a4cde3e`  |
| 1156   | No file              | `2ef58a4cde3e`  |
| 1149   | No file              | `2ef58a4cde3e`  |
| 1144   | No file              | `2ef58a4cde3e`  |
| 1137   | No file              | `2ef58a4cde3e`  |
| 1132   | No file              | `2ef58a4cde3e`  |
| 1127   | No documented layout | `2ef58a4cde3e`  |
| 1122   | No documented layout | `2ef58a4cde3e`  |
| 1118   | No documented layout | `2ef58a4cde3e`  |
| 1114   | No documented layout | `2ef58a4cde3e`  |
| 1109   | No documented layout | `2ef58a4cde3e`  |
| 1102   | No file              | `2ef58a4cde3e`  |
| 1096   | No file              | `2ef58a4cde3e`  |
| 1088   | No file              | `2ef58a4cde3e`  |
| 1081   | No file              | `2ef58a4cde3e`  |
| 1076   | No file              | `2ef58a4cde3e`  |
| 1069   | No file              | `2ef58a4cde3e`  |
| 1064   | No file              | `2ef58a4cde3e`  |
| 1058   | No file              | `2ef58a4cde3e`  |
| 1051   | No file              | `2ef58a4cde3e`  |
| 1044   | No file              | `2ef58a4cde3e`  |
| 1036   | No file              | `2ef58a4cde3e`  |
| 1026   | No file              | `2ef58a4cde3e`  |
| 1016   | No file              | `2ef58a4cde3e`  |
| 1009   | No file              | `2ef58a4cde3e`  |
| 1005   | No file              | `2ef58a4cde3e`  |
| 1000   | No file              | `2ef58a4cde3e`  |
| 998    | No file              | `2ef58a4cde3e`  |
| 990    | No file              | `2ef58a4cde3e`  |
| 979    | No file              | `2ef58a4cde3e`  |
| 972    | No file              | `2ef58a4cde3e`  |
| 963    | No file              | `2ef58a4cde3e`  |
| 955    | No file              | `2ef58a4cde3e`  |
| 946    | No file              | `2ef58a4cde3e`  |
| 938    | No file              | `2ef58a4cde3e`  |
| 927    | No file              | `2ef58a4cde3e`  |
| 911    | No file              | `2ef58a4cde3e`  |
| 904    | No file              | `2ef58a4cde3e`  |
| 899    | No file              | `2ef58a4cde3e`  |
| 894    | No file              | `2ef58a4cde3e`  |
| 885    | No file              | `2ef58a4cde3e`  |
| 879    | No file              | `2ef58a4cde3e`  |
| 872    | No file              | `2ef58a4cde3e`  |
| 864    | No file              | `2ef58a4cde3e`  |
| 855    | No file              | `2ef58a4cde3e`  |
| 853    | No file              | `2ef58a4cde3e`  |
| 845    | No file              | `2ef58a4cde3e`  |
| 837    | No file              | `2ef58a4cde3e`  |
| 829    | No file              | `2ef58a4cde3e`  |
| 822    | No file              | `2ef58a4cde3e`  |
| 814    | No file              | `2ef58a4cde3e`  |
| 805    | No file              | `2ef58a4cde3e`  |
| 794    | No file              | `2ef58a4cde3e`  |
| 787    | No file              | `2ef58a4cde3e`  |
| 780    | No file              | `2ef58a4cde3e`  |
| 771    | No file              | `2ef58a4cde3e`  |
| 760    | No file              | `2ef58a4cde3e`  |
| 748    | No file              | `2ef58a4cde3e`  |
| 741    | No file              | `2ef58a4cde3e`  |
| 736    | No file              | `2ef58a4cde3e`  |
| 731    | No file              | `2ef58a4cde3e`  |
| 723    | No file              | `2ef58a4cde3e`  |
| 711    | No file              | `2ef58a4cde3e`  |
| 707    | No file              | `2ef58a4cde3e`  |
| 697    | No file              | `2ef58a4cde3e`  |
| 689    | No file              | `2ef58a4cde3e`  |
| 683    | No file              | `2ef58a4cde3e`  |
| 678    | No file              | `2ef58a4cde3e`  |
| 670    | No file              | `2ef58a4cde3e`  |
| 661    | No file              | `2ef58a4cde3e`  |
| 656    | No file              | `2ef58a4cde3e`  |
| 652    | No file              | `2ef58a4cde3e`  |
| 643    | No file              | `2ef58a4cde3e`  |
| 637    | No file              | `2ef58a4cde3e`  |
| 630    | No file              | `2ef58a4cde3e`  |
| 627    | No file              | `2ef58a4cde3e`  |
| 621    | No file              | `2ef58a4cde3e`  |
| 617    | No file              | `2ef58a4cde3e`  |
| 615    | No file              | `2ef58a4cde3e`  |
| 606    | No file              | `2ef58a4cde3e`  |
| 599    | No file              | `2ef58a4cde3e`  |
| 592    | No file              | `2ef58a4cde3e`  |
| 586    | No file              | `2ef58a4cde3e`  |
| 577    | No file              | `2ef58a4cde3e`  |
| 569    | No file              | `2ef58a4cde3e`  |
| 561    | No file              | `2ef58a4cde3e`  |
| 554    | No file              | `2ef58a4cde3e`  |
| 542    | No file              | `2ef58a4cde3e`  |
| 532    | No file              | `2ef58a4cde3e`  |
| 531    | No file              | `2ef58a4cde3e`  |
| 526    | No file              | `2ef58a4cde3e`  |
| 521    | No file              | `2ef58a4cde3e`  |
| 517    | No file              | `2ef58a4cde3e`  |
| 510    | No file              | `2ef58a4cde3e`  |
| 508    | No file              | `2ef58a4cde3e`  |
| 504    | No file              | `2ef58a4cde3e`  |
| 497    | No file              | `2ef58a4cde3e`  |
| 491    | No file              | `2ef58a4cde3e`  |
| 485    | No file              | `2ef58a4cde3e`  |
| 478    | No file              | `2ef58a4cde3e`  |
| 472    | No file              | `2ef58a4cde3e`  |
| 466    | No file              | `2ef58a4cde3e`  |
| 457    | No file              | `2ef58a4cde3e`  |
| 452    | No file              | `2ef58a4cde3e`  |
| 449    | No file              | `2ef58a4cde3e`  |
| 435    | No file              | `2ef58a4cde3e`  |

<!-- versions:end -->

## Companion Files

| File                 | Required | Role                                                                    |
| -------------------- | -------- | ----------------------------------------------------------------------- |
| `barter_npclist.bss` | Optional | The barter NPC of each region key                                       |
| `languagedata_*.loc` | Optional | Region names (type 17), item names (type 0) and barter category names (type 37) |

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset                  | Type                          | Field                 | Notes                                                        |
| ----------------------- | ----------------------------- | --------------------- | ------------------------------------------------------------ |
| `+0x00`                 | char[4]                       | magic                 | ASCII `PABR`                                                 |
| `+0x04`                 | u32                           | region_count          | Number of `regions`; `91` on client 3474                     |
| `+0x08`                 | Region[region_count]          | regions               | The trade item barter slots                                  |
| `regions+0x00`          | u32                           | material_region_count | Number of `material_regions`; `91` on client 3474            |
| `regions+0x04`          | Region[material_region_count] | material_regions      | The material barter slots                                    |
| `material_regions+0x00` | String Table                  | string_table          | The PABR string table, present but empty                     |
| `string_table+0x00`     | u32                           | string_table_start    | Absolute offset of `string_count`, where `material_regions` ends |
| `string_table+0x04`     | u32                           | zero                  | Always `0`                                                   |

Both lists hold the 91 region keys of `barter_npclist.bss` once each
(client 3474), in neither key order nor the order of that file, and the two
lists do not share one order.

### Region (variable: 6 bytes + entries)

| Offset  | Type               | Field       | Notes                                                       |
| ------- | ------------------ | ----------- | ----------------------------------------------------------- |
| `+0x00` | u16                | region_key  | `regioninfo.bss` region key; a `barter_npclist.bss` key     |
| `+0x02` | u32                | entry_count | Number of `entries`; `40` in `regions`, `41` in `material_regions` |
| `+0x06` | Entry[entry_count] | entries     | The region's slots; see Entry                               |

### Entry (70 bytes)

The row of [`barter_special.bss`](barter_special_bss.md) has the same
layout.

| Offset  | Type     | Field             | Notes                                                       |
| ------- | -------- | ----------------- | ----------------------------------------------------------- |
| `+0x00` | u16      | barter_region_key | Equals `region_key` on every entry (client 3474)            |
| `+0x02` | u32      | select_rate       | `0` on every sub group entry; see Open Questions            |
| `+0x06` | Exchange | exchange          | All `0` on every sub group entry; see Exchange              |
| `+0x3e` | u32      | barter_sub_group  | A `bartersubgroup.bss` group key in the same list, or `0` for an exchange of the slot's own |
| `+0x42` | u32      | barter_category   | Bit mask as in `bartersubgroup.bss`; `0` on every sub group entry and every material entry (client 3474) |

### Exchange (56 bytes)

Same structure as the Exchange of
[`bartersubgroup.bss`](bartersubgroup_bss.md#exchange-56-bytes). The notes
count the entries without a sub group (client 3474).

| Offset  | Type | Field              | Notes                                                              |
| ------- | ---- | ------------------ | ------------------------------------------------------------------ |
| `+0x00` | u32  | from_item_key      | The item the player hands over, `enchant_level << 24 \| item_id`; level `0` on every entry |
| `+0x04` | u64  | from_min_count     | Fewest of `from_item_key` the exchange asks for                    |
| `+0x0c` | u64  | from_max_count     | Equals `from_min_count` on every entry                             |
| `+0x14` | u32  | to_item_key        | The item the player gets, `enchant_level << 24 \| item_id`; level `0` on every entry |
| `+0x18` | u64  | to_min_count       | Fewest of `to_item_key` the exchange gives                         |
| `+0x20` | u64  | to_max_count       | Most of `to_item_key` the exchange gives                           |
| `+0x28` | u32  | barter_need_point  | `14286` or `21650` in the trade item list, `61430` or `29430` in the material list |
| `+0x2c` | u32  | exchange_max_count | `1` to `10` in the trade item list, `1` to `3` in the material list |
| `+0x30` | u32  | exchange_min       | `0` to `1000000`                                                   |
| `+0x34` | u32  | exchange_max       | `1000000`, or `0` on 410 material entries                          |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Layout 2

`barter_category` is one byte that holds the category number itself.

### Entry (67 bytes)

| Offset  | Type     | Field             | Notes                                              |
| ------- | -------- | ----------------- | -------------------------------------------------- |
| `+0x00` | u16      | barter_region_key |                                                    |
| `+0x02` | u32      | select_rate       |                                                    |
| `+0x06` | Exchange | exchange          |                                                    |
| `+0x3e` | u32      | barter_sub_group  |                                                    |
| `+0x42` | u8       | barter_category   | The category number: `1` to `7` on the trade item entries without a sub group, `8` on every sub group entry and every material entry (client 1784) |

## Layout 1

The entry ends after `barter_sub_group`: there is no `barter_category`.

### Entry (66 bytes)

| Offset  | Type     | Field             | Notes |
| ------- | -------- | ----------------- | ----- |
| `+0x00` | u16      | barter_region_key |       |
| `+0x02` | u32      | select_rate       |       |
| `+0x06` | Exchange | exchange          |       |
| `+0x3e` | u32      | barter_sub_group  |       |

## Sub Group Entries

On client 3474 the 511 trade item entries with a `barter_sub_group` name
186 of the 197 trade item sub groups, keys `1` to `197`; 9 regions hold
only such entries. The 10 material entries with one sit at slots 6 and 11
of the ship regions `995`, `997`, `999`, `1002` and `1004` and name the
material sub groups `1` to `5`, one per region. A trade item entry names a
group of the first list of `bartersubgroup.bss`, a material entry one of
the second, and every key exists there.

## Field Names

The two lists are the `BarterData` and `MaterialBarterData` sheets of a
private server's `DataSheets.bexcel` on client 1784. Each list holds the
sheet's region keys (`RegionIndex`) once, 81 on client 1784, and a region's
entries are that region's sheet rows in sheet order: matched by region and
place in the region, all 3,240 and 3,321 rows line up. The regions
themselves are in another order than the sheet's.

On the 2,958 trade item rows and 3,316 material rows without a
`BarterSubGroup`, every column matches: `RegionIndex`, `SelectRate`,
`GivedItemKey` with `GivedEnchantLevel` (one packed key), `GivedMinCount`,
`GivedMaxCount`, `TakedItemKey` with `TakedEnchantLevel`, `TakedMinCount`,
`TakedMaxCount`, `BarterNeedPoint`, `ExchangeMaxCount`, `ExchangeMin`,
`ExchangeMax`, `BarterSubGroup` and, in the trade item list,
`BarterCategory`. On the 282 and 5 rows with a `BarterSubGroup`, the
`BarterSubGroup` matches and the file holds `0` in `select_rate` and the
whole Exchange and `8` in `barter_category`, where the sheet fills the
exchange on 120 and 5 of them and leaves `BarterCategory` empty on 162. The
sheet columns `BarterCost`, `ContentsGroup`, `TradeEmployeeExp` and
`BarterTradeExp` are not in the file.

`region_key` and `barter_region_key` both hold the row's `RegionIndex`;
`barter_region_key` takes its name from `barter_npclist.bss`, whose rows
key the same regions. The Exchange field names and the `from` and `to`
naming are explained in
[`bartersubgroup.bss`](bartersubgroup_bss.md#field-names), and the category
values in [Barter Categories](bartersubgroup_bss.md#barter-categories).

## Notes

- On client 3474 the trade item entries without a sub group have one
  category bit set on 2,742 entries and two on 387 (bits 7 and 8 on 369,
  bits 6 and 8 on 18); categories `1` to `9` occur, `10` does not.
- The handler (`_bss/barter_normal/`) shows one row per entry with its
  region's name, the region's NPC from `barter_npclist.bss` and the slot,
  the entry's place in its region from `1`. A sub group entry links to the
  first entry of its group in `bartersubgroup.bss`. The Exchange is read
  with the shared barter reader in `_bss/barter/`, which also walks the two
  lists of `bartersubgroup.bss`.

## Open Questions

### Slot Selection

A region has 40 trade item slots and 41 material slots. The barter windows
read a region's exchanges only through `ToClient_barterWrapper()` and
`ToClient_barterRegionList()`, so which slots a region offers at a time,
and how a sub group entry picks one of its group's exchanges, is not in the
client data read so far. `select_rate` is the lead: `1000000` on 3,084 of the
3,129 trade item slots with an exchange of their own, other values
(`1`, `10000` to `900000`) on 45, and `0` on 1,660 of the 3,721 material
slots with one (client 3474), the same reading as the `select_rate` of
`bartersubgroup.bss` (see its Open Questions).
