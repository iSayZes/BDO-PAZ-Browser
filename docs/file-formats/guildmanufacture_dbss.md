# `guildmanufacture.dbss` Format

## Purpose

The Guild Crafting recipes: one row per product item a guild can craft in
the Guild Crafting window, with its `itemexchangesource.bss` key, the six
required item slots and their counts, the product window category, the guild
houses that can craft it and the guild skill it needs. The client Lua reads
a row through `ToClient_GetGuildManufactureStaticStatusWrapper(itemEnchantKey)`
with the product item key. `guildmanufactureoffset.dbss` is the index into
it, keyed by the product item key.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                          | Bytes | Records       | Row bytes                  |
| ------ | -------------- | ----------------------------- | ----- | ------------- | -------------------------- |
| 2      | 2726 and later | `guildmanufacture.dbss`       | 2,120 | 16 Row        | 125 to 163, 132 on average |
| 2      | 2726 and later | `guildmanufactureoffset.dbss` | 196   | 16 Offset Row | 12                         |
| 1      | 1346 to 2717   | `guildmanufacture.dbss`       | 2,612 | 20 Row        | 123 to 161, 130 on average |
| 1      | 1346 to 2717   | `guildmanufactureoffset.dbss` | 244   | 20 Offset Row | 12                         |

| Layout | File                          | Known            | Unknown    |
| ------ | ----------------------------- | ---------------- | ---------- |
| 2      | `guildmanufacture.dbss`       | 2,120 B (100.0%) | 0 B (0.0%) |
| 2      | `guildmanufactureoffset.dbss` | 196 B (100.0%)   | 0 B (0.0%) |
| 1      | `guildmanufacture.dbss`       | 2,612 B (100.0%) | 0 B (0.0%) |
| 1      | `guildmanufactureoffset.dbss` | 244 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `62dac76d680e`  |
| 3482   | Layout 2             | `62dac76d680e`  |
| 3474   | Layout 2             | `62dac76d680e`  |
| 3473   | Layout 2             | `62dac76d680e`  |
| 3464   | Layout 2             | `62dac76d680e`  |
| 3458   | Layout 2             | `62dac76d680e`  |
| 3454   | Layout 2             | `62dac76d680e`  |
| 3444   | Layout 2             | `62dac76d680e`  |
| 3435   | Layout 2             | `62dac76d680e`  |
| 3426   | Layout 2             | `62dac76d680e`  |
| 3418   | Layout 2             | `62dac76d680e`  |
| 3412   | Layout 2             | `62dac76d680e`  |
| 3402   | Layout 2             | `62dac76d680e`  |
| 3396   | Layout 2             | `62dac76d680e`  |
| 3387   | Layout 2             | `62dac76d680e`  |
| 3381   | Layout 2             | `62dac76d680e`  |
| 3373   | Layout 2             | `62dac76d680e`  |
| 3364   | Layout 2             | `62dac76d680e`  |
| 3356   | Layout 2             | `62dac76d680e`  |
| 3349   | Layout 2             | `62dac76d680e`  |
| 3342   | Layout 2             | `62dac76d680e`  |
| 3335   | Layout 2             | `62dac76d680e`  |
| 3326   | Layout 2             | `62dac76d680e`  |
| 3321   | Layout 2             | `62dac76d680e`  |
| 3314   | Layout 2             | `62dac76d680e`  |
| 3303   | Layout 2             | `62dac76d680e`  |
| 3302   | Layout 2             | `62dac76d680e`  |
| 3293   | Layout 2             | `62dac76d680e`  |
| 3283   | Layout 2             | `62dac76d680e`  |
| 3275   | Layout 2             | `62dac76d680e`  |
| 3267   | Layout 2             | `62dac76d680e`  |
| 3258   | Layout 2             | `62dac76d680e`  |
| 3251   | Layout 2             | `62dac76d680e`  |
| 3242   | Layout 2             | `62dac76d680e`  |
| 3235   | Layout 2             | `62dac76d680e`  |
| 3229   | Layout 2             | `62dac76d680e`  |
| 3212   | Layout 2             | `62dac76d680e`  |
| 3203   | Layout 2             | `62dac76d680e`  |
| 3193   | Layout 2             | `62dac76d680e`  |
| 3186   | Layout 2             | `62dac76d680e`  |
| 3177   | Layout 2             | `62dac76d680e`  |
| 3169   | Layout 2             | `62dac76d680e`  |
| 3158   | Layout 2             | `62dac76d680e`  |
| 3151   | Layout 2             | `62dac76d680e`  |
| 3144   | Layout 2             | `62dac76d680e`  |
| 3133   | Layout 2             | `62dac76d680e`  |
| 3125   | Layout 2             | `62dac76d680e`  |
| 3118   | Layout 2             | `62dac76d680e`  |
| 3111   | Layout 2             | `62dac76d680e`  |
| 3103   | Layout 2             | `62dac76d680e`  |
| 3095   | Layout 2             | `62dac76d680e`  |
| 3086   | Layout 2             | `62dac76d680e`  |
| 3072   | Layout 2             | `62dac76d680e`  |
| 3062   | Layout 2             | `62dac76d680e`  |
| 3052   | Layout 2             | `62dac76d680e`  |
| 3045   | Layout 2             | `62dac76d680e`  |
| 3037   | Layout 2             | `62dac76d680e`  |
| 3030   | Layout 2             | `62dac76d680e`  |
| 3021   | Layout 2             | `62dac76d680e`  |
| 3012   | Layout 2             | `62dac76d680e`  |
| 3002   | Layout 2             | `62dac76d680e`  |
| 2995   | Layout 2             | `62dac76d680e`  |
| 2987   | Layout 2             | `62dac76d680e`  |
| 2978   | Layout 2             | `62dac76d680e`  |
| 2970   | Layout 2             | `62dac76d680e`  |
| 2959   | Layout 2             | `62dac76d680e`  |
| 2951   | Layout 2             | `62dac76d680e`  |
| 2942   | Layout 2             | `62dac76d680e`  |
| 2935   | Layout 2             | `62dac76d680e`  |
| 2932   | Layout 2             | `62dac76d680e`  |
| 2923   | Layout 2             | `62dac76d680e`  |
| 2919   | Layout 2             | `62dac76d680e`  |
| 2907   | Layout 2             | `62dac76d680e`  |
| 2900   | Layout 2             | `62dac76d680e`  |
| 2891   | Layout 2             | `62dac76d680e`  |
| 2882   | Layout 2             | `62dac76d680e`  |
| 2872   | Layout 2             | `62dac76d680e`  |
| 2863   | Layout 2             | `62dac76d680e`  |
| 2855   | Layout 2             | `62dac76d680e`  |
| 2849   | Layout 2             | `62dac76d680e`  |
| 2844   | Layout 2             | `62dac76d680e`  |
| 2834   | Layout 2             | `62dac76d680e`  |
| 2825   | Layout 2             | `62dac76d680e`  |
| 2819   | Layout 2             | `62dac76d680e`  |
| 2811   | Layout 2             | `62dac76d680e`  |
| 2803   | Layout 2             | `62dac76d680e`  |
| 2794   | Layout 2             | `62dac76d680e`  |
| 2783   | Layout 2             | `62dac76d680e`  |
| 2774   | Layout 2             | `62dac76d680e`  |
| 2765   | Layout 2             | `62dac76d680e`  |
| 2756   | Layout 2             | `62dac76d680e`  |
| 2750   | Layout 2             | `62dac76d680e`  |
| 2743   | Layout 2             | `62dac76d680e`  |
| 2736   | Layout 2             | `62dac76d680e`  |
| 2726   | Layout 2             | `62dac76d680e`  |
| 2717   | Layout 1             | `62dac76d680e`  |
| 2709   | Layout 1             | `62dac76d680e`  |
| 2703   | Layout 1             | `62dac76d680e`  |
| 2695   | Layout 1             | `62dac76d680e`  |
| 2684   | Layout 1             | `62dac76d680e`  |
| 2672   | Layout 1             | `62dac76d680e`  |
| 2665   | Layout 1             | `62dac76d680e`  |
| 2657   | Layout 1             | `62dac76d680e`  |
| 2649   | Layout 1             | `62dac76d680e`  |
| 2644   | Layout 1             | `62dac76d680e`  |
| 2637   | Layout 1             | `62dac76d680e`  |
| 2629   | Layout 1             | `62dac76d680e`  |
| 2619   | Layout 1             | `62dac76d680e`  |
| 2612   | Layout 1             | `62dac76d680e`  |
| 2606   | Layout 1             | `62dac76d680e`  |
| 2602   | Layout 1             | `62dac76d680e`  |
| 2601   | Layout 1             | `62dac76d680e`  |
| 2592   | Layout 1             | `62dac76d680e`  |
| 2583   | Layout 1             | `62dac76d680e`  |
| 2575   | Layout 1             | `62dac76d680e`  |
| 2567   | Layout 1             | `62dac76d680e`  |
| 2560   | Layout 1             | `62dac76d680e`  |
| 2553   | Layout 1             | `62dac76d680e`  |
| 2545   | Layout 1             | `62dac76d680e`  |
| 2538   | Layout 1             | `62dac76d680e`  |
| 2529   | Layout 1             | `62dac76d680e`  |
| 2519   | Layout 1             | `62dac76d680e`  |
| 2513   | Layout 1             | `62dac76d680e`  |
| 2510   | Layout 1             | `62dac76d680e`  |
| 2507   | Layout 1             | `62dac76d680e`  |
| 2503   | Layout 1             | `62dac76d680e`  |
| 2498   | Layout 1             | `62dac76d680e`  |
| 2492   | Layout 1             | `62dac76d680e`  |
| 2487   | Layout 1             | `62dac76d680e`  |
| 2480   | Layout 1             | `62dac76d680e`  |
| 2474   | Layout 1             | `62dac76d680e`  |
| 2468   | Layout 1             | `62dac76d680e`  |
| 2460   | Layout 1             | `62dac76d680e`  |
| 2453   | Layout 1             | `62dac76d680e`  |
| 2444   | Layout 1             | `62dac76d680e`  |
| 2438   | Layout 1             | `62dac76d680e`  |
| 2434   | Layout 1             | `62dac76d680e`  |
| 2429   | Layout 1             | `62dac76d680e`  |
| 2421   | Layout 1             | `62dac76d680e`  |
| 2414   | Layout 1             | `62dac76d680e`  |
| 2407   | Layout 1             | `62dac76d680e`  |
| 2401   | Layout 1             | `62dac76d680e`  |
| 2397   | Layout 1             | `62dac76d680e`  |
| 2393   | Layout 1             | `62dac76d680e`  |
| 2384   | Layout 1             | `62dac76d680e`  |
| 2378   | Layout 1             | `62dac76d680e`  |
| 2372   | Layout 1             | `62dac76d680e`  |
| 2358   | Layout 1             | `62dac76d680e`  |
| 2352   | Layout 1             | `62dac76d680e`  |
| 2347   | Layout 1             | `62dac76d680e`  |
| 2343   | Layout 1             | `62dac76d680e`  |
| 2335   | Layout 1             | `62dac76d680e`  |
| 2327   | Layout 1             | `62dac76d680e`  |
| 2324   | Layout 1             | `62dac76d680e`  |
| 2319   | Layout 1             | `62dac76d680e`  |
| 2313   | Layout 1             | `62dac76d680e`  |
| 2308   | Layout 1             | `62dac76d680e`  |
| 2302   | Layout 1             | `62dac76d680e`  |
| 2295   | Layout 1             | `62dac76d680e`  |
| 2290   | Layout 1             | `62dac76d680e`  |
| 2284   | Layout 1             | `62dac76d680e`  |
| 2276   | Layout 1             | `62dac76d680e`  |
| 2269   | Layout 1             | `62dac76d680e`  |
| 2259   | Layout 1             | `62dac76d680e`  |
| 2250   | Layout 1             | `62dac76d680e`  |
| 2243   | Layout 1             | `62dac76d680e`  |
| 2235   | Layout 1             | `62dac76d680e`  |
| 2229   | Layout 1             | `62dac76d680e`  |
| 2224   | Layout 1             | `62dac76d680e`  |
| 2218   | Layout 1             | `62dac76d680e`  |
| 2215   | Layout 1             | `62dac76d680e`  |
| 2207   | Layout 1             | `62dac76d680e`  |
| 2203   | Layout 1             | `62dac76d680e`  |
| 2196   | Layout 1             | `62dac76d680e`  |
| 2192   | Layout 1             | `62dac76d680e`  |
| 2189   | Layout 1             | `62dac76d680e`  |
| 2183   | Layout 1             | `62dac76d680e`  |
| 2179   | Layout 1             | `62dac76d680e`  |
| 2171   | Layout 1             | `62dac76d680e`  |
| 2163   | Layout 1             | `62dac76d680e`  |
| 2156   | Layout 1             | `62dac76d680e`  |
| 2151   | Layout 1             | `62dac76d680e`  |
| 2147   | Layout 1             | `62dac76d680e`  |
| 2142   | Layout 1             | `62dac76d680e`  |
| 2138   | Layout 1             | `62dac76d680e`  |
| 2134   | Layout 1             | `62dac76d680e`  |
| 2130   | Layout 1             | `62dac76d680e`  |
| 2122   | Layout 1             | `62dac76d680e`  |
| 2107   | Layout 1             | `62dac76d680e`  |
| 2098   | Layout 1             | `62dac76d680e`  |
| 2089   | Layout 1             | `62dac76d680e`  |
| 2081   | Layout 1             | `62dac76d680e`  |
| 2073   | Layout 1             | `62dac76d680e`  |
| 2067   | Layout 1             | `62dac76d680e`  |
| 2063   | Layout 1             | `62dac76d680e`  |
| 2059   | Layout 1             | `62dac76d680e`  |
| 2052   | Layout 1             | `62dac76d680e`  |
| 2044   | Layout 1             | `62dac76d680e`  |
| 2039   | Layout 1             | `62dac76d680e`  |
| 2032   | Layout 1             | `62dac76d680e`  |
| 2025   | Layout 1             | `62dac76d680e`  |
| 2011   | Layout 1             | `62dac76d680e`  |
| 2005   | Layout 1             | `62dac76d680e`  |
| 2000   | Layout 1             | `62dac76d680e`  |
| 1996   | Layout 1             | `62dac76d680e`  |
| 1991   | Layout 1             | `62dac76d680e`  |
| 1985   | Layout 1             | `62dac76d680e`  |
| 1980   | Layout 1             | `62dac76d680e`  |
| 1969   | Layout 1             | `62dac76d680e`  |
| 1964   | Layout 1             | `62dac76d680e`  |
| 1958   | Layout 1             | `62dac76d680e`  |
| 1950   | Layout 1             | `62dac76d680e`  |
| 1945   | Layout 1             | `62dac76d680e`  |
| 1937   | Layout 1             | `62dac76d680e`  |
| 1933   | Layout 1             | `62dac76d680e`  |
| 1927   | Layout 1             | `62dac76d680e`  |
| 1921   | Layout 1             | `62dac76d680e`  |
| 1914   | Layout 1             | `62dac76d680e`  |
| 1908   | Layout 1             | `62dac76d680e`  |
| 1897   | Layout 1             | `62dac76d680e`  |
| 1892   | Layout 1             | `62dac76d680e`  |
| 1886   | Layout 1             | `62dac76d680e`  |
| 1881   | Layout 1             | `62dac76d680e`  |
| 1871   | Layout 1             | `62dac76d680e`  |
| 1866   | Layout 1             | `62dac76d680e`  |
| 1862   | Layout 1             | `62dac76d680e`  |
| 1854   | Layout 1             | `62dac76d680e`  |
| 1846   | Layout 1             | `62dac76d680e`  |
| 1838   | Layout 1             | `62dac76d680e`  |
| 1832   | Layout 1             | `62dac76d680e`  |
| 1826   | Layout 1             | `62dac76d680e`  |
| 1822   | Layout 1             | `62dac76d680e`  |
| 1818   | Layout 1             | `62dac76d680e`  |
| 1804   | Layout 1             | `62dac76d680e`  |
| 1794   | Layout 1             | `62dac76d680e`  |
| 1790   | Layout 1             | `62dac76d680e`  |
| 1784   | Layout 1             | `62dac76d680e`  |
| 1774   | Layout 1             | `62dac76d680e`  |
| 1771   | Layout 1             | `62dac76d680e`  |
| 1762   | Layout 1             | `62dac76d680e`  |
| 1759   | Layout 1             | `62dac76d680e`  |
| 1754   | Layout 1             | `62dac76d680e`  |
| 1749   | Layout 1             | `62dac76d680e`  |
| 1743   | Layout 1             | `62dac76d680e`  |
| 1737   | Layout 1             | `62dac76d680e`  |
| 1731   | Layout 1             | `62dac76d680e`  |
| 1725   | Layout 1             | `62dac76d680e`  |
| 1717   | Layout 1             | `62dac76d680e`  |
| 1710   | Layout 1             | `62dac76d680e`  |
| 1704   | Layout 1             | `62dac76d680e`  |
| 1698   | Layout 1             | `62dac76d680e`  |
| 1690   | Layout 1             | `62dac76d680e`  |
| 1685   | Layout 1             | `62dac76d680e`  |
| 1680   | Layout 1             | `62dac76d680e`  |
| 1674   | Layout 1             | `62dac76d680e`  |
| 1668   | Layout 1             | `62dac76d680e`  |
| 1659   | Layout 1             | `62dac76d680e`  |
| 1649   | Layout 1             | `62dac76d680e`  |
| 1642   | Layout 1             | `62dac76d680e`  |
| 1636   | Layout 1             | `62dac76d680e`  |
| 1628   | Layout 1             | `62dac76d680e`  |
| 1622   | Layout 1             | `62dac76d680e`  |
| 1614   | Layout 1             | `62dac76d680e`  |
| 1608   | Layout 1             | `62dac76d680e`  |
| 1602   | Layout 1             | `62dac76d680e`  |
| 1598   | Layout 1             | `62dac76d680e`  |
| 1594   | Layout 1             | `62dac76d680e`  |
| 1590   | Layout 1             | `62dac76d680e`  |
| 1587   | Layout 1             | `62dac76d680e`  |
| 1584   | Layout 1             | `62dac76d680e`  |
| 1579   | Layout 1             | `62dac76d680e`  |
| 1572   | Layout 1             | `62dac76d680e`  |
| 1565   | Layout 1             | `62dac76d680e`  |
| 1559   | Layout 1             | `62dac76d680e`  |
| 1554   | Layout 1             | `62dac76d680e`  |
| 1547   | Layout 1             | `62dac76d680e`  |
| 1537   | Layout 1             | `62dac76d680e`  |
| 1529   | Layout 1             | `62dac76d680e`  |
| 1524   | Layout 1             | `62dac76d680e`  |
| 1519   | Layout 1             | `62dac76d680e`  |
| 1509   | Layout 1             | `62dac76d680e`  |
| 1506   | Layout 1             | `62dac76d680e`  |
| 1504   | Layout 1             | `62dac76d680e`  |
| 1500   | Layout 1             | `62dac76d680e`  |
| 1493   | Layout 1             | `62dac76d680e`  |
| 1489   | Layout 1             | `62dac76d680e`  |
| 1485   | Layout 1             | `62dac76d680e`  |
| 1481   | Layout 1             | `62dac76d680e`  |
| 1474   | Layout 1             | `62dac76d680e`  |
| 1466   | Layout 1             | `62dac76d680e`  |
| 1462   | Layout 1             | `62dac76d680e`  |
| 1459   | Layout 1             | `62dac76d680e`  |
| 1453   | Layout 1             | `62dac76d680e`  |
| 1450   | Layout 1             | `62dac76d680e`  |
| 1445   | Layout 1             | `62dac76d680e`  |
| 1439   | Layout 1             | `62dac76d680e`  |
| 1433   | Layout 1             | `62dac76d680e`  |
| 1430   | Layout 1             | `62dac76d680e`  |
| 1426   | Layout 1             | `62dac76d680e`  |
| 1421   | Layout 1             | `62dac76d680e`  |
| 1417   | Layout 1             | `62dac76d680e`  |
| 1416   | Layout 1             | `62dac76d680e`  |
| 1409   | Layout 1             | `62dac76d680e`  |
| 1405   | Layout 1             | `62dac76d680e`  |
| 1401   | Layout 1             | `62dac76d680e`  |
| 1396   | Layout 1             | `62dac76d680e`  |
| 1391   | Layout 1             | `62dac76d680e`  |
| 1390   | Layout 1             | `62dac76d680e`  |
| 1386   | Layout 1             | `62dac76d680e`  |
| 1381   | Layout 1             | `62dac76d680e`  |
| 1379   | Layout 1             | `62dac76d680e`  |
| 1372   | Layout 1             | `62dac76d680e`  |
| 1366   | Layout 1             | `62dac76d680e`  |
| 1364   | Layout 1             | `62dac76d680e`  |
| 1363   | Layout 1             | `62dac76d680e`  |
| 1360   | Layout 1             | `62dac76d680e`  |
| 1358   | Layout 1             | `62dac76d680e`  |
| 1355   | Layout 1             | `62dac76d680e`  |
| 1351   | Layout 1             | `62dac76d680e`  |
| 1348   | Layout 1             | `62dac76d680e`  |
| 1346   | Layout 1             | `62dac76d680e`  |
| 1341   | No documented layout | `62dac76d680e`  |
| 1340   | No documented layout | `62dac76d680e`  |
| 1338   | No documented layout | `62dac76d680e`  |
| 1335   | No documented layout | `62dac76d680e`  |
| 1333   | No documented layout | `62dac76d680e`  |
| 1329   | No documented layout | `62dac76d680e`  |
| 1327   | No documented layout | `62dac76d680e`  |
| 1324   | No documented layout | `62dac76d680e`  |
| 1321   | No documented layout | `62dac76d680e`  |
| 1319   | No documented layout | `62dac76d680e`  |
| 1318   | No documented layout | `62dac76d680e`  |
| 1316   | No documented layout | `62dac76d680e`  |
| 1313   | No documented layout | `62dac76d680e`  |
| 1311   | No documented layout | `62dac76d680e`  |
| 1309   | No documented layout | `62dac76d680e`  |
| 1304   | No documented layout | `62dac76d680e`  |
| 1292   | No documented layout | `62dac76d680e`  |
| 1286   | No documented layout | `62dac76d680e`  |
| 1280   | No documented layout | `62dac76d680e`  |
| 1276   | No documented layout | `62dac76d680e`  |
| 1267   | No file              | `62dac76d680e`  |
| 1261   | No file              | `62dac76d680e`  |
| 1256   | No file              | `62dac76d680e`  |
| 1250   | No file              | `62dac76d680e`  |
| 1246   | No file              | `62dac76d680e`  |
| 1239   | No file              | `62dac76d680e`  |
| 1230   | No file              | `62dac76d680e`  |
| 1226   | No file              | `62dac76d680e`  |
| 1220   | No file              | `62dac76d680e`  |
| 1217   | No file              | `62dac76d680e`  |
| 1211   | No file              | `62dac76d680e`  |
| 1210   | No file              | `62dac76d680e`  |
| 1208   | No file              | `62dac76d680e`  |
| 1203   | No file              | `62dac76d680e`  |
| 1197   | No file              | `62dac76d680e`  |
| 1194   | No file              | `62dac76d680e`  |
| 1192   | No file              | `62dac76d680e`  |
| 1187   | No file              | `62dac76d680e`  |
| 1183   | No file              | `62dac76d680e`  |
| 1177   | No file              | `62dac76d680e`  |
| 1173   | No file              | `62dac76d680e`  |
| 1167   | No file              | `62dac76d680e`  |
| 1164   | No file              | `62dac76d680e`  |
| 1156   | No file              | `62dac76d680e`  |
| 1149   | No file              | `62dac76d680e`  |
| 1144   | No file              | `62dac76d680e`  |
| 1137   | No file              | `62dac76d680e`  |
| 1132   | No file              | `62dac76d680e`  |
| 1127   | No file              | `62dac76d680e`  |
| 1122   | No file              | `62dac76d680e`  |
| 1118   | No file              | `62dac76d680e`  |
| 1114   | No file              | `62dac76d680e`  |
| 1109   | No file              | `62dac76d680e`  |
| 1102   | No file              | `62dac76d680e`  |
| 1096   | No file              | `62dac76d680e`  |
| 1088   | No file              | `62dac76d680e`  |
| 1081   | No file              | `62dac76d680e`  |
| 1076   | No file              | `62dac76d680e`  |
| 1069   | No file              | `62dac76d680e`  |
| 1064   | No file              | `62dac76d680e`  |
| 1058   | No file              | `62dac76d680e`  |
| 1051   | No file              | `62dac76d680e`  |
| 1044   | No file              | `62dac76d680e`  |
| 1036   | No file              | `62dac76d680e`  |
| 1026   | No file              | `62dac76d680e`  |
| 1016   | No file              | `62dac76d680e`  |
| 1009   | No file              | `62dac76d680e`  |
| 1005   | No file              | `62dac76d680e`  |
| 1000   | No file              | `62dac76d680e`  |
| 998    | No file              | `62dac76d680e`  |
| 990    | No file              | `62dac76d680e`  |
| 979    | No file              | `62dac76d680e`  |
| 972    | No file              | `62dac76d680e`  |
| 963    | No file              | `62dac76d680e`  |
| 955    | No file              | `62dac76d680e`  |
| 946    | No file              | `62dac76d680e`  |
| 938    | No file              | `62dac76d680e`  |
| 927    | No file              | `62dac76d680e`  |
| 911    | No file              | `62dac76d680e`  |
| 904    | No file              | `62dac76d680e`  |
| 899    | No file              | `62dac76d680e`  |
| 894    | No file              | `62dac76d680e`  |
| 885    | No file              | `62dac76d680e`  |
| 879    | No file              | `62dac76d680e`  |
| 872    | No file              | `62dac76d680e`  |
| 864    | No file              | `62dac76d680e`  |
| 855    | No file              | `62dac76d680e`  |
| 853    | No file              | `62dac76d680e`  |
| 845    | No file              | `62dac76d680e`  |
| 837    | No file              | `62dac76d680e`  |
| 829    | No file              | `62dac76d680e`  |
| 822    | No file              | `62dac76d680e`  |
| 814    | No file              | `62dac76d680e`  |
| 805    | No file              | `62dac76d680e`  |
| 794    | No file              | `62dac76d680e`  |
| 787    | No file              | `62dac76d680e`  |
| 780    | No file              | `62dac76d680e`  |
| 771    | No file              | `62dac76d680e`  |
| 760    | No file              | `62dac76d680e`  |
| 748    | No file              | `62dac76d680e`  |
| 741    | No file              | `62dac76d680e`  |
| 736    | No file              | `62dac76d680e`  |
| 731    | No file              | `62dac76d680e`  |
| 723    | No file              | `62dac76d680e`  |
| 711    | No file              | `62dac76d680e`  |
| 707    | No file              | `62dac76d680e`  |
| 697    | No file              | `62dac76d680e`  |
| 689    | No file              | `62dac76d680e`  |
| 683    | No file              | `62dac76d680e`  |
| 678    | No file              | `62dac76d680e`  |
| 670    | No file              | `62dac76d680e`  |
| 661    | No file              | `62dac76d680e`  |
| 656    | No file              | `62dac76d680e`  |
| 652    | No file              | `62dac76d680e`  |
| 643    | No file              | `62dac76d680e`  |
| 637    | No file              | `62dac76d680e`  |
| 630    | No file              | `62dac76d680e`  |
| 627    | No file              | `62dac76d680e`  |
| 621    | No file              | `62dac76d680e`  |
| 617    | No file              | `62dac76d680e`  |
| 615    | No file              | `62dac76d680e`  |
| 606    | No file              | `62dac76d680e`  |
| 599    | No file              | `62dac76d680e`  |
| 592    | No file              | `62dac76d680e`  |
| 586    | No file              | `62dac76d680e`  |
| 577    | No file              | `62dac76d680e`  |
| 569    | No file              | `62dac76d680e`  |
| 561    | No file              | `62dac76d680e`  |
| 554    | No file              | `62dac76d680e`  |
| 542    | No file              | `62dac76d680e`  |
| 532    | No file              | `62dac76d680e`  |
| 531    | No file              | `62dac76d680e`  |
| 526    | No file              | `62dac76d680e`  |
| 521    | No file              | `62dac76d680e`  |
| 517    | No file              | `62dac76d680e`  |
| 510    | No file              | `62dac76d680e`  |
| 508    | No file              | `62dac76d680e`  |
| 504    | No file              | `62dac76d680e`  |
| 497    | No file              | `62dac76d680e`  |
| 491    | No file              | `62dac76d680e`  |
| 485    | No file              | `62dac76d680e`  |
| 478    | No file              | `62dac76d680e`  |
| 472    | No file              | `62dac76d680e`  |
| 466    | No file              | `62dac76d680e`  |
| 457    | No file              | `62dac76d680e`  |
| 452    | No file              | `62dac76d680e`  |
| 449    | No file              | `62dac76d680e`  |
| 435    | No file              | `62dac76d680e`  |

<!-- versions:end -->

## Companion Files

| File                          | Required | Role                                                                 |
| ----------------------------- | -------- | -------------------------------------------------------------------- |
| `guildmanufactureoffset.dbss` | Optional | `product_item_key -> (data_offset, data_size)` index; the rows carry their own counts and can be walked without it |
| `languagedata_en.loc`         | Optional | Item names (type `0`), guild skill names (type `10`), guild house names (type `6`), exchange names (type `24`) and the category titles (type `37`, `GAME` sheet) |
| `itemexchangesource.bss`      | Optional | The exchange each row names. The handler reads the exchange name from the `EXCHANGE_NAME_KR` lookup index (see `docs/handler.md`), shows `[Guild] Ship License: Galley (7901)` in the Exchange column and links it to the exchange's row; it does not open the file |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset  | Type       | Field | Notes                                        |
| ------- | ---------- | ----- | -------------------------------------------- |
| `+0x00` | u32        | count | Number of rows; `16` on client 3474          |
| `+0x04` | Row[count] | rows  | Back to back to the end of the file; see Row |

### Row (variable: 117 bytes + guild house keys)

| Offset                  | Type                   | Field                | Notes                                                        |
| ----------------------- | ---------------------- | -------------------- | ------------------------------------------------------------ |
| `+0x00`                 | u32                    | product_item_key     | Item key (`enchant_level << 24 \| item_id`) of the product; the index key, unique per row |
| `+0x04`                 | u32                    | exchange_item_key    | [`itemexchangesource.bss`](itemexchangesource_bss.md) key the product slot's tooltip reads (`getExchangeKey()`); `7901` to `7932` and `9773` to `9776` on client 3474, all 16 `exchange_type` 8 (GuildHouseLargeCraft) rows |
| `+0x08`                 | u32                    | product_item_key_dup | Equal to `product_item_key` in every row                     |
| `+0x0C`                 | u64                    | time                 | `43200`, `72000` or `86400` on client 3474; the unit is an In-Game Check |
| `+0x14`                 | u64                    | price                | `10000` in every row of clients 1784 and 3474; see Open Questions |
| `+0x1C`                 | u64                    | product_item_limit   | `1` or `2` on client 3474                                    |
| `+0x24`                 | u32[6]                 | required_item_keys   | Item keys of the six material slots (`getRequiredItemEnchantKey(i)`); filled from slot 0, `0` for an empty slot |
| `+0x3C`                 | u64[6]                 | required_item_counts | Count per slot for one product (`getRequiredItemCount(i)`); `0` for an empty slot |
| `+0x6C`                 | u8                     | category             | Product window category, see Categories                     |
| `+0x6D`                 | u32                    | guild_house_count    | Number of `guild_house_keys`; `4`, `8` or `23` on client 3474 |
| `+0x71`                 | u16[guild_house_count] | guild_house_keys     | Character keys of the guild houses that can craft the product, ascending |
| `guild_house_keys+0x00` | u32                    | skill_key            | Guild skill the guild needs, `skill_no << 16 \| level`; level `1` in every row |

The rows are not sorted by key.

### `guildmanufactureoffset.dbss`

| Offset  | Type              | Field | Notes                                     |
| ------- | ----------------- | ----- | ----------------------------------------- |
| `+0x00` | u32               | count | Equals the `guildmanufacture.dbss` count  |
| `+0x04` | Offset Row[count] | rows  | No magic, no trailer; see Offset Row      |

### Offset Row (12 bytes)

| Offset  | Type | Field            | Notes                                                    |
| ------- | ---- | ---------------- | -------------------------------------------------------- |
| `+0x00` | u32  | product_item_key | `product_item_key` of the row                            |
| `+0x04` | u32  | data_offset      | Row start + 4, at `exchange_item_key`                    |
| `+0x08` | u32  | data_size        | Row size - 4: `117 + 2 * guild_house_count - 4`          |

Read by `parse_bare_u32_offset_rows()` in `_common/pabr_offset.py`. The index
rows are not in file order; on clients 1784 and 3474 every index row points
at the row with its key and covers the rest of it.

## Layout 1

### Row (variable: 115 bytes + guild house keys)

| Offset                  | Type                   | Field                | Notes                                  |
| ----------------------- | ---------------------- | -------------------- | -------------------------------------- |
| `+0x00`                 | u32                    | product_item_key     |                                        |
| `+0x04`                 | u16                    | exchange_item_key    | Two bytes here, four in Layout 2       |
| `+0x06`                 | u32                    | product_item_key_dup |                                        |
| `+0x0A`                 | u64                    | time                 |                                        |
| `+0x12`                 | u64                    | price                |                                        |
| `+0x1A`                 | u64                    | product_item_limit   |                                        |
| `+0x22`                 | u32[6]                 | required_item_keys   |                                        |
| `+0x3A`                 | u64[6]                 | required_item_counts |                                        |
| `+0x6A`                 | u8                     | category             |                                        |
| `+0x6B`                 | u32                    | guild_house_count    |                                        |
| `+0x6F`                 | u16[guild_house_count] | guild_house_keys     |                                        |
| `guild_house_keys+0x00` | u32                    | skill_key            |                                        |

Every row is 2 bytes shorter than in Layout 2, and the index's `data_size`
is `115 + 2 * guild_house_count - 4`. Client 1784 has 17 rows. Client 3474
drops `50007` ([Guild] Registration: Valencia Elephant) and the four "for
Combat" elephant items `59002`, `59102`, `59202` and `59302` (Steel Mask,
Steel Armor, Silk Saddle, Silk Stirrups), and adds the four Improved Galley
parts `49794` to `49797`.

## Categories

The product window (`panel_guild_manufactureselect_all.luac`) groups the
products by `getCategoryNo()` and titles each group with a `GAME` sheet key.
The fourth group exists only when the client's `_ContentsGroup_SummonGuildDrill`
is set, and its key skips `CATEGORY3`.

| Value | `GAME` key                               | Title (client 3474)      | Rows (client 3474) |
| ----- | ---------------------------------------- | ------------------------ | ------------------ |
| `0`   | `LUA_GUILD_MANUFACTURE_SELECT_CATEGORY0` | License and Registration | 2                  |
| `1`   | `LUA_GUILD_MANUFACTURE_SELECT_CATEGORY1` | Mount Equipment          | 12                 |
| `2`   | `LUA_GUILD_MANUFACTURE_SELECT_CATEGORY2` | Mount Recovery           | 2                  |
| `3`   | `LUA_GUILD_MANUFACTURE_SELECT_CATEGORY4` | Resource Gathering Tool  | 0                  |

## Field Names

The row is the `GuildManufactureInfo` sheet of a private server's
`DataSheets.bexcel` on client 1784, matched by `ProductItemNo`. The 2016
client has no guild crafting structure, so the names come from the sheet
columns and the Lua getters.

| Field                | Column                       | Same value (client 1784) | Same value (client 3474) |
| -------------------- | ---------------------------- | ------------------------ | ------------------------ |
| product_item_key     | `ProductItemNo`              | 17 of 17 rows            | 12 of 16 rows            |
| exchange_item_key    | `ExchangeItemKey`            | 17 of 17                 | 12 of 12                 |
| category             | `CategoryNo`                 | 17 of 17                 | 12 of 12                 |
| guild_house_keys     | `GuildHouse`                 | 17 of 17, as a set       | 12 of 12, as a set       |
| skill_key            | `SkillNo1` (the skill_no half) | 17 of 17               | 12 of 12                 |
| required_item_keys   | `RequiredItemNo0` to `5`     | 17 of 17                 | 6 of 12                  |
| required_item_counts | `RequiredItemCount0` to `5`  | 17 of 17                 | 2 of 12                  |
| time                 | `Time`                       | 17 of 17                 | 12 of 12                 |
| price                | `Price`                      | 17 of 17                 | 12 of 12                 |
| product_item_limit   | `ProductItemLimit`           | 17 of 17                 | 12 of 12                 |

The four Improved Galley rows of client 3474 (`49794` to `49797`) are not
in the sheet. Of the 12 shared rows, five dropped their last material
(`54026` and the galley parts `49709` to `49712`), `50119` needs `9916` in
place of `50007` in slot 1, and the four Capotia rows keep their items with
new counts. The sheet lists `GuildHouse` with `2569` after
`2691`; the file stores the keys ascending. An empty sheet cell is `0` in
the file. The sheet's `ContentsOption` column has no field: the 13 sheet
rows missing from client 1784 are the rows whose option is `1000`, `1449` or
`1636`.

## Notes

- The Guild Crafting window (`panel_guild_manufacture_all_1.luac`) shows
  `__eGuildManufactureRequiredItemCount` material slots per product. For a
  slot it reads the key from the guild's current crafting job and the count
  of one product from this file, multiplied by the job's product count.
- The guide text `LUA_GUILD_MANUFACTURE_NOTICE_INFORMATION` says a guild
  needs a guild house that can craft the item, won at the guild house
  auction, and the guild skill needed for it; these are `guild_house_keys`
  and `skill_key`.
- On client 3474 the guild house lists are three sets: `2110`, `2140`,
  `2880`, `2905` (Velia, Olvia, Altinova Guild House 1 and 2) for the galley
  rows, `3351` to `3358` (Cadry, Pujiya and the other Valencia guild houses)
  for the elephant rows, and all 23 for the two Mount Recovery rows.
- The guild skills on client 3474 are `65042` and `65043` (Building Boat Lv.
  1 and 2), `65052` and `65053` (Monstrous Force Lv. 1 and 2) and `65059`
  (Fully Prepared). The level in the skill name belongs to the skill number;
  the key's level half is `1`.
- No decompiled guild crafting Lua reads `product_item_limit`. The `GAME`
  key `LUA_GUILD_MANUFACTURE_COUNT_LIMIT` reads "Daily Crafting Limit:
  {itemLimit}" on client 3474.

## Open Questions

### What price Is

`price` is `10000` in every row of both clients and matches the sheet's
`Price` column. The Complete Now cost the window shows
(`FromClient_Guild_Manufacture_All_CompletePrice`) comes from the server as
`price_s64`, so the Lua does not show whether this is the start cost, the
Complete Now cost or something else.

## In-Game Checks

### Unit of time

Needs item: the materials of [[Guild] Galley: Cloud Breeze Sail](https://bdocodex.com/us/item/49712/)

Needs zone: a Velia, Olvia or Altinova guild house that your guild holds

Needs skill: guild skill Building Boat Lv. 2

1. Open the Guild Crafting window of that guild house.
2. Select [Guild] Galley: Cloud Breeze Sail and start crafting.
3. Read the finish time the window shows (Processing will finish on ...).

A finish time 20 hours after the start means `time` is seconds (`72000`).

### Daily Crafting Limit

Needs zone: a guild house with a Guild Crafting window that your guild holds

1. Open the Guild Crafting window of that guild house.
2. Select each item in the list and read the "Daily Crafting Limit" line.

A limit equal to the row's `product_item_limit` (`1` or `2` on client 3474)
confirms the field name.
