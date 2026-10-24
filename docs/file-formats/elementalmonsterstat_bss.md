# `elementalmonsterstat.bss` Format

## Purpose

The monsters of the Black Shrine (검은 사당) boss blitz in the Land of the
Morning Light: one variable-length row per character, the boss of each
group and difficulty and the monsters of its fight. A row holds the boss
group and difficulty, the aura the monster is weak to, its aura offence and
defence, the minimum AP of the higher Calamities, what unlocks the
difficulty, the reward preview of the window and the world position the
window navigates to. The Black Shrine window reads a row through
`ToClient_getElementalMonsterInfo(group, level)` and
`ToClient_getElementalMonsterInfoByCharacterKey(characterKey)`.

On client 3474 the 1,000 rows hold 108 bosses in 17 groups: groups `0` to
`9` are Black Shrine: Donghae (Solo) with ten Calamities each (seven for
groups `3` and `9`), groups `10` to `16` Black Shrine: Hwanghae (Party)
with a Normal and a Hard difficulty each.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                       | Bytes  | Records                  | Row bytes               |
| ------ | -------------- | ------- | -------------------------- | ------ | ------------------------ | ----------------------- |
| 3      | 3473 and later | 3483    | `elementalmonsterstat.bss` | 10,311 | 104 Reward Item, 201 Row | 43 to 59, 51 on average |
| 2      | 2726 to 3464   | 3464    | `elementalmonsterstat.bss` | 43,436 | 1,000 Row                | 43 to 47, 43 on average |
| 1      | 2224 to 2606   | 2606    | `elementalmonsterstat.bss` | 38,138 | 993 Row                  | 38 to 42, 38 on average |

| Layout | File                       | Known             | Unknown    |
| ------ | -------------------------- | ----------------- | ---------- |
| 3      | `elementalmonsterstat.bss` | 10,311 B (100.0%) | 0 B (0.0%) |
| 2      | `elementalmonsterstat.bss` | 43,436 B (100.0%) | 0 B (0.0%) |
| 1      | `elementalmonsterstat.bss` | 38,138 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 3             | `9ccfbcba01de`  |
| 3482   | Layout 3             | `9ccfbcba01de`  |
| 3474   | Layout 3             | `9ccfbcba01de`  |
| 3473   | Layout 3             | `9ccfbcba01de`  |
| 3464   | Layout 2             | `9ccfbcba01de`  |
| 3458   | Layout 2             | `9ccfbcba01de`  |
| 3454   | Layout 2             | `9ccfbcba01de`  |
| 3444   | Layout 2             | `9ccfbcba01de`  |
| 3435   | Layout 2             | `9ccfbcba01de`  |
| 3426   | Layout 2             | `9ccfbcba01de`  |
| 3418   | Layout 2             | `9ccfbcba01de`  |
| 3412   | Layout 2             | `9ccfbcba01de`  |
| 3402   | Layout 2             | `9ccfbcba01de`  |
| 3396   | Layout 2             | `9ccfbcba01de`  |
| 3387   | Layout 2             | `9ccfbcba01de`  |
| 3381   | Layout 2             | `9ccfbcba01de`  |
| 3373   | Layout 2             | `9ccfbcba01de`  |
| 3364   | Layout 2             | `9ccfbcba01de`  |
| 3356   | Layout 2             | `9ccfbcba01de`  |
| 3349   | Layout 2             | `9ccfbcba01de`  |
| 3342   | Layout 2             | `9ccfbcba01de`  |
| 3335   | Layout 2             | `9ccfbcba01de`  |
| 3326   | Layout 2             | `9ccfbcba01de`  |
| 3321   | Layout 2             | `9ccfbcba01de`  |
| 3314   | Layout 2             | `9ccfbcba01de`  |
| 3303   | Layout 2             | `9ccfbcba01de`  |
| 3302   | Layout 2             | `9ccfbcba01de`  |
| 3293   | Layout 2             | `9ccfbcba01de`  |
| 3283   | Layout 2             | `9ccfbcba01de`  |
| 3275   | Layout 2             | `9ccfbcba01de`  |
| 3267   | Layout 2             | `9ccfbcba01de`  |
| 3258   | Layout 2             | `9ccfbcba01de`  |
| 3251   | Layout 2             | `9ccfbcba01de`  |
| 3242   | Layout 2             | `9ccfbcba01de`  |
| 3235   | Layout 2             | `9ccfbcba01de`  |
| 3229   | Layout 2             | `9ccfbcba01de`  |
| 3212   | Layout 2             | `9ccfbcba01de`  |
| 3203   | Layout 2             | `9ccfbcba01de`  |
| 3193   | Layout 2             | `9ccfbcba01de`  |
| 3186   | Layout 2             | `9ccfbcba01de`  |
| 3177   | Layout 2             | `9ccfbcba01de`  |
| 3169   | Layout 2             | `9ccfbcba01de`  |
| 3158   | Layout 2             | `9ccfbcba01de`  |
| 3151   | Layout 2             | `9ccfbcba01de`  |
| 3144   | Layout 2             | `9ccfbcba01de`  |
| 3133   | Layout 2             | `9ccfbcba01de`  |
| 3125   | Layout 2             | `9ccfbcba01de`  |
| 3118   | Layout 2             | `9ccfbcba01de`  |
| 3111   | Layout 2             | `9ccfbcba01de`  |
| 3103   | Layout 2             | `9ccfbcba01de`  |
| 3095   | Layout 2             | `9ccfbcba01de`  |
| 3086   | Layout 2             | `9ccfbcba01de`  |
| 3072   | Layout 2             | `9ccfbcba01de`  |
| 3062   | Layout 2             | `9ccfbcba01de`  |
| 3052   | Layout 2             | `9ccfbcba01de`  |
| 3045   | Layout 2             | `9ccfbcba01de`  |
| 3037   | Layout 2             | `9ccfbcba01de`  |
| 3030   | Layout 2             | `9ccfbcba01de`  |
| 3021   | Layout 2             | `9ccfbcba01de`  |
| 3012   | Layout 2             | `9ccfbcba01de`  |
| 3002   | Layout 2             | `9ccfbcba01de`  |
| 2995   | Layout 2             | `9ccfbcba01de`  |
| 2987   | Layout 2             | `9ccfbcba01de`  |
| 2978   | Layout 2             | `9ccfbcba01de`  |
| 2970   | Layout 2             | `9ccfbcba01de`  |
| 2959   | Layout 2             | `9ccfbcba01de`  |
| 2951   | Layout 2             | `9ccfbcba01de`  |
| 2942   | Layout 2             | `9ccfbcba01de`  |
| 2935   | Layout 2             | `9ccfbcba01de`  |
| 2932   | Layout 2             | `9ccfbcba01de`  |
| 2923   | Layout 2             | `9ccfbcba01de`  |
| 2919   | Layout 2             | `9ccfbcba01de`  |
| 2907   | Layout 2             | `9ccfbcba01de`  |
| 2900   | Layout 2             | `9ccfbcba01de`  |
| 2891   | Layout 2             | `9ccfbcba01de`  |
| 2882   | Layout 2             | `9ccfbcba01de`  |
| 2872   | Layout 2             | `9ccfbcba01de`  |
| 2863   | Layout 2             | `9ccfbcba01de`  |
| 2855   | Layout 2             | `9ccfbcba01de`  |
| 2849   | Layout 2             | `9ccfbcba01de`  |
| 2844   | Layout 2             | `9ccfbcba01de`  |
| 2834   | Layout 2             | `9ccfbcba01de`  |
| 2825   | Layout 2             | `9ccfbcba01de`  |
| 2819   | Layout 2             | `9ccfbcba01de`  |
| 2811   | Layout 2             | `9ccfbcba01de`  |
| 2803   | Layout 2             | `9ccfbcba01de`  |
| 2794   | Layout 2             | `9ccfbcba01de`  |
| 2783   | Layout 2             | `9ccfbcba01de`  |
| 2774   | Layout 2             | `9ccfbcba01de`  |
| 2765   | Layout 2             | `9ccfbcba01de`  |
| 2756   | Layout 2             | `9ccfbcba01de`  |
| 2750   | Layout 2             | `9ccfbcba01de`  |
| 2743   | Layout 2             | `9ccfbcba01de`  |
| 2736   | Layout 2             | `9ccfbcba01de`  |
| 2726   | Layout 2             | `9ccfbcba01de`  |
| 2717   | No documented layout | `9ccfbcba01de`  |
| 2709   | No documented layout | `9ccfbcba01de`  |
| 2703   | No documented layout | `9ccfbcba01de`  |
| 2695   | No documented layout | `9ccfbcba01de`  |
| 2684   | No documented layout | `9ccfbcba01de`  |
| 2672   | No documented layout | `9ccfbcba01de`  |
| 2665   | No documented layout | `9ccfbcba01de`  |
| 2657   | No documented layout | `9ccfbcba01de`  |
| 2649   | No documented layout | `9ccfbcba01de`  |
| 2644   | No documented layout | `9ccfbcba01de`  |
| 2637   | No documented layout | `9ccfbcba01de`  |
| 2629   | No documented layout | `9ccfbcba01de`  |
| 2619   | No documented layout | `9ccfbcba01de`  |
| 2612   | No documented layout | `9ccfbcba01de`  |
| 2606   | Layout 1             | `9ccfbcba01de`  |
| 2602   | Layout 1             | `9ccfbcba01de`  |
| 2601   | Layout 1             | `9ccfbcba01de`  |
| 2592   | Layout 1             | `9ccfbcba01de`  |
| 2583   | Layout 1             | `9ccfbcba01de`  |
| 2575   | Layout 1             | `9ccfbcba01de`  |
| 2567   | Layout 1             | `9ccfbcba01de`  |
| 2560   | Layout 1             | `9ccfbcba01de`  |
| 2553   | Layout 1             | `9ccfbcba01de`  |
| 2545   | Layout 1             | `9ccfbcba01de`  |
| 2538   | Layout 1             | `9ccfbcba01de`  |
| 2529   | Layout 1             | `9ccfbcba01de`  |
| 2519   | Layout 1             | `9ccfbcba01de`  |
| 2513   | Layout 1             | `9ccfbcba01de`  |
| 2510   | Layout 1             | `9ccfbcba01de`  |
| 2507   | Layout 1             | `9ccfbcba01de`  |
| 2503   | Layout 1             | `9ccfbcba01de`  |
| 2498   | Layout 1             | `9ccfbcba01de`  |
| 2492   | Layout 1             | `9ccfbcba01de`  |
| 2487   | Layout 1             | `9ccfbcba01de`  |
| 2480   | Layout 1             | `9ccfbcba01de`  |
| 2474   | Layout 1             | `9ccfbcba01de`  |
| 2468   | Layout 1             | `9ccfbcba01de`  |
| 2460   | Layout 1             | `9ccfbcba01de`  |
| 2453   | Layout 1             | `9ccfbcba01de`  |
| 2444   | Layout 1             | `9ccfbcba01de`  |
| 2438   | Layout 1             | `9ccfbcba01de`  |
| 2434   | Layout 1             | `9ccfbcba01de`  |
| 2429   | Layout 1             | `9ccfbcba01de`  |
| 2421   | Layout 1             | `9ccfbcba01de`  |
| 2414   | Layout 1             | `9ccfbcba01de`  |
| 2407   | Layout 1             | `9ccfbcba01de`  |
| 2401   | Layout 1             | `9ccfbcba01de`  |
| 2397   | Layout 1             | `9ccfbcba01de`  |
| 2393   | Layout 1             | `9ccfbcba01de`  |
| 2384   | Layout 1             | `9ccfbcba01de`  |
| 2378   | Layout 1             | `9ccfbcba01de`  |
| 2372   | Layout 1             | `9ccfbcba01de`  |
| 2358   | Layout 1             | `9ccfbcba01de`  |
| 2352   | Layout 1             | `9ccfbcba01de`  |
| 2347   | Layout 1             | `9ccfbcba01de`  |
| 2343   | Layout 1             | `9ccfbcba01de`  |
| 2335   | Layout 1             | `9ccfbcba01de`  |
| 2327   | Layout 1             | `9ccfbcba01de`  |
| 2324   | Layout 1             | `9ccfbcba01de`  |
| 2319   | Layout 1             | `9ccfbcba01de`  |
| 2313   | Layout 1             | `9ccfbcba01de`  |
| 2308   | Layout 1             | `9ccfbcba01de`  |
| 2302   | Layout 1             | `9ccfbcba01de`  |
| 2295   | Layout 1             | `9ccfbcba01de`  |
| 2290   | Layout 1             | `9ccfbcba01de`  |
| 2284   | Layout 1             | `9ccfbcba01de`  |
| 2276   | Layout 1             | `9ccfbcba01de`  |
| 2269   | Layout 1             | `9ccfbcba01de`  |
| 2259   | Layout 1             | `9ccfbcba01de`  |
| 2250   | Layout 1             | `9ccfbcba01de`  |
| 2243   | Layout 1             | `9ccfbcba01de`  |
| 2235   | Layout 1             | `9ccfbcba01de`  |
| 2229   | Layout 1             | `9ccfbcba01de`  |
| 2224   | Layout 1             | `9ccfbcba01de`  |
| 2218   | No file              | `9ccfbcba01de`  |
| 2215   | No file              | `9ccfbcba01de`  |
| 2207   | No file              | `9ccfbcba01de`  |
| 2203   | No file              | `9ccfbcba01de`  |
| 2196   | No file              | `9ccfbcba01de`  |
| 2192   | No file              | `9ccfbcba01de`  |
| 2189   | No file              | `9ccfbcba01de`  |
| 2183   | No file              | `9ccfbcba01de`  |
| 2179   | No file              | `9ccfbcba01de`  |
| 2171   | No file              | `9ccfbcba01de`  |
| 2163   | No file              | `9ccfbcba01de`  |
| 2156   | No file              | `9ccfbcba01de`  |
| 2151   | No file              | `9ccfbcba01de`  |
| 2147   | No file              | `9ccfbcba01de`  |
| 2142   | No file              | `9ccfbcba01de`  |
| 2138   | No file              | `9ccfbcba01de`  |
| 2134   | No file              | `9ccfbcba01de`  |
| 2130   | No file              | `9ccfbcba01de`  |
| 2122   | No file              | `9ccfbcba01de`  |
| 2107   | No file              | `9ccfbcba01de`  |
| 2098   | No file              | `9ccfbcba01de`  |
| 2089   | No file              | `9ccfbcba01de`  |
| 2081   | No file              | `9ccfbcba01de`  |
| 2073   | No file              | `9ccfbcba01de`  |
| 2067   | No file              | `9ccfbcba01de`  |
| 2063   | No file              | `9ccfbcba01de`  |
| 2059   | No file              | `9ccfbcba01de`  |
| 2052   | No file              | `9ccfbcba01de`  |
| 2044   | No file              | `9ccfbcba01de`  |
| 2039   | No file              | `9ccfbcba01de`  |
| 2032   | No file              | `9ccfbcba01de`  |
| 2025   | No file              | `9ccfbcba01de`  |
| 2011   | No file              | `9ccfbcba01de`  |
| 2005   | No file              | `9ccfbcba01de`  |
| 2000   | No file              | `9ccfbcba01de`  |
| 1996   | No file              | `9ccfbcba01de`  |
| 1991   | No file              | `9ccfbcba01de`  |
| 1985   | No file              | `9ccfbcba01de`  |
| 1980   | No file              | `9ccfbcba01de`  |
| 1969   | No file              | `9ccfbcba01de`  |
| 1964   | No file              | `9ccfbcba01de`  |
| 1958   | No file              | `9ccfbcba01de`  |
| 1950   | No file              | `9ccfbcba01de`  |
| 1945   | No file              | `9ccfbcba01de`  |
| 1937   | No file              | `9ccfbcba01de`  |
| 1933   | No file              | `9ccfbcba01de`  |
| 1927   | No file              | `9ccfbcba01de`  |
| 1921   | No file              | `9ccfbcba01de`  |
| 1914   | No file              | `9ccfbcba01de`  |
| 1908   | No file              | `9ccfbcba01de`  |
| 1897   | No file              | `9ccfbcba01de`  |
| 1892   | No file              | `9ccfbcba01de`  |
| 1886   | No file              | `9ccfbcba01de`  |
| 1881   | No file              | `9ccfbcba01de`  |
| 1871   | No file              | `9ccfbcba01de`  |
| 1866   | No file              | `9ccfbcba01de`  |
| 1862   | No file              | `9ccfbcba01de`  |
| 1854   | No file              | `9ccfbcba01de`  |
| 1846   | No file              | `9ccfbcba01de`  |
| 1838   | No file              | `9ccfbcba01de`  |
| 1832   | No file              | `9ccfbcba01de`  |
| 1826   | No file              | `9ccfbcba01de`  |
| 1822   | No file              | `9ccfbcba01de`  |
| 1818   | No file              | `9ccfbcba01de`  |
| 1804   | No file              | `9ccfbcba01de`  |
| 1794   | No file              | `9ccfbcba01de`  |
| 1790   | No file              | `9ccfbcba01de`  |
| 1784   | No file              | `9ccfbcba01de`  |
| 1774   | No file              | `9ccfbcba01de`  |
| 1771   | No file              | `9ccfbcba01de`  |
| 1762   | No file              | `9ccfbcba01de`  |
| 1759   | No file              | `9ccfbcba01de`  |
| 1754   | No file              | `9ccfbcba01de`  |
| 1749   | No file              | `9ccfbcba01de`  |
| 1743   | No file              | `9ccfbcba01de`  |
| 1737   | No file              | `9ccfbcba01de`  |
| 1731   | No file              | `9ccfbcba01de`  |
| 1725   | No file              | `9ccfbcba01de`  |
| 1717   | No file              | `9ccfbcba01de`  |
| 1710   | No file              | `9ccfbcba01de`  |
| 1704   | No file              | `9ccfbcba01de`  |
| 1698   | No file              | `9ccfbcba01de`  |
| 1690   | No file              | `9ccfbcba01de`  |
| 1685   | No file              | `9ccfbcba01de`  |
| 1680   | No file              | `9ccfbcba01de`  |
| 1674   | No file              | `9ccfbcba01de`  |
| 1668   | No file              | `9ccfbcba01de`  |
| 1659   | No file              | `9ccfbcba01de`  |
| 1649   | No file              | `9ccfbcba01de`  |
| 1642   | No file              | `9ccfbcba01de`  |
| 1636   | No file              | `9ccfbcba01de`  |
| 1628   | No file              | `9ccfbcba01de`  |
| 1622   | No file              | `9ccfbcba01de`  |
| 1614   | No file              | `9ccfbcba01de`  |
| 1608   | No file              | `9ccfbcba01de`  |
| 1602   | No file              | `9ccfbcba01de`  |
| 1598   | No file              | `9ccfbcba01de`  |
| 1594   | No file              | `9ccfbcba01de`  |
| 1590   | No file              | `9ccfbcba01de`  |
| 1587   | No file              | `9ccfbcba01de`  |
| 1584   | No file              | `9ccfbcba01de`  |
| 1579   | No file              | `9ccfbcba01de`  |
| 1572   | No file              | `9ccfbcba01de`  |
| 1565   | No file              | `9ccfbcba01de`  |
| 1559   | No file              | `9ccfbcba01de`  |
| 1554   | No file              | `9ccfbcba01de`  |
| 1547   | No file              | `9ccfbcba01de`  |
| 1537   | No file              | `9ccfbcba01de`  |
| 1529   | No file              | `9ccfbcba01de`  |
| 1524   | No file              | `9ccfbcba01de`  |
| 1519   | No file              | `9ccfbcba01de`  |
| 1509   | No file              | `9ccfbcba01de`  |
| 1506   | No file              | `9ccfbcba01de`  |
| 1504   | No file              | `9ccfbcba01de`  |
| 1500   | No file              | `9ccfbcba01de`  |
| 1493   | No file              | `9ccfbcba01de`  |
| 1489   | No file              | `9ccfbcba01de`  |
| 1485   | No file              | `9ccfbcba01de`  |
| 1481   | No file              | `9ccfbcba01de`  |
| 1474   | No file              | `9ccfbcba01de`  |
| 1466   | No file              | `9ccfbcba01de`  |
| 1462   | No file              | `9ccfbcba01de`  |
| 1459   | No file              | `9ccfbcba01de`  |
| 1453   | No file              | `9ccfbcba01de`  |
| 1450   | No file              | `9ccfbcba01de`  |
| 1445   | No file              | `9ccfbcba01de`  |
| 1439   | No file              | `9ccfbcba01de`  |
| 1433   | No file              | `9ccfbcba01de`  |
| 1430   | No file              | `9ccfbcba01de`  |
| 1426   | No file              | `9ccfbcba01de`  |
| 1421   | No file              | `9ccfbcba01de`  |
| 1417   | No file              | `9ccfbcba01de`  |
| 1416   | No file              | `9ccfbcba01de`  |
| 1409   | No file              | `9ccfbcba01de`  |
| 1405   | No file              | `9ccfbcba01de`  |
| 1401   | No file              | `9ccfbcba01de`  |
| 1396   | No file              | `9ccfbcba01de`  |
| 1391   | No file              | `9ccfbcba01de`  |
| 1390   | No file              | `9ccfbcba01de`  |
| 1386   | No file              | `9ccfbcba01de`  |
| 1381   | No file              | `9ccfbcba01de`  |
| 1379   | No file              | `9ccfbcba01de`  |
| 1372   | No file              | `9ccfbcba01de`  |
| 1366   | No file              | `9ccfbcba01de`  |
| 1364   | No file              | `9ccfbcba01de`  |
| 1363   | No file              | `9ccfbcba01de`  |
| 1360   | No file              | `9ccfbcba01de`  |
| 1358   | No file              | `9ccfbcba01de`  |
| 1355   | No file              | `9ccfbcba01de`  |
| 1351   | No file              | `9ccfbcba01de`  |
| 1348   | No file              | `9ccfbcba01de`  |
| 1346   | No file              | `9ccfbcba01de`  |
| 1341   | No file              | `9ccfbcba01de`  |
| 1340   | No file              | `9ccfbcba01de`  |
| 1338   | No file              | `9ccfbcba01de`  |
| 1335   | No file              | `9ccfbcba01de`  |
| 1333   | No file              | `9ccfbcba01de`  |
| 1329   | No file              | `9ccfbcba01de`  |
| 1327   | No file              | `9ccfbcba01de`  |
| 1324   | No file              | `9ccfbcba01de`  |
| 1321   | No file              | `9ccfbcba01de`  |
| 1319   | No file              | `9ccfbcba01de`  |
| 1318   | No file              | `9ccfbcba01de`  |
| 1316   | No file              | `9ccfbcba01de`  |
| 1313   | No file              | `9ccfbcba01de`  |
| 1311   | No file              | `9ccfbcba01de`  |
| 1309   | No file              | `9ccfbcba01de`  |
| 1304   | No file              | `9ccfbcba01de`  |
| 1292   | No file              | `9ccfbcba01de`  |
| 1286   | No file              | `9ccfbcba01de`  |
| 1280   | No file              | `9ccfbcba01de`  |
| 1276   | No file              | `9ccfbcba01de`  |
| 1267   | No file              | `9ccfbcba01de`  |
| 1261   | No file              | `9ccfbcba01de`  |
| 1256   | No file              | `9ccfbcba01de`  |
| 1250   | No file              | `9ccfbcba01de`  |
| 1246   | No file              | `9ccfbcba01de`  |
| 1239   | No file              | `9ccfbcba01de`  |
| 1230   | No file              | `9ccfbcba01de`  |
| 1226   | No file              | `9ccfbcba01de`  |
| 1220   | No file              | `9ccfbcba01de`  |
| 1217   | No file              | `9ccfbcba01de`  |
| 1211   | No file              | `9ccfbcba01de`  |
| 1210   | No file              | `9ccfbcba01de`  |
| 1208   | No file              | `9ccfbcba01de`  |
| 1203   | No file              | `9ccfbcba01de`  |
| 1197   | No file              | `9ccfbcba01de`  |
| 1194   | No file              | `9ccfbcba01de`  |
| 1192   | No file              | `9ccfbcba01de`  |
| 1187   | No file              | `9ccfbcba01de`  |
| 1183   | No file              | `9ccfbcba01de`  |
| 1177   | No file              | `9ccfbcba01de`  |
| 1173   | No file              | `9ccfbcba01de`  |
| 1167   | No file              | `9ccfbcba01de`  |
| 1164   | No file              | `9ccfbcba01de`  |
| 1156   | No file              | `9ccfbcba01de`  |
| 1149   | No file              | `9ccfbcba01de`  |
| 1144   | No file              | `9ccfbcba01de`  |
| 1137   | No file              | `9ccfbcba01de`  |
| 1132   | No file              | `9ccfbcba01de`  |
| 1127   | No file              | `9ccfbcba01de`  |
| 1122   | No file              | `9ccfbcba01de`  |
| 1118   | No file              | `9ccfbcba01de`  |
| 1114   | No file              | `9ccfbcba01de`  |
| 1109   | No file              | `9ccfbcba01de`  |
| 1102   | No file              | `9ccfbcba01de`  |
| 1096   | No file              | `9ccfbcba01de`  |
| 1088   | No file              | `9ccfbcba01de`  |
| 1081   | No file              | `9ccfbcba01de`  |
| 1076   | No file              | `9ccfbcba01de`  |
| 1069   | No file              | `9ccfbcba01de`  |
| 1064   | No file              | `9ccfbcba01de`  |
| 1058   | No file              | `9ccfbcba01de`  |
| 1051   | No file              | `9ccfbcba01de`  |
| 1044   | No file              | `9ccfbcba01de`  |
| 1036   | No file              | `9ccfbcba01de`  |
| 1026   | No file              | `9ccfbcba01de`  |
| 1016   | No file              | `9ccfbcba01de`  |
| 1009   | No file              | `9ccfbcba01de`  |
| 1005   | No file              | `9ccfbcba01de`  |
| 1000   | No file              | `9ccfbcba01de`  |
| 998    | No file              | `9ccfbcba01de`  |
| 990    | No file              | `9ccfbcba01de`  |
| 979    | No file              | `9ccfbcba01de`  |
| 972    | No file              | `9ccfbcba01de`  |
| 963    | No file              | `9ccfbcba01de`  |
| 955    | No file              | `9ccfbcba01de`  |
| 946    | No file              | `9ccfbcba01de`  |
| 938    | No file              | `9ccfbcba01de`  |
| 927    | No file              | `9ccfbcba01de`  |
| 911    | No file              | `9ccfbcba01de`  |
| 904    | No file              | `9ccfbcba01de`  |
| 899    | No file              | `9ccfbcba01de`  |
| 894    | No file              | `9ccfbcba01de`  |
| 885    | No file              | `9ccfbcba01de`  |
| 879    | No file              | `9ccfbcba01de`  |
| 872    | No file              | `9ccfbcba01de`  |
| 864    | No file              | `9ccfbcba01de`  |
| 855    | No file              | `9ccfbcba01de`  |
| 853    | No file              | `9ccfbcba01de`  |
| 845    | No file              | `9ccfbcba01de`  |
| 837    | No file              | `9ccfbcba01de`  |
| 829    | No file              | `9ccfbcba01de`  |
| 822    | No file              | `9ccfbcba01de`  |
| 814    | No file              | `9ccfbcba01de`  |
| 805    | No file              | `9ccfbcba01de`  |
| 794    | No file              | `9ccfbcba01de`  |
| 787    | No file              | `9ccfbcba01de`  |
| 780    | No file              | `9ccfbcba01de`  |
| 771    | No file              | `9ccfbcba01de`  |
| 760    | No file              | `9ccfbcba01de`  |
| 748    | No file              | `9ccfbcba01de`  |
| 741    | No file              | `9ccfbcba01de`  |
| 736    | No file              | `9ccfbcba01de`  |
| 731    | No file              | `9ccfbcba01de`  |
| 723    | No file              | `9ccfbcba01de`  |
| 711    | No file              | `9ccfbcba01de`  |
| 707    | No file              | `9ccfbcba01de`  |
| 697    | No file              | `9ccfbcba01de`  |
| 689    | No file              | `9ccfbcba01de`  |
| 683    | No file              | `9ccfbcba01de`  |
| 678    | No file              | `9ccfbcba01de`  |
| 670    | No file              | `9ccfbcba01de`  |
| 661    | No file              | `9ccfbcba01de`  |
| 656    | No file              | `9ccfbcba01de`  |
| 652    | No file              | `9ccfbcba01de`  |
| 643    | No file              | `9ccfbcba01de`  |
| 637    | No file              | `9ccfbcba01de`  |
| 630    | No file              | `9ccfbcba01de`  |
| 627    | No file              | `9ccfbcba01de`  |
| 621    | No file              | `9ccfbcba01de`  |
| 617    | No file              | `9ccfbcba01de`  |
| 615    | No file              | `9ccfbcba01de`  |
| 606    | No file              | `9ccfbcba01de`  |
| 599    | No file              | `9ccfbcba01de`  |
| 592    | No file              | `9ccfbcba01de`  |
| 586    | No file              | `9ccfbcba01de`  |
| 577    | No file              | `9ccfbcba01de`  |
| 569    | No file              | `9ccfbcba01de`  |
| 561    | No file              | `9ccfbcba01de`  |
| 554    | No file              | `9ccfbcba01de`  |
| 542    | No file              | `9ccfbcba01de`  |
| 532    | No file              | `9ccfbcba01de`  |
| 531    | No file              | `9ccfbcba01de`  |
| 526    | No file              | `9ccfbcba01de`  |
| 521    | No file              | `9ccfbcba01de`  |
| 517    | No file              | `9ccfbcba01de`  |
| 510    | No file              | `9ccfbcba01de`  |
| 508    | No file              | `9ccfbcba01de`  |
| 504    | No file              | `9ccfbcba01de`  |
| 497    | No file              | `9ccfbcba01de`  |
| 491    | No file              | `9ccfbcba01de`  |
| 485    | No file              | `9ccfbcba01de`  |
| 478    | No file              | `9ccfbcba01de`  |
| 472    | No file              | `9ccfbcba01de`  |
| 466    | No file              | `9ccfbcba01de`  |
| 457    | No file              | `9ccfbcba01de`  |
| 452    | No file              | `9ccfbcba01de`  |
| 449    | No file              | `9ccfbcba01de`  |
| 435    | No file              | `9ccfbcba01de`  |

<!-- versions:end -->

## Companion Files

None. The handler names characters, items and knowledge from
`languagedata_*.loc` and the lookup indexes, and the parts, difficulties and
auras with the `stringtable.bss` keys the Black Shrine window uses (LOC
type 37), when they are loaded.

All multi-byte values are little-endian.

## Layout 3

### File Layout

Plain binary: no `PABR` magic, no offset file and no trailer.

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (variable: 43 bytes + show rewards)

| Offset              | Type                            | Field                  | Notes                                                                              |
| ------------------- | ------------------------------- | ---------------------- | ---------------------------------------------------------------------------------- |
| `+0x00`             | u16                             | character_key          | Row key, the `characterstatic.dbss` character; `getCharacterKeyRaw()`              |
| `+0x02`             | u16                             | character_key_dup      | Equals `character_key` on every row                                                |
| `+0x04`             | u16                             | unlock_character_key   | Boss of the previous difficulty of the group, `0` when none; see Field Names       |
| `+0x06`             | u32                             | unlock_mental_card_key | Knowledge (LOC type 34) that unlocks the group, `0` when none; `getUnlockConditionMentalCardKeyRaw()` |
| `+0x0a`             | f32                             | offence_stat           | Aura offence; `getOffenceStat()`, see Open Questions                               |
| `+0x0e`             | f32                             | defence_stat           | Aura defence; `getDffenceStat()`, see Open Questions                               |
| `+0x12`             | u8                              | element_type           | The aura the monster is weak to, see [`elementalstat.bss` Element Types](elementalstat_bss.md#element-types); `getElementalStatType()` |
| `+0x13`             | u8                              | level                  | Difficulty, from `0`; `getLevel()`, see [Difficulties](#difficulties)              |
| `+0x14`             | u8                              | group                  | Boss group, see [Groups](#groups); `getGroup()`                                    |
| `+0x15`             | u8                              | is_boss                | `1` on the boss of the group and difficulty, `0` on the other monsters; `getIsBoss()` |
| `+0x16`             | u8                              | monster_part           | `1` Donghae (Solo), `2` Hwanghae (Party); `getMorningLandMonsterPartRaw()`         |
| `+0x17`             | u32                             | show_reward_count      | Number of `show_rewards`; `1` on the 108 bosses, `0` on the other rows (client 3474) |
| `+0x1b`             | Reward Item[show_reward_count]  | show_rewards           | The reward preview of the window; `ToClient_getElementalMonsterShowRewardItemKey` |
| `show_rewards+0x00` | f32                             | position_x             | World position the window navigates to; `getPosition()`                            |
| `show_rewards+0x04` | f32                             | position_y             | Height                                                                             |
| `show_rewards+0x08` | f32                             | position_z             |                                                                                    |
| `show_rewards+0x0c` | f32                             | min_ap                 | Minimum displayed AP to enter; `getMinAP()`, `0` when there is none               |

### Reward Item (16 bytes)

| Offset  | Type     | Field      | Notes                                                                    |
| ------- | -------- | ---------- | ------------------------------------------------------------------------ |
| `+0x00` | u32      | item_key   | Item key, `enchant_level << 24 \| item_id` (`ItemEnchantKey` in the Lua) |
| `+0x04` | bytes[4] | padding_04 | Alignment of `count`; `bf 00 00 00` on every entry (client 3474), see Notes |
| `+0x08` | i64      | count      | Number of the item; `ToClient_getElementalMonsterShowRewardItemCount`    |

## Layout 2

### Row (variable: 43 bytes + show rewards)

| Offset              | Type                    | Field                  | Notes                                 |
| ------------------- | ----------------------- | ---------------------- | ------------------------------------- |
| `+0x00`             | u16                     | character_key          |                                       |
| `+0x02`             | u16                     | character_key_dup      |                                       |
| `+0x04`             | u16                     | unlock_character_key   |                                       |
| `+0x06`             | u32                     | unlock_mental_card_key |                                       |
| `+0x0a`             | f32                     | offence_stat           |                                       |
| `+0x0e`             | f32                     | defence_stat           |                                       |
| `+0x12`             | u8                      | element_type           |                                       |
| `+0x13`             | u8                      | level                  |                                       |
| `+0x14`             | u8                      | group                  |                                       |
| `+0x15`             | u8                      | is_boss                |                                       |
| `+0x16`             | u8                      | monster_part           |                                       |
| `+0x17`             | u32                     | show_reward_count      |                                       |
| `+0x1b`             | u32[show_reward_count]  | show_rewards           | Item keys alone, no count             |
| `show_rewards+0x00` | f32                     | position_x             |                                       |
| `show_rewards+0x04` | f32                     | position_y             |                                       |
| `show_rewards+0x08` | f32                     | position_z             |                                       |
| `show_rewards+0x0c` | f32                     | min_ap                 |                                       |

## Layout 1

### Row (variable: 38 bytes + show rewards)

| Offset              | Type                    | Field                  | Notes                                 |
| ------------------- | ----------------------- | ---------------------- | ------------------------------------- |
| `+0x00`             | u16                     | character_key          |                                       |
| `+0x02`             | u16                     | character_key_dup      |                                       |
| `+0x04`             | u16                     | unlock_character_key   |                                       |
| `+0x06`             | u32                     | unlock_mental_card_key |                                       |
| `+0x0a`             | f32                     | offence_stat           |                                       |
| `+0x0e`             | f32                     | defence_stat           |                                       |
| `+0x12`             | u8                      | element_type           |                                       |
| `+0x13`             | u8                      | level                  |                                       |
| `+0x14`             | u8                      | group                  |                                       |
| `+0x15`             | u8                      | is_boss                |                                       |
| `+0x16`             | u32                     | show_reward_count      |                                       |
| `+0x1a`             | u32[show_reward_count]  | show_rewards           | Item keys alone, no count             |
| `show_rewards+0x00` | f32                     | position_x             |                                       |
| `show_rewards+0x04` | f32                     | position_y             |                                       |
| `show_rewards+0x08` | f32                     | position_z             |                                       |

Layout 1 has no `monster_part` and no `min_ap`: the client had only the
Donghae (Solo) bosses, and every difficulty was gated by its offence and
defence.

## Groups

The level `0` boss of each group on client 3474, with the aura it is weak
to. The weak auras are the ones the official event notice "[Black Shrine]
Enhanced Blessing and Unpurified Energy" lists per boss.

| Group | Part             | Boss (level 0)           | Weak aura | Levels | `unlock_mental_card_key` (levels 0 to 4) |
| ----- | ---------------- | ------------------------ | --------- | ------ | ---------------------------------------- |
| `0`   | Donghae (Solo)   | Golden Pig King          | Sun       | 0 to 9 | `11742` Tale of the Golden Pig King      |
| `1`   | Donghae (Solo)   | Oduksini                 | Sun       | 0 to 9 | `11756` Tale of the Oduksini             |
| `2`   | Donghae (Solo)   | Apex Changui             | Sun       | 0 to 9 | `11750` Tale of the Apex Changui         |
| `3`   | Donghae (Solo)   | Bari                     | Moon      | 0 to 6 | `11733` Tale of the Mudang Wraith        |
| `4`   | Donghae (Solo)   | Songakshi                | Moon      | 0 to 9 | `11739` Tale of the Songakshi            |
| `5`   | Donghae (Solo)   | Bamboo Legion Lieutenant | Moon      | 0 to 9 | `11748` Tale of the Bamboo Legion        |
| `6`   | Donghae (Solo)   | Sangoon                  | Earth     | 0 to 9 | `11753` Tale of Sangoon                  |
| `7`   | Donghae (Solo)   | Gumiho                   | Earth     | 0 to 9 | `11736` Tale of the Gumiho               |
| `8`   | Donghae (Solo)   | Duoksini                 | Earth     | 0 to 9 | `11745` Tale of Duoksini                 |
| `9`   | Donghae (Solo)   | Imoogi                   | Earth     | 0 to 6 | `11756` Tale of the Oduksini             |
| `10`  | Hwanghae (Party) | Jigwi                    | Sun       | 0 to 1 | `0`                                      |
| `11`  | Hwanghae (Party) | Blue-clad Youth          | Sun       | 0 to 1 | `0`                                      |
| `12`  | Hwanghae (Party) | Bulgasal                 | Sun       | 0 to 1 | `0`                                      |
| `13`  | Hwanghae (Party) | Uturi                    | Sun       | 0 to 1 | `0`                                      |
| `14`  | Hwanghae (Party) | Dark Bonghwang           | Sun       | 0 to 1 | `0`                                      |
| `15`  | Hwanghae (Party) | Deposed Crown Prince     | Sun       | 0 to 1 | `0`                                      |
| `16`  | Hwanghae (Party) | Bihyung                  | Sun       | 0 to 1 | `0`                                      |

Every Hwanghae (Party) row holds `element_type` `0`.

## Difficulties

The window names a Donghae (Solo) `level` with the GAME sheet key
`LUA_MORNING_ATTRBOSS_DIFFICULTY_<level>` ("Calamity 1" for `0`) and the
two Hwanghae (Party) levels with the RESOURCE sheet keys
`PANEL_MORNING2_EASY` ("Normal", `0`) and `PANEL_MORNING2_HARD` ("Hard",
`1`); its radio buttons pass `0` and `1` to `difficultySelectMorning2`.

On client 3474 the stats split by difficulty:

| Rows                         | `offence_stat`, `defence_stat` | `min_ap`              |
| ---------------------------- | ------------------------------ | --------------------- |
| Donghae (Solo), levels 0 to 6 | Set on every row              | `0`                   |
| Donghae (Solo), levels 7 to 9 | `0`                           | `305` to `385`        |
| Hwanghae (Party)             | `0`                            | `0`                   |

Client 3482 reworks the Donghae (Solo) difficulties: its 201 rows hold 104
bosses, nine levels (`0` to `8`) per Donghae group, each gated by `min_ap`
alone (`300` to `430`). `unlock_character_key`, `unlock_mental_card_key`,
`offence_stat` and `defence_stat` are `0` on every row.

## Field Names

No reference source has the file. It first appears on client 2519 (absent
on client 2107), so a private server's `DataSheets.bexcel`, `.xlsm` sheets
and server dump on client 1784 have no `Elemental` sheet or column, and the
2016 client and the client 519 server tables predate it.

The names follow the getters the client Lua of client 3474 calls on a row
(`panel_window_morningland_boss_all_1.luac`,
`panel_window_morningland_detailreward_all.luac`,
`panel_widget_monsterbar_renew.luac`): `getCharacterKeyRaw`, `getGroup`,
`getLevel`, `getElementalStatType`, `getIsBoss`,
`getMorningLandMonsterPartRaw`, `getUnlockConditionMentalCardKeyRaw`,
`getPosition`, `getMinAP`, `getOffenceStat` and `getDffenceStat`. Each
field matches its getter by value:

- `character_key` is the key the window passes to
  `getCharacterStaticStatusWarpper`; the names are the bosses of the official
  wiki pages "Black Shrine: Donghae (Solo)" and "Black Shrine: Hwanghae
  (Party)".
- `group` and `level` are the two arguments of
  `ToClient_getElementalMonsterInfo(group, level)`: the window walks groups
  `0` to `_MORNINGLAND_PART1_BOSSCOUNT - 1` for Donghae and on to
  `_MORNINGLAND_PART2_BOSSCOUNT - 1` for Hwanghae, levels `0` to `9` in the
  first and `0` to `1` in the second, which are the values the rows hold.
- `element_type` is the boss weakness of the window
  (`_frmBossWeeknessUV[getElementalStatType()]`), and its values match the
  weak auras of [Groups](#groups).
- `is_boss` and `show_reward_count` are `1` on the same 108 rows, one per
  group and difficulty, and each of those rows' `show_rewards` item is the
  boss's own reward box ("Boss Blitz Reward: Golden Pig King" `761555` on
  group `0`, "Boss Slayer's Haul - Jigwi (Normal)" `761337` on group `10`
  level `0`).
- `monster_part`: the window compares `getMorningLandMonsterPartRaw()` with
  `__eMorningLandMosterPart1` and `__eMorningLandMosterPart2`, whose values
  the client Lua does not hold; `1` sits on groups `0` to `9`, `2` on
  groups `10` to `16`.
- `unlock_mental_card_key`: the window reads it from level `0` of a group
  and names the knowledge in `LUA_MORNING_ATTRBOSS_LOCK` when the group is
  locked. Each group's key is its boss's "Tale of" knowledge (LOC type 34),
  on levels `0` to `4`.
- `unlock_character_key` has no getter in the Lua. On every one of its 20
  non-zero rows (client 3474) it is the boss of the same group one level
  lower, on levels `5` and `6` (Calamity 6 and 7). The official wiki page
  "Black Shrine: Donghae (Solo)" says "Calamity 6 to 10 bosses will only
  unlock if an Adventurer successfully defeats the boss of the previous
  level". On client 2519 the field held the lower boss on levels `5` to
  `9`, before Calamity 8 to 10 moved to `min_ap`.
- `min_ap` is the "At least {value} AP" line (`PANEL_MORNINGBOSS_LIMITAPVALUE`)
  of the window, which greys out the enter button below it. The official
  "[Update History] Black Shrine (Boss Blitz)" page lists "Displayed AP"
  requirements of 330 to 380 for Calamity 8 to 10, the range of the
  levels `7` to `9` rows.
- `offence_stat` and `defence_stat`: the monster bar of a developer client
  prints `getElementalStatType()`, `getOffenceStat()` and `getDffenceStat()`
  as "속성" (aura), "공" (attack) and "방" (defence). The two f32 values at
  `+0x0a` and `+0x0e` are the only fields left for them; their order is an
  Open Question.

## Notes

- Client 3474 has 1,000 rows and every `character_key` is unique. The 892
  rows with `is_boss` `0` are the other monsters of a fight and carry the
  group, level, weak aura and stats of their boss's fight; one of them,
  `21082` Imoogi, also has a position.
- `padding_04` is the 4 bytes between the u32 `item_key` and the 8-aligned
  i64 `count`. It holds `bf 00 00 00` on every entry here and `fc 7f 00 00`
  or `f7 7f 00 00` in [`elementalmonsterreward.bss`](elementalmonsterreward_bss.md),
  the leftover bytes of the tool that wrote the file.
- The 108 boss rows hold the same position on every difficulty of a group.
- Layout 2 (clients 3002 and 3251) stored the reward preview as item keys
  alone; Layout 3 (client 3474) adds the count and the padding.
- On client 2519 (Layout 1), levels `7` to `9` held an offence and defence
  like the lower levels (`1240` and `358` on the group `0` level `7` boss),
  and `unlock_mental_card_key` was set on level `0` alone. On clients 3002
  and 3251 it was also set on levels `7` to `9` of some groups.
- The handler (`_bss/elementalmonsterstat/`) links each `character_key` to
  its `characterstatic.dbss` row, names the unlock boss with its difficulty
  ("Gumiho (Calamity 6)"), the knowledge, the weak aura, the part and the
  difficulty with the window's own text, and shows a zero `min_ap` or
  unlock key as empty.
- The rewards a boss gives by its ranking are in
  [`elementalmonsterreward.bss`](elementalmonsterreward_bss.md), keyed by the
  same `character_key`. The server blessings of a defeated boss, by its
  `element_type`, are in [`elementalserverbuff.bss`](elementalserverbuff_bss.md),
  the aura stats of the player in [`elementalstat.bss`](elementalstat_bss.md).

## Open Questions

### Order of the Offence and Defence Stats

`offence_stat` (`+0x0a`) holds the larger value on every row (`1000` and
`233` on group `1` level `5`), `defence_stat` (`+0x0e`) the smaller. The
Lua getters `getOffenceStat` and `getDffenceStat` show only their names,
not their offsets. A boss offence near the 1,000 DP of ten Light Orbs (100
DP each) and a defence near their 500 AP (50 AP each) fit this order, but
only a developer client's monster bar line, or a fight that changes with
one orb, would confirm it.
