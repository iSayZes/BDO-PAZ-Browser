# `boss_spawnlevel.bss` Format

## Purpose

The difficulty levels of the Guild Boss Summon window
(`panel_guild_bosssummon_all`): per guild boss, one 21-byte entry per level
with the reward item, the window image and the boss character. The window
reads an entry through `ToClient_bossSpawnOptionWrapper(bossKey, level)`
(`getImagePath()`, `getItemEnchantKey()`). The boss key is the key of
[`boss_spawn.bss`](boss_spawn_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                  | Bytes | Records           | Row bytes |
| ------ | -------------- | ------- | --------------------- | ----- | ----------------- | --------- |
| 2      | 3412 and later | 3483    | `boss_spawnlevel.bss` | 1,070 | 24 Entry, 6 Group | 21        |
| 1      | 1280 to 3402   | 3402    | `boss_spawnlevel.bss` | 841   | 20 Entry, 5 Group | 19        |

| Layout | File                  | Known         | Unknown       |
| ------ | --------------------- | ------------- | ------------- |
| 2      | `boss_spawnlevel.bss` | 926 B (86.5%) | 144 B (13.5%) |
| 1      | `boss_spawnlevel.bss` | 721 B (85.7%) | 120 B (14.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `18a4c45b799f`  |
| 3482   | Layout 2             | `18a4c45b799f`  |
| 3474   | Layout 2             | `18a4c45b799f`  |
| 3473   | Layout 2             | `18a4c45b799f`  |
| 3464   | Layout 2             | `18a4c45b799f`  |
| 3458   | Layout 2             | `18a4c45b799f`  |
| 3454   | Layout 2             | `18a4c45b799f`  |
| 3444   | Layout 2             | `18a4c45b799f`  |
| 3435   | Layout 2             | `18a4c45b799f`  |
| 3426   | Layout 2             | `18a4c45b799f`  |
| 3418   | Layout 2             | `18a4c45b799f`  |
| 3412   | Layout 2             | `18a4c45b799f`  |
| 3402   | Layout 1             | `18a4c45b799f`  |
| 3396   | Layout 1             | `18a4c45b799f`  |
| 3387   | Layout 1             | `18a4c45b799f`  |
| 3381   | Layout 1             | `18a4c45b799f`  |
| 3373   | Layout 1             | `18a4c45b799f`  |
| 3364   | Layout 1             | `18a4c45b799f`  |
| 3356   | Layout 1             | `18a4c45b799f`  |
| 3349   | Layout 1             | `18a4c45b799f`  |
| 3342   | Layout 1             | `18a4c45b799f`  |
| 3335   | Layout 1             | `18a4c45b799f`  |
| 3326   | Layout 1             | `18a4c45b799f`  |
| 3321   | Layout 1             | `18a4c45b799f`  |
| 3314   | Layout 1             | `18a4c45b799f`  |
| 3303   | Layout 1             | `18a4c45b799f`  |
| 3302   | Layout 1             | `18a4c45b799f`  |
| 3293   | Layout 1             | `18a4c45b799f`  |
| 3283   | Layout 1             | `18a4c45b799f`  |
| 3275   | Layout 1             | `18a4c45b799f`  |
| 3267   | Layout 1             | `18a4c45b799f`  |
| 3258   | Layout 1             | `18a4c45b799f`  |
| 3251   | Layout 1             | `18a4c45b799f`  |
| 3242   | Layout 1             | `18a4c45b799f`  |
| 3235   | Layout 1             | `18a4c45b799f`  |
| 3229   | Layout 1             | `18a4c45b799f`  |
| 3212   | Layout 1             | `18a4c45b799f`  |
| 3203   | Layout 1             | `18a4c45b799f`  |
| 3193   | Layout 1             | `18a4c45b799f`  |
| 3186   | Layout 1             | `18a4c45b799f`  |
| 3177   | Layout 1             | `18a4c45b799f`  |
| 3169   | Layout 1             | `18a4c45b799f`  |
| 3158   | Layout 1             | `18a4c45b799f`  |
| 3151   | Layout 1             | `18a4c45b799f`  |
| 3144   | Layout 1             | `18a4c45b799f`  |
| 3133   | Layout 1             | `18a4c45b799f`  |
| 3125   | Layout 1             | `18a4c45b799f`  |
| 3118   | Layout 1             | `18a4c45b799f`  |
| 3111   | Layout 1             | `18a4c45b799f`  |
| 3103   | Layout 1             | `18a4c45b799f`  |
| 3095   | Layout 1             | `18a4c45b799f`  |
| 3086   | Layout 1             | `18a4c45b799f`  |
| 3072   | Layout 1             | `18a4c45b799f`  |
| 3062   | Layout 1             | `18a4c45b799f`  |
| 3052   | Layout 1             | `18a4c45b799f`  |
| 3045   | Layout 1             | `18a4c45b799f`  |
| 3037   | Layout 1             | `18a4c45b799f`  |
| 3030   | Layout 1             | `18a4c45b799f`  |
| 3021   | Layout 1             | `18a4c45b799f`  |
| 3012   | Layout 1             | `18a4c45b799f`  |
| 3002   | Layout 1             | `18a4c45b799f`  |
| 2995   | Layout 1             | `18a4c45b799f`  |
| 2987   | Layout 1             | `18a4c45b799f`  |
| 2978   | Layout 1             | `18a4c45b799f`  |
| 2970   | Layout 1             | `18a4c45b799f`  |
| 2959   | Layout 1             | `18a4c45b799f`  |
| 2951   | Layout 1             | `18a4c45b799f`  |
| 2942   | Layout 1             | `18a4c45b799f`  |
| 2935   | Layout 1             | `18a4c45b799f`  |
| 2932   | Layout 1             | `18a4c45b799f`  |
| 2923   | Layout 1             | `18a4c45b799f`  |
| 2919   | Layout 1             | `18a4c45b799f`  |
| 2907   | Layout 1             | `18a4c45b799f`  |
| 2900   | Layout 1             | `18a4c45b799f`  |
| 2891   | Layout 1             | `18a4c45b799f`  |
| 2882   | Layout 1             | `18a4c45b799f`  |
| 2872   | Layout 1             | `18a4c45b799f`  |
| 2863   | Layout 1             | `18a4c45b799f`  |
| 2855   | Layout 1             | `18a4c45b799f`  |
| 2849   | Layout 1             | `18a4c45b799f`  |
| 2844   | Layout 1             | `18a4c45b799f`  |
| 2834   | Layout 1             | `18a4c45b799f`  |
| 2825   | Layout 1             | `18a4c45b799f`  |
| 2819   | Layout 1             | `18a4c45b799f`  |
| 2811   | Layout 1             | `18a4c45b799f`  |
| 2803   | Layout 1             | `18a4c45b799f`  |
| 2794   | Layout 1             | `18a4c45b799f`  |
| 2783   | Layout 1             | `18a4c45b799f`  |
| 2774   | Layout 1             | `18a4c45b799f`  |
| 2765   | Layout 1             | `18a4c45b799f`  |
| 2756   | Layout 1             | `18a4c45b799f`  |
| 2750   | Layout 1             | `18a4c45b799f`  |
| 2743   | Layout 1             | `18a4c45b799f`  |
| 2736   | Layout 1             | `18a4c45b799f`  |
| 2726   | Layout 1             | `18a4c45b799f`  |
| 2717   | Layout 1             | `18a4c45b799f`  |
| 2709   | Layout 1             | `18a4c45b799f`  |
| 2703   | Layout 1             | `18a4c45b799f`  |
| 2695   | Layout 1             | `18a4c45b799f`  |
| 2684   | Layout 1             | `18a4c45b799f`  |
| 2672   | Layout 1             | `18a4c45b799f`  |
| 2665   | Layout 1             | `18a4c45b799f`  |
| 2657   | Layout 1             | `18a4c45b799f`  |
| 2649   | Layout 1             | `18a4c45b799f`  |
| 2644   | Layout 1             | `18a4c45b799f`  |
| 2637   | Layout 1             | `18a4c45b799f`  |
| 2629   | Layout 1             | `18a4c45b799f`  |
| 2619   | Layout 1             | `18a4c45b799f`  |
| 2612   | Layout 1             | `18a4c45b799f`  |
| 2606   | Layout 1             | `18a4c45b799f`  |
| 2602   | Layout 1             | `18a4c45b799f`  |
| 2601   | Layout 1             | `18a4c45b799f`  |
| 2592   | Layout 1             | `18a4c45b799f`  |
| 2583   | Layout 1             | `18a4c45b799f`  |
| 2575   | Layout 1             | `18a4c45b799f`  |
| 2567   | Layout 1             | `18a4c45b799f`  |
| 2560   | Layout 1             | `18a4c45b799f`  |
| 2553   | Layout 1             | `18a4c45b799f`  |
| 2545   | Layout 1             | `18a4c45b799f`  |
| 2538   | Layout 1             | `18a4c45b799f`  |
| 2529   | Layout 1             | `18a4c45b799f`  |
| 2519   | Layout 1             | `18a4c45b799f`  |
| 2513   | Layout 1             | `18a4c45b799f`  |
| 2510   | Layout 1             | `18a4c45b799f`  |
| 2507   | Layout 1             | `18a4c45b799f`  |
| 2503   | Layout 1             | `18a4c45b799f`  |
| 2498   | Layout 1             | `18a4c45b799f`  |
| 2492   | Layout 1             | `18a4c45b799f`  |
| 2487   | Layout 1             | `18a4c45b799f`  |
| 2480   | Layout 1             | `18a4c45b799f`  |
| 2474   | Layout 1             | `18a4c45b799f`  |
| 2468   | Layout 1             | `18a4c45b799f`  |
| 2460   | Layout 1             | `18a4c45b799f`  |
| 2453   | Layout 1             | `18a4c45b799f`  |
| 2444   | Layout 1             | `18a4c45b799f`  |
| 2438   | Layout 1             | `18a4c45b799f`  |
| 2434   | Layout 1             | `18a4c45b799f`  |
| 2429   | Layout 1             | `18a4c45b799f`  |
| 2421   | Layout 1             | `18a4c45b799f`  |
| 2414   | Layout 1             | `18a4c45b799f`  |
| 2407   | Layout 1             | `18a4c45b799f`  |
| 2401   | Layout 1             | `18a4c45b799f`  |
| 2397   | Layout 1             | `18a4c45b799f`  |
| 2393   | Layout 1             | `18a4c45b799f`  |
| 2384   | Layout 1             | `18a4c45b799f`  |
| 2378   | Layout 1             | `18a4c45b799f`  |
| 2372   | Layout 1             | `18a4c45b799f`  |
| 2358   | Layout 1             | `18a4c45b799f`  |
| 2352   | Layout 1             | `18a4c45b799f`  |
| 2347   | Layout 1             | `18a4c45b799f`  |
| 2343   | Layout 1             | `18a4c45b799f`  |
| 2335   | Layout 1             | `18a4c45b799f`  |
| 2327   | Layout 1             | `18a4c45b799f`  |
| 2324   | Layout 1             | `18a4c45b799f`  |
| 2319   | Layout 1             | `18a4c45b799f`  |
| 2313   | Layout 1             | `18a4c45b799f`  |
| 2308   | Layout 1             | `18a4c45b799f`  |
| 2302   | Layout 1             | `18a4c45b799f`  |
| 2295   | Layout 1             | `18a4c45b799f`  |
| 2290   | Layout 1             | `18a4c45b799f`  |
| 2284   | Layout 1             | `18a4c45b799f`  |
| 2276   | Layout 1             | `18a4c45b799f`  |
| 2269   | Layout 1             | `18a4c45b799f`  |
| 2259   | Layout 1             | `18a4c45b799f`  |
| 2250   | Layout 1             | `18a4c45b799f`  |
| 2243   | Layout 1             | `18a4c45b799f`  |
| 2235   | Layout 1             | `18a4c45b799f`  |
| 2229   | Layout 1             | `18a4c45b799f`  |
| 2224   | Layout 1             | `18a4c45b799f`  |
| 2218   | Layout 1             | `18a4c45b799f`  |
| 2215   | Layout 1             | `18a4c45b799f`  |
| 2207   | Layout 1             | `18a4c45b799f`  |
| 2203   | Layout 1             | `18a4c45b799f`  |
| 2196   | Layout 1             | `18a4c45b799f`  |
| 2192   | Layout 1             | `18a4c45b799f`  |
| 2189   | Layout 1             | `18a4c45b799f`  |
| 2183   | Layout 1             | `18a4c45b799f`  |
| 2179   | Layout 1             | `18a4c45b799f`  |
| 2171   | Layout 1             | `18a4c45b799f`  |
| 2163   | Layout 1             | `18a4c45b799f`  |
| 2156   | Layout 1             | `18a4c45b799f`  |
| 2151   | Layout 1             | `18a4c45b799f`  |
| 2147   | Layout 1             | `18a4c45b799f`  |
| 2142   | Layout 1             | `18a4c45b799f`  |
| 2138   | Layout 1             | `18a4c45b799f`  |
| 2134   | Layout 1             | `18a4c45b799f`  |
| 2130   | Layout 1             | `18a4c45b799f`  |
| 2122   | Layout 1             | `18a4c45b799f`  |
| 2107   | Layout 1             | `18a4c45b799f`  |
| 2098   | Layout 1             | `18a4c45b799f`  |
| 2089   | Layout 1             | `18a4c45b799f`  |
| 2081   | Layout 1             | `18a4c45b799f`  |
| 2073   | Layout 1             | `18a4c45b799f`  |
| 2067   | Layout 1             | `18a4c45b799f`  |
| 2063   | Layout 1             | `18a4c45b799f`  |
| 2059   | Layout 1             | `18a4c45b799f`  |
| 2052   | Layout 1             | `18a4c45b799f`  |
| 2044   | Layout 1             | `18a4c45b799f`  |
| 2039   | Layout 1             | `18a4c45b799f`  |
| 2032   | Layout 1             | `18a4c45b799f`  |
| 2025   | Layout 1             | `18a4c45b799f`  |
| 2011   | Layout 1             | `18a4c45b799f`  |
| 2005   | Layout 1             | `18a4c45b799f`  |
| 2000   | Layout 1             | `18a4c45b799f`  |
| 1996   | Layout 1             | `18a4c45b799f`  |
| 1991   | Layout 1             | `18a4c45b799f`  |
| 1985   | Layout 1             | `18a4c45b799f`  |
| 1980   | Layout 1             | `18a4c45b799f`  |
| 1969   | Layout 1             | `18a4c45b799f`  |
| 1964   | Layout 1             | `18a4c45b799f`  |
| 1958   | Layout 1             | `18a4c45b799f`  |
| 1950   | Layout 1             | `18a4c45b799f`  |
| 1945   | Layout 1             | `18a4c45b799f`  |
| 1937   | Layout 1             | `18a4c45b799f`  |
| 1933   | Layout 1             | `18a4c45b799f`  |
| 1927   | Layout 1             | `18a4c45b799f`  |
| 1921   | Layout 1             | `18a4c45b799f`  |
| 1914   | Layout 1             | `18a4c45b799f`  |
| 1908   | Layout 1             | `18a4c45b799f`  |
| 1897   | Layout 1             | `18a4c45b799f`  |
| 1892   | Layout 1             | `18a4c45b799f`  |
| 1886   | Layout 1             | `18a4c45b799f`  |
| 1881   | Layout 1             | `18a4c45b799f`  |
| 1871   | Layout 1             | `18a4c45b799f`  |
| 1866   | Layout 1             | `18a4c45b799f`  |
| 1862   | Layout 1             | `18a4c45b799f`  |
| 1854   | Layout 1             | `18a4c45b799f`  |
| 1846   | Layout 1             | `18a4c45b799f`  |
| 1838   | Layout 1             | `18a4c45b799f`  |
| 1832   | Layout 1             | `18a4c45b799f`  |
| 1826   | Layout 1             | `18a4c45b799f`  |
| 1822   | Layout 1             | `18a4c45b799f`  |
| 1818   | Layout 1             | `18a4c45b799f`  |
| 1804   | Layout 1             | `18a4c45b799f`  |
| 1794   | Layout 1             | `18a4c45b799f`  |
| 1790   | Layout 1             | `18a4c45b799f`  |
| 1784   | Layout 1             | `18a4c45b799f`  |
| 1774   | Layout 1             | `18a4c45b799f`  |
| 1771   | Layout 1             | `18a4c45b799f`  |
| 1762   | Layout 1             | `18a4c45b799f`  |
| 1759   | Layout 1             | `18a4c45b799f`  |
| 1754   | Layout 1             | `18a4c45b799f`  |
| 1749   | Layout 1             | `18a4c45b799f`  |
| 1743   | Layout 1             | `18a4c45b799f`  |
| 1737   | Layout 1             | `18a4c45b799f`  |
| 1731   | Layout 1             | `18a4c45b799f`  |
| 1725   | Layout 1             | `18a4c45b799f`  |
| 1717   | Layout 1             | `18a4c45b799f`  |
| 1710   | Layout 1             | `18a4c45b799f`  |
| 1704   | Layout 1             | `18a4c45b799f`  |
| 1698   | Layout 1             | `18a4c45b799f`  |
| 1690   | Layout 1             | `18a4c45b799f`  |
| 1685   | Layout 1             | `18a4c45b799f`  |
| 1680   | Layout 1             | `18a4c45b799f`  |
| 1674   | Layout 1             | `18a4c45b799f`  |
| 1668   | Layout 1             | `18a4c45b799f`  |
| 1659   | Layout 1             | `18a4c45b799f`  |
| 1649   | Layout 1             | `18a4c45b799f`  |
| 1642   | Layout 1             | `18a4c45b799f`  |
| 1636   | Layout 1             | `18a4c45b799f`  |
| 1628   | Layout 1             | `18a4c45b799f`  |
| 1622   | Layout 1             | `18a4c45b799f`  |
| 1614   | Layout 1             | `18a4c45b799f`  |
| 1608   | Layout 1             | `18a4c45b799f`  |
| 1602   | Layout 1             | `18a4c45b799f`  |
| 1598   | Layout 1             | `18a4c45b799f`  |
| 1594   | Layout 1             | `18a4c45b799f`  |
| 1590   | Layout 1             | `18a4c45b799f`  |
| 1587   | Layout 1             | `18a4c45b799f`  |
| 1584   | Layout 1             | `18a4c45b799f`  |
| 1579   | Layout 1             | `18a4c45b799f`  |
| 1572   | Layout 1             | `18a4c45b799f`  |
| 1565   | Layout 1             | `18a4c45b799f`  |
| 1559   | Layout 1             | `18a4c45b799f`  |
| 1554   | Layout 1             | `18a4c45b799f`  |
| 1547   | Layout 1             | `18a4c45b799f`  |
| 1537   | Layout 1             | `18a4c45b799f`  |
| 1529   | Layout 1             | `18a4c45b799f`  |
| 1524   | Layout 1             | `18a4c45b799f`  |
| 1519   | Layout 1             | `18a4c45b799f`  |
| 1509   | Layout 1             | `18a4c45b799f`  |
| 1506   | Layout 1             | `18a4c45b799f`  |
| 1504   | Layout 1             | `18a4c45b799f`  |
| 1500   | Layout 1             | `18a4c45b799f`  |
| 1493   | Layout 1             | `18a4c45b799f`  |
| 1489   | Layout 1             | `18a4c45b799f`  |
| 1485   | Layout 1             | `18a4c45b799f`  |
| 1481   | Layout 1             | `18a4c45b799f`  |
| 1474   | Layout 1             | `18a4c45b799f`  |
| 1466   | Layout 1             | `18a4c45b799f`  |
| 1462   | Layout 1             | `18a4c45b799f`  |
| 1459   | Layout 1             | `18a4c45b799f`  |
| 1453   | Layout 1             | `18a4c45b799f`  |
| 1450   | Layout 1             | `18a4c45b799f`  |
| 1445   | Layout 1             | `18a4c45b799f`  |
| 1439   | Layout 1             | `18a4c45b799f`  |
| 1433   | Layout 1             | `18a4c45b799f`  |
| 1430   | Layout 1             | `18a4c45b799f`  |
| 1426   | Layout 1             | `18a4c45b799f`  |
| 1421   | Layout 1             | `18a4c45b799f`  |
| 1417   | Layout 1             | `18a4c45b799f`  |
| 1416   | Layout 1             | `18a4c45b799f`  |
| 1409   | Layout 1             | `18a4c45b799f`  |
| 1405   | Layout 1             | `18a4c45b799f`  |
| 1401   | Layout 1             | `18a4c45b799f`  |
| 1396   | Layout 1             | `18a4c45b799f`  |
| 1391   | Layout 1             | `18a4c45b799f`  |
| 1390   | Layout 1             | `18a4c45b799f`  |
| 1386   | Layout 1             | `18a4c45b799f`  |
| 1381   | Layout 1             | `18a4c45b799f`  |
| 1379   | Layout 1             | `18a4c45b799f`  |
| 1372   | Layout 1             | `18a4c45b799f`  |
| 1366   | Layout 1             | `18a4c45b799f`  |
| 1364   | Layout 1             | `18a4c45b799f`  |
| 1363   | Layout 1             | `18a4c45b799f`  |
| 1360   | Layout 1             | `18a4c45b799f`  |
| 1358   | Layout 1             | `18a4c45b799f`  |
| 1355   | Layout 1             | `18a4c45b799f`  |
| 1351   | Layout 1             | `18a4c45b799f`  |
| 1348   | Layout 1             | `18a4c45b799f`  |
| 1346   | Layout 1             | `18a4c45b799f`  |
| 1341   | Layout 1             | `18a4c45b799f`  |
| 1340   | Layout 1             | `18a4c45b799f`  |
| 1338   | Layout 1             | `18a4c45b799f`  |
| 1335   | Layout 1             | `18a4c45b799f`  |
| 1333   | Layout 1             | `18a4c45b799f`  |
| 1329   | Layout 1             | `18a4c45b799f`  |
| 1327   | Layout 1             | `18a4c45b799f`  |
| 1324   | Layout 1             | `18a4c45b799f`  |
| 1321   | Layout 1             | `18a4c45b799f`  |
| 1319   | Layout 1             | `18a4c45b799f`  |
| 1318   | Layout 1             | `18a4c45b799f`  |
| 1316   | Layout 1             | `18a4c45b799f`  |
| 1313   | Layout 1             | `18a4c45b799f`  |
| 1311   | Layout 1             | `18a4c45b799f`  |
| 1309   | Layout 1             | `18a4c45b799f`  |
| 1304   | Layout 1             | `18a4c45b799f`  |
| 1292   | Layout 1             | `18a4c45b799f`  |
| 1286   | Layout 1             | `18a4c45b799f`  |
| 1280   | Layout 1             | `18a4c45b799f`  |
| 1276   | No documented layout | `18a4c45b799f`  |
| 1267   | No documented layout | `18a4c45b799f`  |
| 1261   | No documented layout | `18a4c45b799f`  |
| 1256   | No documented layout | `18a4c45b799f`  |
| 1250   | No file              | `18a4c45b799f`  |
| 1246   | No file              | `18a4c45b799f`  |
| 1239   | No file              | `18a4c45b799f`  |
| 1230   | No file              | `18a4c45b799f`  |
| 1226   | No file              | `18a4c45b799f`  |
| 1220   | No file              | `18a4c45b799f`  |
| 1217   | No file              | `18a4c45b799f`  |
| 1211   | No file              | `18a4c45b799f`  |
| 1210   | No file              | `18a4c45b799f`  |
| 1208   | No file              | `18a4c45b799f`  |
| 1203   | No file              | `18a4c45b799f`  |
| 1197   | No file              | `18a4c45b799f`  |
| 1194   | No file              | `18a4c45b799f`  |
| 1192   | No file              | `18a4c45b799f`  |
| 1187   | No file              | `18a4c45b799f`  |
| 1183   | No file              | `18a4c45b799f`  |
| 1177   | No file              | `18a4c45b799f`  |
| 1173   | No file              | `18a4c45b799f`  |
| 1167   | No file              | `18a4c45b799f`  |
| 1164   | No file              | `18a4c45b799f`  |
| 1156   | No file              | `18a4c45b799f`  |
| 1149   | No file              | `18a4c45b799f`  |
| 1144   | No file              | `18a4c45b799f`  |
| 1137   | No file              | `18a4c45b799f`  |
| 1132   | No file              | `18a4c45b799f`  |
| 1127   | No file              | `18a4c45b799f`  |
| 1122   | No file              | `18a4c45b799f`  |
| 1118   | No file              | `18a4c45b799f`  |
| 1114   | No file              | `18a4c45b799f`  |
| 1109   | No file              | `18a4c45b799f`  |
| 1102   | No file              | `18a4c45b799f`  |
| 1096   | No file              | `18a4c45b799f`  |
| 1088   | No file              | `18a4c45b799f`  |
| 1081   | No file              | `18a4c45b799f`  |
| 1076   | No file              | `18a4c45b799f`  |
| 1069   | No file              | `18a4c45b799f`  |
| 1064   | No file              | `18a4c45b799f`  |
| 1058   | No file              | `18a4c45b799f`  |
| 1051   | No file              | `18a4c45b799f`  |
| 1044   | No file              | `18a4c45b799f`  |
| 1036   | No file              | `18a4c45b799f`  |
| 1026   | No file              | `18a4c45b799f`  |
| 1016   | No file              | `18a4c45b799f`  |
| 1009   | No file              | `18a4c45b799f`  |
| 1005   | No file              | `18a4c45b799f`  |
| 1000   | No file              | `18a4c45b799f`  |
| 998    | No file              | `18a4c45b799f`  |
| 990    | No file              | `18a4c45b799f`  |
| 979    | No file              | `18a4c45b799f`  |
| 972    | No file              | `18a4c45b799f`  |
| 963    | No file              | `18a4c45b799f`  |
| 955    | No file              | `18a4c45b799f`  |
| 946    | No file              | `18a4c45b799f`  |
| 938    | No file              | `18a4c45b799f`  |
| 927    | No file              | `18a4c45b799f`  |
| 911    | No file              | `18a4c45b799f`  |
| 904    | No file              | `18a4c45b799f`  |
| 899    | No file              | `18a4c45b799f`  |
| 894    | No file              | `18a4c45b799f`  |
| 885    | No file              | `18a4c45b799f`  |
| 879    | No file              | `18a4c45b799f`  |
| 872    | No file              | `18a4c45b799f`  |
| 864    | No file              | `18a4c45b799f`  |
| 855    | No file              | `18a4c45b799f`  |
| 853    | No file              | `18a4c45b799f`  |
| 845    | No file              | `18a4c45b799f`  |
| 837    | No file              | `18a4c45b799f`  |
| 829    | No file              | `18a4c45b799f`  |
| 822    | No file              | `18a4c45b799f`  |
| 814    | No file              | `18a4c45b799f`  |
| 805    | No file              | `18a4c45b799f`  |
| 794    | No file              | `18a4c45b799f`  |
| 787    | No file              | `18a4c45b799f`  |
| 780    | No file              | `18a4c45b799f`  |
| 771    | No file              | `18a4c45b799f`  |
| 760    | No file              | `18a4c45b799f`  |
| 748    | No file              | `18a4c45b799f`  |
| 741    | No file              | `18a4c45b799f`  |
| 736    | No file              | `18a4c45b799f`  |
| 731    | No file              | `18a4c45b799f`  |
| 723    | No file              | `18a4c45b799f`  |
| 711    | No file              | `18a4c45b799f`  |
| 707    | No file              | `18a4c45b799f`  |
| 697    | No file              | `18a4c45b799f`  |
| 689    | No file              | `18a4c45b799f`  |
| 683    | No file              | `18a4c45b799f`  |
| 678    | No file              | `18a4c45b799f`  |
| 670    | No file              | `18a4c45b799f`  |
| 661    | No file              | `18a4c45b799f`  |
| 656    | No file              | `18a4c45b799f`  |
| 652    | No file              | `18a4c45b799f`  |
| 643    | No file              | `18a4c45b799f`  |
| 637    | No file              | `18a4c45b799f`  |
| 630    | No file              | `18a4c45b799f`  |
| 627    | No file              | `18a4c45b799f`  |
| 621    | No file              | `18a4c45b799f`  |
| 617    | No file              | `18a4c45b799f`  |
| 615    | No file              | `18a4c45b799f`  |
| 606    | No file              | `18a4c45b799f`  |
| 599    | No file              | `18a4c45b799f`  |
| 592    | No file              | `18a4c45b799f`  |
| 586    | No file              | `18a4c45b799f`  |
| 577    | No file              | `18a4c45b799f`  |
| 569    | No file              | `18a4c45b799f`  |
| 561    | No file              | `18a4c45b799f`  |
| 554    | No file              | `18a4c45b799f`  |
| 542    | No file              | `18a4c45b799f`  |
| 532    | No file              | `18a4c45b799f`  |
| 531    | No file              | `18a4c45b799f`  |
| 526    | No file              | `18a4c45b799f`  |
| 521    | No file              | `18a4c45b799f`  |
| 517    | No file              | `18a4c45b799f`  |
| 510    | No file              | `18a4c45b799f`  |
| 508    | No file              | `18a4c45b799f`  |
| 504    | No file              | `18a4c45b799f`  |
| 497    | No file              | `18a4c45b799f`  |
| 491    | No file              | `18a4c45b799f`  |
| 485    | No file              | `18a4c45b799f`  |
| 478    | No file              | `18a4c45b799f`  |
| 472    | No file              | `18a4c45b799f`  |
| 466    | No file              | `18a4c45b799f`  |
| 457    | No file              | `18a4c45b799f`  |
| 452    | No file              | `18a4c45b799f`  |
| 449    | No file              | `18a4c45b799f`  |
| 435    | No file              | `18a4c45b799f`  |

<!-- versions:end -->

## Companion Files

None. Character names come from LOC type 6, reward names from LOC type 0.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type               | Field        | Notes                                                      |
| ------------------- | ------------------ | ------------ | ---------------------------------------------------------- |
| `+0x00`             | char[4]            | magic        | `PABR`                                                     |
| `+0x04`             | u32                | group_count  | `6` on client 3464, one group per boss                     |
| `+0x08`             | Group[group_count] | groups       | Variable size; the last ends where the string table starts |
| `groups+0x00`       | String Table       | string_table | Counted string table (`_common/pabr_strings.py`), UTF-16 image paths |
| `string_table+0x00` | u32                | table_start  | Offset of the string table                                 |
| `string_table+0x04` | u32                | zero         |                                                            |

### Group (variable: 4 bytes + entries)

| Offset  | Type                 | Field       | Notes              |
| ------- | -------------------- | ----------- | ------------------ |
| `+0x00` | u32                  | entry_count | `4` on every group |
| `+0x04` | Entry[entry_count]   | entries     | See Entry          |

### Entry (21 bytes)

| Offset  | Type | Field          | Notes                                                                  |
| ------- | ---- | -------------- | ---------------------------------------------------------------------- |
| `+0x00` | u32  | boss_key       | `boss_spawn.bss` key; the same on every entry of a group               |
| `+0x04` | u8   | level          | `0` to `3`, the second argument of `ToClient_bossSpawnOptionWrapper`   |
| `+0x05` | u16  | unknown_05     | `1` on every entry                                                     |
| `+0x07` | u16  | unknown_07     | Falls by 1 per level within a group (65308 to 65305 for Ferrid); see Open Questions |
| `+0x09` | u32  | reward_item_id | `getItemEnchantKey()`: the boss's Small, Medium, Large and Extra Large Reward |
| `+0x0D` | u32  | image          | String index: `getImagePath()`, relative to `ui_texture/`              |
| `+0x11` | u16  | unknown_11     | A character ID; equals `character_id` except on Khan and Gumiho & Duoksini |
| `+0x13` | u16  | character_id   | The boss character, LOC type 6                                        |

The groups on client 3464:

| Key | Boss              | character_id (levels 0 to 3) | Rewards          |
| --- | ----------------- | ---------------------------- | ---------------- |
| 1   | Ferrid            | 28856 to 28853               | 756210 to 756213 |
| 2   | Moghulis          | 29700 to 29697               | 756214 to 756217 |
| 3   | Giant Mudster     | 28852 to 28849               | 756206 to 756209 |
| 4   | Org               | 29696 to 29693               | 756275 to 756278 |
| 5   | Khan              | 23843 to 23840               | 756218 to 756221 |
| 8   | Gumiho & Duoksini | 27897, 27895, 27894, 29539   | 790880, 790877, 790878, 790879 |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                  |
| ------- | ------------------ | ------------ | -------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings                      |
| `+0x04` | pstr[string_count] | strings      | Image paths; `image` indexes this list |

## Layout 1

On client 1784 the entry ends after `unknown_11`: it is 19 bytes and has no
`character_id`. Only the Entry differs from Layout 2.

### Entry (19 bytes)

| Offset  | Type | Field          | Notes                                                              |
| ------- | ---- | -------------- | ------------------------------------------------------------------ |
| `+0x00` | u32  | boss_key       |                                                                    |
| `+0x04` | u8   | level          |                                                                    |
| `+0x05` | u16  | unknown_05     |                                                                    |
| `+0x07` | u16  | unknown_07     |                                                                    |
| `+0x09` | u32  | reward_item_id |                                                                    |
| `+0x0D` | u32  | image          |                                                                    |
| `+0x11` | u16  | unknown_11     | Key 4 holds 27198, 27197, 27196 and 27186, the Khan values of `unknown_11` on client 3473 |

Client 1784 has 4 groups (keys 1 to 4) of 4 entries.

## Notes

- `unknown_11` on Khan is 27198, 27197, 27196 and 27186, a "Khan" with the model
  `monster/partyleader/ocean_bellj_boss_ghost`, while `character_id` is the
  Khan of `monster/m0423_ocean_boss_junior_boss`. On Gumiho & Duoksini
  `unknown_11` is the `monster/guildraidboss/mainreward_guildraid` character
  and `character_id` the nine-tailed fox (`m0498_ninetailedfox_guildraid`).
- The string table has one image per group, in group order; the client
  ships more `GuildBoss_Renewal_*` images (`Gamos`) than the file uses.
- The window prints the level with `LUA_GUILD_BOSSSUMON_DIFFICULTYCOUNT`.

## Open Questions

### unknown_07

Two runs of values: 65301 to 65316 on Ferrid, Giant Mudster and Khan, and
62810 to 62856 on Moghulis, Org and Gumiho & Duoksini, falling by 1 per
level. They are not character IDs or `guildquest.dbss` keys, and the four
checked in LOC (65308, 62856, 65316, 62813) only match unrelated type 0
item names.

### unknown_11

A character ID that equals `character_id` on four of the six bosses. On
Khan and Gumiho & Duoksini it is a different character (a party leader
ghost, a main reward object), which may be the character the summon places
first, but no Lua call names it.
