# `solareoptionstaticstatusmanager.bss` Format

## Purpose

Arena of Solare options. Per game mode the rank tiers: eight rank groups,
each with up to four tiers, and per tier the lowest rating, a ranking
limit, the `GAME` sheet key of the tier name, the tier icon, the four frame
textures of the match slot and the HP widget, and nine item lists: the
match rewards of Ranked, Practice and Custom matches, each for a victory,
a defeat and a draw (see [Item Lists](#item-lists)). After the modes
come common values, a list of 20 item keys and the Solare equipment
presets: per class type the weapons a player can pick, and one shared
preset with the armor, accessories and crystals. On client 3482 game modes `0` and `1` hold 24 tiers each, and 32
class types have weapon presets.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                  | Bytes  | Records                                                                             | Row bytes              |
| ------ | -------------- | ------------------------------------- | ------ | ----------------------------------------------------------------------------------- | ---------------------- |
| 4      | 3473 and later | `solareoptionstaticstatusmanager.bss` | 17,773 | 333 List Item, 432 Item List, 48 Tier, 32 Group, 4 Mode, 132 Preset Item, 48 Preset | 8 to 40, 20 on average |
| 3      | 3412 to 3458   | `solareoptionstaticstatusmanager.bss` | 14,169 | 144 Item Block, 48 Tier, 32 Group, 4 Mode, 132 Preset Item, 48 Preset               | 36                     |
| 2      | 3381 to 3402   | `solareoptionstaticstatusmanager.bss` | 14,129 | 144 Item Block, 48 Tier, 32 Group, 4 Mode, 132 Preset Item, 48 Preset               | 36                     |
| 1      | 3302 to 3356   | `solareoptionstaticstatusmanager.bss` | 13,846 | 144 Item Block, 48 Tier, 32 Group, 4 Mode, 129 Preset Item, 38 Preset               | 36                     |

| Layout | File                                  | Known            | Unknown         |
| ------ | ------------------------------------- | ---------------- | --------------- |
| 4      | `solareoptionstaticstatusmanager.bss` | 13,709 B (77.1%) | 4,064 B (22.9%) |
| 3      | `solareoptionstaticstatusmanager.bss` | 11,441 B (80.7%) | 2,728 B (19.3%) |
| 2      | `solareoptionstaticstatusmanager.bss` | 11,441 B (81.0%) | 2,688 B (19.0%) |
| 1      | `solareoptionstaticstatusmanager.bss` | 11,253 B (81.3%) | 2,593 B (18.7%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 4             | `11fc7f2bd6f1`  |
| 3482   | Layout 4             | `11fc7f2bd6f1`  |
| 3474   | Layout 4             | `11fc7f2bd6f1`  |
| 3473   | Layout 4             | `11fc7f2bd6f1`  |
| 3464   | No documented layout | `11fc7f2bd6f1`  |
| 3458   | Layout 3             | `11fc7f2bd6f1`  |
| 3454   | Layout 3             | `11fc7f2bd6f1`  |
| 3444   | Layout 3             | `11fc7f2bd6f1`  |
| 3435   | Layout 3             | `11fc7f2bd6f1`  |
| 3426   | Layout 3             | `11fc7f2bd6f1`  |
| 3418   | Layout 3             | `11fc7f2bd6f1`  |
| 3412   | Layout 3             | `11fc7f2bd6f1`  |
| 3402   | Layout 2             | `11fc7f2bd6f1`  |
| 3396   | Layout 2             | `11fc7f2bd6f1`  |
| 3387   | Layout 2             | `11fc7f2bd6f1`  |
| 3381   | Layout 2             | `11fc7f2bd6f1`  |
| 3373   | No documented layout | `11fc7f2bd6f1`  |
| 3364   | No documented layout | `11fc7f2bd6f1`  |
| 3356   | Layout 1             | `11fc7f2bd6f1`  |
| 3349   | Layout 1             | `11fc7f2bd6f1`  |
| 3342   | Layout 1             | `11fc7f2bd6f1`  |
| 3335   | Layout 1             | `11fc7f2bd6f1`  |
| 3326   | Layout 1             | `11fc7f2bd6f1`  |
| 3321   | Layout 1             | `11fc7f2bd6f1`  |
| 3314   | Layout 1             | `11fc7f2bd6f1`  |
| 3303   | Layout 1             | `11fc7f2bd6f1`  |
| 3302   | Layout 1             | `11fc7f2bd6f1`  |
| 3293   | No file              | `11fc7f2bd6f1`  |
| 3283   | No file              | `11fc7f2bd6f1`  |
| 3275   | No file              | `11fc7f2bd6f1`  |
| 3267   | No file              | `11fc7f2bd6f1`  |
| 3258   | No file              | `11fc7f2bd6f1`  |
| 3251   | No file              | `11fc7f2bd6f1`  |
| 3242   | No file              | `11fc7f2bd6f1`  |
| 3235   | No file              | `11fc7f2bd6f1`  |
| 3229   | No file              | `11fc7f2bd6f1`  |
| 3212   | No file              | `11fc7f2bd6f1`  |
| 3203   | No file              | `11fc7f2bd6f1`  |
| 3193   | No file              | `11fc7f2bd6f1`  |
| 3186   | No file              | `11fc7f2bd6f1`  |
| 3177   | No file              | `11fc7f2bd6f1`  |
| 3169   | No file              | `11fc7f2bd6f1`  |
| 3158   | No file              | `11fc7f2bd6f1`  |
| 3151   | No file              | `11fc7f2bd6f1`  |
| 3144   | No file              | `11fc7f2bd6f1`  |
| 3133   | No file              | `11fc7f2bd6f1`  |
| 3125   | No file              | `11fc7f2bd6f1`  |
| 3118   | No file              | `11fc7f2bd6f1`  |
| 3111   | No file              | `11fc7f2bd6f1`  |
| 3103   | No file              | `11fc7f2bd6f1`  |
| 3095   | No file              | `11fc7f2bd6f1`  |
| 3086   | No file              | `11fc7f2bd6f1`  |
| 3072   | No file              | `11fc7f2bd6f1`  |
| 3062   | No file              | `11fc7f2bd6f1`  |
| 3052   | No file              | `11fc7f2bd6f1`  |
| 3045   | No file              | `11fc7f2bd6f1`  |
| 3037   | No file              | `11fc7f2bd6f1`  |
| 3030   | No file              | `11fc7f2bd6f1`  |
| 3021   | No file              | `11fc7f2bd6f1`  |
| 3012   | No file              | `11fc7f2bd6f1`  |
| 3002   | No file              | `11fc7f2bd6f1`  |
| 2995   | No file              | `11fc7f2bd6f1`  |
| 2987   | No file              | `11fc7f2bd6f1`  |
| 2978   | No file              | `11fc7f2bd6f1`  |
| 2970   | No file              | `11fc7f2bd6f1`  |
| 2959   | No file              | `11fc7f2bd6f1`  |
| 2951   | No file              | `11fc7f2bd6f1`  |
| 2942   | No file              | `11fc7f2bd6f1`  |
| 2935   | No file              | `11fc7f2bd6f1`  |
| 2932   | No file              | `11fc7f2bd6f1`  |
| 2923   | No file              | `11fc7f2bd6f1`  |
| 2919   | No file              | `11fc7f2bd6f1`  |
| 2907   | No file              | `11fc7f2bd6f1`  |
| 2900   | No file              | `11fc7f2bd6f1`  |
| 2891   | No file              | `11fc7f2bd6f1`  |
| 2882   | No file              | `11fc7f2bd6f1`  |
| 2872   | No file              | `11fc7f2bd6f1`  |
| 2863   | No file              | `11fc7f2bd6f1`  |
| 2855   | No file              | `11fc7f2bd6f1`  |
| 2849   | No file              | `11fc7f2bd6f1`  |
| 2844   | No file              | `11fc7f2bd6f1`  |
| 2834   | No file              | `11fc7f2bd6f1`  |
| 2825   | No file              | `11fc7f2bd6f1`  |
| 2819   | No file              | `11fc7f2bd6f1`  |
| 2811   | No file              | `11fc7f2bd6f1`  |
| 2803   | No file              | `11fc7f2bd6f1`  |
| 2794   | No file              | `11fc7f2bd6f1`  |
| 2783   | No file              | `11fc7f2bd6f1`  |
| 2774   | No file              | `11fc7f2bd6f1`  |
| 2765   | No file              | `11fc7f2bd6f1`  |
| 2756   | No file              | `11fc7f2bd6f1`  |
| 2750   | No file              | `11fc7f2bd6f1`  |
| 2743   | No file              | `11fc7f2bd6f1`  |
| 2736   | No file              | `11fc7f2bd6f1`  |
| 2726   | No file              | `11fc7f2bd6f1`  |
| 2717   | No file              | `11fc7f2bd6f1`  |
| 2709   | No file              | `11fc7f2bd6f1`  |
| 2703   | No file              | `11fc7f2bd6f1`  |
| 2695   | No file              | `11fc7f2bd6f1`  |
| 2684   | No file              | `11fc7f2bd6f1`  |
| 2672   | No file              | `11fc7f2bd6f1`  |
| 2665   | No file              | `11fc7f2bd6f1`  |
| 2657   | No file              | `11fc7f2bd6f1`  |
| 2649   | No file              | `11fc7f2bd6f1`  |
| 2644   | No file              | `11fc7f2bd6f1`  |
| 2637   | No file              | `11fc7f2bd6f1`  |
| 2629   | No file              | `11fc7f2bd6f1`  |
| 2619   | No file              | `11fc7f2bd6f1`  |
| 2612   | No file              | `11fc7f2bd6f1`  |
| 2606   | No file              | `11fc7f2bd6f1`  |
| 2602   | No file              | `11fc7f2bd6f1`  |
| 2601   | No file              | `11fc7f2bd6f1`  |
| 2592   | No file              | `11fc7f2bd6f1`  |
| 2583   | No file              | `11fc7f2bd6f1`  |
| 2575   | No file              | `11fc7f2bd6f1`  |
| 2567   | No file              | `11fc7f2bd6f1`  |
| 2560   | No file              | `11fc7f2bd6f1`  |
| 2553   | No file              | `11fc7f2bd6f1`  |
| 2545   | No file              | `11fc7f2bd6f1`  |
| 2538   | No file              | `11fc7f2bd6f1`  |
| 2529   | No file              | `11fc7f2bd6f1`  |
| 2519   | No file              | `11fc7f2bd6f1`  |
| 2513   | No file              | `11fc7f2bd6f1`  |
| 2510   | No file              | `11fc7f2bd6f1`  |
| 2507   | No file              | `11fc7f2bd6f1`  |
| 2503   | No file              | `11fc7f2bd6f1`  |
| 2498   | No file              | `11fc7f2bd6f1`  |
| 2492   | No file              | `11fc7f2bd6f1`  |
| 2487   | No file              | `11fc7f2bd6f1`  |
| 2480   | No file              | `11fc7f2bd6f1`  |
| 2474   | No file              | `11fc7f2bd6f1`  |
| 2468   | No file              | `11fc7f2bd6f1`  |
| 2460   | No file              | `11fc7f2bd6f1`  |
| 2453   | No file              | `11fc7f2bd6f1`  |
| 2444   | No file              | `11fc7f2bd6f1`  |
| 2438   | No file              | `11fc7f2bd6f1`  |
| 2434   | No file              | `11fc7f2bd6f1`  |
| 2429   | No file              | `11fc7f2bd6f1`  |
| 2421   | No file              | `11fc7f2bd6f1`  |
| 2414   | No file              | `11fc7f2bd6f1`  |
| 2407   | No file              | `11fc7f2bd6f1`  |
| 2401   | No file              | `11fc7f2bd6f1`  |
| 2397   | No file              | `11fc7f2bd6f1`  |
| 2393   | No file              | `11fc7f2bd6f1`  |
| 2384   | No file              | `11fc7f2bd6f1`  |
| 2378   | No file              | `11fc7f2bd6f1`  |
| 2372   | No file              | `11fc7f2bd6f1`  |
| 2358   | No file              | `11fc7f2bd6f1`  |
| 2352   | No file              | `11fc7f2bd6f1`  |
| 2347   | No file              | `11fc7f2bd6f1`  |
| 2343   | No file              | `11fc7f2bd6f1`  |
| 2335   | No file              | `11fc7f2bd6f1`  |
| 2327   | No file              | `11fc7f2bd6f1`  |
| 2324   | No file              | `11fc7f2bd6f1`  |
| 2319   | No file              | `11fc7f2bd6f1`  |
| 2313   | No file              | `11fc7f2bd6f1`  |
| 2308   | No file              | `11fc7f2bd6f1`  |
| 2302   | No file              | `11fc7f2bd6f1`  |
| 2295   | No file              | `11fc7f2bd6f1`  |
| 2290   | No file              | `11fc7f2bd6f1`  |
| 2284   | No file              | `11fc7f2bd6f1`  |
| 2276   | No file              | `11fc7f2bd6f1`  |
| 2269   | No file              | `11fc7f2bd6f1`  |
| 2259   | No file              | `11fc7f2bd6f1`  |
| 2250   | No file              | `11fc7f2bd6f1`  |
| 2243   | No file              | `11fc7f2bd6f1`  |
| 2235   | No file              | `11fc7f2bd6f1`  |
| 2229   | No file              | `11fc7f2bd6f1`  |
| 2224   | No file              | `11fc7f2bd6f1`  |
| 2218   | No file              | `11fc7f2bd6f1`  |
| 2215   | No file              | `11fc7f2bd6f1`  |
| 2207   | No file              | `11fc7f2bd6f1`  |
| 2203   | No file              | `11fc7f2bd6f1`  |
| 2196   | No file              | `11fc7f2bd6f1`  |
| 2192   | No file              | `11fc7f2bd6f1`  |
| 2189   | No file              | `11fc7f2bd6f1`  |
| 2183   | No file              | `11fc7f2bd6f1`  |
| 2179   | No file              | `11fc7f2bd6f1`  |
| 2171   | No file              | `11fc7f2bd6f1`  |
| 2163   | No file              | `11fc7f2bd6f1`  |
| 2156   | No file              | `11fc7f2bd6f1`  |
| 2151   | No file              | `11fc7f2bd6f1`  |
| 2147   | No file              | `11fc7f2bd6f1`  |
| 2142   | No file              | `11fc7f2bd6f1`  |
| 2138   | No file              | `11fc7f2bd6f1`  |
| 2134   | No file              | `11fc7f2bd6f1`  |
| 2130   | No file              | `11fc7f2bd6f1`  |
| 2122   | No file              | `11fc7f2bd6f1`  |
| 2107   | No file              | `11fc7f2bd6f1`  |
| 2098   | No file              | `11fc7f2bd6f1`  |
| 2089   | No file              | `11fc7f2bd6f1`  |
| 2081   | No file              | `11fc7f2bd6f1`  |
| 2073   | No file              | `11fc7f2bd6f1`  |
| 2067   | No file              | `11fc7f2bd6f1`  |
| 2063   | No file              | `11fc7f2bd6f1`  |
| 2059   | No file              | `11fc7f2bd6f1`  |
| 2052   | No file              | `11fc7f2bd6f1`  |
| 2044   | No file              | `11fc7f2bd6f1`  |
| 2039   | No file              | `11fc7f2bd6f1`  |
| 2032   | No file              | `11fc7f2bd6f1`  |
| 2025   | No file              | `11fc7f2bd6f1`  |
| 2011   | No file              | `11fc7f2bd6f1`  |
| 2005   | No file              | `11fc7f2bd6f1`  |
| 2000   | No file              | `11fc7f2bd6f1`  |
| 1996   | No file              | `11fc7f2bd6f1`  |
| 1991   | No file              | `11fc7f2bd6f1`  |
| 1985   | No file              | `11fc7f2bd6f1`  |
| 1980   | No file              | `11fc7f2bd6f1`  |
| 1969   | No file              | `11fc7f2bd6f1`  |
| 1964   | No file              | `11fc7f2bd6f1`  |
| 1958   | No file              | `11fc7f2bd6f1`  |
| 1950   | No file              | `11fc7f2bd6f1`  |
| 1945   | No file              | `11fc7f2bd6f1`  |
| 1937   | No file              | `11fc7f2bd6f1`  |
| 1933   | No file              | `11fc7f2bd6f1`  |
| 1927   | No file              | `11fc7f2bd6f1`  |
| 1921   | No file              | `11fc7f2bd6f1`  |
| 1914   | No file              | `11fc7f2bd6f1`  |
| 1908   | No file              | `11fc7f2bd6f1`  |
| 1897   | No file              | `11fc7f2bd6f1`  |
| 1892   | No file              | `11fc7f2bd6f1`  |
| 1886   | No file              | `11fc7f2bd6f1`  |
| 1881   | No file              | `11fc7f2bd6f1`  |
| 1871   | No file              | `11fc7f2bd6f1`  |
| 1866   | No file              | `11fc7f2bd6f1`  |
| 1862   | No file              | `11fc7f2bd6f1`  |
| 1854   | No file              | `11fc7f2bd6f1`  |
| 1846   | No file              | `11fc7f2bd6f1`  |
| 1838   | No file              | `11fc7f2bd6f1`  |
| 1832   | No file              | `11fc7f2bd6f1`  |
| 1826   | No file              | `11fc7f2bd6f1`  |
| 1822   | No file              | `11fc7f2bd6f1`  |
| 1818   | No file              | `11fc7f2bd6f1`  |
| 1804   | No file              | `11fc7f2bd6f1`  |
| 1794   | No file              | `11fc7f2bd6f1`  |
| 1790   | No file              | `11fc7f2bd6f1`  |
| 1784   | No file              | `11fc7f2bd6f1`  |
| 1774   | No file              | `11fc7f2bd6f1`  |
| 1771   | No file              | `11fc7f2bd6f1`  |
| 1762   | No file              | `11fc7f2bd6f1`  |
| 1759   | No file              | `11fc7f2bd6f1`  |
| 1754   | No file              | `11fc7f2bd6f1`  |
| 1749   | No file              | `11fc7f2bd6f1`  |
| 1743   | No file              | `11fc7f2bd6f1`  |
| 1737   | No file              | `11fc7f2bd6f1`  |
| 1731   | No file              | `11fc7f2bd6f1`  |
| 1725   | No file              | `11fc7f2bd6f1`  |
| 1717   | No file              | `11fc7f2bd6f1`  |
| 1710   | No file              | `11fc7f2bd6f1`  |
| 1704   | No file              | `11fc7f2bd6f1`  |
| 1698   | No file              | `11fc7f2bd6f1`  |
| 1690   | No file              | `11fc7f2bd6f1`  |
| 1685   | No file              | `11fc7f2bd6f1`  |
| 1680   | No file              | `11fc7f2bd6f1`  |
| 1674   | No file              | `11fc7f2bd6f1`  |
| 1668   | No file              | `11fc7f2bd6f1`  |
| 1659   | No file              | `11fc7f2bd6f1`  |
| 1649   | No file              | `11fc7f2bd6f1`  |
| 1642   | No file              | `11fc7f2bd6f1`  |
| 1636   | No file              | `11fc7f2bd6f1`  |
| 1628   | No file              | `11fc7f2bd6f1`  |
| 1622   | No file              | `11fc7f2bd6f1`  |
| 1614   | No file              | `11fc7f2bd6f1`  |
| 1608   | No file              | `11fc7f2bd6f1`  |
| 1602   | No file              | `11fc7f2bd6f1`  |
| 1598   | No file              | `11fc7f2bd6f1`  |
| 1594   | No file              | `11fc7f2bd6f1`  |
| 1590   | No file              | `11fc7f2bd6f1`  |
| 1587   | No file              | `11fc7f2bd6f1`  |
| 1584   | No file              | `11fc7f2bd6f1`  |
| 1579   | No file              | `11fc7f2bd6f1`  |
| 1572   | No file              | `11fc7f2bd6f1`  |
| 1565   | No file              | `11fc7f2bd6f1`  |
| 1559   | No file              | `11fc7f2bd6f1`  |
| 1554   | No file              | `11fc7f2bd6f1`  |
| 1547   | No file              | `11fc7f2bd6f1`  |
| 1537   | No file              | `11fc7f2bd6f1`  |
| 1529   | No file              | `11fc7f2bd6f1`  |
| 1524   | No file              | `11fc7f2bd6f1`  |
| 1519   | No file              | `11fc7f2bd6f1`  |
| 1509   | No file              | `11fc7f2bd6f1`  |
| 1506   | No file              | `11fc7f2bd6f1`  |
| 1504   | No file              | `11fc7f2bd6f1`  |
| 1500   | No file              | `11fc7f2bd6f1`  |
| 1493   | No file              | `11fc7f2bd6f1`  |
| 1489   | No file              | `11fc7f2bd6f1`  |
| 1485   | No file              | `11fc7f2bd6f1`  |
| 1481   | No file              | `11fc7f2bd6f1`  |
| 1474   | No file              | `11fc7f2bd6f1`  |
| 1466   | No file              | `11fc7f2bd6f1`  |
| 1462   | No file              | `11fc7f2bd6f1`  |
| 1459   | No file              | `11fc7f2bd6f1`  |
| 1453   | No file              | `11fc7f2bd6f1`  |
| 1450   | No file              | `11fc7f2bd6f1`  |
| 1445   | No file              | `11fc7f2bd6f1`  |
| 1439   | No file              | `11fc7f2bd6f1`  |
| 1433   | No file              | `11fc7f2bd6f1`  |
| 1430   | No file              | `11fc7f2bd6f1`  |
| 1426   | No file              | `11fc7f2bd6f1`  |
| 1421   | No file              | `11fc7f2bd6f1`  |
| 1417   | No file              | `11fc7f2bd6f1`  |
| 1416   | No file              | `11fc7f2bd6f1`  |
| 1409   | No file              | `11fc7f2bd6f1`  |
| 1405   | No file              | `11fc7f2bd6f1`  |
| 1401   | No file              | `11fc7f2bd6f1`  |
| 1396   | No file              | `11fc7f2bd6f1`  |
| 1391   | No file              | `11fc7f2bd6f1`  |
| 1390   | No file              | `11fc7f2bd6f1`  |
| 1386   | No file              | `11fc7f2bd6f1`  |
| 1381   | No file              | `11fc7f2bd6f1`  |
| 1379   | No file              | `11fc7f2bd6f1`  |
| 1372   | No file              | `11fc7f2bd6f1`  |
| 1366   | No file              | `11fc7f2bd6f1`  |
| 1364   | No file              | `11fc7f2bd6f1`  |
| 1363   | No file              | `11fc7f2bd6f1`  |
| 1360   | No file              | `11fc7f2bd6f1`  |
| 1358   | No file              | `11fc7f2bd6f1`  |
| 1355   | No file              | `11fc7f2bd6f1`  |
| 1351   | No file              | `11fc7f2bd6f1`  |
| 1348   | No file              | `11fc7f2bd6f1`  |
| 1346   | No file              | `11fc7f2bd6f1`  |
| 1341   | No file              | `11fc7f2bd6f1`  |
| 1340   | No file              | `11fc7f2bd6f1`  |
| 1338   | No file              | `11fc7f2bd6f1`  |
| 1335   | No file              | `11fc7f2bd6f1`  |
| 1333   | No file              | `11fc7f2bd6f1`  |
| 1329   | No file              | `11fc7f2bd6f1`  |
| 1327   | No file              | `11fc7f2bd6f1`  |
| 1324   | No file              | `11fc7f2bd6f1`  |
| 1321   | No file              | `11fc7f2bd6f1`  |
| 1319   | No file              | `11fc7f2bd6f1`  |
| 1318   | No file              | `11fc7f2bd6f1`  |
| 1316   | No file              | `11fc7f2bd6f1`  |
| 1313   | No file              | `11fc7f2bd6f1`  |
| 1311   | No file              | `11fc7f2bd6f1`  |
| 1309   | No file              | `11fc7f2bd6f1`  |
| 1304   | No file              | `11fc7f2bd6f1`  |
| 1292   | No file              | `11fc7f2bd6f1`  |
| 1286   | No file              | `11fc7f2bd6f1`  |
| 1280   | No file              | `11fc7f2bd6f1`  |
| 1276   | No file              | `11fc7f2bd6f1`  |
| 1267   | No file              | `11fc7f2bd6f1`  |
| 1261   | No file              | `11fc7f2bd6f1`  |
| 1256   | No file              | `11fc7f2bd6f1`  |
| 1250   | No file              | `11fc7f2bd6f1`  |
| 1246   | No file              | `11fc7f2bd6f1`  |
| 1239   | No file              | `11fc7f2bd6f1`  |
| 1230   | No file              | `11fc7f2bd6f1`  |
| 1226   | No file              | `11fc7f2bd6f1`  |
| 1220   | No file              | `11fc7f2bd6f1`  |
| 1217   | No file              | `11fc7f2bd6f1`  |
| 1211   | No file              | `11fc7f2bd6f1`  |
| 1210   | No file              | `11fc7f2bd6f1`  |
| 1208   | No file              | `11fc7f2bd6f1`  |
| 1203   | No file              | `11fc7f2bd6f1`  |
| 1197   | No file              | `11fc7f2bd6f1`  |
| 1194   | No file              | `11fc7f2bd6f1`  |
| 1192   | No file              | `11fc7f2bd6f1`  |
| 1187   | No file              | `11fc7f2bd6f1`  |
| 1183   | No file              | `11fc7f2bd6f1`  |
| 1177   | No file              | `11fc7f2bd6f1`  |
| 1173   | No file              | `11fc7f2bd6f1`  |
| 1167   | No file              | `11fc7f2bd6f1`  |
| 1164   | No file              | `11fc7f2bd6f1`  |
| 1156   | No file              | `11fc7f2bd6f1`  |
| 1149   | No file              | `11fc7f2bd6f1`  |
| 1144   | No file              | `11fc7f2bd6f1`  |
| 1137   | No file              | `11fc7f2bd6f1`  |
| 1132   | No file              | `11fc7f2bd6f1`  |
| 1127   | No file              | `11fc7f2bd6f1`  |
| 1122   | No file              | `11fc7f2bd6f1`  |
| 1118   | No file              | `11fc7f2bd6f1`  |
| 1114   | No file              | `11fc7f2bd6f1`  |
| 1109   | No file              | `11fc7f2bd6f1`  |
| 1102   | No file              | `11fc7f2bd6f1`  |
| 1096   | No file              | `11fc7f2bd6f1`  |
| 1088   | No file              | `11fc7f2bd6f1`  |
| 1081   | No file              | `11fc7f2bd6f1`  |
| 1076   | No file              | `11fc7f2bd6f1`  |
| 1069   | No file              | `11fc7f2bd6f1`  |
| 1064   | No file              | `11fc7f2bd6f1`  |
| 1058   | No file              | `11fc7f2bd6f1`  |
| 1051   | No file              | `11fc7f2bd6f1`  |
| 1044   | No file              | `11fc7f2bd6f1`  |
| 1036   | No file              | `11fc7f2bd6f1`  |
| 1026   | No file              | `11fc7f2bd6f1`  |
| 1016   | No file              | `11fc7f2bd6f1`  |
| 1009   | No file              | `11fc7f2bd6f1`  |
| 1005   | No file              | `11fc7f2bd6f1`  |
| 1000   | No file              | `11fc7f2bd6f1`  |
| 998    | No file              | `11fc7f2bd6f1`  |
| 990    | No file              | `11fc7f2bd6f1`  |
| 979    | No file              | `11fc7f2bd6f1`  |
| 972    | No file              | `11fc7f2bd6f1`  |
| 963    | No file              | `11fc7f2bd6f1`  |
| 955    | No file              | `11fc7f2bd6f1`  |
| 946    | No file              | `11fc7f2bd6f1`  |
| 938    | No file              | `11fc7f2bd6f1`  |
| 927    | No file              | `11fc7f2bd6f1`  |
| 911    | No file              | `11fc7f2bd6f1`  |
| 904    | No file              | `11fc7f2bd6f1`  |
| 899    | No file              | `11fc7f2bd6f1`  |
| 894    | No file              | `11fc7f2bd6f1`  |
| 885    | No file              | `11fc7f2bd6f1`  |
| 879    | No file              | `11fc7f2bd6f1`  |
| 872    | No file              | `11fc7f2bd6f1`  |
| 864    | No file              | `11fc7f2bd6f1`  |
| 855    | No file              | `11fc7f2bd6f1`  |
| 853    | No file              | `11fc7f2bd6f1`  |
| 845    | No file              | `11fc7f2bd6f1`  |
| 837    | No file              | `11fc7f2bd6f1`  |
| 829    | No file              | `11fc7f2bd6f1`  |
| 822    | No file              | `11fc7f2bd6f1`  |
| 814    | No file              | `11fc7f2bd6f1`  |
| 805    | No file              | `11fc7f2bd6f1`  |
| 794    | No file              | `11fc7f2bd6f1`  |
| 787    | No file              | `11fc7f2bd6f1`  |
| 780    | No file              | `11fc7f2bd6f1`  |
| 771    | No file              | `11fc7f2bd6f1`  |
| 760    | No file              | `11fc7f2bd6f1`  |
| 748    | No file              | `11fc7f2bd6f1`  |
| 741    | No file              | `11fc7f2bd6f1`  |
| 736    | No file              | `11fc7f2bd6f1`  |
| 731    | No file              | `11fc7f2bd6f1`  |
| 723    | No file              | `11fc7f2bd6f1`  |
| 711    | No file              | `11fc7f2bd6f1`  |
| 707    | No file              | `11fc7f2bd6f1`  |
| 697    | No file              | `11fc7f2bd6f1`  |
| 689    | No file              | `11fc7f2bd6f1`  |
| 683    | No file              | `11fc7f2bd6f1`  |
| 678    | No file              | `11fc7f2bd6f1`  |
| 670    | No file              | `11fc7f2bd6f1`  |
| 661    | No file              | `11fc7f2bd6f1`  |
| 656    | No file              | `11fc7f2bd6f1`  |
| 652    | No file              | `11fc7f2bd6f1`  |
| 643    | No file              | `11fc7f2bd6f1`  |
| 637    | No file              | `11fc7f2bd6f1`  |
| 630    | No file              | `11fc7f2bd6f1`  |
| 627    | No file              | `11fc7f2bd6f1`  |
| 621    | No file              | `11fc7f2bd6f1`  |
| 617    | No file              | `11fc7f2bd6f1`  |
| 615    | No file              | `11fc7f2bd6f1`  |
| 606    | No file              | `11fc7f2bd6f1`  |
| 599    | No file              | `11fc7f2bd6f1`  |
| 592    | No file              | `11fc7f2bd6f1`  |
| 586    | No file              | `11fc7f2bd6f1`  |
| 577    | No file              | `11fc7f2bd6f1`  |
| 569    | No file              | `11fc7f2bd6f1`  |
| 561    | No file              | `11fc7f2bd6f1`  |
| 554    | No file              | `11fc7f2bd6f1`  |
| 542    | No file              | `11fc7f2bd6f1`  |
| 532    | No file              | `11fc7f2bd6f1`  |
| 531    | No file              | `11fc7f2bd6f1`  |
| 526    | No file              | `11fc7f2bd6f1`  |
| 521    | No file              | `11fc7f2bd6f1`  |
| 517    | No file              | `11fc7f2bd6f1`  |
| 510    | No file              | `11fc7f2bd6f1`  |
| 508    | No file              | `11fc7f2bd6f1`  |
| 504    | No file              | `11fc7f2bd6f1`  |
| 497    | No file              | `11fc7f2bd6f1`  |
| 491    | No file              | `11fc7f2bd6f1`  |
| 485    | No file              | `11fc7f2bd6f1`  |
| 478    | No file              | `11fc7f2bd6f1`  |
| 472    | No file              | `11fc7f2bd6f1`  |
| 466    | No file              | `11fc7f2bd6f1`  |
| 457    | No file              | `11fc7f2bd6f1`  |
| 452    | No file              | `11fc7f2bd6f1`  |
| 449    | No file              | `11fc7f2bd6f1`  |
| 435    | No file              | `11fc7f2bd6f1`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role |
| --------------------- | -------- | ---- |
| `stringtable.bss`     | Optional | Hash of the `description` key, for its LOC type 37 text |
| `ui_texture/texturestringkey/texturestring_combine.xml` | Optional | Sprite sheet and rectangle of the `icon_texture` key |
| `languagedata_en.loc` | Optional | Tier name in the user's language, item names (LOC type 0) |

All multi-byte values are little-endian.

## Layout 4

### File Layout

A PABR file with no record count. Every array has a fixed length: four
game modes, eight rank groups per mode and 48 presets.

| Offset                      | Type                       | Field                       | Notes |
| --------------------------- | -------------------------- | --------------------------- | ----- |
| `+0x00`                     | char[4]                    | magic                       | `PABR` |
| `+0x04`                     | Mode[4]                    | modes                       | See Mode; modes `0` and `1`, then two unused |
| `modes+0x00`                | f32                        | unknown_modes_00            | `10000` |
| `modes+0x04`                | u8                         | unknown_modes_04            | `100` |
| `modes+0x05`                | f32                        | unknown_modes_05            | `5000` |
| `modes+0x09`                | u64[9]                     | unknown_modes_09            | `120, 180, 60, 30, 180, 15, 180, 180, 60` |
| `modes+0x51`                | u32                        | unknown_win_str_ref         | Index into `strings`: `SOLARE_WIN` |
| `modes+0x55`                | u32                        | unknown_draw_str_ref        | Index into `strings`: `SOLARE_DRAW` |
| `modes+0x59`                | u32                        | unknown_lose_str_ref        | Index into `strings`: `SOLARE_LOSE` |
| `modes+0x5D`                | u32                        | unknown_modes_5d            | `14` |
| `modes+0x61`                | u32                        | unknown_modes_61            | `7` |
| `modes+0x65`                | u32                        | unknown_modes_65            | `2500` |
| `modes+0x69`                | u64                        | unknown_item_count          | Number of `unknown_item_keys`, `20` |
| `modes+0x71`                | u32[unknown_item_count]    | unknown_item_keys           | Item keys; see [unknown_item_keys](#unknown_item_keys) |
| `unknown_item_keys+0x00`    | bytes[3]                   | unknown_item_keys_00        | `0` |
| `unknown_item_keys+0x03`    | Preset[48]                 | equip_presets               | See Preset; index `0` to `46` is the class type, index `47` the shared preset |
| `equip_presets+0x00`        | f32[3]                     | unknown_equip_presets_00    | `3351, -8003, 83845`, a world position |
| `equip_presets+0x0C`        | f32[3]                     | unknown_equip_presets_0c    | `12889, -6781, 77556`, a world position |
| `equip_presets+0x18`        | f32                        | unknown_equip_presets_18    | `300` |
| `equip_presets+0x1C`        | f32                        | unknown_equip_presets_1c    | `13000` |
| `equip_presets+0x20`        | String Table               | string_table                | See String Table |
| `string_table+0x00`         | u32                        | string_table_start          | Absolute offset of `string_count` |
| `string_table+0x04`         | u32                        | zero                        | `0` |

### Mode (variable: 79 bytes + groups)

| Offset  | Type     | Field      | Notes |
| ------- | -------- | ---------- | ----- |
| `+0x00` | u8       | game_mode  | `0` and `1`; `4` on the two unused modes, which are `0` in every other byte |
| `+0x01` | u8       | unknown_01 | `0` |
| `+0x02` | u32      | unknown_02 | `60` |
| `+0x06` | u32      | unknown_06 | `401` |
| `+0x0A` | u8       | unknown_0a | `10` |
| `+0x0B` | f32      | unknown_0b | `1.5` |
| `+0x0F` | u32      | unknown_0f | `75` |
| `+0x13` | u32      | unknown_13 | `300` |
| `+0x17` | u32      | unknown_17 | `400` |
| `+0x1B` | u32      | unknown_1b | `150` |
| `+0x1F` | u32      | unknown_1f | `450` |
| `+0x23` | u32      | unknown_23 | `600` |
| `+0x27` | u32      | unknown_27 | `1` in mode `0`, `800` in mode `1`; the only value the two modes do not share |
| `+0x2B` | u32      | unknown_2b | `10` |
| `+0x2F` | f32      | unknown_2f | `400` |
| `+0x33` | u32      | unknown_33 | `10000` |
| `+0x37` | u32      | unknown_37 | `150` |
| `+0x3B` | i32      | unknown_3b | `-200` |
| `+0x3F` | u32      | unknown_3f | `100` |
| `+0x43` | u32      | unknown_43 | `300` |
| `+0x47` | u32      | unknown_47 | `300` |
| `+0x4B` | u32      | unknown_4b | `40` |
| `+0x4F` | Group[8] | groups     | See Group; rank groups `0` to `7` |

The values are those of client 3482, the same in modes `0` and `1` except
`unknown_27`.

### Group (variable: 49 bytes + tiers)

| Offset  | Type             | Field      | Notes |
| ------- | ---------------- | ---------- | ----- |
| `+0x00` | u8               | rank_group | `0` to `7` in file order; `8` in the unused modes |
| `+0x01` | f32              | unknown_01 | `40` in group `0` rising to `70` in groups `5` to `7` |
| `+0x05` | f32              | unknown_05 | `40` in group `0`, `46` in group `1`, `50` from group `2` on |
| `+0x09` | u16              | unknown_09 | `2` in groups `0` and `1`, `3` in group `2`, else `0` |
| `+0x0B` | u16              | unknown_0b | `1` in groups `0` and `1`, `2` in group `2`, else `0` |
| `+0x0D` | u16              | unknown_0d | `50`, `40`, `30` in groups `0` to `2`, else `0` |
| `+0x0F` | u8               | unknown_0f | `3`, or `0` in group `0` with three zero values after it |
| `+0x10` | f32[3]           | unknown_10 | `1.1, 1.2, 0.025` in groups `1` and `2`, up to `1.1, 1.5, 0.1` from group `4` on |
| `+0x1C` | u8               | unknown_1c | `3` in groups `0` to `2`, else `0` with three zero values after it |
| `+0x1D` | f32[3]           | unknown_1d | `1.05, 1.1, 0.05` in groups `0` and `1` |
| `+0x29` | u64              | tier_count | `3`, `4` in groups `5` and `6`, `1` in group `7`, `0` in the unused modes |
| `+0x31` | Tier[tier_count] | tiers      | See Tier |

### Tier (variable: 34 bytes + item lists)

| Offset  | Type          | Field                  | Notes |
| ------- | ------------- | ---------------------- | ----- |
| `+0x00` | u32           | min_rating             | Lowest rating of the tier: `2401` in group `0`, then `2301` down by 100 to `401`, and `0` for the last tier |
| `+0x04` | u32           | max_ranking            | `1` and `30` on the first two tiers of group `0`, else `0` (no ranking limit) |
| `+0x08` | u16           | rank_tier_key          | Rank group in the high byte, tier `1` up in the low byte (`0x0101` group 1, tier 1) |
| `+0x0A` | u32           | description            | Index into `strings`: a `GAME` sheet key (`LUA_SOLARE_RANK_TIER_00`) |
| `+0x0E` | u32           | icon_texture           | Index into `strings`: a texture key (`Solare_Tier01`) |
| `+0x12` | u32           | match_slot_right_frame | Index into `strings`: `Combine_Etc_Solare_War_MatchSlot_Right_Frame_NN` |
| `+0x16` | u32           | match_slot_left_frame  | Index into `strings`: `..._MatchSlot_Left_Frame_NN` |
| `+0x1A` | u32           | hp_widget_right_frame  | Index into `strings`: `..._HPWidget_Right_Frame_NN` |
| `+0x1E` | u32           | hp_widget_left_frame   | Index into `strings`: `..._HPWidget_Left_Frame_NN` |
| `+0x22` | Item List[9]  | item_lists             | See Item List and [Item Lists](#item-lists) |

### Item List (variable: 8 bytes + items)

| Offset  | Type             | Field      | Notes |
| ------- | ---------------- | ---------- | ----- |
| `+0x00` | u64              | item_count | Number of items, `0` to `2` |
| `+0x08` | List Item[item_count] | items | See List Item |

### List Item (16 bytes)

| Offset  | Type | Field      | Notes |
| ------- | ---- | ---------- | ----- |
| `+0x00` | u32  | item_key   | Item key (`890008` Enthusiastic Solare Box, `65396` Seal of Solare) |
| `+0x04` | u32  | unknown_04 | `0x7FF6` on client 3482, `0x7FF7` on client 3474; the only bytes that differ between the two files |
| `+0x08` | u64  | count      | Item count |

### Preset (variable: 25 bytes + items)

| Offset             | Type                      | Field       | Notes |
| ------------------ | ------------------------- | ----------- | ----- |
| `+0x00`            | u8                        | class_type  | Class type (`0` Warrior), or `47` (`__eClassType_Count`) on the shared preset and on the unused entries |
| `+0x01`            | f32                       | unknown_01  | `1` on every filled preset, `0` on the unused ones |
| `+0x05`            | f32                       | unknown_05  | Equals `unknown_01` |
| `+0x09`            | u64                       | equip_count | Number of `equip_items`: `3` per class, `18` in the shared preset |
| `+0x11`            | Preset Item[equip_count]  | equip_items | See Preset Item |
| `equip_items+0x00` | u64                       | jewel_count | Number of `jewel_items`: `18` in the shared preset, else `0` |
| `equip_items+0x08` | Preset Item[jewel_count]  | jewel_items | See Preset Item; `index` is the socket |

### Preset Item (10 bytes)

| Offset  | Type | Field         | Notes |
| ------- | ---- | ------------- | ----- |
| `+0x00` | u32  | item_key      | Item key (`741301` Resolute Longsword, `15721` Secrua's Flaming Crystal) |
| `+0x04` | i32  | unknown_04    | `-1` on every item |
| `+0x08` | u8   | equip_slot_no | Equipment slot: `0` main weapon, `1` sub-weapon, `29` awakening weapon, `3` to `12` and `27` in the shared preset |
| `+0x09` | u8   | index         | `0` up per slot: the preset level of an equip item, the socket of a jewel item |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `80` on client 3482 |
| `+0x04` | pstr[string_count] | strings      | UTF-8 keys: tier names, tier icons, frame textures, then `SOLARE_WIN`, `SOLARE_DRAW`, `SOLARE_LOSE` |

## Layout 3

Clients 3412 and 3454 store one item per list: each tier holds three
blocks of three items with their counts, where Layout 4 has nine lists of
any length. The common values have no `unknown_modes_65`.

### File Layout

| Offset                   | Type                    | Field                    | Notes    |
| ------------------------ | ----------------------- | ------------------------ | -------- |
| `+0x00`                  | char[4]                 | magic                    | `PABR`   |
| `+0x04`                  | Mode[4]                 | modes                    | See Mode |
| `modes+0x00`             | f32                     | unknown_modes_00         |          |
| `modes+0x04`             | u8                      | unknown_modes_04         |          |
| `modes+0x05`             | f32                     | unknown_modes_05         |          |
| `modes+0x09`             | u64[9]                  | unknown_modes_09         |          |
| `modes+0x51`             | u32                     | unknown_win_str_ref      |          |
| `modes+0x55`             | u32                     | unknown_draw_str_ref     |          |
| `modes+0x59`             | u32                     | unknown_lose_str_ref     |          |
| `modes+0x5D`             | u32                     | unknown_modes_5d         |          |
| `modes+0x61`             | u32                     | unknown_modes_61         |          |
| `modes+0x65`             | u64                     | unknown_item_count       |          |
| `modes+0x6D`             | u32[unknown_item_count] | unknown_item_keys        |          |
| `unknown_item_keys+0x00` | bytes[3]                | unknown_item_keys_00     |          |
| `unknown_item_keys+0x03` | Preset[48]              | equip_presets            |          |
| `equip_presets+0x00`     | f32[3]                  | unknown_equip_presets_00 |          |
| `equip_presets+0x0C`     | f32[3]                  | unknown_equip_presets_0c |          |
| `equip_presets+0x18`     | f32                     | unknown_equip_presets_18 |          |
| `equip_presets+0x1C`     | f32                     | unknown_equip_presets_1c |          |
| `equip_presets+0x20`     | String Table            | string_table             |          |
| `string_table+0x00`      | u32                     | string_table_start       |          |
| `string_table+0x04`      | u32                     | zero                     | `0`      |

### Tier (142 bytes)

| Offset  | Type          | Field                  | Notes |
| ------- | ------------- | ---------------------- | ----- |
| `+0x00` | u32           | min_rating             | |
| `+0x04` | u32           | max_ranking            | |
| `+0x08` | u16           | rank_tier_key          | |
| `+0x0A` | u32           | description            | |
| `+0x0E` | u32           | icon_texture           | |
| `+0x12` | u32           | match_slot_right_frame | |
| `+0x16` | u32           | match_slot_left_frame  | |
| `+0x1A` | u32           | hp_widget_right_frame  | |
| `+0x1E` | u32           | hp_widget_left_frame   | |
| `+0x22` | Item Block[3] | item_lists             | See Item Block |

### Item Block (36 bytes)

| Offset  | Type   | Field     | Notes |
| ------- | ------ | --------- | ----- |
| `+0x00` | u32[3] | item_keys | One item key per list, `0` for none |
| `+0x0C` | u64[3] | counts    | The count of each item |

## Layout 2

Client 3381 has the item blocks of Layout 3, no `unknown_modes_5d` and
`unknown_modes_61`, and no values after the presets.

### File Layout

| Offset                   | Type                    | Field                | Notes                     |
| ------------------------ | ----------------------- | -------------------- | ------------------------- |
| `+0x00`                  | char[4]                 | magic                | `PABR`                    |
| `+0x04`                  | Mode[4]                 | modes                | See Mode                  |
| `modes+0x00`             | f32                     | unknown_modes_00     |                           |
| `modes+0x04`             | u8                      | unknown_modes_04     |                           |
| `modes+0x05`             | f32                     | unknown_modes_05     |                           |
| `modes+0x09`             | u64[9]                  | unknown_modes_09     |                           |
| `modes+0x51`             | u32                     | unknown_win_str_ref  |                           |
| `modes+0x55`             | u32                     | unknown_draw_str_ref |                           |
| `modes+0x59`             | u32                     | unknown_lose_str_ref |                           |
| `modes+0x5D`             | u64                     | unknown_item_count   |                           |
| `modes+0x65`             | u32[unknown_item_count] | unknown_item_keys    |                           |
| `unknown_item_keys+0x00` | bytes[3]                | unknown_item_keys_00 | `01 01 01` on client 3381 |
| `unknown_item_keys+0x03` | Preset[48]              | equip_presets        |                           |
| `equip_presets+0x00`     | String Table            | string_table         |                           |
| `string_table+0x00`      | u32                     | string_table_start   |                           |
| `string_table+0x04`      | u32                     | zero                 | `0`                       |

### Tier (142 bytes)

| Offset  | Type          | Field                  | Notes |
| ------- | ------------- | ---------------------- | ----- |
| `+0x00` | u32           | min_rating             | |
| `+0x04` | u32           | max_ranking            | |
| `+0x08` | u16           | rank_tier_key          | |
| `+0x0A` | u32           | description            | |
| `+0x0E` | u32           | icon_texture           | |
| `+0x12` | u32           | match_slot_right_frame | |
| `+0x16` | u32           | match_slot_left_frame  | |
| `+0x1A` | u32           | hp_widget_right_frame  | |
| `+0x1E` | u32           | hp_widget_left_frame   | |
| `+0x22` | Item Block[3] | item_lists             | See Item Block |

### Item Block (36 bytes)

| Offset  | Type   | Field     | Notes |
| ------- | ------ | --------- | ----- |
| `+0x00` | u32[3] | item_keys | One item key per list, `0` for none |
| `+0x0C` | u64[3] | counts    | The count of each item |

## Layout 1

Clients 3314 and 3349 have the item blocks of Layout 3 and 38 presets,
the shared one at index `37`; the three bytes after the item keys and
the values after the presets are not there.

### File Layout

| Offset                   | Type                    | Field                | Notes    |
| ------------------------ | ----------------------- | -------------------- | -------- |
| `+0x00`                  | char[4]                 | magic                | `PABR`   |
| `+0x04`                  | Mode[4]                 | modes                | See Mode |
| `modes+0x00`             | f32                     | unknown_modes_00     |          |
| `modes+0x04`             | u8                      | unknown_modes_04     |          |
| `modes+0x05`             | f32                     | unknown_modes_05     |          |
| `modes+0x09`             | u64[9]                  | unknown_modes_09     |          |
| `modes+0x51`             | u32                     | unknown_win_str_ref  |          |
| `modes+0x55`             | u32                     | unknown_draw_str_ref |          |
| `modes+0x59`             | u32                     | unknown_lose_str_ref |          |
| `modes+0x5D`             | u64                     | unknown_item_count   |          |
| `modes+0x65`             | u32[unknown_item_count] | unknown_item_keys    |          |
| `unknown_item_keys+0x00` | Preset[38]              | equip_presets        |          |
| `equip_presets+0x00`     | String Table            | string_table         |          |
| `string_table+0x00`      | u32                     | string_table_start   |          |
| `string_table+0x04`      | u32                     | zero                 | `0`      |

### Tier (142 bytes)

| Offset  | Type          | Field                  | Notes |
| ------- | ------------- | ---------------------- | ----- |
| `+0x00` | u32           | min_rating             | |
| `+0x04` | u32           | max_ranking            | |
| `+0x08` | u16           | rank_tier_key          | |
| `+0x0A` | u32           | description            | |
| `+0x0E` | u32           | icon_texture           | |
| `+0x12` | u32           | match_slot_right_frame | |
| `+0x16` | u32           | match_slot_left_frame  | |
| `+0x1A` | u32           | hp_widget_right_frame  | |
| `+0x1E` | u32           | hp_widget_left_frame   | |
| `+0x22` | Item Block[3] | item_lists             | See Item Block |

### Item Block (36 bytes)

| Offset  | Type   | Field     | Notes |
| ------- | ------ | --------- | ----- |
| `+0x00` | u32[3] | item_keys | One item key per list, `0` for none |
| `+0x0C` | u64[3] | counts    | The count of each item |

## Item Lists

Every tier holds nine item lists, three per match type in the order
Ranked, Practice, Custom, and within each three the rewards of a
victory, a defeat and a draw. This is not the `SOLARE_WIN`,
`SOLARE_DRAW`, `SOLARE_LOSE` order of the strings.

| List | Match    | Result  |
| ---- | -------- | ------- |
| 1    | Ranked   | Victory |
| 2    | Ranked   | Defeat  |
| 3    | Ranked   | Draw    |
| 4    | Practice | Victory |
| 5    | Practice | Defeat  |
| 6    | Practice | Draw    |
| 7    | Custom   | Victory |
| 8    | Custom   | Defeat  |
| 9    | Custom   | Draw    |

On client 3482 lists 4 to 6 hold Seal of Solare `65396` x30, x15 and x20
on every tier, and lists 7 to 9 are empty. The Arena of Solare GM note on
the official NA/EU site (2025-05-29) gives Seal of Solare 30 for a
victory, 20 for a draw and 15 for a defeat, names a Victory and a Defeat
box for ranked matches and says Custom matches give no reward and
Practice matches keep the seal rewards. The 2026-04-30 patch notes list
the ranked boxes per point bracket: Enthusiastic and Indomitable from
1801 points, Elated and Courageous from 1201, Exultant and Rallying from
601, and Seal of Solare x30 and x15 at 600 points or less. Lists 1 and 2
of mode `0` hold the same boxes for the same `min_rating` ranges. Item
`890117` is Combat Secret Book (S) in `languagedata_en.loc`.

| Mode | Tiers (`rank_tier_key`) | List 1 | List 2 | List 3 |
| ---- | ----------------------- | ------ | ------ | ------ |
| 0    | `0x0001` to `0x0203`    | Enthusiastic Solare Box `890008` x1, `890117` x1 | Indomitable Solare Box `890009` x1 | Seal of Solare x20 |
| 0    | `0x0301` to `0x0403`    | Elated Solare Box `890006` x1, `890117` x1 | Courageous Solare Box `890007` x1 | Seal of Solare x20 |
| 0    | `0x0501` to `0x0602`    | Exultant Solare Box `890004` x1, `890117` x1 | Rallying Solare Box `890005` x1 | Seal of Solare x20 |
| 0    | `0x0603` to `0x0701`    | Seal of Solare x30 | Seal of Solare x15 | Seal of Solare x20 |
| 1    | `0x0001` to `0x0303`    | Elated Solare Box `761882` x1, `890117` x1 | Courageous Solare Box `761883` x1 | Seal of Solare x20 |
| 1    | `0x0401` to `0x0504`    | Exultant Solare Box `761606` x1, `890117` x1 | Rallying Solare Box `761607` x1 | Seal of Solare x20 |
| 1    | `0x0601` to `0x0701`    | Rallying Solare Box `761607` x1, `890117` x1 | Seal of Solare x15 | Seal of Solare x20 |

## Field Names

The tier fields follow the getters of the object that
`ToClient_GetSolareRankTierOption(gameMode, rating, ranking)` returns in
`panel_solrare_match_score.luac`, `panel_solrare_matching_1.luac` and
`panel_solrare_ranking_2.luac` (client 3482): `getRankTierKey()` with
`getRankGroup()` and `getTier()`, `getDescription()` (shown with
`PAGetString(Defines.StringSheet_GAME, ...)`), `getIconTextureID()` and
`getFrameTextureID(isLeft, isHPWidget)`; the four frame strings name the
side and the widget. The getter takes the game mode, which is the key of
a Mode, and a rating and ranking: `min_rating` falls by 100 from tier to
tier, and `max_ranking` limits the two top tiers to rank 1 and the top 30.
The preset fields follow `ToClient_GetSolareEquipPresetItemKey(equipSlotNo,
classType, presetLevel)` and `ToClient_GetSolareJewelPresetItemKey(equipSlot,
socketIndex)` in `panel_solrare_equippresetlist.luac`; the window passes
`__eClassType_Count` as the class type for every tab but the weapon tab,
and only the shared preset holds jewel items. The file is not in client
1784, and no sheet of a private server's `DataSheets.bexcel` on client
1784 has `Solare` in its name.

## Notes

- The file is in client 3314 and later. Apart from the `unknown_04` of
  the list items, the files of clients 3474 and 3482 are equal.
- Group `7` has one tier, `0x0701` with `min_rating` `0` (`Solare_Tier21`).
  The icons of group `0` are `Solare_Tier22` (rank 1), `Solare_Tier00`
  (top 30) and `Solare_Tier01`; every later tier has its own icon.
- The `unknown_04` of a list item looks like the upper half of a 64-bit
  value the build tool left unset.
- The handler (`_bss/solareoptionstaticstatusmanager/`) shows one row per
  tier of modes `0` and `1` with its non-empty item lists; the presets and
  the common values stay in the parser's result.

## Open Questions

### Game Modes 0 and 1

Both modes hold the same tiers and seal counts. Mode `1` has its own box
items (`761882`, `761883`, `761606`, `761607`), named like the Elated,
Courageous, Exultant and Rallying boxes of mode `0`, on other rank groups
(see the table in Item Lists), and no Enthusiastic or Indomitable box.
Which arena season or setting each mode is stays open. `ToClient_GetSolareRewardSize(solareMatchMode,
gameResultType)` in `panel_solrare_match_score.luac` reads the rewards by
match type and result; Layouts 1 to 3 keep the same grouping as three
blocks of three single items per tier.

### unknown_item_keys

On client 3482 the 20 item keys are two Sharp Alchemy Stones (`45220`,
`45252`), two Resolute Alchemy Stones (`741627`, `741628`), Secret Books
of Old Moon of every length (`46889`, `46890`, `47003`, `47006`, `47120`,
`47121`, `320133`, `601200` to `601207`) and item `48033`, which has no
LOC name. They could be items that are allowed,
or blocked, in the arena; no Lua getter reads them.

### Mode and Group Values

The 21 values of a mode and the nine fields of a group have no name. The group's
two `u8` + three `f32` blocks and the falling `unknown_0d` (`50`, `40`,
`30`) look like rating gain and loss settings per rank group.
