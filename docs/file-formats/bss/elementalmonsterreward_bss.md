# `elementalmonsterreward.bss` Format

## Purpose

The ranking rewards of the Black Shrine (검은 사당) bosses in the Land of the
Morning Light: per boss character, the items of each rank tier ("#1",
"#2 ~ #5") and the items of the "Bonus Rewards" row for players outside the
ranks. The detailed reward window
(`panel_window_morningland_detailreward_all.luac`) reads it per boss through
`ToClient_getElementalMonsterRankReward*` and
`ToClient_getElementalMonsterBaseReward*`, with a flag that picks the
second table for the Hwanghae (Party) ranking.

On client 3474 the first table has a record for each of the 108 bosses of
[`elementalmonsterstat.bss`](elementalmonsterstat_bss.md): the 94 Donghae
(Solo) bosses with the tiers `1`, `5` and `20` and two base items, the 14
Hwanghae (Party) bosses with two base items and no tiers. The second table
has the 14 Hwanghae (Party) bosses with their party tiers and no base items.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                         | Bytes  | Records                                    | Row bytes |
| ------ | -------------- | ---------------------------- | ------ | ------------------------------------------ | --------- |
| 3      | 3473 and later | `elementalmonsterreward.bss` | 18,240 | 797 Reward Item, 319 Rank Tier, 118 Record | 16        |
| 2      | 2619 to 3464   | `elementalmonsterreward.bss` | 4,782  | 453 Reward Item, 331 Rank Tier, 122 Record | 6         |
| 1      | 2224 to 2612   | `elementalmonsterreward.bss` | 4,204  | 400 Reward Item, 300 Rank Tier, 100 Record | 6         |

| Layout | File                         | Known             | Unknown    |
| ------ | ---------------------------- | ----------------- | ---------- |
| 3      | `elementalmonsterreward.bss` | 18,240 B (100.0%) | 0 B (0.0%) |
| 2      | `elementalmonsterreward.bss` | 4,782 B (100.0%)  | 0 B (0.0%) |
| 1      | `elementalmonsterreward.bss` | 4,204 B (100.0%)  | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 3 | `fb43e6d6e69c`  |
| 3482   | Layout 3 | `fb43e6d6e69c`  |
| 3474   | Layout 3 | `fb43e6d6e69c`  |
| 3473   | Layout 3 | `fb43e6d6e69c`  |
| 3464   | Layout 2 | `fb43e6d6e69c`  |
| 3458   | Layout 2 | `fb43e6d6e69c`  |
| 3454   | Layout 2 | `fb43e6d6e69c`  |
| 3444   | Layout 2 | `fb43e6d6e69c`  |
| 3435   | Layout 2 | `fb43e6d6e69c`  |
| 3426   | Layout 2 | `fb43e6d6e69c`  |
| 3418   | Layout 2 | `fb43e6d6e69c`  |
| 3412   | Layout 2 | `fb43e6d6e69c`  |
| 3402   | Layout 2 | `fb43e6d6e69c`  |
| 3396   | Layout 2 | `fb43e6d6e69c`  |
| 3387   | Layout 2 | `fb43e6d6e69c`  |
| 3381   | Layout 2 | `fb43e6d6e69c`  |
| 3373   | Layout 2 | `fb43e6d6e69c`  |
| 3364   | Layout 2 | `fb43e6d6e69c`  |
| 3356   | Layout 2 | `fb43e6d6e69c`  |
| 3349   | Layout 2 | `fb43e6d6e69c`  |
| 3342   | Layout 2 | `fb43e6d6e69c`  |
| 3335   | Layout 2 | `fb43e6d6e69c`  |
| 3326   | Layout 2 | `fb43e6d6e69c`  |
| 3321   | Layout 2 | `fb43e6d6e69c`  |
| 3314   | Layout 2 | `fb43e6d6e69c`  |
| 3303   | Layout 2 | `fb43e6d6e69c`  |
| 3302   | Layout 2 | `fb43e6d6e69c`  |
| 3293   | Layout 2 | `fb43e6d6e69c`  |
| 3283   | Layout 2 | `fb43e6d6e69c`  |
| 3275   | Layout 2 | `fb43e6d6e69c`  |
| 3267   | Layout 2 | `fb43e6d6e69c`  |
| 3258   | Layout 2 | `fb43e6d6e69c`  |
| 3251   | Layout 2 | `fb43e6d6e69c`  |
| 3242   | Layout 2 | `fb43e6d6e69c`  |
| 3235   | Layout 2 | `fb43e6d6e69c`  |
| 3229   | Layout 2 | `fb43e6d6e69c`  |
| 3212   | Layout 2 | `fb43e6d6e69c`  |
| 3203   | Layout 2 | `fb43e6d6e69c`  |
| 3193   | Layout 2 | `fb43e6d6e69c`  |
| 3186   | Layout 2 | `fb43e6d6e69c`  |
| 3177   | Layout 2 | `fb43e6d6e69c`  |
| 3169   | Layout 2 | `fb43e6d6e69c`  |
| 3158   | Layout 2 | `fb43e6d6e69c`  |
| 3151   | Layout 2 | `fb43e6d6e69c`  |
| 3144   | Layout 2 | `fb43e6d6e69c`  |
| 3133   | Layout 2 | `fb43e6d6e69c`  |
| 3125   | Layout 2 | `fb43e6d6e69c`  |
| 3118   | Layout 2 | `fb43e6d6e69c`  |
| 3111   | Layout 2 | `fb43e6d6e69c`  |
| 3103   | Layout 2 | `fb43e6d6e69c`  |
| 3095   | Layout 2 | `fb43e6d6e69c`  |
| 3086   | Layout 2 | `fb43e6d6e69c`  |
| 3072   | Layout 2 | `fb43e6d6e69c`  |
| 3062   | Layout 2 | `fb43e6d6e69c`  |
| 3052   | Layout 2 | `fb43e6d6e69c`  |
| 3045   | Layout 2 | `fb43e6d6e69c`  |
| 3037   | Layout 2 | `fb43e6d6e69c`  |
| 3030   | Layout 2 | `fb43e6d6e69c`  |
| 3021   | Layout 2 | `fb43e6d6e69c`  |
| 3012   | Layout 2 | `fb43e6d6e69c`  |
| 3002   | Layout 2 | `fb43e6d6e69c`  |
| 2995   | Layout 2 | `fb43e6d6e69c`  |
| 2987   | Layout 2 | `fb43e6d6e69c`  |
| 2978   | Layout 2 | `fb43e6d6e69c`  |
| 2970   | Layout 2 | `fb43e6d6e69c`  |
| 2959   | Layout 2 | `fb43e6d6e69c`  |
| 2951   | Layout 2 | `fb43e6d6e69c`  |
| 2942   | Layout 2 | `fb43e6d6e69c`  |
| 2935   | Layout 2 | `fb43e6d6e69c`  |
| 2932   | Layout 2 | `fb43e6d6e69c`  |
| 2923   | Layout 2 | `fb43e6d6e69c`  |
| 2919   | Layout 2 | `fb43e6d6e69c`  |
| 2907   | Layout 2 | `fb43e6d6e69c`  |
| 2900   | Layout 2 | `fb43e6d6e69c`  |
| 2891   | Layout 2 | `fb43e6d6e69c`  |
| 2882   | Layout 2 | `fb43e6d6e69c`  |
| 2872   | Layout 2 | `fb43e6d6e69c`  |
| 2863   | Layout 2 | `fb43e6d6e69c`  |
| 2855   | Layout 2 | `fb43e6d6e69c`  |
| 2849   | Layout 2 | `fb43e6d6e69c`  |
| 2844   | Layout 2 | `fb43e6d6e69c`  |
| 2834   | Layout 2 | `fb43e6d6e69c`  |
| 2825   | Layout 2 | `fb43e6d6e69c`  |
| 2819   | Layout 2 | `fb43e6d6e69c`  |
| 2811   | Layout 2 | `fb43e6d6e69c`  |
| 2803   | Layout 2 | `fb43e6d6e69c`  |
| 2794   | Layout 2 | `fb43e6d6e69c`  |
| 2783   | Layout 2 | `fb43e6d6e69c`  |
| 2774   | Layout 2 | `fb43e6d6e69c`  |
| 2765   | Layout 2 | `fb43e6d6e69c`  |
| 2756   | Layout 2 | `fb43e6d6e69c`  |
| 2750   | Layout 2 | `fb43e6d6e69c`  |
| 2743   | Layout 2 | `fb43e6d6e69c`  |
| 2736   | Layout 2 | `fb43e6d6e69c`  |
| 2726   | Layout 2 | `fb43e6d6e69c`  |
| 2717   | Layout 2 | `fb43e6d6e69c`  |
| 2709   | Layout 2 | `fb43e6d6e69c`  |
| 2703   | Layout 2 | `fb43e6d6e69c`  |
| 2695   | Layout 2 | `fb43e6d6e69c`  |
| 2684   | Layout 2 | `fb43e6d6e69c`  |
| 2672   | Layout 2 | `fb43e6d6e69c`  |
| 2665   | Layout 2 | `fb43e6d6e69c`  |
| 2657   | Layout 2 | `fb43e6d6e69c`  |
| 2649   | Layout 2 | `fb43e6d6e69c`  |
| 2644   | Layout 2 | `fb43e6d6e69c`  |
| 2637   | Layout 2 | `fb43e6d6e69c`  |
| 2629   | Layout 2 | `fb43e6d6e69c`  |
| 2619   | Layout 2 | `fb43e6d6e69c`  |
| 2612   | Layout 1 | `fb43e6d6e69c`  |
| 2606   | Layout 1 | `fb43e6d6e69c`  |
| 2602   | Layout 1 | `fb43e6d6e69c`  |
| 2601   | Layout 1 | `fb43e6d6e69c`  |
| 2592   | Layout 1 | `fb43e6d6e69c`  |
| 2583   | Layout 1 | `fb43e6d6e69c`  |
| 2575   | Layout 1 | `fb43e6d6e69c`  |
| 2567   | Layout 1 | `fb43e6d6e69c`  |
| 2560   | Layout 1 | `fb43e6d6e69c`  |
| 2553   | Layout 1 | `fb43e6d6e69c`  |
| 2545   | Layout 1 | `fb43e6d6e69c`  |
| 2538   | Layout 1 | `fb43e6d6e69c`  |
| 2529   | Layout 1 | `fb43e6d6e69c`  |
| 2519   | Layout 1 | `fb43e6d6e69c`  |
| 2513   | Layout 1 | `fb43e6d6e69c`  |
| 2510   | Layout 1 | `fb43e6d6e69c`  |
| 2507   | Layout 1 | `fb43e6d6e69c`  |
| 2503   | Layout 1 | `fb43e6d6e69c`  |
| 2498   | Layout 1 | `fb43e6d6e69c`  |
| 2492   | Layout 1 | `fb43e6d6e69c`  |
| 2487   | Layout 1 | `fb43e6d6e69c`  |
| 2480   | Layout 1 | `fb43e6d6e69c`  |
| 2474   | Layout 1 | `fb43e6d6e69c`  |
| 2468   | Layout 1 | `fb43e6d6e69c`  |
| 2460   | Layout 1 | `fb43e6d6e69c`  |
| 2453   | Layout 1 | `fb43e6d6e69c`  |
| 2444   | Layout 1 | `fb43e6d6e69c`  |
| 2438   | Layout 1 | `fb43e6d6e69c`  |
| 2434   | Layout 1 | `fb43e6d6e69c`  |
| 2429   | Layout 1 | `fb43e6d6e69c`  |
| 2421   | Layout 1 | `fb43e6d6e69c`  |
| 2414   | Layout 1 | `fb43e6d6e69c`  |
| 2407   | Layout 1 | `fb43e6d6e69c`  |
| 2401   | Layout 1 | `fb43e6d6e69c`  |
| 2397   | Layout 1 | `fb43e6d6e69c`  |
| 2393   | Layout 1 | `fb43e6d6e69c`  |
| 2384   | Layout 1 | `fb43e6d6e69c`  |
| 2378   | Layout 1 | `fb43e6d6e69c`  |
| 2372   | Layout 1 | `fb43e6d6e69c`  |
| 2358   | Layout 1 | `fb43e6d6e69c`  |
| 2352   | Layout 1 | `fb43e6d6e69c`  |
| 2347   | Layout 1 | `fb43e6d6e69c`  |
| 2343   | Layout 1 | `fb43e6d6e69c`  |
| 2335   | Layout 1 | `fb43e6d6e69c`  |
| 2327   | Layout 1 | `fb43e6d6e69c`  |
| 2324   | Layout 1 | `fb43e6d6e69c`  |
| 2319   | Layout 1 | `fb43e6d6e69c`  |
| 2313   | Layout 1 | `fb43e6d6e69c`  |
| 2308   | Layout 1 | `fb43e6d6e69c`  |
| 2302   | Layout 1 | `fb43e6d6e69c`  |
| 2295   | Layout 1 | `fb43e6d6e69c`  |
| 2290   | Layout 1 | `fb43e6d6e69c`  |
| 2284   | Layout 1 | `fb43e6d6e69c`  |
| 2276   | Layout 1 | `fb43e6d6e69c`  |
| 2269   | Layout 1 | `fb43e6d6e69c`  |
| 2259   | Layout 1 | `fb43e6d6e69c`  |
| 2250   | Layout 1 | `fb43e6d6e69c`  |
| 2243   | Layout 1 | `fb43e6d6e69c`  |
| 2235   | Layout 1 | `fb43e6d6e69c`  |
| 2229   | Layout 1 | `fb43e6d6e69c`  |
| 2224   | Layout 1 | `fb43e6d6e69c`  |
| 2218   | No file  | `fb43e6d6e69c`  |
| 2215   | No file  | `fb43e6d6e69c`  |
| 2207   | No file  | `fb43e6d6e69c`  |
| 2203   | No file  | `fb43e6d6e69c`  |
| 2196   | No file  | `fb43e6d6e69c`  |
| 2192   | No file  | `fb43e6d6e69c`  |
| 2189   | No file  | `fb43e6d6e69c`  |
| 2183   | No file  | `fb43e6d6e69c`  |
| 2179   | No file  | `fb43e6d6e69c`  |
| 2171   | No file  | `fb43e6d6e69c`  |
| 2163   | No file  | `fb43e6d6e69c`  |
| 2156   | No file  | `fb43e6d6e69c`  |
| 2151   | No file  | `fb43e6d6e69c`  |
| 2147   | No file  | `fb43e6d6e69c`  |
| 2142   | No file  | `fb43e6d6e69c`  |
| 2138   | No file  | `fb43e6d6e69c`  |
| 2134   | No file  | `fb43e6d6e69c`  |
| 2130   | No file  | `fb43e6d6e69c`  |
| 2122   | No file  | `fb43e6d6e69c`  |
| 2107   | No file  | `fb43e6d6e69c`  |
| 2098   | No file  | `fb43e6d6e69c`  |
| 2089   | No file  | `fb43e6d6e69c`  |
| 2081   | No file  | `fb43e6d6e69c`  |
| 2073   | No file  | `fb43e6d6e69c`  |
| 2067   | No file  | `fb43e6d6e69c`  |
| 2063   | No file  | `fb43e6d6e69c`  |
| 2059   | No file  | `fb43e6d6e69c`  |
| 2052   | No file  | `fb43e6d6e69c`  |
| 2044   | No file  | `fb43e6d6e69c`  |
| 2039   | No file  | `fb43e6d6e69c`  |
| 2032   | No file  | `fb43e6d6e69c`  |
| 2025   | No file  | `fb43e6d6e69c`  |
| 2011   | No file  | `fb43e6d6e69c`  |
| 2005   | No file  | `fb43e6d6e69c`  |
| 2000   | No file  | `fb43e6d6e69c`  |
| 1996   | No file  | `fb43e6d6e69c`  |
| 1991   | No file  | `fb43e6d6e69c`  |
| 1985   | No file  | `fb43e6d6e69c`  |
| 1980   | No file  | `fb43e6d6e69c`  |
| 1969   | No file  | `fb43e6d6e69c`  |
| 1964   | No file  | `fb43e6d6e69c`  |
| 1958   | No file  | `fb43e6d6e69c`  |
| 1950   | No file  | `fb43e6d6e69c`  |
| 1945   | No file  | `fb43e6d6e69c`  |
| 1937   | No file  | `fb43e6d6e69c`  |
| 1933   | No file  | `fb43e6d6e69c`  |
| 1927   | No file  | `fb43e6d6e69c`  |
| 1921   | No file  | `fb43e6d6e69c`  |
| 1914   | No file  | `fb43e6d6e69c`  |
| 1908   | No file  | `fb43e6d6e69c`  |
| 1897   | No file  | `fb43e6d6e69c`  |
| 1892   | No file  | `fb43e6d6e69c`  |
| 1886   | No file  | `fb43e6d6e69c`  |
| 1881   | No file  | `fb43e6d6e69c`  |
| 1871   | No file  | `fb43e6d6e69c`  |
| 1866   | No file  | `fb43e6d6e69c`  |
| 1862   | No file  | `fb43e6d6e69c`  |
| 1854   | No file  | `fb43e6d6e69c`  |
| 1846   | No file  | `fb43e6d6e69c`  |
| 1838   | No file  | `fb43e6d6e69c`  |
| 1832   | No file  | `fb43e6d6e69c`  |
| 1826   | No file  | `fb43e6d6e69c`  |
| 1822   | No file  | `fb43e6d6e69c`  |
| 1818   | No file  | `fb43e6d6e69c`  |
| 1804   | No file  | `fb43e6d6e69c`  |
| 1794   | No file  | `fb43e6d6e69c`  |
| 1790   | No file  | `fb43e6d6e69c`  |
| 1784   | No file  | `fb43e6d6e69c`  |
| 1774   | No file  | `fb43e6d6e69c`  |
| 1771   | No file  | `fb43e6d6e69c`  |
| 1762   | No file  | `fb43e6d6e69c`  |
| 1759   | No file  | `fb43e6d6e69c`  |
| 1754   | No file  | `fb43e6d6e69c`  |
| 1749   | No file  | `fb43e6d6e69c`  |
| 1743   | No file  | `fb43e6d6e69c`  |
| 1737   | No file  | `fb43e6d6e69c`  |
| 1731   | No file  | `fb43e6d6e69c`  |
| 1725   | No file  | `fb43e6d6e69c`  |
| 1717   | No file  | `fb43e6d6e69c`  |
| 1710   | No file  | `fb43e6d6e69c`  |
| 1704   | No file  | `fb43e6d6e69c`  |
| 1698   | No file  | `fb43e6d6e69c`  |
| 1690   | No file  | `fb43e6d6e69c`  |
| 1685   | No file  | `fb43e6d6e69c`  |
| 1680   | No file  | `fb43e6d6e69c`  |
| 1674   | No file  | `fb43e6d6e69c`  |
| 1668   | No file  | `fb43e6d6e69c`  |
| 1659   | No file  | `fb43e6d6e69c`  |
| 1649   | No file  | `fb43e6d6e69c`  |
| 1642   | No file  | `fb43e6d6e69c`  |
| 1636   | No file  | `fb43e6d6e69c`  |
| 1628   | No file  | `fb43e6d6e69c`  |
| 1622   | No file  | `fb43e6d6e69c`  |
| 1614   | No file  | `fb43e6d6e69c`  |
| 1608   | No file  | `fb43e6d6e69c`  |
| 1602   | No file  | `fb43e6d6e69c`  |
| 1598   | No file  | `fb43e6d6e69c`  |
| 1594   | No file  | `fb43e6d6e69c`  |
| 1590   | No file  | `fb43e6d6e69c`  |
| 1587   | No file  | `fb43e6d6e69c`  |
| 1584   | No file  | `fb43e6d6e69c`  |
| 1579   | No file  | `fb43e6d6e69c`  |
| 1572   | No file  | `fb43e6d6e69c`  |
| 1565   | No file  | `fb43e6d6e69c`  |
| 1559   | No file  | `fb43e6d6e69c`  |
| 1554   | No file  | `fb43e6d6e69c`  |
| 1547   | No file  | `fb43e6d6e69c`  |
| 1537   | No file  | `fb43e6d6e69c`  |
| 1529   | No file  | `fb43e6d6e69c`  |
| 1524   | No file  | `fb43e6d6e69c`  |
| 1519   | No file  | `fb43e6d6e69c`  |
| 1509   | No file  | `fb43e6d6e69c`  |
| 1506   | No file  | `fb43e6d6e69c`  |
| 1504   | No file  | `fb43e6d6e69c`  |
| 1500   | No file  | `fb43e6d6e69c`  |
| 1493   | No file  | `fb43e6d6e69c`  |
| 1489   | No file  | `fb43e6d6e69c`  |
| 1485   | No file  | `fb43e6d6e69c`  |
| 1481   | No file  | `fb43e6d6e69c`  |
| 1474   | No file  | `fb43e6d6e69c`  |
| 1466   | No file  | `fb43e6d6e69c`  |
| 1462   | No file  | `fb43e6d6e69c`  |
| 1459   | No file  | `fb43e6d6e69c`  |
| 1453   | No file  | `fb43e6d6e69c`  |
| 1450   | No file  | `fb43e6d6e69c`  |
| 1445   | No file  | `fb43e6d6e69c`  |
| 1439   | No file  | `fb43e6d6e69c`  |
| 1433   | No file  | `fb43e6d6e69c`  |
| 1430   | No file  | `fb43e6d6e69c`  |
| 1426   | No file  | `fb43e6d6e69c`  |
| 1421   | No file  | `fb43e6d6e69c`  |
| 1417   | No file  | `fb43e6d6e69c`  |
| 1416   | No file  | `fb43e6d6e69c`  |
| 1409   | No file  | `fb43e6d6e69c`  |
| 1405   | No file  | `fb43e6d6e69c`  |
| 1401   | No file  | `fb43e6d6e69c`  |
| 1396   | No file  | `fb43e6d6e69c`  |
| 1391   | No file  | `fb43e6d6e69c`  |
| 1390   | No file  | `fb43e6d6e69c`  |
| 1386   | No file  | `fb43e6d6e69c`  |
| 1381   | No file  | `fb43e6d6e69c`  |
| 1379   | No file  | `fb43e6d6e69c`  |
| 1372   | No file  | `fb43e6d6e69c`  |
| 1366   | No file  | `fb43e6d6e69c`  |
| 1364   | No file  | `fb43e6d6e69c`  |
| 1363   | No file  | `fb43e6d6e69c`  |
| 1360   | No file  | `fb43e6d6e69c`  |
| 1358   | No file  | `fb43e6d6e69c`  |
| 1355   | No file  | `fb43e6d6e69c`  |
| 1351   | No file  | `fb43e6d6e69c`  |
| 1348   | No file  | `fb43e6d6e69c`  |
| 1346   | No file  | `fb43e6d6e69c`  |
| 1341   | No file  | `fb43e6d6e69c`  |
| 1340   | No file  | `fb43e6d6e69c`  |
| 1338   | No file  | `fb43e6d6e69c`  |
| 1335   | No file  | `fb43e6d6e69c`  |
| 1333   | No file  | `fb43e6d6e69c`  |
| 1329   | No file  | `fb43e6d6e69c`  |
| 1327   | No file  | `fb43e6d6e69c`  |
| 1324   | No file  | `fb43e6d6e69c`  |
| 1321   | No file  | `fb43e6d6e69c`  |
| 1319   | No file  | `fb43e6d6e69c`  |
| 1318   | No file  | `fb43e6d6e69c`  |
| 1316   | No file  | `fb43e6d6e69c`  |
| 1313   | No file  | `fb43e6d6e69c`  |
| 1311   | No file  | `fb43e6d6e69c`  |
| 1309   | No file  | `fb43e6d6e69c`  |
| 1304   | No file  | `fb43e6d6e69c`  |
| 1292   | No file  | `fb43e6d6e69c`  |
| 1286   | No file  | `fb43e6d6e69c`  |
| 1280   | No file  | `fb43e6d6e69c`  |
| 1276   | No file  | `fb43e6d6e69c`  |
| 1267   | No file  | `fb43e6d6e69c`  |
| 1261   | No file  | `fb43e6d6e69c`  |
| 1256   | No file  | `fb43e6d6e69c`  |
| 1250   | No file  | `fb43e6d6e69c`  |
| 1246   | No file  | `fb43e6d6e69c`  |
| 1239   | No file  | `fb43e6d6e69c`  |
| 1230   | No file  | `fb43e6d6e69c`  |
| 1226   | No file  | `fb43e6d6e69c`  |
| 1220   | No file  | `fb43e6d6e69c`  |
| 1217   | No file  | `fb43e6d6e69c`  |
| 1211   | No file  | `fb43e6d6e69c`  |
| 1210   | No file  | `fb43e6d6e69c`  |
| 1208   | No file  | `fb43e6d6e69c`  |
| 1203   | No file  | `fb43e6d6e69c`  |
| 1197   | No file  | `fb43e6d6e69c`  |
| 1194   | No file  | `fb43e6d6e69c`  |
| 1192   | No file  | `fb43e6d6e69c`  |
| 1187   | No file  | `fb43e6d6e69c`  |
| 1183   | No file  | `fb43e6d6e69c`  |
| 1177   | No file  | `fb43e6d6e69c`  |
| 1173   | No file  | `fb43e6d6e69c`  |
| 1167   | No file  | `fb43e6d6e69c`  |
| 1164   | No file  | `fb43e6d6e69c`  |
| 1156   | No file  | `fb43e6d6e69c`  |
| 1149   | No file  | `fb43e6d6e69c`  |
| 1144   | No file  | `fb43e6d6e69c`  |
| 1137   | No file  | `fb43e6d6e69c`  |
| 1132   | No file  | `fb43e6d6e69c`  |
| 1127   | No file  | `fb43e6d6e69c`  |
| 1122   | No file  | `fb43e6d6e69c`  |
| 1118   | No file  | `fb43e6d6e69c`  |
| 1114   | No file  | `fb43e6d6e69c`  |
| 1109   | No file  | `fb43e6d6e69c`  |
| 1102   | No file  | `fb43e6d6e69c`  |
| 1096   | No file  | `fb43e6d6e69c`  |
| 1088   | No file  | `fb43e6d6e69c`  |
| 1081   | No file  | `fb43e6d6e69c`  |
| 1076   | No file  | `fb43e6d6e69c`  |
| 1069   | No file  | `fb43e6d6e69c`  |
| 1064   | No file  | `fb43e6d6e69c`  |
| 1058   | No file  | `fb43e6d6e69c`  |
| 1051   | No file  | `fb43e6d6e69c`  |
| 1044   | No file  | `fb43e6d6e69c`  |
| 1036   | No file  | `fb43e6d6e69c`  |
| 1026   | No file  | `fb43e6d6e69c`  |
| 1016   | No file  | `fb43e6d6e69c`  |
| 1009   | No file  | `fb43e6d6e69c`  |
| 1005   | No file  | `fb43e6d6e69c`  |
| 1000   | No file  | `fb43e6d6e69c`  |
| 998    | No file  | `fb43e6d6e69c`  |
| 990    | No file  | `fb43e6d6e69c`  |
| 979    | No file  | `fb43e6d6e69c`  |
| 972    | No file  | `fb43e6d6e69c`  |
| 963    | No file  | `fb43e6d6e69c`  |
| 955    | No file  | `fb43e6d6e69c`  |
| 946    | No file  | `fb43e6d6e69c`  |
| 938    | No file  | `fb43e6d6e69c`  |
| 927    | No file  | `fb43e6d6e69c`  |
| 911    | No file  | `fb43e6d6e69c`  |
| 904    | No file  | `fb43e6d6e69c`  |
| 899    | No file  | `fb43e6d6e69c`  |
| 894    | No file  | `fb43e6d6e69c`  |
| 885    | No file  | `fb43e6d6e69c`  |
| 879    | No file  | `fb43e6d6e69c`  |
| 872    | No file  | `fb43e6d6e69c`  |
| 864    | No file  | `fb43e6d6e69c`  |
| 855    | No file  | `fb43e6d6e69c`  |
| 853    | No file  | `fb43e6d6e69c`  |
| 845    | No file  | `fb43e6d6e69c`  |
| 837    | No file  | `fb43e6d6e69c`  |
| 829    | No file  | `fb43e6d6e69c`  |
| 822    | No file  | `fb43e6d6e69c`  |
| 814    | No file  | `fb43e6d6e69c`  |
| 805    | No file  | `fb43e6d6e69c`  |
| 794    | No file  | `fb43e6d6e69c`  |
| 787    | No file  | `fb43e6d6e69c`  |
| 780    | No file  | `fb43e6d6e69c`  |
| 771    | No file  | `fb43e6d6e69c`  |
| 760    | No file  | `fb43e6d6e69c`  |
| 748    | No file  | `fb43e6d6e69c`  |
| 741    | No file  | `fb43e6d6e69c`  |
| 736    | No file  | `fb43e6d6e69c`  |
| 731    | No file  | `fb43e6d6e69c`  |
| 723    | No file  | `fb43e6d6e69c`  |
| 711    | No file  | `fb43e6d6e69c`  |
| 707    | No file  | `fb43e6d6e69c`  |
| 697    | No file  | `fb43e6d6e69c`  |
| 689    | No file  | `fb43e6d6e69c`  |
| 683    | No file  | `fb43e6d6e69c`  |
| 678    | No file  | `fb43e6d6e69c`  |
| 670    | No file  | `fb43e6d6e69c`  |
| 661    | No file  | `fb43e6d6e69c`  |
| 656    | No file  | `fb43e6d6e69c`  |
| 652    | No file  | `fb43e6d6e69c`  |
| 643    | No file  | `fb43e6d6e69c`  |
| 637    | No file  | `fb43e6d6e69c`  |
| 630    | No file  | `fb43e6d6e69c`  |
| 627    | No file  | `fb43e6d6e69c`  |
| 621    | No file  | `fb43e6d6e69c`  |
| 617    | No file  | `fb43e6d6e69c`  |
| 615    | No file  | `fb43e6d6e69c`  |
| 606    | No file  | `fb43e6d6e69c`  |
| 599    | No file  | `fb43e6d6e69c`  |
| 592    | No file  | `fb43e6d6e69c`  |
| 586    | No file  | `fb43e6d6e69c`  |
| 577    | No file  | `fb43e6d6e69c`  |
| 569    | No file  | `fb43e6d6e69c`  |
| 561    | No file  | `fb43e6d6e69c`  |
| 554    | No file  | `fb43e6d6e69c`  |
| 542    | No file  | `fb43e6d6e69c`  |
| 532    | No file  | `fb43e6d6e69c`  |
| 531    | No file  | `fb43e6d6e69c`  |
| 526    | No file  | `fb43e6d6e69c`  |
| 521    | No file  | `fb43e6d6e69c`  |
| 517    | No file  | `fb43e6d6e69c`  |
| 510    | No file  | `fb43e6d6e69c`  |
| 508    | No file  | `fb43e6d6e69c`  |
| 504    | No file  | `fb43e6d6e69c`  |
| 497    | No file  | `fb43e6d6e69c`  |
| 491    | No file  | `fb43e6d6e69c`  |
| 485    | No file  | `fb43e6d6e69c`  |
| 478    | No file  | `fb43e6d6e69c`  |
| 472    | No file  | `fb43e6d6e69c`  |
| 466    | No file  | `fb43e6d6e69c`  |
| 457    | No file  | `fb43e6d6e69c`  |
| 452    | No file  | `fb43e6d6e69c`  |
| 449    | No file  | `fb43e6d6e69c`  |
| 435    | No file  | `fb43e6d6e69c`  |

<!-- versions:end -->

## Companion Files

| File                       | Required | Role                                                        |
| -------------------------- | -------- | ----------------------------------------------------------- |
| `elementalmonsterstat.bss` | Optional | The part and difficulty of each boss, by `character_key`    |
| `languagedata_*.loc`       | Optional | Boss and item names, and the rank labels of the window      |

All multi-byte values are little-endian.

## Layout 3

### File Layout

Plain binary: no `PABR` magic, no offset file and no trailer.

| Offset         | Type                 | Field         | Notes                                                     |
| -------------- | -------------------- | ------------- | --------------------------------------------------------- |
| `+0x00`        | u32                  | count         | Number of `records`                                       |
| `+0x04`        | Record[count]        | records       | The rewards the window reads with the Part 2 flag off     |
| `records+0x00` | u32                  | part2_count   | Number of `part2_records`                                 |
| `records+0x04` | Record[part2_count]  | part2_records | The rewards the window reads with the Part 2 flag on      |

### Record (variable: 14 bytes + rank tiers and base rewards)

| Offset            | Type                            | Field             | Notes                                                                 |
| ----------------- | ------------------------------- | ----------------- | --------------------------------------------------------------------- |
| `+0x00`           | u16                             | character_key     | The boss, the `character_key` of `elementalmonsterstat.bss`           |
| `+0x02`           | u32                             | rank_tier_count   | Number of `rank_tiers`; `ToClient_getElementalMonsterRankRewardListCount` |
| `+0x06`           | Rank Tier[rank_tier_count]      | rank_tiers        | See Rank Tier                                                         |
| `rank_tiers+0x00` | u64                             | base_reward_count | Number of `base_rewards`; `ToClient_getElementalMonsterBaseRewardSize` |
| `rank_tiers+0x08` | Reward Item[base_reward_count]  | base_rewards      | The "Bonus Rewards" row, for players outside the ranks                |

### Rank Tier (variable: 12 bytes + rewards)

| Offset  | Type                       | Field        | Notes                                                                 |
| ------- | -------------------------- | ------------ | --------------------------------------------------------------------- |
| `+0x00` | u32                        | rank         | Lowest rank of the tier; `ToClient_getElementalMonsterRankByIndex`    |
| `+0x04` | u64                        | reward_count | Number of `rewards`; `ToClient_getElementalMonsterRankRewardSizeByIndex` |
| `+0x0c` | Reward Item[reward_count]  | rewards      | See Reward Item                                                       |

### Reward Item (16 bytes)

Same structure as the Reward Item of
[`elementalmonsterstat.bss`](elementalmonsterstat_bss.md#reward-item-16-bytes).

| Offset  | Type     | Field      | Notes                                                                     |
| ------- | -------- | ---------- | ------------------------------------------------------------------------- |
| `+0x00` | u32      | item_key   | Item key, `enchant_level << 24 \| item_id`; `...RewardItemKeyByIndex`     |
| `+0x04` | bytes[4] | padding_04 | Alignment of `count`; `fc 7f 00 00` or `f7 7f 00 00` (client 3474), see Notes |
| `+0x08` | i64      | count      | Number of the item; `...RewardItemCountByIndex`, `1` on every entry (client 3474) |

## Layout 2

### Record (variable: 12 bytes + rank tiers)

| Offset            | Type                        | Field           | Notes                                    |
| ----------------- | --------------------------- | --------------- | ---------------------------------------- |
| `+0x00`           | u16                         | character_key   |                                          |
| `+0x02`           | u32                         | rank_tier_count |                                          |
| `+0x06`           | Rank Tier[rank_tier_count]  | rank_tiers      |                                          |
| `rank_tiers+0x00` | Reward Item                 | base_rewards    | Exactly one item, no count before it     |

### Rank Tier (10 bytes)

| Offset  | Type        | Field   | Notes                                |
| ------- | ----------- | ------- | ------------------------------------ |
| `+0x00` | u32         | rank    |                                      |
| `+0x04` | Reward Item | rewards | Exactly one item, no count before it |

### Reward Item (6 bytes)

| Offset  | Type | Field    | Notes                              |
| ------- | ---- | -------- | ---------------------------------- |
| `+0x00` | u32  | item_key |                                    |
| `+0x04` | u16  | count    | `1` on every entry (client 3251)   |

## Layout 1

### File Layout

| Offset  | Type          | Field   | Notes                       |
| ------- | ------------- | ------- | --------------------------- |
| `+0x00` | u32           | count   | Number of `records`         |
| `+0x04` | Record[count] | records | The only table; see Notes   |

## Rank Tiers

The window labels a tier with the GAME sheet key `LUA_MORNING_ATTRBOSS_RANK`
("#{rank}"). A tier whose `rank` is above 1 reads from one past the
previous tier's `rank` to its own (`#2 ~ #5`, and `#2 ~ #2` for the tiers
`1`, `2`), or `~ #50` when it is the first tier; the base rewards row reads
`LUA_MORNING_ATTRBOSS_OUTOFRANKREWARD` ("Bonus Rewards"). The window shows
the base rewards only for a boss that has rank tiers and only with the Part
2 flag off.

| Table           | Bosses (client 3474) | `rank` of the tiers        | Items per tier | Base rewards |
| --------------- | -------------------- | -------------------------- | -------------- | ------------ |
| `records`       | 94 Donghae (Solo)    | `1`, `5`, `20`             | 2              | 2            |
| `records`       | 14 Hwanghae (Party)  | None                       |                | 2            |
| `part2_records` | 7 Hwanghae (Party)   | `1`, `2`, `3`, `10`, `25`, `50` | 1         | 0            |
| `part2_records` | 7 Hwanghae (Party)   | `50`                       | 1              | 0            |

## Field Names

No reference source has the file. It first appears on client 2519 (absent
on client 2107), so a private server's `DataSheets.bexcel`, `.xlsm` sheets
and server dump on client 1784 have no `Elemental` sheet or column, and the
2016 client and the client 519 server tables predate it.

The names follow the client Lua of client 3474
(`panel_window_morningland_detailreward_all.luac`): per boss character
key and Part 2 flag it reads `ToClient_getElementalMonsterRankRewardListCount`,
then per tier `ToClient_getElementalMonsterRankByIndex`,
`ToClient_getElementalMonsterRankRewardSizeByIndex` and per item
`...RankRewardItemKeyByIndex` and `...RankRewardItemCountByIndex`; for the
base row `ToClient_getElementalMonsterBaseRewardSize`,
`...BaseRewardItemKey` and `...BaseRewardItemCount`. The counts, ranks and
items sit in the file in that order, and the item names match the tiers:
`790001` "C-1 Boss Blitz Reward: Golden Pig King (Rank 1)" is the tier `1`
item of the Calamity 1 Golden Pig King `23608`, `790011` "(Rank 2)" its
tier `5` item.

`part2_count` and `part2_records` are named after the Lua flag
`isMorningLandMonsterPart2`: its 14 keys are the Hwanghae (Party) bosses
(`monster_part` `2` in `elementalmonsterstat.bss`), and their tier items
are "Boss Blitz Reward (Rank 1)" `761108` to "(Rank 6)" `761113`.

## Notes

- The second item of every `records` tier and base row is `890117`
  (Korean name 전투 비급서(소형); no English LOC name on client 3474).
- The base items of the Hwanghae (Party) bosses in `records` are their
  "Boss Slayer's Haul" boxes, the same item as their `show_rewards` in
  `elementalmonsterstat.bss` (`761337` "Boss Slayer's Haul - Jigwi
  (Normal)" for `24562`). The window does not show them, as it skips the
  base row with the Part 2 flag on and the tier list is empty with it off.
- The handler (`_bss/elementalmonsterreward/`) shows one row per rank tier
  and per non-empty base rewards row, labelled as the window labels them,
  with a Party Ranking flag on the `part2_records` rows. It links each boss
  to its `elementalmonsterstat.bss` row and takes the part and difficulty
  from there.
- `padding_04` is the 4 bytes between the u32 `item_key` and the 8-aligned
  i64 `count`, as in `elementalmonsterstat.bss`.
- Layout 2 (clients 3002 and 3251) has one item per tier and one base item,
  with a u16 count; Layout 1 (client 2519) has the same records and no
  second table, as the Hwanghae (Party) bosses came later.
- The Layout 2 `count` is a u16 that holds `1` on every entry; it takes its
  name from the Layout 3 `count` at the same place after `item_key`.
