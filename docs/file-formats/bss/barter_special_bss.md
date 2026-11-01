# `barter_special.bss` Format

## Purpose

The special barter offers of the Great Ocean barters: one row per offer,
with the item the player hands over, the item the player gets and their
count ranges. The special barter window
(`panel_window_barterinfosearch_special_1.luac`) opens only for a player
with the Value Pack (`isApplyChargeSkill(__eUserChargeType_PremiumPackage)`)
and shows one offer from `ToClient_specialBarterWrapper()`: its from item
and count, its to item and count, and the region and NPC where it can be
traded, which the wrapper gives at run time.

On client 3474 the 105 rows hand over Gold Bars (`3` to `5`) or
`[Level 4]` trade items (`800043` to `800056`) and give Crow Coins (`10`),
Manos accessories, Vell's and Khan's Concentrated Magic, Garmoth's Heart,
crystals, Sethra's Artifacts and other items.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                 | Bytes | Records               | Row bytes |
| ------ | -------------- | -------------------- | ----- | --------------------- | --------- |
| 3      | 1102 and later | `barter_special.bss` | 7,370 | 105 Exchange, 105 Row | 56        |
| 2      | 1261 to 2855   | `barter_special.bss` | 8,194 | 122 Exchange, 122 Row | 56        |
| 1      | 1304 to 1685   | `barter_special.bss` | 9,788 | 148 Exchange, 148 Row | 56        |

| Layout | File                 | Known            | Unknown    |
| ------ | -------------------- | ---------------- | ---------- |
| 3      | `barter_special.bss` | 7,370 B (100.0%) | 0 B (0.0%) |
| 2      | `barter_special.bss` | 8,194 B (100.0%) | 0 B (0.0%) |
| 1      | `barter_special.bss` | 9,788 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 3             | `450d3b6666e9`  |
| 3482   | Layout 3             | `450d3b6666e9`  |
| 3474   | Layout 3             | `450d3b6666e9`  |
| 3473   | Layout 3             | `450d3b6666e9`  |
| 3464   | Layout 3             | `450d3b6666e9`  |
| 3458   | Layout 3             | `450d3b6666e9`  |
| 3454   | Layout 3             | `450d3b6666e9`  |
| 3444   | Layout 3             | `450d3b6666e9`  |
| 3435   | Layout 3             | `450d3b6666e9`  |
| 3426   | Layout 3             | `450d3b6666e9`  |
| 3418   | Layout 3             | `450d3b6666e9`  |
| 3412   | Layout 3             | `450d3b6666e9`  |
| 3402   | Layout 3             | `450d3b6666e9`  |
| 3396   | Layout 3             | `450d3b6666e9`  |
| 3387   | Layout 3             | `450d3b6666e9`  |
| 3381   | Layout 3             | `450d3b6666e9`  |
| 3373   | Layout 3             | `450d3b6666e9`  |
| 3364   | Layout 3             | `450d3b6666e9`  |
| 3356   | Layout 3             | `450d3b6666e9`  |
| 3349   | Layout 3             | `450d3b6666e9`  |
| 3342   | Layout 3             | `450d3b6666e9`  |
| 3335   | Layout 3             | `450d3b6666e9`  |
| 3326   | Layout 3             | `450d3b6666e9`  |
| 3321   | Layout 3             | `450d3b6666e9`  |
| 3314   | Layout 3             | `450d3b6666e9`  |
| 3303   | Layout 3             | `450d3b6666e9`  |
| 3302   | Layout 3             | `450d3b6666e9`  |
| 3293   | Layout 3             | `450d3b6666e9`  |
| 3283   | Layout 3             | `450d3b6666e9`  |
| 3275   | Layout 3             | `450d3b6666e9`  |
| 3267   | Layout 3             | `450d3b6666e9`  |
| 3258   | Layout 3             | `450d3b6666e9`  |
| 3251   | Layout 3             | `450d3b6666e9`  |
| 3242   | Layout 3             | `450d3b6666e9`  |
| 3235   | Layout 3             | `450d3b6666e9`  |
| 3229   | Layout 3             | `450d3b6666e9`  |
| 3212   | Layout 3             | `450d3b6666e9`  |
| 3203   | Layout 3             | `450d3b6666e9`  |
| 3193   | Layout 3             | `450d3b6666e9`  |
| 3186   | Layout 3             | `450d3b6666e9`  |
| 3177   | Layout 3             | `450d3b6666e9`  |
| 3169   | Layout 3             | `450d3b6666e9`  |
| 3158   | Layout 3             | `450d3b6666e9`  |
| 3151   | Layout 3             | `450d3b6666e9`  |
| 3144   | Layout 3             | `450d3b6666e9`  |
| 3133   | Layout 3             | `450d3b6666e9`  |
| 3125   | Layout 3             | `450d3b6666e9`  |
| 3118   | Layout 3             | `450d3b6666e9`  |
| 3111   | Layout 3             | `450d3b6666e9`  |
| 3103   | Layout 3             | `450d3b6666e9`  |
| 3095   | Layout 3             | `450d3b6666e9`  |
| 3086   | Layout 3             | `450d3b6666e9`  |
| 3072   | Layout 3             | `450d3b6666e9`  |
| 3062   | Layout 3             | `450d3b6666e9`  |
| 3052   | Layout 3             | `450d3b6666e9`  |
| 3045   | Layout 3             | `450d3b6666e9`  |
| 3037   | Layout 3             | `450d3b6666e9`  |
| 3030   | Layout 3             | `450d3b6666e9`  |
| 3021   | Layout 3             | `450d3b6666e9`  |
| 3012   | Layout 3             | `450d3b6666e9`  |
| 3002   | Layout 3             | `450d3b6666e9`  |
| 2995   | Layout 3             | `450d3b6666e9`  |
| 2987   | Layout 3             | `450d3b6666e9`  |
| 2978   | Layout 3             | `450d3b6666e9`  |
| 2970   | Layout 3             | `450d3b6666e9`  |
| 2959   | Layout 3             | `450d3b6666e9`  |
| 2951   | Layout 3             | `450d3b6666e9`  |
| 2942   | Layout 3             | `450d3b6666e9`  |
| 2935   | Layout 3             | `450d3b6666e9`  |
| 2932   | Layout 3             | `450d3b6666e9`  |
| 2923   | Layout 3             | `450d3b6666e9`  |
| 2919   | Layout 3             | `450d3b6666e9`  |
| 2907   | Layout 3             | `450d3b6666e9`  |
| 2900   | Layout 3             | `450d3b6666e9`  |
| 2891   | Layout 3             | `450d3b6666e9`  |
| 2882   | Layout 3             | `450d3b6666e9`  |
| 2872   | Layout 3             | `450d3b6666e9`  |
| 2863   | Layout 3             | `450d3b6666e9`  |
| 2855   | Layout 2             | `450d3b6666e9`  |
| 2849   | Layout 2             | `450d3b6666e9`  |
| 2844   | Layout 2             | `450d3b6666e9`  |
| 2834   | Layout 2             | `450d3b6666e9`  |
| 2825   | Layout 2             | `450d3b6666e9`  |
| 2819   | Layout 2             | `450d3b6666e9`  |
| 2811   | Layout 2             | `450d3b6666e9`  |
| 2803   | Layout 2             | `450d3b6666e9`  |
| 2794   | Layout 2             | `450d3b6666e9`  |
| 2783   | Layout 2             | `450d3b6666e9`  |
| 2774   | Layout 2             | `450d3b6666e9`  |
| 2765   | Layout 2             | `450d3b6666e9`  |
| 2756   | Layout 2             | `450d3b6666e9`  |
| 2750   | Layout 2             | `450d3b6666e9`  |
| 2743   | Layout 2             | `450d3b6666e9`  |
| 2736   | Layout 2             | `450d3b6666e9`  |
| 2726   | Layout 2             | `450d3b6666e9`  |
| 2717   | Layout 2             | `450d3b6666e9`  |
| 2709   | Layout 2             | `450d3b6666e9`  |
| 2703   | Layout 2             | `450d3b6666e9`  |
| 2695   | Layout 2             | `450d3b6666e9`  |
| 2684   | Layout 2             | `450d3b6666e9`  |
| 2672   | Layout 2             | `450d3b6666e9`  |
| 2665   | Layout 2             | `450d3b6666e9`  |
| 2657   | Layout 2             | `450d3b6666e9`  |
| 2649   | Layout 2             | `450d3b6666e9`  |
| 2644   | Layout 2             | `450d3b6666e9`  |
| 2637   | Layout 2             | `450d3b6666e9`  |
| 2629   | Layout 2             | `450d3b6666e9`  |
| 2619   | Layout 2             | `450d3b6666e9`  |
| 2612   | Layout 2             | `450d3b6666e9`  |
| 2606   | Layout 2             | `450d3b6666e9`  |
| 2602   | Layout 2             | `450d3b6666e9`  |
| 2601   | Layout 2             | `450d3b6666e9`  |
| 2592   | Layout 2             | `450d3b6666e9`  |
| 2583   | Layout 2             | `450d3b6666e9`  |
| 2575   | Layout 2             | `450d3b6666e9`  |
| 2567   | Layout 2             | `450d3b6666e9`  |
| 2560   | Layout 2             | `450d3b6666e9`  |
| 2553   | Layout 2             | `450d3b6666e9`  |
| 2545   | Layout 2             | `450d3b6666e9`  |
| 2538   | Layout 2             | `450d3b6666e9`  |
| 2529   | Layout 2             | `450d3b6666e9`  |
| 2519   | Layout 2             | `450d3b6666e9`  |
| 2513   | Layout 2             | `450d3b6666e9`  |
| 2510   | Layout 2             | `450d3b6666e9`  |
| 2507   | Layout 2             | `450d3b6666e9`  |
| 2503   | Layout 2             | `450d3b6666e9`  |
| 2498   | Layout 2             | `450d3b6666e9`  |
| 2492   | Layout 2             | `450d3b6666e9`  |
| 2487   | Layout 2             | `450d3b6666e9`  |
| 2480   | Layout 2             | `450d3b6666e9`  |
| 2474   | Layout 2             | `450d3b6666e9`  |
| 2468   | Layout 2             | `450d3b6666e9`  |
| 2460   | Layout 2             | `450d3b6666e9`  |
| 2453   | Layout 2             | `450d3b6666e9`  |
| 2444   | Layout 2             | `450d3b6666e9`  |
| 2438   | Layout 2             | `450d3b6666e9`  |
| 2434   | Layout 2             | `450d3b6666e9`  |
| 2429   | Layout 2             | `450d3b6666e9`  |
| 2421   | Layout 2             | `450d3b6666e9`  |
| 2414   | Layout 2             | `450d3b6666e9`  |
| 2407   | Layout 2             | `450d3b6666e9`  |
| 2401   | Layout 2             | `450d3b6666e9`  |
| 2397   | Layout 2             | `450d3b6666e9`  |
| 2393   | Layout 2             | `450d3b6666e9`  |
| 2384   | Layout 2             | `450d3b6666e9`  |
| 2378   | Layout 2             | `450d3b6666e9`  |
| 2372   | Layout 2             | `450d3b6666e9`  |
| 2358   | Layout 2             | `450d3b6666e9`  |
| 2352   | Layout 2             | `450d3b6666e9`  |
| 2347   | Layout 2             | `450d3b6666e9`  |
| 2343   | Layout 2             | `450d3b6666e9`  |
| 2335   | Layout 2             | `450d3b6666e9`  |
| 2327   | Layout 2             | `450d3b6666e9`  |
| 2324   | Layout 2             | `450d3b6666e9`  |
| 2319   | Layout 2             | `450d3b6666e9`  |
| 2313   | Layout 2             | `450d3b6666e9`  |
| 2308   | Layout 2             | `450d3b6666e9`  |
| 2302   | Layout 2             | `450d3b6666e9`  |
| 2295   | Layout 2             | `450d3b6666e9`  |
| 2290   | Layout 2             | `450d3b6666e9`  |
| 2284   | Layout 2             | `450d3b6666e9`  |
| 2276   | Layout 2             | `450d3b6666e9`  |
| 2269   | Layout 2             | `450d3b6666e9`  |
| 2259   | Layout 2             | `450d3b6666e9`  |
| 2250   | Layout 2             | `450d3b6666e9`  |
| 2243   | Layout 2             | `450d3b6666e9`  |
| 2235   | Layout 2             | `450d3b6666e9`  |
| 2229   | Layout 2             | `450d3b6666e9`  |
| 2224   | Layout 2             | `450d3b6666e9`  |
| 2218   | Layout 2             | `450d3b6666e9`  |
| 2215   | Layout 2             | `450d3b6666e9`  |
| 2207   | Layout 2             | `450d3b6666e9`  |
| 2203   | Layout 2             | `450d3b6666e9`  |
| 2196   | Layout 2             | `450d3b6666e9`  |
| 2192   | Layout 2             | `450d3b6666e9`  |
| 2189   | Layout 2             | `450d3b6666e9`  |
| 2183   | Layout 2             | `450d3b6666e9`  |
| 2179   | Layout 2             | `450d3b6666e9`  |
| 2171   | Layout 2             | `450d3b6666e9`  |
| 2163   | Layout 2             | `450d3b6666e9`  |
| 2156   | Layout 2             | `450d3b6666e9`  |
| 2151   | Layout 2             | `450d3b6666e9`  |
| 2147   | Layout 2             | `450d3b6666e9`  |
| 2142   | Layout 2             | `450d3b6666e9`  |
| 2138   | Layout 2             | `450d3b6666e9`  |
| 2134   | Layout 2             | `450d3b6666e9`  |
| 2130   | Layout 2             | `450d3b6666e9`  |
| 2122   | Layout 2             | `450d3b6666e9`  |
| 2107   | Layout 2             | `450d3b6666e9`  |
| 2098   | Layout 2             | `450d3b6666e9`  |
| 2089   | Layout 2             | `450d3b6666e9`  |
| 2081   | Layout 2             | `450d3b6666e9`  |
| 2073   | Layout 2             | `450d3b6666e9`  |
| 2067   | Layout 2             | `450d3b6666e9`  |
| 2063   | Layout 2             | `450d3b6666e9`  |
| 2059   | Layout 2             | `450d3b6666e9`  |
| 2052   | Layout 2             | `450d3b6666e9`  |
| 2044   | Layout 2             | `450d3b6666e9`  |
| 2039   | Layout 2             | `450d3b6666e9`  |
| 2032   | Layout 2             | `450d3b6666e9`  |
| 2025   | Layout 2             | `450d3b6666e9`  |
| 2011   | Layout 2             | `450d3b6666e9`  |
| 2005   | Layout 2             | `450d3b6666e9`  |
| 2000   | Layout 2             | `450d3b6666e9`  |
| 1996   | Layout 2             | `450d3b6666e9`  |
| 1991   | Layout 2             | `450d3b6666e9`  |
| 1985   | Layout 2             | `450d3b6666e9`  |
| 1980   | Layout 2             | `450d3b6666e9`  |
| 1969   | Layout 2             | `450d3b6666e9`  |
| 1964   | Layout 2             | `450d3b6666e9`  |
| 1958   | Layout 2             | `450d3b6666e9`  |
| 1950   | Layout 2             | `450d3b6666e9`  |
| 1945   | Layout 2             | `450d3b6666e9`  |
| 1937   | Layout 2             | `450d3b6666e9`  |
| 1933   | Layout 2             | `450d3b6666e9`  |
| 1927   | Layout 2             | `450d3b6666e9`  |
| 1921   | Layout 2             | `450d3b6666e9`  |
| 1914   | Layout 2             | `450d3b6666e9`  |
| 1908   | Layout 2             | `450d3b6666e9`  |
| 1897   | Layout 2             | `450d3b6666e9`  |
| 1892   | Layout 2             | `450d3b6666e9`  |
| 1886   | Layout 2             | `450d3b6666e9`  |
| 1881   | Layout 2             | `450d3b6666e9`  |
| 1871   | Layout 2             | `450d3b6666e9`  |
| 1866   | Layout 2             | `450d3b6666e9`  |
| 1862   | Layout 2             | `450d3b6666e9`  |
| 1854   | Layout 2             | `450d3b6666e9`  |
| 1846   | Layout 2             | `450d3b6666e9`  |
| 1838   | Layout 2             | `450d3b6666e9`  |
| 1832   | Layout 2             | `450d3b6666e9`  |
| 1826   | Layout 2             | `450d3b6666e9`  |
| 1822   | Layout 2             | `450d3b6666e9`  |
| 1818   | Layout 2             | `450d3b6666e9`  |
| 1804   | Layout 2             | `450d3b6666e9`  |
| 1794   | Layout 2             | `450d3b6666e9`  |
| 1790   | Layout 2             | `450d3b6666e9`  |
| 1784   | Layout 2             | `450d3b6666e9`  |
| 1774   | Layout 2             | `450d3b6666e9`  |
| 1771   | Layout 2             | `450d3b6666e9`  |
| 1762   | Layout 2             | `450d3b6666e9`  |
| 1759   | Layout 2             | `450d3b6666e9`  |
| 1754   | Layout 2             | `450d3b6666e9`  |
| 1749   | Layout 2             | `450d3b6666e9`  |
| 1743   | Layout 2             | `450d3b6666e9`  |
| 1737   | Layout 2             | `450d3b6666e9`  |
| 1731   | Layout 2             | `450d3b6666e9`  |
| 1725   | Layout 2             | `450d3b6666e9`  |
| 1717   | Layout 2             | `450d3b6666e9`  |
| 1710   | Layout 2             | `450d3b6666e9`  |
| 1704   | Layout 2             | `450d3b6666e9`  |
| 1698   | Layout 2             | `450d3b6666e9`  |
| 1690   | Layout 2             | `450d3b6666e9`  |
| 1685   | Layout 1             | `450d3b6666e9`  |
| 1680   | Layout 1             | `450d3b6666e9`  |
| 1674   | Layout 1             | `450d3b6666e9`  |
| 1668   | Layout 1             | `450d3b6666e9`  |
| 1659   | Layout 1             | `450d3b6666e9`  |
| 1649   | Layout 1             | `450d3b6666e9`  |
| 1642   | Layout 1             | `450d3b6666e9`  |
| 1636   | Layout 1             | `450d3b6666e9`  |
| 1628   | Layout 1             | `450d3b6666e9`  |
| 1622   | Layout 1             | `450d3b6666e9`  |
| 1614   | Layout 1             | `450d3b6666e9`  |
| 1608   | Layout 1             | `450d3b6666e9`  |
| 1602   | Layout 1             | `450d3b6666e9`  |
| 1598   | Layout 1             | `450d3b6666e9`  |
| 1594   | Layout 1             | `450d3b6666e9`  |
| 1590   | Layout 1             | `450d3b6666e9`  |
| 1587   | Layout 1             | `450d3b6666e9`  |
| 1584   | Layout 1             | `450d3b6666e9`  |
| 1579   | Layout 1             | `450d3b6666e9`  |
| 1572   | Layout 1             | `450d3b6666e9`  |
| 1565   | Layout 1             | `450d3b6666e9`  |
| 1559   | Layout 1             | `450d3b6666e9`  |
| 1554   | Layout 1             | `450d3b6666e9`  |
| 1547   | Layout 1             | `450d3b6666e9`  |
| 1537   | Layout 1             | `450d3b6666e9`  |
| 1529   | Layout 1             | `450d3b6666e9`  |
| 1524   | Layout 1             | `450d3b6666e9`  |
| 1519   | Layout 1             | `450d3b6666e9`  |
| 1509   | Layout 1             | `450d3b6666e9`  |
| 1506   | Layout 1             | `450d3b6666e9`  |
| 1504   | Layout 1             | `450d3b6666e9`  |
| 1500   | Layout 1             | `450d3b6666e9`  |
| 1493   | Layout 1             | `450d3b6666e9`  |
| 1489   | Layout 1             | `450d3b6666e9`  |
| 1485   | Layout 1             | `450d3b6666e9`  |
| 1481   | Layout 1             | `450d3b6666e9`  |
| 1474   | Layout 1             | `450d3b6666e9`  |
| 1466   | Layout 1             | `450d3b6666e9`  |
| 1462   | Layout 1             | `450d3b6666e9`  |
| 1459   | Layout 1             | `450d3b6666e9`  |
| 1453   | Layout 1             | `450d3b6666e9`  |
| 1450   | Layout 1             | `450d3b6666e9`  |
| 1445   | Layout 1             | `450d3b6666e9`  |
| 1439   | Layout 1             | `450d3b6666e9`  |
| 1433   | Layout 1             | `450d3b6666e9`  |
| 1430   | Layout 1             | `450d3b6666e9`  |
| 1426   | Layout 1             | `450d3b6666e9`  |
| 1421   | Layout 1             | `450d3b6666e9`  |
| 1417   | Layout 1             | `450d3b6666e9`  |
| 1416   | Layout 1             | `450d3b6666e9`  |
| 1409   | Layout 1             | `450d3b6666e9`  |
| 1405   | Layout 1             | `450d3b6666e9`  |
| 1401   | Layout 1             | `450d3b6666e9`  |
| 1396   | Layout 1             | `450d3b6666e9`  |
| 1391   | Layout 1             | `450d3b6666e9`  |
| 1390   | Layout 1             | `450d3b6666e9`  |
| 1386   | Layout 1             | `450d3b6666e9`  |
| 1381   | Layout 1             | `450d3b6666e9`  |
| 1379   | Layout 1             | `450d3b6666e9`  |
| 1372   | Layout 1             | `450d3b6666e9`  |
| 1366   | Layout 1             | `450d3b6666e9`  |
| 1364   | Layout 1             | `450d3b6666e9`  |
| 1363   | Layout 1             | `450d3b6666e9`  |
| 1360   | Layout 1             | `450d3b6666e9`  |
| 1358   | Layout 1             | `450d3b6666e9`  |
| 1355   | Layout 1             | `450d3b6666e9`  |
| 1351   | Layout 1             | `450d3b6666e9`  |
| 1348   | Layout 1             | `450d3b6666e9`  |
| 1346   | Layout 1             | `450d3b6666e9`  |
| 1341   | Layout 1             | `450d3b6666e9`  |
| 1340   | Layout 1             | `450d3b6666e9`  |
| 1338   | Layout 1             | `450d3b6666e9`  |
| 1335   | Layout 1             | `450d3b6666e9`  |
| 1333   | Layout 1             | `450d3b6666e9`  |
| 1329   | Layout 1             | `450d3b6666e9`  |
| 1327   | Layout 1             | `450d3b6666e9`  |
| 1324   | Layout 1             | `450d3b6666e9`  |
| 1321   | Layout 1             | `450d3b6666e9`  |
| 1319   | Layout 1             | `450d3b6666e9`  |
| 1318   | Layout 1             | `450d3b6666e9`  |
| 1316   | Layout 1             | `450d3b6666e9`  |
| 1313   | Layout 1             | `450d3b6666e9`  |
| 1311   | Layout 1             | `450d3b6666e9`  |
| 1309   | Layout 1             | `450d3b6666e9`  |
| 1304   | Layout 1             | `450d3b6666e9`  |
| 1292   | Layout 2             | `450d3b6666e9`  |
| 1286   | Layout 2             | `450d3b6666e9`  |
| 1280   | Layout 2             | `450d3b6666e9`  |
| 1276   | Layout 2             | `450d3b6666e9`  |
| 1267   | Layout 2             | `450d3b6666e9`  |
| 1261   | Layout 2             | `450d3b6666e9`  |
| 1256   | No documented layout | `450d3b6666e9`  |
| 1250   | No documented layout | `450d3b6666e9`  |
| 1246   | No documented layout | `450d3b6666e9`  |
| 1239   | No documented layout | `450d3b6666e9`  |
| 1230   | No file              | `450d3b6666e9`  |
| 1226   | No file              | `450d3b6666e9`  |
| 1220   | No file              | `450d3b6666e9`  |
| 1217   | No file              | `450d3b6666e9`  |
| 1211   | No file              | `450d3b6666e9`  |
| 1210   | No file              | `450d3b6666e9`  |
| 1208   | No file              | `450d3b6666e9`  |
| 1203   | No file              | `450d3b6666e9`  |
| 1197   | No file              | `450d3b6666e9`  |
| 1194   | No file              | `450d3b6666e9`  |
| 1192   | No file              | `450d3b6666e9`  |
| 1187   | No file              | `450d3b6666e9`  |
| 1183   | No file              | `450d3b6666e9`  |
| 1177   | No file              | `450d3b6666e9`  |
| 1173   | No file              | `450d3b6666e9`  |
| 1167   | No file              | `450d3b6666e9`  |
| 1164   | No file              | `450d3b6666e9`  |
| 1156   | No file              | `450d3b6666e9`  |
| 1149   | No file              | `450d3b6666e9`  |
| 1144   | No file              | `450d3b6666e9`  |
| 1137   | No file              | `450d3b6666e9`  |
| 1132   | No file              | `450d3b6666e9`  |
| 1127   | Layout 3             | `450d3b6666e9`  |
| 1122   | Layout 3             | `450d3b6666e9`  |
| 1118   | Layout 3             | `450d3b6666e9`  |
| 1114   | Layout 3             | `450d3b6666e9`  |
| 1109   | Layout 3             | `450d3b6666e9`  |
| 1102   | Layout 3             | `450d3b6666e9`  |
| 1096   | No file              | `450d3b6666e9`  |
| 1088   | No file              | `450d3b6666e9`  |
| 1081   | No file              | `450d3b6666e9`  |
| 1076   | No file              | `450d3b6666e9`  |
| 1069   | No file              | `450d3b6666e9`  |
| 1064   | No file              | `450d3b6666e9`  |
| 1058   | No file              | `450d3b6666e9`  |
| 1051   | No file              | `450d3b6666e9`  |
| 1044   | No file              | `450d3b6666e9`  |
| 1036   | No file              | `450d3b6666e9`  |
| 1026   | No file              | `450d3b6666e9`  |
| 1016   | No file              | `450d3b6666e9`  |
| 1009   | No file              | `450d3b6666e9`  |
| 1005   | No file              | `450d3b6666e9`  |
| 1000   | No file              | `450d3b6666e9`  |
| 998    | No file              | `450d3b6666e9`  |
| 990    | No file              | `450d3b6666e9`  |
| 979    | No file              | `450d3b6666e9`  |
| 972    | No file              | `450d3b6666e9`  |
| 963    | No file              | `450d3b6666e9`  |
| 955    | No file              | `450d3b6666e9`  |
| 946    | No file              | `450d3b6666e9`  |
| 938    | No file              | `450d3b6666e9`  |
| 927    | No file              | `450d3b6666e9`  |
| 911    | No file              | `450d3b6666e9`  |
| 904    | No file              | `450d3b6666e9`  |
| 899    | No file              | `450d3b6666e9`  |
| 894    | No file              | `450d3b6666e9`  |
| 885    | No file              | `450d3b6666e9`  |
| 879    | No file              | `450d3b6666e9`  |
| 872    | No file              | `450d3b6666e9`  |
| 864    | No file              | `450d3b6666e9`  |
| 855    | No file              | `450d3b6666e9`  |
| 853    | No file              | `450d3b6666e9`  |
| 845    | No file              | `450d3b6666e9`  |
| 837    | No file              | `450d3b6666e9`  |
| 829    | No file              | `450d3b6666e9`  |
| 822    | No file              | `450d3b6666e9`  |
| 814    | No file              | `450d3b6666e9`  |
| 805    | No file              | `450d3b6666e9`  |
| 794    | No file              | `450d3b6666e9`  |
| 787    | No file              | `450d3b6666e9`  |
| 780    | No file              | `450d3b6666e9`  |
| 771    | No file              | `450d3b6666e9`  |
| 760    | No file              | `450d3b6666e9`  |
| 748    | No file              | `450d3b6666e9`  |
| 741    | No file              | `450d3b6666e9`  |
| 736    | No file              | `450d3b6666e9`  |
| 731    | No file              | `450d3b6666e9`  |
| 723    | No file              | `450d3b6666e9`  |
| 711    | No file              | `450d3b6666e9`  |
| 707    | No file              | `450d3b6666e9`  |
| 697    | No file              | `450d3b6666e9`  |
| 689    | No file              | `450d3b6666e9`  |
| 683    | No file              | `450d3b6666e9`  |
| 678    | No file              | `450d3b6666e9`  |
| 670    | No file              | `450d3b6666e9`  |
| 661    | No file              | `450d3b6666e9`  |
| 656    | No file              | `450d3b6666e9`  |
| 652    | No file              | `450d3b6666e9`  |
| 643    | No file              | `450d3b6666e9`  |
| 637    | No file              | `450d3b6666e9`  |
| 630    | No file              | `450d3b6666e9`  |
| 627    | No file              | `450d3b6666e9`  |
| 621    | No file              | `450d3b6666e9`  |
| 617    | No file              | `450d3b6666e9`  |
| 615    | No file              | `450d3b6666e9`  |
| 606    | No file              | `450d3b6666e9`  |
| 599    | No file              | `450d3b6666e9`  |
| 592    | No file              | `450d3b6666e9`  |
| 586    | No file              | `450d3b6666e9`  |
| 577    | No file              | `450d3b6666e9`  |
| 569    | No file              | `450d3b6666e9`  |
| 561    | No file              | `450d3b6666e9`  |
| 554    | No file              | `450d3b6666e9`  |
| 542    | No file              | `450d3b6666e9`  |
| 532    | No file              | `450d3b6666e9`  |
| 531    | No file              | `450d3b6666e9`  |
| 526    | No file              | `450d3b6666e9`  |
| 521    | No file              | `450d3b6666e9`  |
| 517    | No file              | `450d3b6666e9`  |
| 510    | No file              | `450d3b6666e9`  |
| 508    | No file              | `450d3b6666e9`  |
| 504    | No file              | `450d3b6666e9`  |
| 497    | No file              | `450d3b6666e9`  |
| 491    | No file              | `450d3b6666e9`  |
| 485    | No file              | `450d3b6666e9`  |
| 478    | No file              | `450d3b6666e9`  |
| 472    | No file              | `450d3b6666e9`  |
| 466    | No file              | `450d3b6666e9`  |
| 457    | No file              | `450d3b6666e9`  |
| 452    | No file              | `450d3b6666e9`  |
| 449    | No file              | `450d3b6666e9`  |
| 435    | No file              | `450d3b6666e9`  |

<!-- versions:end -->

## Companion Files

| File                 | Required | Role                     |
| -------------------- | -------- | ------------------------ |
| `languagedata_*.loc` | Optional | Item names (type 0)      |

All multi-byte values are little-endian.

## Layout 3

### File Layout

| Offset              | Type           | Field              | Notes                                                   |
| ------------------- | -------------- | ------------------ | ------------------------------------------------------- |
| `+0x00`             | char[4]        | magic              | ASCII `PABR`                                            |
| `+0x04`             | u32            | row_count          | Number of `rows`; `105` on client 3474                  |
| `+0x08`             | Row[row_count] | rows               | See Row                                                 |
| `rows+0x00`         | String Table   | string_table       | The PABR string table, present but empty                |
| `string_table+0x00` | u32            | string_table_start | Absolute offset of `string_count`; equals `8 + 70 × row_count` |
| `string_table+0x04` | u32            | zero               | Always `0`                                              |

### Row (70 bytes)

The Entry of [`barter_normal.bss`](barter_normal_bss.md) has the same
layout; see Field Names for the three fields that are `0` here.

| Offset  | Type     | Field             | Notes                                                       |
| ------- | -------- | ----------------- | ----------------------------------------------------------- |
| `+0x00` | u16      | barter_region_key | `0` on every row (clients 1784 and 3474)                    |
| `+0x02` | u32      | select_rate       | `0` on every row (clients 1784 and 3474)                    |
| `+0x06` | Exchange | exchange          | See Exchange                                                |
| `+0x3e` | u32      | barter_sub_group  | `0` on every row (clients 1784 and 3474)                    |
| `+0x42` | u32      | barter_category   | Bit mask as in `bartersubgroup.bss`; `0` on every row (client 3474) |

### Exchange (56 bytes)

Same structure as the Exchange of
[`bartersubgroup.bss`](bartersubgroup_bss.md#exchange-56-bytes).

| Offset  | Type | Field              | Notes                                                              |
| ------- | ---- | ------------------ | ------------------------------------------------------------------ |
| `+0x00` | u32  | from_item_key      | The item the player hands over, `enchant_level << 24 \| item_id`; level `0` on every row (client 3474) |
| `+0x04` | u64  | from_min_count     | `1` to `10` (client 3474)                                          |
| `+0x0c` | u64  | from_max_count     | `1` to `10` (client 3474)                                          |
| `+0x14` | u32  | to_item_key        | The item the player gets; 20 rows give an enhanced item (client 3474) |
| `+0x18` | u64  | to_min_count       | `1` to `10000` (client 3474)                                       |
| `+0x20` | u64  | to_max_count       | `1` to `10000` (client 3474)                                       |
| `+0x28` | u32  | barter_need_point  | `0` on every row (clients 1784 and 3474)                           |
| `+0x2c` | u32  | exchange_max_count | `1` on every row (clients 1784 and 3474)                           |
| `+0x30` | u32  | exchange_min       | `1` on every row (client 3474), `15000` (client 1784)              |
| `+0x34` | u32  | exchange_max       | `1000000` on every row (client 3474)                               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Layout 2

### Row (67 bytes)

| Offset  | Type     | Field             | Notes                                              |
| ------- | -------- | ----------------- | -------------------------------------------------- |
| `+0x00` | u16      | barter_region_key |                                                    |
| `+0x02` | u32      | select_rate       |                                                    |
| `+0x06` | Exchange | exchange          |                                                    |
| `+0x3e` | u32      | barter_sub_group  |                                                    |
| `+0x42` | u8       | barter_category   | The category number; `8` on every row (client 1784), as on the material entries of `bartersubgroup.bss`, whose sheet has no category column either |

## Layout 1

The row ends after `barter_sub_group`: there is no `barter_category`.

### Row (66 bytes)

| Offset  | Type     | Field             | Notes |
| ------- | -------- | ----------------- | ----- |
| `+0x00` | u16      | barter_region_key |       |
| `+0x02` | u32      | select_rate       |       |
| `+0x06` | Exchange | exchange          |       |
| `+0x3e` | u32      | barter_sub_group  |       |

## Field Names

The row is the `SpecialBarterData` sheet of a private server's
`DataSheets.bexcel` on client 1784. The client 1784 file holds the 148
sheet rows in sheet order, and these columns match on all 148:
`SelectRate`, `GivedItemKey` with `GivedEnchantLevel` (one packed key),
`GivedMinCount`, `GivedMaxCount`, `TakedItemKey` with `TakedEnchantLevel`,
`TakedMinCount`, `TakedMaxCount`, `ExchangeMin` and `ExchangeMax`. The
sheet's `SpecialBarterIndex` (`1` to `148` in row order) is not stored;
`ContentsGroup` and `TradeEmployeeExp` are not in the file. The Exchange
field names and the `from` and `to` naming are explained in
[`bartersubgroup.bss`](bartersubgroup_bss.md#field-names).

The sheet has no column for `barter_region_key`, `barter_sub_group`,
`barter_category`, `barter_need_point` or `exchange_max_count`. The last two
are Exchange fields and take their names from `bartersubgroup.bss`. The
other three are named after the same slots of
[`barter_normal.bss`](barter_normal_bss.md#field-names), whose entries are
this 70-byte row (67 bytes on client 1784) grouped by region:

- `barter_region_key`: in `barter_normal.bss` the u16 equals the key of the
  region the entry sits in, on all 3,640 + 3,731 entries of client 3474.
- `barter_sub_group`: its values in `barter_normal.bss` are the
  `bartersubgroup.bss` keys, `1` to `197` in the trade item list and `1`
  to `5` in the material list (client 3474), and on client 1784 it matches
  the `BarterSubGroup` column of the `BarterData` and `MaterialBarterData`
  sheets on all 3,240 + 3,321 rows.
- `barter_category`: on client 1784 it matches the `BarterCategory` column
  of the `BarterData` sheet on the 2,958 rows without a sub group; on
  client 3474 it is the bit mask of
  [Barter Categories](bartersubgroup_bss.md#barter-categories).

## Notes

- The special barter window reads the region with
  `specialBarterWrapper:getRegionKey()`, but `barter_region_key` is `0` on
  every row, so the region is not taken from this file.
- The handler (`_bss/barter_special/`) shows one row per offer with its
  place in the file as the index, from `1`, the way the 1784 sheet
  numbers its rows. It reads the Exchange with the shared barter reader in
  `_bss/barter/`.
