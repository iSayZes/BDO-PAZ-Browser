# `boss_spawn.bss` Format

## Purpose

The guild bosses of the Guild Boss Summon window
(`panel_guild_bosssummon_all`): one 43-byte row per summonable boss with its
spawn key, the number of difficulty levels, where it spawns and the spawn
range. The window reads a row through `ToClient_bossSpawnList()` and, by
`BossSpawnKey`, `ToClient_bossSpawnPosition`, `ToClient_bossSpawnRange` and
`ToClient_bossSpawnMaxLevel`. The per-level reward and image are in
[`boss_spawnlevel.bss`](boss_spawnlevel_bss.md), which uses the same keys.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File             | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | ---------------- | ----- | ------- | --------- |
| 2      | 2134 and later | 3483    | `boss_spawn.bss` | 278   | 6 Row   | 43        |
| 1      | 1426 to 2107   | 2107    | `boss_spawn.bss` | 180   | 4 Row   | 40        |

| Layout | File             | Known         | Unknown       |
| ------ | ---------------- | ------------- | ------------- |
| 2      | `boss_spawn.bss` | 164 B (59.0%) | 114 B (41.0%) |
| 1      | `boss_spawn.bss` | 116 B (64.4%) | 64 B (35.6%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `1d471f2e6c2c`  |
| 3482   | Layout 2             | `1d471f2e6c2c`  |
| 3474   | Layout 2             | `1d471f2e6c2c`  |
| 3473   | Layout 2             | `1d471f2e6c2c`  |
| 3464   | Layout 2             | `1d471f2e6c2c`  |
| 3458   | Layout 2             | `1d471f2e6c2c`  |
| 3454   | Layout 2             | `1d471f2e6c2c`  |
| 3444   | Layout 2             | `1d471f2e6c2c`  |
| 3435   | Layout 2             | `1d471f2e6c2c`  |
| 3426   | Layout 2             | `1d471f2e6c2c`  |
| 3418   | Layout 2             | `1d471f2e6c2c`  |
| 3412   | Layout 2             | `1d471f2e6c2c`  |
| 3402   | Layout 2             | `1d471f2e6c2c`  |
| 3396   | Layout 2             | `1d471f2e6c2c`  |
| 3387   | Layout 2             | `1d471f2e6c2c`  |
| 3381   | Layout 2             | `1d471f2e6c2c`  |
| 3373   | Layout 2             | `1d471f2e6c2c`  |
| 3364   | Layout 2             | `1d471f2e6c2c`  |
| 3356   | Layout 2             | `1d471f2e6c2c`  |
| 3349   | Layout 2             | `1d471f2e6c2c`  |
| 3342   | Layout 2             | `1d471f2e6c2c`  |
| 3335   | Layout 2             | `1d471f2e6c2c`  |
| 3326   | Layout 2             | `1d471f2e6c2c`  |
| 3321   | Layout 2             | `1d471f2e6c2c`  |
| 3314   | Layout 2             | `1d471f2e6c2c`  |
| 3303   | Layout 2             | `1d471f2e6c2c`  |
| 3302   | Layout 2             | `1d471f2e6c2c`  |
| 3293   | Layout 2             | `1d471f2e6c2c`  |
| 3283   | Layout 2             | `1d471f2e6c2c`  |
| 3275   | Layout 2             | `1d471f2e6c2c`  |
| 3267   | Layout 2             | `1d471f2e6c2c`  |
| 3258   | Layout 2             | `1d471f2e6c2c`  |
| 3251   | Layout 2             | `1d471f2e6c2c`  |
| 3242   | Layout 2             | `1d471f2e6c2c`  |
| 3235   | Layout 2             | `1d471f2e6c2c`  |
| 3229   | Layout 2             | `1d471f2e6c2c`  |
| 3212   | Layout 2             | `1d471f2e6c2c`  |
| 3203   | Layout 2             | `1d471f2e6c2c`  |
| 3193   | Layout 2             | `1d471f2e6c2c`  |
| 3186   | Layout 2             | `1d471f2e6c2c`  |
| 3177   | Layout 2             | `1d471f2e6c2c`  |
| 3169   | Layout 2             | `1d471f2e6c2c`  |
| 3158   | Layout 2             | `1d471f2e6c2c`  |
| 3151   | Layout 2             | `1d471f2e6c2c`  |
| 3144   | Layout 2             | `1d471f2e6c2c`  |
| 3133   | Layout 2             | `1d471f2e6c2c`  |
| 3125   | Layout 2             | `1d471f2e6c2c`  |
| 3118   | Layout 2             | `1d471f2e6c2c`  |
| 3111   | Layout 2             | `1d471f2e6c2c`  |
| 3103   | Layout 2             | `1d471f2e6c2c`  |
| 3095   | Layout 2             | `1d471f2e6c2c`  |
| 3086   | Layout 2             | `1d471f2e6c2c`  |
| 3072   | Layout 2             | `1d471f2e6c2c`  |
| 3062   | Layout 2             | `1d471f2e6c2c`  |
| 3052   | Layout 2             | `1d471f2e6c2c`  |
| 3045   | Layout 2             | `1d471f2e6c2c`  |
| 3037   | Layout 2             | `1d471f2e6c2c`  |
| 3030   | Layout 2             | `1d471f2e6c2c`  |
| 3021   | Layout 2             | `1d471f2e6c2c`  |
| 3012   | Layout 2             | `1d471f2e6c2c`  |
| 3002   | Layout 2             | `1d471f2e6c2c`  |
| 2995   | Layout 2             | `1d471f2e6c2c`  |
| 2987   | Layout 2             | `1d471f2e6c2c`  |
| 2978   | Layout 2             | `1d471f2e6c2c`  |
| 2970   | Layout 2             | `1d471f2e6c2c`  |
| 2959   | Layout 2             | `1d471f2e6c2c`  |
| 2951   | Layout 2             | `1d471f2e6c2c`  |
| 2942   | Layout 2             | `1d471f2e6c2c`  |
| 2935   | Layout 2             | `1d471f2e6c2c`  |
| 2932   | Layout 2             | `1d471f2e6c2c`  |
| 2923   | Layout 2             | `1d471f2e6c2c`  |
| 2919   | Layout 2             | `1d471f2e6c2c`  |
| 2907   | Layout 2             | `1d471f2e6c2c`  |
| 2900   | Layout 2             | `1d471f2e6c2c`  |
| 2891   | Layout 2             | `1d471f2e6c2c`  |
| 2882   | Layout 2             | `1d471f2e6c2c`  |
| 2872   | Layout 2             | `1d471f2e6c2c`  |
| 2863   | Layout 2             | `1d471f2e6c2c`  |
| 2855   | Layout 2             | `1d471f2e6c2c`  |
| 2849   | Layout 2             | `1d471f2e6c2c`  |
| 2844   | Layout 2             | `1d471f2e6c2c`  |
| 2834   | Layout 2             | `1d471f2e6c2c`  |
| 2825   | Layout 2             | `1d471f2e6c2c`  |
| 2819   | Layout 2             | `1d471f2e6c2c`  |
| 2811   | Layout 2             | `1d471f2e6c2c`  |
| 2803   | Layout 2             | `1d471f2e6c2c`  |
| 2794   | Layout 2             | `1d471f2e6c2c`  |
| 2783   | Layout 2             | `1d471f2e6c2c`  |
| 2774   | Layout 2             | `1d471f2e6c2c`  |
| 2765   | Layout 2             | `1d471f2e6c2c`  |
| 2756   | Layout 2             | `1d471f2e6c2c`  |
| 2750   | Layout 2             | `1d471f2e6c2c`  |
| 2743   | Layout 2             | `1d471f2e6c2c`  |
| 2736   | Layout 2             | `1d471f2e6c2c`  |
| 2726   | Layout 2             | `1d471f2e6c2c`  |
| 2717   | Layout 2             | `1d471f2e6c2c`  |
| 2709   | Layout 2             | `1d471f2e6c2c`  |
| 2703   | Layout 2             | `1d471f2e6c2c`  |
| 2695   | Layout 2             | `1d471f2e6c2c`  |
| 2684   | Layout 2             | `1d471f2e6c2c`  |
| 2672   | Layout 2             | `1d471f2e6c2c`  |
| 2665   | Layout 2             | `1d471f2e6c2c`  |
| 2657   | Layout 2             | `1d471f2e6c2c`  |
| 2649   | Layout 2             | `1d471f2e6c2c`  |
| 2644   | Layout 2             | `1d471f2e6c2c`  |
| 2637   | Layout 2             | `1d471f2e6c2c`  |
| 2629   | Layout 2             | `1d471f2e6c2c`  |
| 2619   | Layout 2             | `1d471f2e6c2c`  |
| 2612   | Layout 2             | `1d471f2e6c2c`  |
| 2606   | Layout 2             | `1d471f2e6c2c`  |
| 2602   | Layout 2             | `1d471f2e6c2c`  |
| 2601   | Layout 2             | `1d471f2e6c2c`  |
| 2592   | Layout 2             | `1d471f2e6c2c`  |
| 2583   | Layout 2             | `1d471f2e6c2c`  |
| 2575   | Layout 2             | `1d471f2e6c2c`  |
| 2567   | Layout 2             | `1d471f2e6c2c`  |
| 2560   | Layout 2             | `1d471f2e6c2c`  |
| 2553   | Layout 2             | `1d471f2e6c2c`  |
| 2545   | Layout 2             | `1d471f2e6c2c`  |
| 2538   | Layout 2             | `1d471f2e6c2c`  |
| 2529   | Layout 2             | `1d471f2e6c2c`  |
| 2519   | Layout 2             | `1d471f2e6c2c`  |
| 2513   | Layout 2             | `1d471f2e6c2c`  |
| 2510   | Layout 2             | `1d471f2e6c2c`  |
| 2507   | Layout 2             | `1d471f2e6c2c`  |
| 2503   | Layout 2             | `1d471f2e6c2c`  |
| 2498   | Layout 2             | `1d471f2e6c2c`  |
| 2492   | Layout 2             | `1d471f2e6c2c`  |
| 2487   | Layout 2             | `1d471f2e6c2c`  |
| 2480   | Layout 2             | `1d471f2e6c2c`  |
| 2474   | Layout 2             | `1d471f2e6c2c`  |
| 2468   | Layout 2             | `1d471f2e6c2c`  |
| 2460   | Layout 2             | `1d471f2e6c2c`  |
| 2453   | Layout 2             | `1d471f2e6c2c`  |
| 2444   | Layout 2             | `1d471f2e6c2c`  |
| 2438   | Layout 2             | `1d471f2e6c2c`  |
| 2434   | Layout 2             | `1d471f2e6c2c`  |
| 2429   | Layout 2             | `1d471f2e6c2c`  |
| 2421   | Layout 2             | `1d471f2e6c2c`  |
| 2414   | Layout 2             | `1d471f2e6c2c`  |
| 2407   | Layout 2             | `1d471f2e6c2c`  |
| 2401   | Layout 2             | `1d471f2e6c2c`  |
| 2397   | Layout 2             | `1d471f2e6c2c`  |
| 2393   | Layout 2             | `1d471f2e6c2c`  |
| 2384   | Layout 2             | `1d471f2e6c2c`  |
| 2378   | Layout 2             | `1d471f2e6c2c`  |
| 2372   | Layout 2             | `1d471f2e6c2c`  |
| 2358   | Layout 2             | `1d471f2e6c2c`  |
| 2352   | Layout 2             | `1d471f2e6c2c`  |
| 2347   | Layout 2             | `1d471f2e6c2c`  |
| 2343   | Layout 2             | `1d471f2e6c2c`  |
| 2335   | Layout 2             | `1d471f2e6c2c`  |
| 2327   | Layout 2             | `1d471f2e6c2c`  |
| 2324   | Layout 2             | `1d471f2e6c2c`  |
| 2319   | Layout 2             | `1d471f2e6c2c`  |
| 2313   | Layout 2             | `1d471f2e6c2c`  |
| 2308   | Layout 2             | `1d471f2e6c2c`  |
| 2302   | Layout 2             | `1d471f2e6c2c`  |
| 2295   | Layout 2             | `1d471f2e6c2c`  |
| 2290   | Layout 2             | `1d471f2e6c2c`  |
| 2284   | Layout 2             | `1d471f2e6c2c`  |
| 2276   | Layout 2             | `1d471f2e6c2c`  |
| 2269   | Layout 2             | `1d471f2e6c2c`  |
| 2259   | Layout 2             | `1d471f2e6c2c`  |
| 2250   | Layout 2             | `1d471f2e6c2c`  |
| 2243   | Layout 2             | `1d471f2e6c2c`  |
| 2235   | Layout 2             | `1d471f2e6c2c`  |
| 2229   | Layout 2             | `1d471f2e6c2c`  |
| 2224   | Layout 2             | `1d471f2e6c2c`  |
| 2218   | Layout 2             | `1d471f2e6c2c`  |
| 2215   | Layout 2             | `1d471f2e6c2c`  |
| 2207   | Layout 2             | `1d471f2e6c2c`  |
| 2203   | Layout 2             | `1d471f2e6c2c`  |
| 2196   | Layout 2             | `1d471f2e6c2c`  |
| 2192   | Layout 2             | `1d471f2e6c2c`  |
| 2189   | Layout 2             | `1d471f2e6c2c`  |
| 2183   | Layout 2             | `1d471f2e6c2c`  |
| 2179   | Layout 2             | `1d471f2e6c2c`  |
| 2171   | Layout 2             | `1d471f2e6c2c`  |
| 2163   | Layout 2             | `1d471f2e6c2c`  |
| 2156   | Layout 2             | `1d471f2e6c2c`  |
| 2151   | Layout 2             | `1d471f2e6c2c`  |
| 2147   | Layout 2             | `1d471f2e6c2c`  |
| 2142   | Layout 2             | `1d471f2e6c2c`  |
| 2138   | Layout 2             | `1d471f2e6c2c`  |
| 2134   | Layout 2             | `1d471f2e6c2c`  |
| 2130   | No documented layout | `1d471f2e6c2c`  |
| 2122   | No documented layout | `1d471f2e6c2c`  |
| 2107   | Layout 1             | `1d471f2e6c2c`  |
| 2098   | Layout 1             | `1d471f2e6c2c`  |
| 2089   | Layout 1             | `1d471f2e6c2c`  |
| 2081   | Layout 1             | `1d471f2e6c2c`  |
| 2073   | Layout 1             | `1d471f2e6c2c`  |
| 2067   | Layout 1             | `1d471f2e6c2c`  |
| 2063   | Layout 1             | `1d471f2e6c2c`  |
| 2059   | Layout 1             | `1d471f2e6c2c`  |
| 2052   | Layout 1             | `1d471f2e6c2c`  |
| 2044   | Layout 1             | `1d471f2e6c2c`  |
| 2039   | Layout 1             | `1d471f2e6c2c`  |
| 2032   | Layout 1             | `1d471f2e6c2c`  |
| 2025   | Layout 1             | `1d471f2e6c2c`  |
| 2011   | Layout 1             | `1d471f2e6c2c`  |
| 2005   | Layout 1             | `1d471f2e6c2c`  |
| 2000   | Layout 1             | `1d471f2e6c2c`  |
| 1996   | Layout 1             | `1d471f2e6c2c`  |
| 1991   | Layout 1             | `1d471f2e6c2c`  |
| 1985   | Layout 1             | `1d471f2e6c2c`  |
| 1980   | Layout 1             | `1d471f2e6c2c`  |
| 1969   | Layout 1             | `1d471f2e6c2c`  |
| 1964   | Layout 1             | `1d471f2e6c2c`  |
| 1958   | Layout 1             | `1d471f2e6c2c`  |
| 1950   | Layout 1             | `1d471f2e6c2c`  |
| 1945   | Layout 1             | `1d471f2e6c2c`  |
| 1937   | Layout 1             | `1d471f2e6c2c`  |
| 1933   | Layout 1             | `1d471f2e6c2c`  |
| 1927   | Layout 1             | `1d471f2e6c2c`  |
| 1921   | Layout 1             | `1d471f2e6c2c`  |
| 1914   | Layout 1             | `1d471f2e6c2c`  |
| 1908   | Layout 1             | `1d471f2e6c2c`  |
| 1897   | Layout 1             | `1d471f2e6c2c`  |
| 1892   | Layout 1             | `1d471f2e6c2c`  |
| 1886   | Layout 1             | `1d471f2e6c2c`  |
| 1881   | Layout 1             | `1d471f2e6c2c`  |
| 1871   | Layout 1             | `1d471f2e6c2c`  |
| 1866   | Layout 1             | `1d471f2e6c2c`  |
| 1862   | Layout 1             | `1d471f2e6c2c`  |
| 1854   | Layout 1             | `1d471f2e6c2c`  |
| 1846   | Layout 1             | `1d471f2e6c2c`  |
| 1838   | Layout 1             | `1d471f2e6c2c`  |
| 1832   | Layout 1             | `1d471f2e6c2c`  |
| 1826   | Layout 1             | `1d471f2e6c2c`  |
| 1822   | Layout 1             | `1d471f2e6c2c`  |
| 1818   | Layout 1             | `1d471f2e6c2c`  |
| 1804   | Layout 1             | `1d471f2e6c2c`  |
| 1794   | Layout 1             | `1d471f2e6c2c`  |
| 1790   | Layout 1             | `1d471f2e6c2c`  |
| 1784   | Layout 1             | `1d471f2e6c2c`  |
| 1774   | Layout 1             | `1d471f2e6c2c`  |
| 1771   | Layout 1             | `1d471f2e6c2c`  |
| 1762   | Layout 1             | `1d471f2e6c2c`  |
| 1759   | Layout 1             | `1d471f2e6c2c`  |
| 1754   | Layout 1             | `1d471f2e6c2c`  |
| 1749   | Layout 1             | `1d471f2e6c2c`  |
| 1743   | Layout 1             | `1d471f2e6c2c`  |
| 1737   | Layout 1             | `1d471f2e6c2c`  |
| 1731   | Layout 1             | `1d471f2e6c2c`  |
| 1725   | Layout 1             | `1d471f2e6c2c`  |
| 1717   | Layout 1             | `1d471f2e6c2c`  |
| 1710   | Layout 1             | `1d471f2e6c2c`  |
| 1704   | Layout 1             | `1d471f2e6c2c`  |
| 1698   | Layout 1             | `1d471f2e6c2c`  |
| 1690   | Layout 1             | `1d471f2e6c2c`  |
| 1685   | Layout 1             | `1d471f2e6c2c`  |
| 1680   | Layout 1             | `1d471f2e6c2c`  |
| 1674   | Layout 1             | `1d471f2e6c2c`  |
| 1668   | Layout 1             | `1d471f2e6c2c`  |
| 1659   | Layout 1             | `1d471f2e6c2c`  |
| 1649   | Layout 1             | `1d471f2e6c2c`  |
| 1642   | Layout 1             | `1d471f2e6c2c`  |
| 1636   | Layout 1             | `1d471f2e6c2c`  |
| 1628   | Layout 1             | `1d471f2e6c2c`  |
| 1622   | Layout 1             | `1d471f2e6c2c`  |
| 1614   | Layout 1             | `1d471f2e6c2c`  |
| 1608   | Layout 1             | `1d471f2e6c2c`  |
| 1602   | Layout 1             | `1d471f2e6c2c`  |
| 1598   | Layout 1             | `1d471f2e6c2c`  |
| 1594   | Layout 1             | `1d471f2e6c2c`  |
| 1590   | Layout 1             | `1d471f2e6c2c`  |
| 1587   | Layout 1             | `1d471f2e6c2c`  |
| 1584   | Layout 1             | `1d471f2e6c2c`  |
| 1579   | Layout 1             | `1d471f2e6c2c`  |
| 1572   | Layout 1             | `1d471f2e6c2c`  |
| 1565   | Layout 1             | `1d471f2e6c2c`  |
| 1559   | Layout 1             | `1d471f2e6c2c`  |
| 1554   | Layout 1             | `1d471f2e6c2c`  |
| 1547   | Layout 1             | `1d471f2e6c2c`  |
| 1537   | Layout 1             | `1d471f2e6c2c`  |
| 1529   | Layout 1             | `1d471f2e6c2c`  |
| 1524   | Layout 1             | `1d471f2e6c2c`  |
| 1519   | Layout 1             | `1d471f2e6c2c`  |
| 1509   | Layout 1             | `1d471f2e6c2c`  |
| 1506   | Layout 1             | `1d471f2e6c2c`  |
| 1504   | Layout 1             | `1d471f2e6c2c`  |
| 1500   | Layout 1             | `1d471f2e6c2c`  |
| 1493   | Layout 1             | `1d471f2e6c2c`  |
| 1489   | Layout 1             | `1d471f2e6c2c`  |
| 1485   | Layout 1             | `1d471f2e6c2c`  |
| 1481   | Layout 1             | `1d471f2e6c2c`  |
| 1474   | Layout 1             | `1d471f2e6c2c`  |
| 1466   | Layout 1             | `1d471f2e6c2c`  |
| 1462   | Layout 1             | `1d471f2e6c2c`  |
| 1459   | Layout 1             | `1d471f2e6c2c`  |
| 1453   | Layout 1             | `1d471f2e6c2c`  |
| 1450   | Layout 1             | `1d471f2e6c2c`  |
| 1445   | Layout 1             | `1d471f2e6c2c`  |
| 1439   | Layout 1             | `1d471f2e6c2c`  |
| 1433   | Layout 1             | `1d471f2e6c2c`  |
| 1430   | Layout 1             | `1d471f2e6c2c`  |
| 1426   | Layout 1             | `1d471f2e6c2c`  |
| 1421   | No documented layout | `1d471f2e6c2c`  |
| 1417   | No documented layout | `1d471f2e6c2c`  |
| 1416   | No documented layout | `1d471f2e6c2c`  |
| 1409   | No documented layout | `1d471f2e6c2c`  |
| 1405   | No documented layout | `1d471f2e6c2c`  |
| 1401   | No documented layout | `1d471f2e6c2c`  |
| 1396   | No documented layout | `1d471f2e6c2c`  |
| 1391   | No documented layout | `1d471f2e6c2c`  |
| 1390   | No documented layout | `1d471f2e6c2c`  |
| 1386   | No documented layout | `1d471f2e6c2c`  |
| 1381   | No documented layout | `1d471f2e6c2c`  |
| 1379   | No documented layout | `1d471f2e6c2c`  |
| 1372   | No documented layout | `1d471f2e6c2c`  |
| 1366   | No documented layout | `1d471f2e6c2c`  |
| 1364   | No documented layout | `1d471f2e6c2c`  |
| 1363   | No documented layout | `1d471f2e6c2c`  |
| 1360   | No documented layout | `1d471f2e6c2c`  |
| 1358   | No documented layout | `1d471f2e6c2c`  |
| 1355   | No documented layout | `1d471f2e6c2c`  |
| 1351   | No documented layout | `1d471f2e6c2c`  |
| 1348   | No documented layout | `1d471f2e6c2c`  |
| 1346   | No documented layout | `1d471f2e6c2c`  |
| 1341   | No documented layout | `1d471f2e6c2c`  |
| 1340   | No documented layout | `1d471f2e6c2c`  |
| 1338   | No documented layout | `1d471f2e6c2c`  |
| 1335   | No documented layout | `1d471f2e6c2c`  |
| 1333   | No documented layout | `1d471f2e6c2c`  |
| 1329   | No documented layout | `1d471f2e6c2c`  |
| 1327   | No documented layout | `1d471f2e6c2c`  |
| 1324   | No documented layout | `1d471f2e6c2c`  |
| 1321   | No documented layout | `1d471f2e6c2c`  |
| 1319   | No documented layout | `1d471f2e6c2c`  |
| 1318   | No documented layout | `1d471f2e6c2c`  |
| 1316   | No documented layout | `1d471f2e6c2c`  |
| 1313   | No documented layout | `1d471f2e6c2c`  |
| 1311   | No documented layout | `1d471f2e6c2c`  |
| 1309   | No documented layout | `1d471f2e6c2c`  |
| 1304   | No documented layout | `1d471f2e6c2c`  |
| 1292   | No documented layout | `1d471f2e6c2c`  |
| 1286   | No documented layout | `1d471f2e6c2c`  |
| 1280   | No documented layout | `1d471f2e6c2c`  |
| 1276   | No documented layout | `1d471f2e6c2c`  |
| 1267   | No documented layout | `1d471f2e6c2c`  |
| 1261   | No documented layout | `1d471f2e6c2c`  |
| 1256   | No documented layout | `1d471f2e6c2c`  |
| 1250   | No file              | `1d471f2e6c2c`  |
| 1246   | No file              | `1d471f2e6c2c`  |
| 1239   | No file              | `1d471f2e6c2c`  |
| 1230   | No file              | `1d471f2e6c2c`  |
| 1226   | No file              | `1d471f2e6c2c`  |
| 1220   | No file              | `1d471f2e6c2c`  |
| 1217   | No file              | `1d471f2e6c2c`  |
| 1211   | No file              | `1d471f2e6c2c`  |
| 1210   | No file              | `1d471f2e6c2c`  |
| 1208   | No file              | `1d471f2e6c2c`  |
| 1203   | No file              | `1d471f2e6c2c`  |
| 1197   | No file              | `1d471f2e6c2c`  |
| 1194   | No file              | `1d471f2e6c2c`  |
| 1192   | No file              | `1d471f2e6c2c`  |
| 1187   | No file              | `1d471f2e6c2c`  |
| 1183   | No file              | `1d471f2e6c2c`  |
| 1177   | No file              | `1d471f2e6c2c`  |
| 1173   | No file              | `1d471f2e6c2c`  |
| 1167   | No file              | `1d471f2e6c2c`  |
| 1164   | No file              | `1d471f2e6c2c`  |
| 1156   | No file              | `1d471f2e6c2c`  |
| 1149   | No file              | `1d471f2e6c2c`  |
| 1144   | No file              | `1d471f2e6c2c`  |
| 1137   | No file              | `1d471f2e6c2c`  |
| 1132   | No file              | `1d471f2e6c2c`  |
| 1127   | No file              | `1d471f2e6c2c`  |
| 1122   | No file              | `1d471f2e6c2c`  |
| 1118   | No file              | `1d471f2e6c2c`  |
| 1114   | No file              | `1d471f2e6c2c`  |
| 1109   | No file              | `1d471f2e6c2c`  |
| 1102   | No file              | `1d471f2e6c2c`  |
| 1096   | No file              | `1d471f2e6c2c`  |
| 1088   | No file              | `1d471f2e6c2c`  |
| 1081   | No file              | `1d471f2e6c2c`  |
| 1076   | No file              | `1d471f2e6c2c`  |
| 1069   | No file              | `1d471f2e6c2c`  |
| 1064   | No file              | `1d471f2e6c2c`  |
| 1058   | No file              | `1d471f2e6c2c`  |
| 1051   | No file              | `1d471f2e6c2c`  |
| 1044   | No file              | `1d471f2e6c2c`  |
| 1036   | No file              | `1d471f2e6c2c`  |
| 1026   | No file              | `1d471f2e6c2c`  |
| 1016   | No file              | `1d471f2e6c2c`  |
| 1009   | No file              | `1d471f2e6c2c`  |
| 1005   | No file              | `1d471f2e6c2c`  |
| 1000   | No file              | `1d471f2e6c2c`  |
| 998    | No file              | `1d471f2e6c2c`  |
| 990    | No file              | `1d471f2e6c2c`  |
| 979    | No file              | `1d471f2e6c2c`  |
| 972    | No file              | `1d471f2e6c2c`  |
| 963    | No file              | `1d471f2e6c2c`  |
| 955    | No file              | `1d471f2e6c2c`  |
| 946    | No file              | `1d471f2e6c2c`  |
| 938    | No file              | `1d471f2e6c2c`  |
| 927    | No file              | `1d471f2e6c2c`  |
| 911    | No file              | `1d471f2e6c2c`  |
| 904    | No file              | `1d471f2e6c2c`  |
| 899    | No file              | `1d471f2e6c2c`  |
| 894    | No file              | `1d471f2e6c2c`  |
| 885    | No file              | `1d471f2e6c2c`  |
| 879    | No file              | `1d471f2e6c2c`  |
| 872    | No file              | `1d471f2e6c2c`  |
| 864    | No file              | `1d471f2e6c2c`  |
| 855    | No file              | `1d471f2e6c2c`  |
| 853    | No file              | `1d471f2e6c2c`  |
| 845    | No file              | `1d471f2e6c2c`  |
| 837    | No file              | `1d471f2e6c2c`  |
| 829    | No file              | `1d471f2e6c2c`  |
| 822    | No file              | `1d471f2e6c2c`  |
| 814    | No file              | `1d471f2e6c2c`  |
| 805    | No file              | `1d471f2e6c2c`  |
| 794    | No file              | `1d471f2e6c2c`  |
| 787    | No file              | `1d471f2e6c2c`  |
| 780    | No file              | `1d471f2e6c2c`  |
| 771    | No file              | `1d471f2e6c2c`  |
| 760    | No file              | `1d471f2e6c2c`  |
| 748    | No file              | `1d471f2e6c2c`  |
| 741    | No file              | `1d471f2e6c2c`  |
| 736    | No file              | `1d471f2e6c2c`  |
| 731    | No file              | `1d471f2e6c2c`  |
| 723    | No file              | `1d471f2e6c2c`  |
| 711    | No file              | `1d471f2e6c2c`  |
| 707    | No file              | `1d471f2e6c2c`  |
| 697    | No file              | `1d471f2e6c2c`  |
| 689    | No file              | `1d471f2e6c2c`  |
| 683    | No file              | `1d471f2e6c2c`  |
| 678    | No file              | `1d471f2e6c2c`  |
| 670    | No file              | `1d471f2e6c2c`  |
| 661    | No file              | `1d471f2e6c2c`  |
| 656    | No file              | `1d471f2e6c2c`  |
| 652    | No file              | `1d471f2e6c2c`  |
| 643    | No file              | `1d471f2e6c2c`  |
| 637    | No file              | `1d471f2e6c2c`  |
| 630    | No file              | `1d471f2e6c2c`  |
| 627    | No file              | `1d471f2e6c2c`  |
| 621    | No file              | `1d471f2e6c2c`  |
| 617    | No file              | `1d471f2e6c2c`  |
| 615    | No file              | `1d471f2e6c2c`  |
| 606    | No file              | `1d471f2e6c2c`  |
| 599    | No file              | `1d471f2e6c2c`  |
| 592    | No file              | `1d471f2e6c2c`  |
| 586    | No file              | `1d471f2e6c2c`  |
| 577    | No file              | `1d471f2e6c2c`  |
| 569    | No file              | `1d471f2e6c2c`  |
| 561    | No file              | `1d471f2e6c2c`  |
| 554    | No file              | `1d471f2e6c2c`  |
| 542    | No file              | `1d471f2e6c2c`  |
| 532    | No file              | `1d471f2e6c2c`  |
| 531    | No file              | `1d471f2e6c2c`  |
| 526    | No file              | `1d471f2e6c2c`  |
| 521    | No file              | `1d471f2e6c2c`  |
| 517    | No file              | `1d471f2e6c2c`  |
| 510    | No file              | `1d471f2e6c2c`  |
| 508    | No file              | `1d471f2e6c2c`  |
| 504    | No file              | `1d471f2e6c2c`  |
| 497    | No file              | `1d471f2e6c2c`  |
| 491    | No file              | `1d471f2e6c2c`  |
| 485    | No file              | `1d471f2e6c2c`  |
| 478    | No file              | `1d471f2e6c2c`  |
| 472    | No file              | `1d471f2e6c2c`  |
| 466    | No file              | `1d471f2e6c2c`  |
| 457    | No file              | `1d471f2e6c2c`  |
| 452    | No file              | `1d471f2e6c2c`  |
| 449    | No file              | `1d471f2e6c2c`  |
| 435    | No file              | `1d471f2e6c2c`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                 |
| --------------------- | -------- | -------------------------------------------------------------------- |
| `boss_spawnlevel.bss` | Optional | The boss character of each key, from its level 0 entry ([boss_spawnlevel](boss_spawnlevel_bss.md)) |
| `languagedata_en.loc` | Optional | LOC type 6 boss names                                                |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                              |
| ------------------- | -------------- | ------------ | -------------------------------------------------- |
| `+0x00`             | char[4]        | magic        | `PABR`                                             |
| `+0x04`             | u32            | row_count    | `6` on client 3464                                 |
| `+0x08`             | Row[row_count] | rows         | See Row                                            |
| `rows+0x00`         | String Table   | string_table | The string table is empty                          |
| `string_table+0x00` | u32            | table_start  | Where the rows end                                 |
| `string_table+0x04` | u32            | zero         |                                                    |

### Row (43 bytes)

| Offset  | Type     | Field       | Notes                                                                  |
| ------- | -------- | ----------- | ---------------------------------------------------------------------- |
| `+0x00` | u32      | key         | `BossSpawnKey`; `8, 5, 4, 3, 2, 1` in file order on client 3464        |
| `+0x04` | u32      | max_level   | `4` on every row; `boss_spawnlevel.bss` has 4 levels for every key     |
| `+0x08` | u32      | unknown_08  | `1` on every row                                                       |
| `+0x0C` | f32[3]   | position    | World position; the second value is the height                         |
| `+0x18` | u32      | range       | `ToClient_bossSpawnRange`; `500` (keys 5, 8) or `2000`                 |
| `+0x1C` | u32      | unknown_1c  | `11` on every row                                                      |
| `+0x20` | u8       | unknown_20  | `1` on every row                                                       |
| `+0x21` | u8       | unknown_21  | `0` on keys 5 and 8, `1` on the rest                                    |
| `+0x22` | bytes[4] | unknown_22  | Zero on every row                                                      |
| `+0x26` | u8       | unknown_26  | `1` on every row                                                       |
| `+0x27` | u8       | unknown_27  | Zero on every row                                                      |
| `+0x28` | u8       | unknown_28  | Same as `unknown_21` on every row                                      |
| `+0x29` | u8       | unknown_29  | `1` on every row                                                       |
| `+0x2A` | u8       | unknown_2a  | Zero on every row                                                      |

Keys, with the boss from `boss_spawnlevel.bss` (client 3464):

| Key | Boss              | Range |
| --- | ----------------- | ----- |
| 1   | Ferrid            | 2000  |
| 2   | Moghulis          | 2000  |
| 3   | Giant Mudster     | 2000  |
| 4   | Org               | 2000  |
| 5   | Khan              | 500   |
| 8   | Gumiho & Duoksini | 500   |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes |
| ------- | ------------------ | ------------ | ----- |
| `+0x00` | u32                | string_count | `0`   |
| `+0x04` | pstr[string_count] | strings      | Empty |

## Layout 1

On client 1784 the row ends after `unknown_27`: it is 40 bytes and has no
`unknown_28`, `unknown_29` or `unknown_2a`. Only the Row differs from
Layout 2.

### Row (40 bytes)

| Offset  | Type     | Field      | Notes                                                       |
| ------- | -------- | ---------- | ----------------------------------------------------------- |
| `+0x00` | u32      | key        | `4, 3, 2, 1` in file order on client 1784                   |
| `+0x04` | u32      | max_level  | `5` on key 4, `4` on the rest (client 1784)                 |
| `+0x08` | u32      | unknown_08 | `1` on every row (client 1784)                              |
| `+0x0C` | f32[3]   | position   |                                                             |
| `+0x18` | u32      | range      | `500` (key 4) or `1000` (client 1784)                       |
| `+0x1C` | u32      | unknown_1c | `8` on every row (client 1784)                              |
| `+0x20` | u8       | unknown_20 |                                                             |
| `+0x21` | u8       | unknown_21 | `0` on key 4, `1` on the rest (client 1784)                 |
| `+0x22` | bytes[4] | unknown_22 |                                                             |
| `+0x26` | u8       | unknown_26 |                                                             |
| `+0x27` | u8       | unknown_27 |                                                             |

The keys do not match the newer clients' keys: key 4 on client 1784 has the
position of key 5 on client 3473, and key 2 the position of key 1.

## Notes

- Key 3's position lies 621 units from the Field boss Giant Mudster's
  position in [`bossinfostaicstatusmanager.bss`](bossinfostaicstatusmanager_bss.md),
  and key 1's lies 14,870 units from the Dark Rift Ferrid. The file holds no
  character ID; the names come only through `boss_spawnlevel.bss`.
- Keys 5 (Khan) and 8 (Gumiho & Duoksini) differ from the rest in `range`,
  `unknown_21` and `unknown_28`; in `boss_spawnlevel.bss` they are also the
  two bosses whose two character IDs differ.
- The window also calls `ToClient_bossSpawnMaxCost(bossKey)` and
  `ToClient_bossSpawnMaxCount(bossKey)`; the matching fields are not known
  (see Open Questions).

## Open Questions

### Max Cost and Max Count

The window shows a cost and a count against `ToClient_bossSpawnMaxCost` and
`ToClient_bossSpawnMaxCount`. `unknown_08` (`1`) and `unknown_1c` (`11`) are
the two constant u32s left, but which is which, or whether either is, is not
known. The current values come from the server (`getCurrentCost()`,
`getCurrentCount()`).

### unknown_21 and unknown_28

`0` on Khan and Gumiho & Duoksini, `1` on the rest. The window also checks
`ToClient_IsEnterMirrorField()` and `ToClient_EnterOrLeaveGuildBossField()`,
so one of them may mark a boss fought in a separate field, but no Lua call
reads them by name.
