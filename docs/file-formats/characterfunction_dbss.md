# `characterfunction.dbss` Format

## Purpose

The dialog functions of every NPC: one record per character, holding the buttons its dialog window offers (Shop, Repair, Stable, Conversation, Node Management and so on), each with its Korean button text and an optional condition script that hides it. The Node Management slot also lists the nodes the NPC manages and the town it represents, the shop, guild shop and trade slots point at the [`itemmaingroup.bss`](itemmaingroup_bss.md) item lists of their Buy and Sell tabs, and the stable slot lists the vehicle types it keeps.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                           | Bytes     | Records                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Row bytes                |
| ------ | -------------- | ------------------------------ | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| 2      | 2834 and later | `characterfunction.dbss`       | 1,804,650 | 2,146 Shop Slot, 2,146 Shop Sell Slot, 2,146 Guild Shop Slot, 2,146 Guild Shop Sell Slot, 2,146 Trade Slot, 2,146 Auction Slot, 2,146 Mating Slot, 2,146 Inn Slot, 2,146 Text Slot, 27,898 Button Slot, 2,146 Stable Slot, 2,146 Conversation Slot, 2,146 Node Management Slot, 2,146 Minor Lord Menu Slot, 4,292 Territory Slot, 2,146 Unknown 1aa Slot, 2,146 Crafting Delivery Slot, 2,146 Skill Addon Slot, 6,438 Condition First Slot, 2,146 Maritime Trade Slot, 2,146 Hire Sailor Slot, 2,146 Season Gift Slot, 2,146 Yar Slot, 2,146 Pet Training Slot, 2,146 Lightstone Slot, 2,146 Function Record, 2,146 Record | 17 to 637, 17 on average |
| 2      | 2834 and later | `characterfunctionoffset.dbss` | 21,480    | 2,146 Index Row                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 10                       |
| 1      | 1680 to 1784   | `characterfunction.dbss`       | 1,276,360 | 1,458 Shop Slot, 1,458 Shop Sell Slot, 1,458 Guild Shop Slot, 1,458 Guild Shop Sell Slot, 1,458 Trade Slot, 1,458 Auction Slot, 1,458 Mating Slot, 1,458 Inn Slot, 1,458 Text Slot, 18,954 Button Slot, 1,458 Stable Slot, 1,458 Conversation Slot, 1,458 Node Management Slot, 1,458 Minor Lord Menu Slot, 2,916 Unknown 1aa Slot, 2,916 Territory Slot, 1,458 Crafting Delivery Slot, 1,458 Skill Addon Slot, 4,374 Condition First Slot, 1,458 Maritime Trade Slot, 1,458 Hire Sailor Slot, 1,458 Unknown 287 Slot, 1,458 Season Gift Slot, 1,458 Yar Slot, 1,458 Function Record, 1,458 Record                         | 17 to 289, 17 on average |
| 1      | 1680 to 1784   | `characterfunctionoffset.dbss` | 14,600    | 1,458 Index Row                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 10                       |

| Layout | File                           | Known               | Unknown         |
| ------ | ------------------------------ | ------------------- | --------------- |
| 2      | `characterfunction.dbss`       | 1,772,460 B (98.2%) | 32,190 B (1.8%) |
| 2      | `characterfunctionoffset.dbss` | 21,480 B (100.0%)   | 0 B (0.0%)      |
| 1      | `characterfunction.dbss`       | 1,251,574 B (98.1%) | 24,786 B (1.9%) |
| 1      | `characterfunctionoffset.dbss` | 14,600 B (100.0%)   | 0 B (0.0%)      |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `4009e96c8f82`  |
| 3482   | Layout 2             | `4009e96c8f82`  |
| 3474   | Layout 2             | `4009e96c8f82`  |
| 3473   | Layout 2             | `4009e96c8f82`  |
| 3464   | Layout 2             | `4009e96c8f82`  |
| 3458   | Layout 2             | `4009e96c8f82`  |
| 3454   | Layout 2             | `4009e96c8f82`  |
| 3444   | Layout 2             | `4009e96c8f82`  |
| 3435   | Layout 2             | `4009e96c8f82`  |
| 3426   | Layout 2             | `4009e96c8f82`  |
| 3418   | Layout 2             | `4009e96c8f82`  |
| 3412   | Layout 2             | `4009e96c8f82`  |
| 3402   | Layout 2             | `4009e96c8f82`  |
| 3396   | Layout 2             | `4009e96c8f82`  |
| 3387   | Layout 2             | `4009e96c8f82`  |
| 3381   | Layout 2             | `4009e96c8f82`  |
| 3373   | Layout 2             | `4009e96c8f82`  |
| 3364   | Layout 2             | `4009e96c8f82`  |
| 3356   | Layout 2             | `4009e96c8f82`  |
| 3349   | Layout 2             | `4009e96c8f82`  |
| 3342   | Layout 2             | `4009e96c8f82`  |
| 3335   | Layout 2             | `4009e96c8f82`  |
| 3326   | Layout 2             | `4009e96c8f82`  |
| 3321   | Layout 2             | `4009e96c8f82`  |
| 3314   | Layout 2             | `4009e96c8f82`  |
| 3303   | Layout 2             | `4009e96c8f82`  |
| 3302   | Layout 2             | `4009e96c8f82`  |
| 3293   | Layout 2             | `4009e96c8f82`  |
| 3283   | Layout 2             | `4009e96c8f82`  |
| 3275   | Layout 2             | `4009e96c8f82`  |
| 3267   | Layout 2             | `4009e96c8f82`  |
| 3258   | Layout 2             | `4009e96c8f82`  |
| 3251   | Layout 2             | `4009e96c8f82`  |
| 3242   | Layout 2             | `4009e96c8f82`  |
| 3235   | Layout 2             | `4009e96c8f82`  |
| 3229   | Layout 2             | `4009e96c8f82`  |
| 3212   | Layout 2             | `4009e96c8f82`  |
| 3203   | Layout 2             | `4009e96c8f82`  |
| 3193   | Layout 2             | `4009e96c8f82`  |
| 3186   | Layout 2             | `4009e96c8f82`  |
| 3177   | Layout 2             | `4009e96c8f82`  |
| 3169   | Layout 2             | `4009e96c8f82`  |
| 3158   | Layout 2             | `4009e96c8f82`  |
| 3151   | Layout 2             | `4009e96c8f82`  |
| 3144   | Layout 2             | `4009e96c8f82`  |
| 3133   | Layout 2             | `4009e96c8f82`  |
| 3125   | Layout 2             | `4009e96c8f82`  |
| 3118   | Layout 2             | `4009e96c8f82`  |
| 3111   | Layout 2             | `4009e96c8f82`  |
| 3103   | Layout 2             | `4009e96c8f82`  |
| 3095   | Layout 2             | `4009e96c8f82`  |
| 3086   | Layout 2             | `4009e96c8f82`  |
| 3072   | Layout 2             | `4009e96c8f82`  |
| 3062   | Layout 2             | `4009e96c8f82`  |
| 3052   | Layout 2             | `4009e96c8f82`  |
| 3045   | Layout 2             | `4009e96c8f82`  |
| 3037   | Layout 2             | `4009e96c8f82`  |
| 3030   | Layout 2             | `4009e96c8f82`  |
| 3021   | Layout 2             | `4009e96c8f82`  |
| 3012   | Layout 2             | `4009e96c8f82`  |
| 3002   | Layout 2             | `4009e96c8f82`  |
| 2995   | Layout 2             | `4009e96c8f82`  |
| 2987   | Layout 2             | `4009e96c8f82`  |
| 2978   | Layout 2             | `4009e96c8f82`  |
| 2970   | Layout 2             | `4009e96c8f82`  |
| 2959   | Layout 2             | `4009e96c8f82`  |
| 2951   | Layout 2             | `4009e96c8f82`  |
| 2942   | Layout 2             | `4009e96c8f82`  |
| 2935   | Layout 2             | `4009e96c8f82`  |
| 2932   | Layout 2             | `4009e96c8f82`  |
| 2923   | Layout 2             | `4009e96c8f82`  |
| 2919   | Layout 2             | `4009e96c8f82`  |
| 2907   | Layout 2             | `4009e96c8f82`  |
| 2900   | Layout 2             | `4009e96c8f82`  |
| 2891   | Layout 2             | `4009e96c8f82`  |
| 2882   | Layout 2             | `4009e96c8f82`  |
| 2872   | Layout 2             | `4009e96c8f82`  |
| 2863   | Layout 2             | `4009e96c8f82`  |
| 2855   | Layout 2             | `4009e96c8f82`  |
| 2849   | Layout 2             | `4009e96c8f82`  |
| 2844   | Layout 2             | `4009e96c8f82`  |
| 2834   | Layout 2             | `4009e96c8f82`  |
| 2825   | No documented layout | `4009e96c8f82`  |
| 2819   | No documented layout | `4009e96c8f82`  |
| 2811   | No documented layout | `4009e96c8f82`  |
| 2803   | No documented layout | `4009e96c8f82`  |
| 2794   | No documented layout | `4009e96c8f82`  |
| 2783   | No documented layout | `4009e96c8f82`  |
| 2774   | No documented layout | `4009e96c8f82`  |
| 2765   | No documented layout | `4009e96c8f82`  |
| 2756   | No documented layout | `4009e96c8f82`  |
| 2750   | No documented layout | `4009e96c8f82`  |
| 2743   | No documented layout | `4009e96c8f82`  |
| 2736   | No documented layout | `4009e96c8f82`  |
| 2726   | No documented layout | `4009e96c8f82`  |
| 2717   | No documented layout | `4009e96c8f82`  |
| 2709   | No documented layout | `4009e96c8f82`  |
| 2703   | No documented layout | `4009e96c8f82`  |
| 2695   | No documented layout | `4009e96c8f82`  |
| 2684   | No documented layout | `4009e96c8f82`  |
| 2672   | No documented layout | `4009e96c8f82`  |
| 2665   | No documented layout | `4009e96c8f82`  |
| 2657   | No documented layout | `4009e96c8f82`  |
| 2649   | No documented layout | `4009e96c8f82`  |
| 2644   | No documented layout | `4009e96c8f82`  |
| 2637   | No documented layout | `4009e96c8f82`  |
| 2629   | No documented layout | `4009e96c8f82`  |
| 2619   | No documented layout | `4009e96c8f82`  |
| 2612   | No documented layout | `4009e96c8f82`  |
| 2606   | No documented layout | `4009e96c8f82`  |
| 2602   | No documented layout | `4009e96c8f82`  |
| 2601   | No documented layout | `4009e96c8f82`  |
| 2592   | No documented layout | `4009e96c8f82`  |
| 2583   | No documented layout | `4009e96c8f82`  |
| 2575   | No documented layout | `4009e96c8f82`  |
| 2567   | No documented layout | `4009e96c8f82`  |
| 2560   | No documented layout | `4009e96c8f82`  |
| 2553   | No documented layout | `4009e96c8f82`  |
| 2545   | No documented layout | `4009e96c8f82`  |
| 2538   | No documented layout | `4009e96c8f82`  |
| 2529   | No documented layout | `4009e96c8f82`  |
| 2519   | No documented layout | `4009e96c8f82`  |
| 2513   | No documented layout | `4009e96c8f82`  |
| 2510   | No documented layout | `4009e96c8f82`  |
| 2507   | No documented layout | `4009e96c8f82`  |
| 2503   | No documented layout | `4009e96c8f82`  |
| 2498   | No documented layout | `4009e96c8f82`  |
| 2492   | No documented layout | `4009e96c8f82`  |
| 2487   | No documented layout | `4009e96c8f82`  |
| 2480   | No documented layout | `4009e96c8f82`  |
| 2474   | No documented layout | `4009e96c8f82`  |
| 2468   | No documented layout | `4009e96c8f82`  |
| 2460   | No documented layout | `4009e96c8f82`  |
| 2453   | No documented layout | `4009e96c8f82`  |
| 2444   | No documented layout | `4009e96c8f82`  |
| 2438   | No documented layout | `4009e96c8f82`  |
| 2434   | No documented layout | `4009e96c8f82`  |
| 2429   | No documented layout | `4009e96c8f82`  |
| 2421   | No documented layout | `4009e96c8f82`  |
| 2414   | No documented layout | `4009e96c8f82`  |
| 2407   | No documented layout | `4009e96c8f82`  |
| 2401   | No documented layout | `4009e96c8f82`  |
| 2397   | No documented layout | `4009e96c8f82`  |
| 2393   | No documented layout | `4009e96c8f82`  |
| 2384   | No documented layout | `4009e96c8f82`  |
| 2378   | No documented layout | `4009e96c8f82`  |
| 2372   | No documented layout | `4009e96c8f82`  |
| 2358   | No documented layout | `4009e96c8f82`  |
| 2352   | No documented layout | `4009e96c8f82`  |
| 2347   | No documented layout | `4009e96c8f82`  |
| 2343   | No documented layout | `4009e96c8f82`  |
| 2335   | No documented layout | `4009e96c8f82`  |
| 2327   | No documented layout | `4009e96c8f82`  |
| 2324   | No documented layout | `4009e96c8f82`  |
| 2319   | No documented layout | `4009e96c8f82`  |
| 2313   | No documented layout | `4009e96c8f82`  |
| 2308   | No documented layout | `4009e96c8f82`  |
| 2302   | No documented layout | `4009e96c8f82`  |
| 2295   | No documented layout | `4009e96c8f82`  |
| 2290   | No documented layout | `4009e96c8f82`  |
| 2284   | No documented layout | `4009e96c8f82`  |
| 2276   | No documented layout | `4009e96c8f82`  |
| 2269   | No documented layout | `4009e96c8f82`  |
| 2259   | No documented layout | `4009e96c8f82`  |
| 2250   | No documented layout | `4009e96c8f82`  |
| 2243   | No documented layout | `4009e96c8f82`  |
| 2235   | No documented layout | `4009e96c8f82`  |
| 2229   | No documented layout | `4009e96c8f82`  |
| 2224   | No documented layout | `4009e96c8f82`  |
| 2218   | No documented layout | `4009e96c8f82`  |
| 2215   | No documented layout | `4009e96c8f82`  |
| 2207   | No documented layout | `4009e96c8f82`  |
| 2203   | No documented layout | `4009e96c8f82`  |
| 2196   | No documented layout | `4009e96c8f82`  |
| 2192   | No documented layout | `4009e96c8f82`  |
| 2189   | No documented layout | `4009e96c8f82`  |
| 2183   | No documented layout | `4009e96c8f82`  |
| 2179   | No documented layout | `4009e96c8f82`  |
| 2171   | No documented layout | `4009e96c8f82`  |
| 2163   | No documented layout | `4009e96c8f82`  |
| 2156   | No documented layout | `4009e96c8f82`  |
| 2151   | No documented layout | `4009e96c8f82`  |
| 2147   | No documented layout | `4009e96c8f82`  |
| 2142   | No documented layout | `4009e96c8f82`  |
| 2138   | No documented layout | `4009e96c8f82`  |
| 2134   | No documented layout | `4009e96c8f82`  |
| 2130   | No documented layout | `4009e96c8f82`  |
| 2122   | No documented layout | `4009e96c8f82`  |
| 2107   | No documented layout | `4009e96c8f82`  |
| 2098   | No documented layout | `4009e96c8f82`  |
| 2089   | No documented layout | `4009e96c8f82`  |
| 2081   | No documented layout | `4009e96c8f82`  |
| 2073   | No documented layout | `4009e96c8f82`  |
| 2067   | No documented layout | `4009e96c8f82`  |
| 2063   | No documented layout | `4009e96c8f82`  |
| 2059   | No documented layout | `4009e96c8f82`  |
| 2052   | No documented layout | `4009e96c8f82`  |
| 2044   | No documented layout | `4009e96c8f82`  |
| 2039   | No documented layout | `4009e96c8f82`  |
| 2032   | No documented layout | `4009e96c8f82`  |
| 2025   | No documented layout | `4009e96c8f82`  |
| 2011   | No documented layout | `4009e96c8f82`  |
| 2005   | No documented layout | `4009e96c8f82`  |
| 2000   | No documented layout | `4009e96c8f82`  |
| 1996   | No documented layout | `4009e96c8f82`  |
| 1991   | No documented layout | `4009e96c8f82`  |
| 1985   | No documented layout | `4009e96c8f82`  |
| 1980   | No documented layout | `4009e96c8f82`  |
| 1969   | No documented layout | `4009e96c8f82`  |
| 1964   | No documented layout | `4009e96c8f82`  |
| 1958   | No documented layout | `4009e96c8f82`  |
| 1950   | No documented layout | `4009e96c8f82`  |
| 1945   | No documented layout | `4009e96c8f82`  |
| 1937   | No documented layout | `4009e96c8f82`  |
| 1933   | No documented layout | `4009e96c8f82`  |
| 1927   | No documented layout | `4009e96c8f82`  |
| 1921   | No documented layout | `4009e96c8f82`  |
| 1914   | No documented layout | `4009e96c8f82`  |
| 1908   | No documented layout | `4009e96c8f82`  |
| 1897   | No documented layout | `4009e96c8f82`  |
| 1892   | No documented layout | `4009e96c8f82`  |
| 1886   | No documented layout | `4009e96c8f82`  |
| 1881   | No documented layout | `4009e96c8f82`  |
| 1871   | No documented layout | `4009e96c8f82`  |
| 1866   | No documented layout | `4009e96c8f82`  |
| 1862   | No documented layout | `4009e96c8f82`  |
| 1854   | No documented layout | `4009e96c8f82`  |
| 1846   | No documented layout | `4009e96c8f82`  |
| 1838   | No documented layout | `4009e96c8f82`  |
| 1832   | No documented layout | `4009e96c8f82`  |
| 1826   | No documented layout | `4009e96c8f82`  |
| 1822   | No documented layout | `4009e96c8f82`  |
| 1818   | No documented layout | `4009e96c8f82`  |
| 1804   | No documented layout | `4009e96c8f82`  |
| 1794   | No documented layout | `4009e96c8f82`  |
| 1790   | No documented layout | `4009e96c8f82`  |
| 1784   | Layout 1             | `4009e96c8f82`  |
| 1774   | Layout 1             | `4009e96c8f82`  |
| 1771   | Layout 1             | `4009e96c8f82`  |
| 1762   | Layout 1             | `4009e96c8f82`  |
| 1759   | Layout 1             | `4009e96c8f82`  |
| 1754   | Layout 1             | `4009e96c8f82`  |
| 1749   | Layout 1             | `4009e96c8f82`  |
| 1743   | Layout 1             | `4009e96c8f82`  |
| 1737   | Layout 1             | `4009e96c8f82`  |
| 1731   | Layout 1             | `4009e96c8f82`  |
| 1725   | Layout 1             | `4009e96c8f82`  |
| 1717   | Layout 1             | `4009e96c8f82`  |
| 1710   | Layout 1             | `4009e96c8f82`  |
| 1704   | Layout 1             | `4009e96c8f82`  |
| 1698   | Layout 1             | `4009e96c8f82`  |
| 1690   | Layout 1             | `4009e96c8f82`  |
| 1685   | Layout 1             | `4009e96c8f82`  |
| 1680   | Layout 1             | `4009e96c8f82`  |
| 1674   | No documented layout | `4009e96c8f82`  |
| 1668   | No documented layout | `4009e96c8f82`  |
| 1659   | No documented layout | `4009e96c8f82`  |
| 1649   | No documented layout | `4009e96c8f82`  |
| 1642   | No documented layout | `4009e96c8f82`  |
| 1636   | No documented layout | `4009e96c8f82`  |
| 1628   | No documented layout | `4009e96c8f82`  |
| 1622   | No documented layout | `4009e96c8f82`  |
| 1614   | No documented layout | `4009e96c8f82`  |
| 1608   | No documented layout | `4009e96c8f82`  |
| 1602   | No documented layout | `4009e96c8f82`  |
| 1598   | No documented layout | `4009e96c8f82`  |
| 1594   | No documented layout | `4009e96c8f82`  |
| 1590   | No documented layout | `4009e96c8f82`  |
| 1587   | No documented layout | `4009e96c8f82`  |
| 1584   | No documented layout | `4009e96c8f82`  |
| 1579   | No documented layout | `4009e96c8f82`  |
| 1572   | No documented layout | `4009e96c8f82`  |
| 1565   | No documented layout | `4009e96c8f82`  |
| 1559   | No documented layout | `4009e96c8f82`  |
| 1554   | No documented layout | `4009e96c8f82`  |
| 1547   | No documented layout | `4009e96c8f82`  |
| 1537   | No documented layout | `4009e96c8f82`  |
| 1529   | No documented layout | `4009e96c8f82`  |
| 1524   | No documented layout | `4009e96c8f82`  |
| 1519   | No documented layout | `4009e96c8f82`  |
| 1509   | No documented layout | `4009e96c8f82`  |
| 1506   | No documented layout | `4009e96c8f82`  |
| 1504   | No documented layout | `4009e96c8f82`  |
| 1500   | No documented layout | `4009e96c8f82`  |
| 1493   | No documented layout | `4009e96c8f82`  |
| 1489   | No documented layout | `4009e96c8f82`  |
| 1485   | No documented layout | `4009e96c8f82`  |
| 1481   | No documented layout | `4009e96c8f82`  |
| 1474   | No documented layout | `4009e96c8f82`  |
| 1466   | No documented layout | `4009e96c8f82`  |
| 1462   | No documented layout | `4009e96c8f82`  |
| 1459   | No documented layout | `4009e96c8f82`  |
| 1453   | No documented layout | `4009e96c8f82`  |
| 1450   | No documented layout | `4009e96c8f82`  |
| 1445   | No documented layout | `4009e96c8f82`  |
| 1439   | No documented layout | `4009e96c8f82`  |
| 1433   | No documented layout | `4009e96c8f82`  |
| 1430   | No documented layout | `4009e96c8f82`  |
| 1426   | No documented layout | `4009e96c8f82`  |
| 1421   | No documented layout | `4009e96c8f82`  |
| 1417   | No documented layout | `4009e96c8f82`  |
| 1416   | No documented layout | `4009e96c8f82`  |
| 1409   | No documented layout | `4009e96c8f82`  |
| 1405   | No documented layout | `4009e96c8f82`  |
| 1401   | No documented layout | `4009e96c8f82`  |
| 1396   | No documented layout | `4009e96c8f82`  |
| 1391   | No documented layout | `4009e96c8f82`  |
| 1390   | No documented layout | `4009e96c8f82`  |
| 1386   | No documented layout | `4009e96c8f82`  |
| 1381   | No documented layout | `4009e96c8f82`  |
| 1379   | No documented layout | `4009e96c8f82`  |
| 1372   | No documented layout | `4009e96c8f82`  |
| 1366   | No documented layout | `4009e96c8f82`  |
| 1364   | No documented layout | `4009e96c8f82`  |
| 1363   | No documented layout | `4009e96c8f82`  |
| 1360   | No documented layout | `4009e96c8f82`  |
| 1358   | No documented layout | `4009e96c8f82`  |
| 1355   | No documented layout | `4009e96c8f82`  |
| 1351   | No documented layout | `4009e96c8f82`  |
| 1348   | No documented layout | `4009e96c8f82`  |
| 1346   | No documented layout | `4009e96c8f82`  |
| 1341   | No documented layout | `4009e96c8f82`  |
| 1340   | No documented layout | `4009e96c8f82`  |
| 1338   | No documented layout | `4009e96c8f82`  |
| 1335   | No documented layout | `4009e96c8f82`  |
| 1333   | No documented layout | `4009e96c8f82`  |
| 1329   | No documented layout | `4009e96c8f82`  |
| 1327   | No documented layout | `4009e96c8f82`  |
| 1324   | No documented layout | `4009e96c8f82`  |
| 1321   | No documented layout | `4009e96c8f82`  |
| 1319   | No documented layout | `4009e96c8f82`  |
| 1318   | No documented layout | `4009e96c8f82`  |
| 1316   | No documented layout | `4009e96c8f82`  |
| 1313   | No documented layout | `4009e96c8f82`  |
| 1311   | No documented layout | `4009e96c8f82`  |
| 1309   | No documented layout | `4009e96c8f82`  |
| 1304   | No documented layout | `4009e96c8f82`  |
| 1292   | No documented layout | `4009e96c8f82`  |
| 1286   | No documented layout | `4009e96c8f82`  |
| 1280   | No documented layout | `4009e96c8f82`  |
| 1276   | No documented layout | `4009e96c8f82`  |
| 1267   | No documented layout | `4009e96c8f82`  |
| 1261   | No documented layout | `4009e96c8f82`  |
| 1256   | No documented layout | `4009e96c8f82`  |
| 1250   | No documented layout | `4009e96c8f82`  |
| 1246   | No file              | `4009e96c8f82`  |
| 1239   | No file              | `4009e96c8f82`  |
| 1230   | No file              | `4009e96c8f82`  |
| 1226   | No file              | `4009e96c8f82`  |
| 1220   | No file              | `4009e96c8f82`  |
| 1217   | No file              | `4009e96c8f82`  |
| 1211   | No file              | `4009e96c8f82`  |
| 1210   | No file              | `4009e96c8f82`  |
| 1208   | No file              | `4009e96c8f82`  |
| 1203   | No file              | `4009e96c8f82`  |
| 1197   | No file              | `4009e96c8f82`  |
| 1194   | No file              | `4009e96c8f82`  |
| 1192   | No file              | `4009e96c8f82`  |
| 1187   | No file              | `4009e96c8f82`  |
| 1183   | No file              | `4009e96c8f82`  |
| 1177   | No file              | `4009e96c8f82`  |
| 1173   | No file              | `4009e96c8f82`  |
| 1167   | No file              | `4009e96c8f82`  |
| 1164   | No file              | `4009e96c8f82`  |
| 1156   | No file              | `4009e96c8f82`  |
| 1149   | No file              | `4009e96c8f82`  |
| 1144   | No file              | `4009e96c8f82`  |
| 1137   | No file              | `4009e96c8f82`  |
| 1132   | No file              | `4009e96c8f82`  |
| 1127   | No file              | `4009e96c8f82`  |
| 1122   | No file              | `4009e96c8f82`  |
| 1118   | No file              | `4009e96c8f82`  |
| 1114   | No file              | `4009e96c8f82`  |
| 1109   | No file              | `4009e96c8f82`  |
| 1102   | No file              | `4009e96c8f82`  |
| 1096   | No file              | `4009e96c8f82`  |
| 1088   | No file              | `4009e96c8f82`  |
| 1081   | No file              | `4009e96c8f82`  |
| 1076   | No file              | `4009e96c8f82`  |
| 1069   | No file              | `4009e96c8f82`  |
| 1064   | No file              | `4009e96c8f82`  |
| 1058   | No file              | `4009e96c8f82`  |
| 1051   | No file              | `4009e96c8f82`  |
| 1044   | No file              | `4009e96c8f82`  |
| 1036   | No file              | `4009e96c8f82`  |
| 1026   | No file              | `4009e96c8f82`  |
| 1016   | No file              | `4009e96c8f82`  |
| 1009   | No file              | `4009e96c8f82`  |
| 1005   | No file              | `4009e96c8f82`  |
| 1000   | No file              | `4009e96c8f82`  |
| 998    | No file              | `4009e96c8f82`  |
| 990    | No file              | `4009e96c8f82`  |
| 979    | No file              | `4009e96c8f82`  |
| 972    | No file              | `4009e96c8f82`  |
| 963    | No file              | `4009e96c8f82`  |
| 955    | No file              | `4009e96c8f82`  |
| 946    | No file              | `4009e96c8f82`  |
| 938    | No file              | `4009e96c8f82`  |
| 927    | No file              | `4009e96c8f82`  |
| 911    | No file              | `4009e96c8f82`  |
| 904    | No file              | `4009e96c8f82`  |
| 899    | No file              | `4009e96c8f82`  |
| 894    | No file              | `4009e96c8f82`  |
| 885    | No file              | `4009e96c8f82`  |
| 879    | No file              | `4009e96c8f82`  |
| 872    | No file              | `4009e96c8f82`  |
| 864    | No file              | `4009e96c8f82`  |
| 855    | No file              | `4009e96c8f82`  |
| 853    | No file              | `4009e96c8f82`  |
| 845    | No file              | `4009e96c8f82`  |
| 837    | No file              | `4009e96c8f82`  |
| 829    | No file              | `4009e96c8f82`  |
| 822    | No file              | `4009e96c8f82`  |
| 814    | No file              | `4009e96c8f82`  |
| 805    | No file              | `4009e96c8f82`  |
| 794    | No file              | `4009e96c8f82`  |
| 787    | No file              | `4009e96c8f82`  |
| 780    | No file              | `4009e96c8f82`  |
| 771    | No file              | `4009e96c8f82`  |
| 760    | No file              | `4009e96c8f82`  |
| 748    | No file              | `4009e96c8f82`  |
| 741    | No file              | `4009e96c8f82`  |
| 736    | No file              | `4009e96c8f82`  |
| 731    | No file              | `4009e96c8f82`  |
| 723    | No file              | `4009e96c8f82`  |
| 711    | No file              | `4009e96c8f82`  |
| 707    | No file              | `4009e96c8f82`  |
| 697    | No file              | `4009e96c8f82`  |
| 689    | No file              | `4009e96c8f82`  |
| 683    | No file              | `4009e96c8f82`  |
| 678    | No file              | `4009e96c8f82`  |
| 670    | No file              | `4009e96c8f82`  |
| 661    | No file              | `4009e96c8f82`  |
| 656    | No file              | `4009e96c8f82`  |
| 652    | No file              | `4009e96c8f82`  |
| 643    | No file              | `4009e96c8f82`  |
| 637    | No file              | `4009e96c8f82`  |
| 630    | No file              | `4009e96c8f82`  |
| 627    | No file              | `4009e96c8f82`  |
| 621    | No file              | `4009e96c8f82`  |
| 617    | No file              | `4009e96c8f82`  |
| 615    | No file              | `4009e96c8f82`  |
| 606    | No file              | `4009e96c8f82`  |
| 599    | No file              | `4009e96c8f82`  |
| 592    | No file              | `4009e96c8f82`  |
| 586    | No file              | `4009e96c8f82`  |
| 577    | No file              | `4009e96c8f82`  |
| 569    | No file              | `4009e96c8f82`  |
| 561    | No file              | `4009e96c8f82`  |
| 554    | No file              | `4009e96c8f82`  |
| 542    | No file              | `4009e96c8f82`  |
| 532    | No file              | `4009e96c8f82`  |
| 531    | No file              | `4009e96c8f82`  |
| 526    | No file              | `4009e96c8f82`  |
| 521    | No file              | `4009e96c8f82`  |
| 517    | No file              | `4009e96c8f82`  |
| 510    | No file              | `4009e96c8f82`  |
| 508    | No file              | `4009e96c8f82`  |
| 504    | No file              | `4009e96c8f82`  |
| 497    | No file              | `4009e96c8f82`  |
| 491    | No file              | `4009e96c8f82`  |
| 485    | No file              | `4009e96c8f82`  |
| 478    | No file              | `4009e96c8f82`  |
| 472    | No file              | `4009e96c8f82`  |
| 466    | No file              | `4009e96c8f82`  |
| 457    | No file              | `4009e96c8f82`  |
| 452    | No file              | `4009e96c8f82`  |
| 449    | No file              | `4009e96c8f82`  |
| 435    | No file              | `4009e96c8f82`  |

<!-- versions:end -->

## Companion Files

| File                           | Required | Role                                                              |
| ------------------------------ | -------- | ----------------------------------------------------------------- |
| `characterfunctionoffset.dbss` | Required | Maps `character_id` to the byte offset and size of its record     |
| `languagedata_en.loc`          | Optional | NPC names (type `6`), button text (type `32`), node names (type `29`) |

All multi-byte values are little-endian. A string is a u64 length in UTF-16 code units followed by UTF-16LE text with no terminator.

## Layout 2

### File Layout

| Offset  | Type          | Field   | Notes                                                            |
| ------- | ------------- | ------- | ---------------------------------------------------------------- |
| `+0x00` | u32           | count   | Record count; `2,146` on client 3458, equal to the offset count  |
| `+0x04` | Record[count] | records | Back to back: a u16 `character_id`, then the record it keys      |

Each record is preceded by a u16 inline copy of its `character_id`; `data_offset` points just past it, as in `characterstatic.dbss`. The first record's ID sits at `+0x04` and its data at `+0x06`, every gap between records is exactly those 2 bytes, and the last record ends at end of file. Records are not stored in key order.

### Record (variable: 2 bytes + function record)

| Offset  | Type            | Field           | Notes                                                        |
| ------- | --------------- | --------------- | ------------------------------------------------------------ |
| `+0x00` | u16             | character_id    | Inline copy of the index row's `character_id`                |
| `+0x02` | Function Record | function_record | `data_size` bytes; the index row's `data_offset` points here |

### Function Record (variable: 11 bytes + slots)

A record is a 4-byte head, 40 function slots in a fixed order, then a 7-byte tail. Nothing is optional: a slot the NPC does not use still stores its two strings (empty) and its fields. With every string and list empty a record is 732 bytes; 1,434 of 2,146 records are exactly that plus their string text. The positions in such an all-empty record name the `unknown_<hex>` fields (see the Slots table); in a real record every string and list moves what follows it.

Walking head, slots and tail ends exactly at `data_size` in all 2,146 records.

| Offset                        | Type                       | Field                      | Notes |
| ----------------------------- | -------------------------- | -------------------------- | ----- |
| `+0x00`                       | u8                         | shop_type                  | `eShopType`, see Shop Types; `0` (1,521) to `16`, `14` (ItemMarket) exactly on the 22 Central Market NPCs |
| `+0x01`                       | u8                         | trade_group_type           | `ETradeGroupType`: `1` Normal, or `2` Desert on the desert traders 45011, 45012 and 45209 |
| `+0x02`                       | u8                         | is_smuggle_shop            | Always `0` |
| `+0x03`                       | u8                         | servant_type               | `eServantType`: `0` Vehicle (111, the stable, guild mount and siege stable NPCs), `1` Ship (60, the wharves), `6` on the 1,975 records without a stable |
| `+0x04`                       | Shop Slot                  | shop                       | See Shop Slot |
| `shop+0x00`                   | Shop Sell Slot             | shop_sell                  | See Shop Sell Slot |
| `shop_sell+0x00`              | Guild Shop Slot            | guild_shop                 | See Guild Shop Slot |
| `guild_shop+0x00`             | Guild Shop Sell Slot       | guild_shop_sell            | See Guild Shop Sell Slot |
| `guild_shop_sell+0x00`        | Trade Slot                 | trade                      | See Trade Slot |
| `trade+0x00`                  | Auction Slot               | auction                    | See Auction Slot |
| `auction+0x00`                | Mating Slot                | mating                     | See Mating Slot |
| `mating+0x00`                 | Inn Slot                   | inn                        | See Inn Slot |
| `inn+0x00`                    | Text Slot                  | reward_explore             | See Text Slot |
| `reward_explore+0x00`         | Button Slot                | learn_skill                | See Button Slot |
| `learn_skill+0x00`            | Button Slot                | repair                     | See Button Slot |
| `repair+0x00`                 | Button Slot                | traces_of_blood            | See Button Slot |
| `traces_of_blood+0x00`        | Button Slot                | storage                    | See Button Slot |
| `storage+0x00`                | Stable Slot                | stable                     | See Stable Slot |
| `stable+0x00`                 | Button Slot                | transport                  | See Button Slot |
| `transport+0x00`              | Button Slot                | transport_person           | See Button Slot |
| `transport_person+0x00`       | Conversation Slot          | conversation               | See Conversation Slot |
| `conversation+0x00`           | Button Slot                | create_guild               | See Button Slot |
| `create_guild+0x00`           | Node Management Slot       | node_management            | See Node Management Slot |
| `node_management+0x00`        | Button Slot                | lord_information           | See Button Slot |
| `lord_information+0x00`       | Minor Lord Menu Slot       | minor_lord_menu            | See Minor Lord Menu Slot |
| `minor_lord_menu+0x00`        | Button Slot                | extraction                 | See Button Slot |
| `extraction+0x00`             | Territory Slot             | imperial_delivery          | See Territory Slot |
| `imperial_delivery+0x00`      | Unknown 1aa Slot           | unknown_1aa                | See Unknown 1aa Slot |
| `unknown_1aa+0x00`            | Button Slot                | knowledge_management       | See Button Slot |
| `knowledge_management+0x00`   | Crafting Delivery Slot     | imperial_crafting_delivery | See Crafting Delivery Slot |
| `imperial_crafting_delivery+0x00` | Button Slot            | imperial_fishing_delivery  | See Button Slot |
| `imperial_fishing_delivery+0x00`  | Button Slot            | guild_supply_shop          | See Button Slot |
| `guild_supply_shop+0x00`      | Skill Addon Slot           | skill_addon                | See Skill Addon Slot |
| `skill_addon+0x00`            | Condition First Slot       | give_gift                  | See Condition First Slot |
| `give_gift+0x00`              | Condition First Slot       | cleanse_gear               | See Condition First Slot |
| `cleanse_gear+0x00`           | Condition First Slot       | black_spirit_adventure     | See Condition First Slot |
| `black_spirit_adventure+0x00` | Territory Slot             | central_market             | See Territory Slot |
| `central_market+0x00`         | Maritime Trade Slot        | maritime_trade             | See Maritime Trade Slot |
| `maritime_trade+0x00`         | Hire Sailor Slot           | hire_sailor                | See Hire Sailor Slot |
| `hire_sailor+0x00`            | Season Gift Slot           | season_special_gift        | See Season Gift Slot |
| `season_special_gift+0x00`    | Button Slot                | hall_of_honor              | See Button Slot |
| `hall_of_honor+0x00`          | Yar Slot                   | yar                        | See Yar Slot |
| `yar+0x00`                    | Pet Training Slot          | pet_training               | See Pet Training Slot |
| `pet_training+0x00`           | Lightstone Slot            | lightstone                 | See Lightstone Slot |
| `lightstone+0x00`             | u8                         | unknown_2d5                | `2`, or `1` on the 125 records with a Trade button |
| `lightstone+0x01`             | u8                         | unknown_2d6                | `0`, or `1` on character 62327 only |
| `lightstone+0x02`             | u32                        | unknown_2d7                | Always `0` |
| `lightstone+0x06`             | u8                         | unknown_2db                | Always `1` |

`LOC` is the `str_id4` of the slot's button in LOC type `32`, whose `str_id1` is the character ID. Its English text for each Korean `name` is listed alongside; slots with `-` have no LOC text. Counts are records with button text on client 3458. The second column is the slot's position in the all-empty record.

| #  | Position | Slot                         | LOC | Records | Korean names                                                       | LOC text                                                        | Slot fields |
| -- | -------- | ---------------------------- | --- | ------: | ------------------------------------------------------------------ | --------------------------------------------------------------- | ----------- |
| 1  | `+0x004` | `shop`                       | 0   | 893     | 상점, 환전소, 비밀 상점, 일꾼 계약, 그믐달 상점, ... (25 names)      | Shop, Currency Exchange, Secret Shop, Contract Workers, Old Moon Shop, War Shop (Tier 1) ... | u32 `shop_buy_group` |
| 2  | `+0x018` | `shop_sell`                  | -   | 0       | | | u32 `shop_sell_group` |
| 3  | `+0x02C` | `guild_shop`                 | 4   | 63      | 길드 상점, 길드 군수품, 길드 대장 상점                              | Guild Shop, Guild Military Supply, Guild Master Shop            | u32 `guild_shop_buy_group` |
| 4  | `+0x040` | `guild_shop_sell`            | -   | 0       | | | u32 `guild_shop_sell_group` |
| 5  | `+0x054` | `trade`                      | 2   | 125     | 무역                                                               | Trade, Trading                                                  | u32 `trade_group` |
| 6  | `+0x068` | `auction` | 6 | 48 | 일꾼거래소, 황실 경매, 길드 하우스 경매, 경매 : 천년의 걸작 | Worker Exchange, Imperial Auction, Guild House Auction, Auction: Thousand Years Masterpiece | u16 `auction_key` |
| 7  | `+0x07A` | `mating` | - | 0 | | | u16 `mating_key` |
| 8  | `+0x08C` | `inn` | - | 0 | | | u16 `inn_key` |
| 9  | `+0x09E` | `reward_explore` | - | 0 | | | |
| 10 | `+0x0AE` | `learn_skill` | 10 | 53 | 기술 배우기 | Learn Skills | u8 `has_button` |
| 11 | `+0x0BF` | `repair` | 11 | 260 | 수리 | Repair | u8 `has_button` |
| 12 | `+0x0D0` | `traces_of_blood` | - | 9 | 피의 흔적 | | u8 `has_button` |
| 13 | `+0x0E1` | `storage` | 12 | 34 | 창고 | Storage | u8 `has_button` |
| 14 | `+0x0F2` | `stable` | 13 | 171 | 마구간, 선착장, 길드 선착장, 길드 탑승물 관리 | Stable, Wharf, Guild Wharf, Manage Guild Mounts | u8 `servant_where_type`, u8 list `vehicle_types` |
| 15 | `+0x107` | `transport` | 14 | 32 | 수송 | Transport | u8 `has_button` |
| 16 | `+0x118` | `transport_person` | - | 0 | | | u8 `has_button` |
| 17 | `+0x129` | `conversation` | 16 | 1,133 | 이야기 교류 | Conversation | u8 `has_button`, u8 `is_greet` |
| 18 | `+0x13B` | `create_guild` | 17 | 17 | 길드 창설 | Create Guild | u8 `has_button` |
| 19 | `+0x14C` | `node_management` | 18 | 523 | 탐험 거점 관리 | Node Management | u32 list `managed_node_keys`, u32 list `town_node_keys` |
| 20 | `+0x164` | `lord_information` | 19 | 5 | 영주 정보 | Lord Information | u8 `has_button` |
| 21 | `+0x175` | `minor_lord_menu` | - | 0 | | | u8 `has_button`, u8 `unknown_186` |
| 22 | `+0x187` | `extraction` | 21 | 53 | 추출 | Extract, Extraction | u8 `has_button` |
| 23 | `+0x198` | `imperial_delivery` | 23 | 7 | 황실 납품 | Imperial Delivery | u16 `territory_key` |
| 24 | `+0x1AA` | `unknown_1aa` | - | 0 | | | u16 `unknown_1ba` |
| 25 | `+0x1BC` | `knowledge_management` | 24 | 9 | 지식관리 | Knowledge Management | u8 `has_button` |
| 26 | `+0x1CD` | `imperial_crafting_delivery` | 25 | 13 | 황실제작 납품 | Imperial Crafting Delivery | u8 `has_button`, u8 `supply_shop_key` |
| 27 | `+0x1DF` | `imperial_fishing_delivery` | 26 | 13 | 황실낚시 납품 | Imperial Fishing Delivery | u8 `has_button` |
| 28 | `+0x1F0` | `guild_supply_shop` | - | 0 | | | u8 `has_button` |
| 29 | `+0x201` | `skill_addon` | 28 | 55 | 기술 특화 | Skill Add-on | u8 `has_button`, u8 `is_stallion_skill_training` |
| 30 | `+0x213` | `give_gift` | 29 | 24 | 선물하기 | Give Gift | u8 `has_button` |
| 31 | `+0x224` | `cleanse_gear` | 30 | 29 | 장비 정화 | Cleanse Gear | u8 `has_button` |
| 32 | `+0x235` | `black_spirit_adventure` | - | 1 | 흑정령의 모험 | | u8 `has_button` |
| 33 | `+0x246` | `central_market` | 31 | 22 | 통합 거래소 | Central Market | u16 `territory_key` |
| 34 | `+0x258` | `maritime_trade` | - | 91 | 해상 교역 | | u16 `barter_region_key` |
| 35 | `+0x26A` | `hire_sailor` | 32 | 23 | 선원 고용 | Hire Sailor | u8 `employee_job`, u8 `has_button`, u8 `unknown_27c`, u16 `employee_key` |
| 36 | `+0x27F` | `season_special_gift` | 34 | 1 | 시즌 특별 선물 | Season Special Gift | u8 `unknown_28f` |
| 37 | `+0x290` | `hall_of_honor` | 35 | 1 | 영광의 전장 | Hall of Honor | u8 `has_button` |
| 38 | `+0x2A1` | `yar` | 36 | 8 | 야르 | Yar, Yar! | u8 `unknown_2b1` |
| 39 | `+0x2B2` | `pet_training` | 38 | 6 | 반려동물 5세대 훈련 | Tier 5 Pet Training | u8 `has_button`, u8 `unknown_2c3` |
| 40 | `+0x2C4` | `lightstone` | 39 | 1 | 광명석 교환/정화 | Lightstone | u8 `unknown_2d4` |

A list is a u32 count followed by that many items. The slot keys are the parser's names, after the button text; `shop_sell` and `guild_shop_sell` are named after their item group (see Item Groups). They and the slots `mating`, `inn`, `reward_explore`, `transport_person`, `minor_lord_menu`, `unknown_1aa` and `guild_supply_shop` never have button text.

Every slot opens with two strings: `name`, the Korean button text, empty when the NPC lacks the function, and `condition`, a script that must pass for the button to show, e.g. `isContentsGroupOpen(0,4004);`. The slot's own fields follow. `give_gift`, `cleanse_gear` and `black_spirit_adventure` store `condition` before `name`. Conditions use the client's script calls (`isContentsGroupOpen`, `checkexplore`, `clearquest`, `getlevel`, `getIntimacy`), joined with `;` and alternatives split by `<or>`.

On the slots with a `has_button` field, that u8 is `1` exactly when `name` is not empty, in every record.

The `unknown_<hex>` names of the slot fields are positions in the all-empty record, like the Slots table: a field sits `0x10` past its slot, after the two empty strings. A list counts as its 4-byte count.

### Text Slot (variable: 16 bytes + text)

The `reward_explore` slot.

| Offset      | Type  | Field     | Notes                                                                             |
| ----------- | ----- | --------- | --------------------------------------------------------------------------------- |
| `+0x00`     | str16 | name      | Korean button text, empty when the NPC lacks the function                         |
| `name+0x00` | str16 | condition | Script that must pass for the button to show, e.g. `isContentsGroupOpen(0,4004);` |

### Button Slot (variable: 17 bytes + text)

The `learn_skill`, `repair`, `traces_of_blood`, `storage`, `transport`, `transport_person`, `create_guild`, `lord_information`, `extraction`, `knowledge_management`, `imperial_fishing_delivery`, `guild_supply_shop` and `hall_of_honor` slots.

| Offset           | Type  | Field      | Notes                                         |
| ---------------- | ----- | ---------- | --------------------------------------------- |
| `+0x00`          | str16 | name       | Korean button text                            |
| `name+0x00`      | str16 | condition  | Script that must pass for the button to show  |
| `condition+0x00` | u8    | has_button | `1` exactly when `name` is not empty          |

### Condition First Slot (variable: 17 bytes + text)

The `give_gift`, `cleanse_gear` and `black_spirit_adventure` slots, which store `condition` before `name`.

| Offset           | Type  | Field      | Notes                                         |
| ---------------- | ----- | ---------- | --------------------------------------------- |
| `+0x00`          | str16 | condition  | Script that must pass for the button to show  |
| `condition+0x00` | str16 | name       | Korean button text                            |
| `name+0x00`      | u8    | has_button | `1` exactly when `name` is not empty          |

### Shop Slot (variable: 20 bytes + text)

| Offset           | Type  | Field          | Notes |
| ---------------- | ----- | -------------- | ----- |
| `+0x00`          | str16 | name           | Korean button text |
| `name+0x00`      | str16 | condition      | Script that must pass for the button to show |
| `condition+0x00` | u32   | shop_buy_group | `itemmaingroup.bss` group of the Shop window's Buy tab; non-zero on 884 of the 893 shop records and nowhere else; 491 values in `32,002` to `55,053` |

### Shop Sell Slot (variable: 20 bytes + text)

| Offset           | Type  | Field           | Notes |
| ---------------- | ----- | --------------- | ----- |
| `+0x00`          | str16 | name            | Never set |
| `name+0x00`      | str16 | condition       | Script that must pass for the button to show |
| `condition+0x00` | u32   | shop_sell_group | Group of the Sell tab: `52001` (683), `52002` (41), `32001` (16), `52004` (3), else `0`; the slot never has a button |

### Guild Shop Slot (variable: 20 bytes + text)

| Offset           | Type  | Field                | Notes |
| ---------------- | ----- | -------------------- | ----- |
| `+0x00`          | str16 | name                 | Korean button text |
| `name+0x00`      | str16 | condition            | Script that must pass for the button to show |
| `condition+0x00` | u32   | guild_shop_buy_group | Group of the guild shop's Buy tab; non-zero exactly on the 63 guild shop records; 11 values in `51,100` to `51,908` |

### Guild Shop Sell Slot (variable: 20 bytes + text)

| Offset           | Type  | Field                 | Notes |
| ---------------- | ----- | --------------------- | ----- |
| `+0x00`          | str16 | name                  | Never set |
| `name+0x00`      | str16 | condition             | Script that must pass for the button to show |
| `condition+0x00` | u32   | guild_shop_sell_group | Group of the guild shop's Sell tab: `52003` on 61 of the 63 guild shop records, else `0` |

### Trade Slot (variable: 20 bytes + text)

| Offset           | Type  | Field       | Notes |
| ---------------- | ----- | ----------- | ----- |
| `+0x00`          | str16 | name        | Korean button text |
| `name+0x00`      | str16 | condition   | Script that must pass for the button to show |
| `condition+0x00` | u32   | trade_group | `itemmaingroup.bss` group; non-zero exactly on the 125 trade records; 62 values in `54,002` to `54,146` |

### Auction Slot (variable: 18 bytes + text)

| Offset           | Type  | Field       | Notes |
| ---------------- | ----- | ----------- | ----- |
| `+0x00`          | str16 | name        | Korean button text |
| `name+0x00`      | str16 | condition   | Script that must pass for the button to show |
| `condition+0x00` | u16   | auction_key | `140` Worker Exchange, `1001` Imperial Auction, `101` to `143` Guild House Auction, `1002`/`1003` Thousand Years Masterpiece; also `105` on 46 records without an auction button, 44 of them shop NPCs |

### Mating Slot (variable: 18 bytes + text)

| Offset           | Type  | Field      | Notes |
| ---------------- | ----- | ---------- | ----- |
| `+0x00`          | str16 | name       | Never set |
| `name+0x00`      | str16 | condition  | Script that must pass for the button to show |
| `condition+0x00` | u16   | mating_key | `104` on 46 shop NPCs without an auction button, 44 of them with `auction_key` = `105` |

### Inn Slot (variable: 18 bytes + text)

| Offset           | Type  | Field     | Notes |
| ---------------- | ----- | --------- | ----- |
| `+0x00`          | str16 | name      | Never set |
| `name+0x00`      | str16 | condition | Script that must pass for the button to show |
| `condition+0x00` | u16   | inn_key   | Always `0` |

### Stable Slot (variable: 21 bytes + text and vehicle types)

| Offset                    | Type                     | Field              | Notes |
| ------------------------- | ------------------------ | ------------------ | ----- |
| `+0x00`                   | str16                    | name               | Korean button text |
| `name+0x00`               | str16                    | condition          | Script that must pass for the button to show |
| `condition+0x00`          | u8                       | servant_where_type | `CppEnums.ServantWhereType`, see Vehicle Types; `9` without a stable |
| `condition+0x01`          | u32                      | vehicle_type_count | Number of `vehicle_types` |
| `condition+0x05`          | u8[vehicle_type_count]   | vehicle_types      | `CppEnums.VehicleType` values, see Vehicle Types; empty without a stable |

### Conversation Slot (variable: 18 bytes + text)

| Offset           | Type  | Field      | Notes |
| ---------------- | ----- | ---------- | ----- |
| `+0x00`          | str16 | name       | Korean button text |
| `name+0x00`      | str16 | condition  | Script that must pass for the button to show |
| `condition+0x00` | u8    | has_button | `1` exactly when `name` is not empty |
| `condition+0x01` | u8    | is_greet   | `1` on 1,127 of the 1,133 Conversation records and on 16 others, else `0` |

### Node Management Slot (variable: 24 bytes + text and node lists)

| Offset                   | Type                         | Field                  | Notes |
| ------------------------ | ---------------------------- | ---------------------- | ----- |
| `+0x00`                  | str16                        | name                   | Korean button text |
| `name+0x00`              | str16                        | condition              | Script that must pass for the button to show |
| `condition+0x00`         | u32                          | managed_node_key_count | Number of `managed_node_keys` |
| `condition+0x04`         | u32[managed_node_key_count]  | managed_node_keys      | `exploration.bss` node keys whose `manager_family_id` is this character, in all 957 entries |
| `managed_node_keys+0x00` | u32                          | town_node_key_count    | Number of `town_node_keys` |
| `managed_node_keys+0x04` | u32[town_node_key_count]     | town_node_keys         | One node on 21 records, each a town whose `exploration.bss` `representative_id` is this character (Velia `1` -> 40017) |

### Minor Lord Menu Slot (variable: 18 bytes + text)

| Offset           | Type  | Field       | Notes |
| ---------------- | ----- | ----------- | ----- |
| `+0x00`          | str16 | name        | Never set |
| `name+0x00`      | str16 | condition   | Script that must pass for the button to show |
| `condition+0x00` | u8    | has_button  | `1` exactly when `name` is not empty |
| `condition+0x01` | u8    | unknown_186 | Always `0` |

### Territory Slot (variable: 18 bytes + text)

The `imperial_delivery` and `central_market` slots.

| Offset           | Type  | Field         | Notes |
| ---------------- | ----- | ------------- | ----- |
| `+0x00`          | str16 | name          | Korean button text |
| `name+0x00`      | str16 | condition     | Script that must pass for the button to show |
| `condition+0x00` | u16   | territory_key | Territory key: `0` to `7` on the seven Imperial Delivery NPCs (one value each), `0` to `6` on Central Market NPCs (`0` on 16), else `0xFFFF` (none) |

### Unknown 1aa Slot (variable: 18 bytes + text)

The `unknown_1aa` slot: its own `name` and `condition`; no record has button text in it.

| Offset           | Type  | Field       | Notes |
| ---------------- | ----- | ----------- | ----- |
| `+0x00`          | str16 | name        | Never set |
| `name+0x00`      | str16 | condition   | Script that must pass for the button to show |
| `condition+0x00` | u16   | unknown_1ba | Always `0xFFFF` |

### Crafting Delivery Slot (variable: 18 bytes + text)

The `imperial_crafting_delivery` slot.

| Offset           | Type  | Field           | Notes |
| ---------------- | ----- | --------------- | ----- |
| `+0x00`          | str16 | name            | Korean button text |
| `name+0x00`      | str16 | condition       | Script that must pass for the button to show |
| `condition+0x00` | u8    | has_button      | `1` exactly when `name` is not empty |
| `condition+0x01` | u8    | supply_shop_key | `1` exactly on the 13 Imperial Crafting Delivery records |

### Skill Addon Slot (variable: 18 bytes + text)

| Offset           | Type  | Field                      | Notes |
| ---------------- | ----- | -------------------------- | ----- |
| `+0x00`          | str16 | name                       | Korean button text |
| `name+0x00`      | str16 | condition                  | Script that must pass for the button to show |
| `condition+0x00` | u8    | has_button                 | `1` exactly when `name` is not empty |
| `condition+0x01` | u8    | is_stallion_skill_training | `1` on 3 records |

### Maritime Trade Slot (variable: 18 bytes + text)

| Offset           | Type  | Field             | Notes |
| ---------------- | ----- | ----------------- | ----- |
| `+0x00`          | str16 | name              | Korean button text |
| `name+0x00`      | str16 | condition         | Script that must pass for the button to show |
| `condition+0x00` | u16   | barter_region_key | `regioninfo.bss` region key of the island, port or ship where this NPC barters; a different one on each of the 91 records, else `0`. [`barter_npclist.bss`](barter_npclist_bss.md) lists the same 91 keys, each with this character's ID (all 91 match, client 3464) |

### Hire Sailor Slot (variable: 21 bytes + text)

| Offset           | Type  | Field        | Notes |
| ---------------- | ----- | ------------ | ----- |
| `+0x00`          | str16 | name         | Korean button text |
| `name+0x00`      | str16 | condition    | Script that must pass for the button to show |
| `condition+0x00` | u8    | employee_job | `employeestaticstatus.bss` `job`: `0` (Sailor) on the 23 Hire Sailor records, `2` on all others |
| `condition+0x01` | u8    | has_button   | `1` exactly when `name` is not empty |
| `condition+0x02` | u8    | unknown_27c  | Always `0` |
| `condition+0x03` | u16   | employee_key | `1` to `23`, a different one per Hire Sailor record. With `employee_job` and `has_button` (`1`, the level) it names the `employeestaticstatus.bss` row of the sailor for hire: all 23 records resolve (client 3464) |

### Season Gift Slot (variable: 17 bytes + text)

The `season_special_gift` slot.

| Offset           | Type  | Field       | Notes |
| ---------------- | ----- | ----------- | ----- |
| `+0x00`          | str16 | name        | Korean button text; `<Null>` in 2,139 records |
| `name+0x00`      | str16 | condition   | Script that must pass for the button to show |
| `condition+0x00` | u8    | unknown_28f | `1` only on the record with button text |

The `<Null>` text is a placeholder: `season_special_gift` stores it as `name` in 2,139 records, and LOC type `32` index `34` holds `<Null>` for 138 of them. It is not a button.

### Yar Slot (variable: 17 bytes + text)

| Offset           | Type  | Field       | Notes |
| ---------------- | ----- | ----------- | ----- |
| `+0x00`          | str16 | name        | Korean button text |
| `name+0x00`      | str16 | condition   | Script that must pass for the button to show |
| `condition+0x00` | u8    | unknown_2b1 | `1` on the 8 Yar records and two more |

### Pet Training Slot (variable: 18 bytes + text)

| Offset           | Type  | Field       | Notes |
| ---------------- | ----- | ----------- | ----- |
| `+0x00`          | str16 | name        | Korean button text |
| `name+0x00`      | str16 | condition   | Script that must pass for the button to show |
| `condition+0x00` | u8    | has_button  | `1` exactly when `name` is not empty |
| `condition+0x01` | u8    | unknown_2c3 | `1` on 23 records, all with Shop, Repair and Stable buttons |

### Lightstone Slot (variable: 17 bytes + text)

| Offset           | Type  | Field       | Notes |
| ---------------- | ----- | ----------- | ----- |
| `+0x00`          | str16 | name        | Korean button text |
| `name+0x00`      | str16 | condition   | Script that must pass for the button to show |
| `condition+0x00` | u8    | unknown_2d4 | `1` on the Lightstone record and on 32 stable NPCs |

### `characterfunctionoffset.dbss`

PABR index with 10-byte rows.

| Offset              | Type             | Field        | Observed | Notes                       |
| ------------------- | ---------------- | ------------ | -------- | --------------------------- |
| `+0x00`             | char[4]          | magic        |          | `PABR` (ASCII)              |
| `+0x04`             | u32              | count        | `2,146`  | Number of rows              |
| `+0x08`             | Index Row[count] | rows         |          | See Index Row               |
| `rows+0x00`         | String Table     | string_table |          | The 12-byte trailer starts here; see String Table |
| `string_table+0x00` | u32              | end_of_rows  | `21,468` | `8 + count * 10`            |
| `string_table+0x04` | u32              | zero         | `0`      |                             |

Earlier versions of this doc called `string_count` the trailer's `unknown_00` and `zero` its `unknown_08`.

### Index Row (10 bytes)

| Offset  | Type | Field        | Notes                                                   |
| ------- | ---- | ------------ | ------------------------------------------------------- |
| `+0x00` | u16  | character_id | Unique; observed `9,999` to `64,780`, unsorted          |
| `+0x02` | u32  | data_offset  | Absolute offset of the record, just past its inline ID  |
| `+0x06` | u32  | data_size    | Record size; observed `740` to `3,102`                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes      |
| ------- | ------------------ | ------------ | ---------- |
| `+0x00` | u32                | string_count | Always `0` |
| `+0x04` | pstr[string_count] | strings      | Empty      |

## Layout 1

On client 1784 the five item group fields were u16, a slot with a u16
`0xFFFF` sat before `imperial_delivery`, a slot with the `checkEdanPass();`
condition sat after `hire_sailor`, the `pet_training` and `lightstone`
slots did not exist, and the tail was 5 bytes. The all-empty record is 724
bytes. Field names keep Layout 2's positions; the two slots that exist only
here are named by their position in the all-empty record of this layout.
The parser reads only Layout 2.

### Function Record (variable: 9 bytes + slots)

| Offset                            | Type                   | Field                      | Notes |
| --------------------------------- | ---------------------- | -------------------------- | ----- |
| `+0x00`                           | u8                     | shop_type                  | |
| `+0x01`                           | u8                     | trade_group_type           | |
| `+0x02`                           | u8                     | is_smuggle_shop            | |
| `+0x03`                           | u8                     | servant_type               | |
| `+0x04`                           | Shop Slot              | shop                       | |
| `shop+0x00`                       | Shop Sell Slot         | shop_sell                  | |
| `shop_sell+0x00`                  | Guild Shop Slot        | guild_shop                 | |
| `guild_shop+0x00`                 | Guild Shop Sell Slot   | guild_shop_sell            | |
| `guild_shop_sell+0x00`            | Trade Slot             | trade                      | |
| `trade+0x00`                      | Auction Slot           | auction                    | |
| `auction+0x00`                    | Mating Slot            | mating                     | |
| `mating+0x00`                     | Inn Slot               | inn                        | |
| `inn+0x00`                        | Text Slot              | reward_explore             | |
| `reward_explore+0x00`             | Button Slot            | learn_skill                | |
| `learn_skill+0x00`                | Button Slot            | repair                     | |
| `repair+0x00`                     | Button Slot            | traces_of_blood            | |
| `traces_of_blood+0x00`            | Button Slot            | storage                    | |
| `storage+0x00`                    | Stable Slot            | stable                     | |
| `stable+0x00`                     | Button Slot            | transport                  | |
| `transport+0x00`                  | Button Slot            | transport_person           | |
| `transport_person+0x00`           | Conversation Slot      | conversation               | |
| `conversation+0x00`               | Button Slot            | create_guild               | |
| `create_guild+0x00`               | Node Management Slot   | node_management            | |
| `node_management+0x00`            | Button Slot            | lord_information           | |
| `lord_information+0x00`           | Minor Lord Menu Slot   | minor_lord_menu            | |
| `minor_lord_menu+0x00`            | Button Slot            | extraction                 | |
| `extraction+0x00`                 | Unknown 1aa Slot       | unknown_18e                | Never set; its u16 is `0xFFFF` in all 1,561 records on client 1784 |
| `unknown_18e+0x00`                | Territory Slot         | imperial_delivery          | |
| `imperial_delivery+0x00`          | Unknown 1aa Slot       | unknown_1aa                | |
| `unknown_1aa+0x00`                | Button Slot            | knowledge_management       | |
| `knowledge_management+0x00`       | Crafting Delivery Slot | imperial_crafting_delivery | |
| `imperial_crafting_delivery+0x00` | Button Slot            | imperial_fishing_delivery  | |
| `imperial_fishing_delivery+0x00`  | Button Slot            | guild_supply_shop          | |
| `guild_supply_shop+0x00`          | Skill Addon Slot       | skill_addon                | |
| `skill_addon+0x00`                | Condition First Slot   | give_gift                  | |
| `give_gift+0x00`                  | Condition First Slot   | cleanse_gear               | |
| `cleanse_gear+0x00`               | Condition First Slot   | black_spirit_adventure     | |
| `black_spirit_adventure+0x00`     | Territory Slot         | central_market             | |
| `central_market+0x00`             | Maritime Trade Slot    | maritime_trade             | |
| `maritime_trade+0x00`             | Hire Sailor Slot       | hire_sailor                | |
| `hire_sailor+0x00`                | Unknown 287 Slot       | unknown_287                | See Unknown 287 Slot |
| `unknown_287+0x00`                | Season Gift Slot       | season_special_gift        | |
| `season_special_gift+0x00`        | Button Slot            | hall_of_honor              | |
| `hall_of_honor+0x00`              | Yar Slot               | yar                        | |
| `yar+0x00`                        | u32                    | unknown_2d7                | Always `0` on client 1784 |
| `yar+0x04`                        | u8                     | unknown_2db                | `1`, or `0` on 7 records on client 1784 |

The tail lines up with Layout 2's `unknown_2d7` and `unknown_2db` by value;
the two u8 before them in Layout 2 have no counterpart here.

### Shop Slot (variable: 18 bytes + text)

| Offset           | Type  | Field          | Notes |
| ---------------- | ----- | -------------- | ----- |
| `+0x00`          | str16 | name           | |
| `name+0x00`      | str16 | condition      | |
| `condition+0x00` | u16   | shop_buy_group | |

### Shop Sell Slot (variable: 18 bytes + text)

| Offset           | Type  | Field           | Notes |
| ---------------- | ----- | --------------- | ----- |
| `+0x00`          | str16 | name            | |
| `name+0x00`      | str16 | condition       | |
| `condition+0x00` | u16   | shop_sell_group | |

### Guild Shop Slot (variable: 18 bytes + text)

| Offset           | Type  | Field                | Notes |
| ---------------- | ----- | -------------------- | ----- |
| `+0x00`          | str16 | name                 | |
| `name+0x00`      | str16 | condition            | |
| `condition+0x00` | u16   | guild_shop_buy_group | |

### Guild Shop Sell Slot (variable: 18 bytes + text)

| Offset           | Type  | Field                 | Notes |
| ---------------- | ----- | --------------------- | ----- |
| `+0x00`          | str16 | name                  | |
| `name+0x00`      | str16 | condition             | |
| `condition+0x00` | u16   | guild_shop_sell_group | |

### Trade Slot (variable: 18 bytes + text)

| Offset           | Type  | Field       | Notes |
| ---------------- | ----- | ----------- | ----- |
| `+0x00`          | str16 | name        | |
| `name+0x00`      | str16 | condition   | |
| `condition+0x00` | u16   | trade_group | |

The u16 equals Layout 2's u32 in 1,468 of the 1,557 records both clients
share for `shop_buy_group` and 1,545 for `trade_group`.

### Unknown 287 Slot (variable: 21 bytes + text)

| Offset           | Type  | Field       | Notes |
| ---------------- | ----- | ----------- | ----- |
| `+0x00`          | str16 | name        | `임시` on 420 records on client 1784, empty on the rest |
| `name+0x00`      | str16 | condition   | `checkEdanPass();` on the same 420 records |
| `condition+0x00` | u8    | has_button  | `1` exactly when `name` is not empty |
| `condition+0x01` | u32   | unknown_298 | `0`, or one of 21 values from `1` to `1,691` on 21 records |

## Item Groups

The five `*_group` fields are [`itemmaingroup.bss`](itemmaingroup_bss.md) group IDs; all 884, 743, 63, 61 and 125 non-zero values are in its ID set (client 3464). The client's shop window (`panel_dialog_npcshop_all_1.luac`) has a Buy and a Sell tab, filled from `npcShop_getBuyCount()` / `npcShop_getItemBuy()` and `npcShop_getSellCount()` / `npcShop_getItemSell()`, and opens for `npcShop_isShopContents()` or `npcShop_isGuildShopContents()`. Each shop and guild shop NPC stores two groups, and their items tell them apart:

| Field                   | Example (client 3464)                                                                                       |
| ----------------------- | ----------------------------------------------------------------------------------------------------------- |
| `shop_buy_group`        | General store Benyamin (47459): group 50503, HP and MP potions; Currency Exchange Lafi Bedmountain (47745): 50022, Gold Bar 1G to 10,000G |
| `shop_sell_group`       | 52001, 11,556 items on 683 NPCs, holding Black Stone and Iron Ore but not Memory Fragment or Cron Stone; 52002 on 41 NPCs, 36 of them Currency Exchange, Gold Bars and Bartali Gold Bar; 52004 on the 3 Crow Shop NPCs, ocean materials such as Luminous Cobalt Ingot |
| `guild_shop_buy_group`  | Edan (47754): 51100, `[Guild]` potions, Parchment, Seal                                                      |
| `guild_shop_sell_group` | 52003, 390 items such as `[Guild] HP Potion (Small)`                                                                                   |
| `trade_group`           | Isobelle Encarotia (47747): 54146; every trade group lists subgroup 54001 (item 55151) under `checkexplore(103, 1)` |

`shop_sell_group` sits in its own slot right after `shop` and `guild_shop_sell_group` after `guild_shop`. 11 records set `shop_sell_group` without a shop button; all of them hold `52001`.

Checked in game (2026-10-14, client 3464): Benyamin's Shop Sell tab lists 14 items from a full inventory, Black Stone among them, and every one of them is in group `52001`, his `shop_sell_group`. The Memory Fragment in the same inventory, which `52001` does not hold, is not listed. His Purchase tab lists exactly the 18 items of his `shop_buy_group`, `50503` (HP and MP potions, Medical Kit, the two Alchemy Tools, Empty Crystal and the two Atanis Fireflies), in the order the subgroup stores them.

## Vehicle Types

`vehicle_types` is a u32 count and that many u8 `CppEnums.VehicleType` values (`global_define_cpp_enum.luac`). Every stored value is an enum member. The list is in stored order and can repeat a value: 8 stables store `53` twice.

| Button               | `servant_where_type` | `vehicle_types` (client 3464)                                                                                   |
| -------------------- | -------------------- | --------------------------------------------------------------------------------------------------------------- |
| Stable (91)          | `0` User             | `0` Horse, `2` Camel, `3` Donkey, `9` Carriage, `28` CowCarriage, `32` MountainGoat, `40` RidableBabyElephant, `48` RepairableCarriage, `53` RaceHorse; 88 stables take all nine |
| Wharf (40)           | `0` User             | `18` Boat, `29` Raft, `33` FishingBoat, `44` PersonalBattleShip, `46` PersonTradeShip, `52` PersonalBoat, `55` FastShip, `56` CashPersonalTradeShip, `57` CashPersonalBattleShip, `60` Carrack; 34 wharves take all ten, 5 only the first three, 1 all but FastShip |
| Guild Wharf (20)     | `1` Guild            | `34` SailingBoat                                                                                                |
| Manage Guild Mounts (18) | `1` Guild        | `4` Elephant, `35` Train, `63` GuildDragon                                                                      |
| Stable, Forward Supply Depot (37094) | `2` Siege | `0` Horse, `2` Camel                                                                                  |
| Stable, Miles (59279) | `5` RaceHorse       | `53` RaceHorse                                                                                                  |

`servant_where_type` follows `CppEnums.ServantWhereType` (`ServantWhereTypeUser` 0, `Guild` 1, `Siege` 2, `RaceHorse` 5); the enum gives `5` to both `Camping` and `RaceHorse`, and the one stable with `5` takes only race horses. The `9` on the 1,975 records without a stable is past `ServantWhereTypeCount` (8).

## Shop Types

`shop_type` follows the `_shopType` table of `panel_dialog_main_all.luac` (the `eShopType_` members of the 2016 client's `gc::ShopType` stop at `DayRandomShop`; `ItemMarket` and `Instrument` came later). Records per value on client 3464:

| Value | Name          | Records |
| ----- | ------------- | ------: |
| `0`   | None          | 1,521   |
| `1`   | Potion        | 144     |
| `2`   | Weapon        | 105     |
| `3`   | Jewel         | 16      |
| `4`   | Furniture     | 38      |
| `5`   | Collect       | 59      |
| `6`   | Fish          | 38      |
| `7`   | Worker        | 31      |
| `8`   | Alchemy       | 1       |
| `9`   | Cook          | 35      |
| `10`  | PC            | 0       |
| `11`  | Grocery       | 90      |
| `12`  | RandomShop    | 23      |
| `13`  | DayRandomShop | 10      |
| `14`  | ItemMarket    | 22      |
| `15`  | Instrument    | 4       |
| `16`  | (`_Count`)    | 9       |

The 9 records with `16` (47022, 46041, 50973, 49525 to 49529, 49548) store the enum's `_Count`.

## Field Names

Most names above come from two sources. The 2016 client (build of 2016-01-11) ships with debug symbols: its `gc::CharacterFunctionStaticStatus` starts with `_shopType`, `_tradeGroupType`, `_isSmuggleShop` and `_servantType`, then holds a name, a condition and the slot fields for each function in this order: BuyingFromNpc, SellingToNpc, BuyingFromGuildShopNpc, SellingToGuildShopNpc, Trading, Auction (`_auctionKey`), Mating (`_matingKey`), Inn (`_innKey`), RewardExplore, TrainSkill, Repair, Warehouse, Stable, Transfer, TransferPerson, IntimacyGame (`_isIntimacyGame`, `_isGreet`), Guild, Explore (`_exploreWaypoints`, `_guideWaypoints`), LordMenu, MinorLordMenu (`_minorLordRegionKey`), Extract, TerritoryTrade, TerritorySupply, ItemMarket, Knowledge, SupplyShop, FishSupplyShop and GuildSupplyShop. The server-side `CharacterFunction_Table` of a private server on client 519 has a column for each, and I matched every column against every field over the 1,318 characters it shares with the client file.

The LOC index of a button is the function's place in that column order: `0` BuyingFromNpc, `2` Trading, `4` BuyingFromGuildShopNpc, `6` Auction, `10` TrainSkill ... `23` TerritorySupply, `27` GuildSupplyShop, `31` NewItemMarket, `32` Employee.

Matches on client 3464 (1,318 shared characters):

| Field                        | Slot                         | `CharacterFunction_Table` column | Matching |
| ---------------------------- | ---------------------------- | -------------------------------- | -------: |
| shop_type                    | head                         | `ShopType`                       | 1,302    |
| trade_group_type             | head                         | `TradeGroupType`                 | 1,318    |
| auction_key                  | `auction`                    | `AuctionKey`                     | 1,318    |
| mating_key                   | `mating`                     | `MatingKey`                      | 1,318    |
| servant_where_type           | `stable`                     | `StableType`                     | 1,316    |
| vehicle_types                | `stable`                     | `StableKey`                      | 1,305    |
| is_greet                     | `conversation`               | `isGreetNpc`                     | 1,303    |
| managed_node_keys            | `node_management`            | `ExploreWaypoint`                | 1,271    |
| town_node_keys               | `node_management`            | `GuideWaypoint`                  | 1,316    |
| name, territory_key          | `imperial_delivery`          | `TerritorySupplyName`, `TerritoryKeyForTerritorySupply` | 1,317 |
| supply_shop_key              | `imperial_crafting_delivery` | `SupplyShopKey`                  | 1,318    |
| is_stallion_skill_training   | `skill_addon`                | `isStallionSkillExpTraining`     | 1,318    |
| name                         | `black_spirit_adventure`     | `DiceGame`                       | 1,318    |
| name, territory_key          | `central_market`             | `NewItemMarketName`, `TerritoryKeyForNewItemMarket` | 1,317 |
| name, barter_region_key             | `maritime_trade`             | `BarterName`, `isBarter`         | 1,318    |
| employee_job, employee_key   | `hire_sailor`                | `EmployeeJob`, `EmployeeType`    | 1,318    |

The `territory_key` fields hold `0xFFFF` where the server column is empty, and `employee_job` holds `2`. `is_smuggle_shop`, `servant_type`, `inn_key` and the slots `reward_explore`, `transport_person`, `minor_lord_menu` and `guild_supply_shop` have no server column with values; they are named from their place in the 2016 member order between matched fields. `servant_type` follows `gc::ServantType` (`0` Vehicle, `1` Ship, `2` Pet), which the stable records bear out (see Function Record). The old `auction` slot fields (`unknown_078` u32, 14 skipped bytes, `unknown_08a` u32, 32 skipped bytes) were the auction key and the empty Mating, Inn and RewardExplore slots read across.

## Notes

- 97 records have no button text in any slot.
- LOC type `32` names buttons for 2,049 of the 2,146 characters. It also holds 69 characters this file has no record for, and an index `33` (`temp` or `[PH]`) on 436 records, 414 of them Node Management NPCs, that matches no slot.
- The slot order is close to, but not the same as, the client's `CppEnums.ContentsType` (`Contents_Shop`, `Contents_Skill`, `Contents_Repair`, `Contents_Auction`, `Contents_Warehouse`, `Contents_IntimacyGame`, `Contents_Stable`, ... in `global_define_cpp_enum.luac`), and the LOC indexes do not follow the slot order either (Trade is LOC `2` but the fifth slot): they follow the column order of `CharacterFunction_Table`, see Field Names.
- `itemtradegrouptonpc.dbss` is keyed by character ID too (47747 is a trade NPC), so `trade_group` is not its key.
- `barter_region_key` values are region keys, not `exploration.bss` node keys: the barter windows key their lists by region (`ToClient_barterWrapper(RegionKey(regionKey))` in `panel_window_barterinfosearch_2.luac`).

## Open Questions

### Auction and Mating Keys

`auction_key` (`140` Worker Exchange, `1001` Imperial Auction, `101` to `143` Guild House Auction) and `mating_key` (`104`) are keys of the auction and mating tables (`gc::AuctionStaticStatus` in the 2016 client), but none of their values is an `itemmaingroup.bss` group ID (0 of 94 and 0 of 46 records, client 3464), and the client file holding those tables has not been found.

### Tail Bytes

`unknown_2d5` is `1` exactly on the 125 trade NPCs and `2` elsewhere. Neither the 2016 member list nor the server table has a field for it.

### Slots Without Button Text

`unknown_1aa` (`unknown_1ba` always `0xFFFF`) has no column match. By the LOC column order it is likely TerritoryTrade (`22`, next to TerritorySupply), but this file stores it after `imperial_delivery`, while the 2016 client stores TerritoryTrade first. `minor_lord_menu` stores `0` in both bytes, where the 2016 client had a u16 `_minorLordRegionKey`; the server still lists a region key for 155 characters.
