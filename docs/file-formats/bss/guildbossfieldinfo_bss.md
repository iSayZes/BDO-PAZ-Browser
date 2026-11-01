# `guildbossfieldinfo.bss` Format

## Purpose

A world position per guild boss, keyed by the [`boss_spawn.bss`](boss_spawn_bss.md)
key. The Guild Boss Summon window (`panel_guild_bosssummon_all`) offers to
enter or leave the guild boss field (a mirror field,
`__eMirrorFieldContentsKey_GuildBossField`) only where
`ToClient_IsInGuildBossFieldPos(bossKey)` is true, and
`ToClient_CheckUseGuildBossField(bossKey)` tells whether a boss uses one.
On client 3474 the file has 6 rows, one for each `boss_spawn.bss` boss,
each near that boss's spawn point. The file is a u32 count and fixed rows,
with no PABR magic and no string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                     | Bytes | Records | Row bytes |
| ------ | -------------- | ------------------------ | ----- | ------- | --------- |
| 1      | 2025 and later | `guildbossfieldinfo.bss` | 148   | 6 Row   | 24        |

| Layout | File                     | Known         | Unknown      |
| ------ | ------------------------ | ------------- | ------------ |
| 1      | `guildbossfieldinfo.bss` | 124 B (83.8%) | 24 B (16.2%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `2400f7698098`  |
| 3482   | Layout 1 | `2400f7698098`  |
| 3474   | Layout 1 | `2400f7698098`  |
| 3473   | Layout 1 | `2400f7698098`  |
| 3464   | Layout 1 | `2400f7698098`  |
| 3458   | Layout 1 | `2400f7698098`  |
| 3454   | Layout 1 | `2400f7698098`  |
| 3444   | Layout 1 | `2400f7698098`  |
| 3435   | Layout 1 | `2400f7698098`  |
| 3426   | Layout 1 | `2400f7698098`  |
| 3418   | Layout 1 | `2400f7698098`  |
| 3412   | Layout 1 | `2400f7698098`  |
| 3402   | Layout 1 | `2400f7698098`  |
| 3396   | Layout 1 | `2400f7698098`  |
| 3387   | Layout 1 | `2400f7698098`  |
| 3381   | Layout 1 | `2400f7698098`  |
| 3373   | Layout 1 | `2400f7698098`  |
| 3364   | Layout 1 | `2400f7698098`  |
| 3356   | Layout 1 | `2400f7698098`  |
| 3349   | Layout 1 | `2400f7698098`  |
| 3342   | Layout 1 | `2400f7698098`  |
| 3335   | Layout 1 | `2400f7698098`  |
| 3326   | Layout 1 | `2400f7698098`  |
| 3321   | Layout 1 | `2400f7698098`  |
| 3314   | Layout 1 | `2400f7698098`  |
| 3303   | Layout 1 | `2400f7698098`  |
| 3302   | Layout 1 | `2400f7698098`  |
| 3293   | Layout 1 | `2400f7698098`  |
| 3283   | Layout 1 | `2400f7698098`  |
| 3275   | Layout 1 | `2400f7698098`  |
| 3267   | Layout 1 | `2400f7698098`  |
| 3258   | Layout 1 | `2400f7698098`  |
| 3251   | Layout 1 | `2400f7698098`  |
| 3242   | Layout 1 | `2400f7698098`  |
| 3235   | Layout 1 | `2400f7698098`  |
| 3229   | Layout 1 | `2400f7698098`  |
| 3212   | Layout 1 | `2400f7698098`  |
| 3203   | Layout 1 | `2400f7698098`  |
| 3193   | Layout 1 | `2400f7698098`  |
| 3186   | Layout 1 | `2400f7698098`  |
| 3177   | Layout 1 | `2400f7698098`  |
| 3169   | Layout 1 | `2400f7698098`  |
| 3158   | Layout 1 | `2400f7698098`  |
| 3151   | Layout 1 | `2400f7698098`  |
| 3144   | Layout 1 | `2400f7698098`  |
| 3133   | Layout 1 | `2400f7698098`  |
| 3125   | Layout 1 | `2400f7698098`  |
| 3118   | Layout 1 | `2400f7698098`  |
| 3111   | Layout 1 | `2400f7698098`  |
| 3103   | Layout 1 | `2400f7698098`  |
| 3095   | Layout 1 | `2400f7698098`  |
| 3086   | Layout 1 | `2400f7698098`  |
| 3072   | Layout 1 | `2400f7698098`  |
| 3062   | Layout 1 | `2400f7698098`  |
| 3052   | Layout 1 | `2400f7698098`  |
| 3045   | Layout 1 | `2400f7698098`  |
| 3037   | Layout 1 | `2400f7698098`  |
| 3030   | Layout 1 | `2400f7698098`  |
| 3021   | Layout 1 | `2400f7698098`  |
| 3012   | Layout 1 | `2400f7698098`  |
| 3002   | Layout 1 | `2400f7698098`  |
| 2995   | Layout 1 | `2400f7698098`  |
| 2987   | Layout 1 | `2400f7698098`  |
| 2978   | Layout 1 | `2400f7698098`  |
| 2970   | Layout 1 | `2400f7698098`  |
| 2959   | Layout 1 | `2400f7698098`  |
| 2951   | Layout 1 | `2400f7698098`  |
| 2942   | Layout 1 | `2400f7698098`  |
| 2935   | Layout 1 | `2400f7698098`  |
| 2932   | Layout 1 | `2400f7698098`  |
| 2923   | Layout 1 | `2400f7698098`  |
| 2919   | Layout 1 | `2400f7698098`  |
| 2907   | Layout 1 | `2400f7698098`  |
| 2900   | Layout 1 | `2400f7698098`  |
| 2891   | Layout 1 | `2400f7698098`  |
| 2882   | Layout 1 | `2400f7698098`  |
| 2872   | Layout 1 | `2400f7698098`  |
| 2863   | Layout 1 | `2400f7698098`  |
| 2855   | Layout 1 | `2400f7698098`  |
| 2849   | Layout 1 | `2400f7698098`  |
| 2844   | Layout 1 | `2400f7698098`  |
| 2834   | Layout 1 | `2400f7698098`  |
| 2825   | Layout 1 | `2400f7698098`  |
| 2819   | Layout 1 | `2400f7698098`  |
| 2811   | Layout 1 | `2400f7698098`  |
| 2803   | Layout 1 | `2400f7698098`  |
| 2794   | Layout 1 | `2400f7698098`  |
| 2783   | Layout 1 | `2400f7698098`  |
| 2774   | Layout 1 | `2400f7698098`  |
| 2765   | Layout 1 | `2400f7698098`  |
| 2756   | Layout 1 | `2400f7698098`  |
| 2750   | Layout 1 | `2400f7698098`  |
| 2743   | Layout 1 | `2400f7698098`  |
| 2736   | Layout 1 | `2400f7698098`  |
| 2726   | Layout 1 | `2400f7698098`  |
| 2717   | Layout 1 | `2400f7698098`  |
| 2709   | Layout 1 | `2400f7698098`  |
| 2703   | Layout 1 | `2400f7698098`  |
| 2695   | Layout 1 | `2400f7698098`  |
| 2684   | Layout 1 | `2400f7698098`  |
| 2672   | Layout 1 | `2400f7698098`  |
| 2665   | Layout 1 | `2400f7698098`  |
| 2657   | Layout 1 | `2400f7698098`  |
| 2649   | Layout 1 | `2400f7698098`  |
| 2644   | Layout 1 | `2400f7698098`  |
| 2637   | Layout 1 | `2400f7698098`  |
| 2629   | Layout 1 | `2400f7698098`  |
| 2619   | Layout 1 | `2400f7698098`  |
| 2612   | Layout 1 | `2400f7698098`  |
| 2606   | Layout 1 | `2400f7698098`  |
| 2602   | Layout 1 | `2400f7698098`  |
| 2601   | Layout 1 | `2400f7698098`  |
| 2592   | Layout 1 | `2400f7698098`  |
| 2583   | Layout 1 | `2400f7698098`  |
| 2575   | Layout 1 | `2400f7698098`  |
| 2567   | Layout 1 | `2400f7698098`  |
| 2560   | Layout 1 | `2400f7698098`  |
| 2553   | Layout 1 | `2400f7698098`  |
| 2545   | Layout 1 | `2400f7698098`  |
| 2538   | Layout 1 | `2400f7698098`  |
| 2529   | Layout 1 | `2400f7698098`  |
| 2519   | Layout 1 | `2400f7698098`  |
| 2513   | Layout 1 | `2400f7698098`  |
| 2510   | Layout 1 | `2400f7698098`  |
| 2507   | Layout 1 | `2400f7698098`  |
| 2503   | Layout 1 | `2400f7698098`  |
| 2498   | Layout 1 | `2400f7698098`  |
| 2492   | Layout 1 | `2400f7698098`  |
| 2487   | Layout 1 | `2400f7698098`  |
| 2480   | Layout 1 | `2400f7698098`  |
| 2474   | Layout 1 | `2400f7698098`  |
| 2468   | Layout 1 | `2400f7698098`  |
| 2460   | Layout 1 | `2400f7698098`  |
| 2453   | Layout 1 | `2400f7698098`  |
| 2444   | Layout 1 | `2400f7698098`  |
| 2438   | Layout 1 | `2400f7698098`  |
| 2434   | Layout 1 | `2400f7698098`  |
| 2429   | Layout 1 | `2400f7698098`  |
| 2421   | Layout 1 | `2400f7698098`  |
| 2414   | Layout 1 | `2400f7698098`  |
| 2407   | Layout 1 | `2400f7698098`  |
| 2401   | Layout 1 | `2400f7698098`  |
| 2397   | Layout 1 | `2400f7698098`  |
| 2393   | Layout 1 | `2400f7698098`  |
| 2384   | Layout 1 | `2400f7698098`  |
| 2378   | Layout 1 | `2400f7698098`  |
| 2372   | Layout 1 | `2400f7698098`  |
| 2358   | Layout 1 | `2400f7698098`  |
| 2352   | Layout 1 | `2400f7698098`  |
| 2347   | Layout 1 | `2400f7698098`  |
| 2343   | Layout 1 | `2400f7698098`  |
| 2335   | Layout 1 | `2400f7698098`  |
| 2327   | Layout 1 | `2400f7698098`  |
| 2324   | Layout 1 | `2400f7698098`  |
| 2319   | Layout 1 | `2400f7698098`  |
| 2313   | Layout 1 | `2400f7698098`  |
| 2308   | Layout 1 | `2400f7698098`  |
| 2302   | Layout 1 | `2400f7698098`  |
| 2295   | Layout 1 | `2400f7698098`  |
| 2290   | Layout 1 | `2400f7698098`  |
| 2284   | Layout 1 | `2400f7698098`  |
| 2276   | Layout 1 | `2400f7698098`  |
| 2269   | Layout 1 | `2400f7698098`  |
| 2259   | Layout 1 | `2400f7698098`  |
| 2250   | Layout 1 | `2400f7698098`  |
| 2243   | Layout 1 | `2400f7698098`  |
| 2235   | Layout 1 | `2400f7698098`  |
| 2229   | Layout 1 | `2400f7698098`  |
| 2224   | Layout 1 | `2400f7698098`  |
| 2218   | Layout 1 | `2400f7698098`  |
| 2215   | Layout 1 | `2400f7698098`  |
| 2207   | Layout 1 | `2400f7698098`  |
| 2203   | Layout 1 | `2400f7698098`  |
| 2196   | Layout 1 | `2400f7698098`  |
| 2192   | Layout 1 | `2400f7698098`  |
| 2189   | Layout 1 | `2400f7698098`  |
| 2183   | Layout 1 | `2400f7698098`  |
| 2179   | Layout 1 | `2400f7698098`  |
| 2171   | Layout 1 | `2400f7698098`  |
| 2163   | Layout 1 | `2400f7698098`  |
| 2156   | Layout 1 | `2400f7698098`  |
| 2151   | Layout 1 | `2400f7698098`  |
| 2147   | Layout 1 | `2400f7698098`  |
| 2142   | Layout 1 | `2400f7698098`  |
| 2138   | Layout 1 | `2400f7698098`  |
| 2134   | Layout 1 | `2400f7698098`  |
| 2130   | Layout 1 | `2400f7698098`  |
| 2122   | Layout 1 | `2400f7698098`  |
| 2107   | Layout 1 | `2400f7698098`  |
| 2098   | Layout 1 | `2400f7698098`  |
| 2089   | Layout 1 | `2400f7698098`  |
| 2081   | Layout 1 | `2400f7698098`  |
| 2073   | Layout 1 | `2400f7698098`  |
| 2067   | Layout 1 | `2400f7698098`  |
| 2063   | Layout 1 | `2400f7698098`  |
| 2059   | Layout 1 | `2400f7698098`  |
| 2052   | Layout 1 | `2400f7698098`  |
| 2044   | Layout 1 | `2400f7698098`  |
| 2039   | Layout 1 | `2400f7698098`  |
| 2032   | Layout 1 | `2400f7698098`  |
| 2025   | Layout 1 | `2400f7698098`  |
| 2011   | No file  | `2400f7698098`  |
| 2005   | No file  | `2400f7698098`  |
| 2000   | No file  | `2400f7698098`  |
| 1996   | No file  | `2400f7698098`  |
| 1991   | No file  | `2400f7698098`  |
| 1985   | No file  | `2400f7698098`  |
| 1980   | No file  | `2400f7698098`  |
| 1969   | No file  | `2400f7698098`  |
| 1964   | No file  | `2400f7698098`  |
| 1958   | No file  | `2400f7698098`  |
| 1950   | No file  | `2400f7698098`  |
| 1945   | No file  | `2400f7698098`  |
| 1937   | No file  | `2400f7698098`  |
| 1933   | No file  | `2400f7698098`  |
| 1927   | No file  | `2400f7698098`  |
| 1921   | No file  | `2400f7698098`  |
| 1914   | No file  | `2400f7698098`  |
| 1908   | No file  | `2400f7698098`  |
| 1897   | No file  | `2400f7698098`  |
| 1892   | No file  | `2400f7698098`  |
| 1886   | No file  | `2400f7698098`  |
| 1881   | No file  | `2400f7698098`  |
| 1871   | No file  | `2400f7698098`  |
| 1866   | No file  | `2400f7698098`  |
| 1862   | No file  | `2400f7698098`  |
| 1854   | No file  | `2400f7698098`  |
| 1846   | No file  | `2400f7698098`  |
| 1838   | No file  | `2400f7698098`  |
| 1832   | No file  | `2400f7698098`  |
| 1826   | No file  | `2400f7698098`  |
| 1822   | No file  | `2400f7698098`  |
| 1818   | No file  | `2400f7698098`  |
| 1804   | No file  | `2400f7698098`  |
| 1794   | No file  | `2400f7698098`  |
| 1790   | No file  | `2400f7698098`  |
| 1784   | No file  | `2400f7698098`  |
| 1774   | No file  | `2400f7698098`  |
| 1771   | No file  | `2400f7698098`  |
| 1762   | No file  | `2400f7698098`  |
| 1759   | No file  | `2400f7698098`  |
| 1754   | No file  | `2400f7698098`  |
| 1749   | No file  | `2400f7698098`  |
| 1743   | No file  | `2400f7698098`  |
| 1737   | No file  | `2400f7698098`  |
| 1731   | No file  | `2400f7698098`  |
| 1725   | No file  | `2400f7698098`  |
| 1717   | No file  | `2400f7698098`  |
| 1710   | No file  | `2400f7698098`  |
| 1704   | No file  | `2400f7698098`  |
| 1698   | No file  | `2400f7698098`  |
| 1690   | No file  | `2400f7698098`  |
| 1685   | No file  | `2400f7698098`  |
| 1680   | No file  | `2400f7698098`  |
| 1674   | No file  | `2400f7698098`  |
| 1668   | No file  | `2400f7698098`  |
| 1659   | No file  | `2400f7698098`  |
| 1649   | No file  | `2400f7698098`  |
| 1642   | No file  | `2400f7698098`  |
| 1636   | No file  | `2400f7698098`  |
| 1628   | No file  | `2400f7698098`  |
| 1622   | No file  | `2400f7698098`  |
| 1614   | No file  | `2400f7698098`  |
| 1608   | No file  | `2400f7698098`  |
| 1602   | No file  | `2400f7698098`  |
| 1598   | No file  | `2400f7698098`  |
| 1594   | No file  | `2400f7698098`  |
| 1590   | No file  | `2400f7698098`  |
| 1587   | No file  | `2400f7698098`  |
| 1584   | No file  | `2400f7698098`  |
| 1579   | No file  | `2400f7698098`  |
| 1572   | No file  | `2400f7698098`  |
| 1565   | No file  | `2400f7698098`  |
| 1559   | No file  | `2400f7698098`  |
| 1554   | No file  | `2400f7698098`  |
| 1547   | No file  | `2400f7698098`  |
| 1537   | No file  | `2400f7698098`  |
| 1529   | No file  | `2400f7698098`  |
| 1524   | No file  | `2400f7698098`  |
| 1519   | No file  | `2400f7698098`  |
| 1509   | No file  | `2400f7698098`  |
| 1506   | No file  | `2400f7698098`  |
| 1504   | No file  | `2400f7698098`  |
| 1500   | No file  | `2400f7698098`  |
| 1493   | No file  | `2400f7698098`  |
| 1489   | No file  | `2400f7698098`  |
| 1485   | No file  | `2400f7698098`  |
| 1481   | No file  | `2400f7698098`  |
| 1474   | No file  | `2400f7698098`  |
| 1466   | No file  | `2400f7698098`  |
| 1462   | No file  | `2400f7698098`  |
| 1459   | No file  | `2400f7698098`  |
| 1453   | No file  | `2400f7698098`  |
| 1450   | No file  | `2400f7698098`  |
| 1445   | No file  | `2400f7698098`  |
| 1439   | No file  | `2400f7698098`  |
| 1433   | No file  | `2400f7698098`  |
| 1430   | No file  | `2400f7698098`  |
| 1426   | No file  | `2400f7698098`  |
| 1421   | No file  | `2400f7698098`  |
| 1417   | No file  | `2400f7698098`  |
| 1416   | No file  | `2400f7698098`  |
| 1409   | No file  | `2400f7698098`  |
| 1405   | No file  | `2400f7698098`  |
| 1401   | No file  | `2400f7698098`  |
| 1396   | No file  | `2400f7698098`  |
| 1391   | No file  | `2400f7698098`  |
| 1390   | No file  | `2400f7698098`  |
| 1386   | No file  | `2400f7698098`  |
| 1381   | No file  | `2400f7698098`  |
| 1379   | No file  | `2400f7698098`  |
| 1372   | No file  | `2400f7698098`  |
| 1366   | No file  | `2400f7698098`  |
| 1364   | No file  | `2400f7698098`  |
| 1363   | No file  | `2400f7698098`  |
| 1360   | No file  | `2400f7698098`  |
| 1358   | No file  | `2400f7698098`  |
| 1355   | No file  | `2400f7698098`  |
| 1351   | No file  | `2400f7698098`  |
| 1348   | No file  | `2400f7698098`  |
| 1346   | No file  | `2400f7698098`  |
| 1341   | No file  | `2400f7698098`  |
| 1340   | No file  | `2400f7698098`  |
| 1338   | No file  | `2400f7698098`  |
| 1335   | No file  | `2400f7698098`  |
| 1333   | No file  | `2400f7698098`  |
| 1329   | No file  | `2400f7698098`  |
| 1327   | No file  | `2400f7698098`  |
| 1324   | No file  | `2400f7698098`  |
| 1321   | No file  | `2400f7698098`  |
| 1319   | No file  | `2400f7698098`  |
| 1318   | No file  | `2400f7698098`  |
| 1316   | No file  | `2400f7698098`  |
| 1313   | No file  | `2400f7698098`  |
| 1311   | No file  | `2400f7698098`  |
| 1309   | No file  | `2400f7698098`  |
| 1304   | No file  | `2400f7698098`  |
| 1292   | No file  | `2400f7698098`  |
| 1286   | No file  | `2400f7698098`  |
| 1280   | No file  | `2400f7698098`  |
| 1276   | No file  | `2400f7698098`  |
| 1267   | No file  | `2400f7698098`  |
| 1261   | No file  | `2400f7698098`  |
| 1256   | No file  | `2400f7698098`  |
| 1250   | No file  | `2400f7698098`  |
| 1246   | No file  | `2400f7698098`  |
| 1239   | No file  | `2400f7698098`  |
| 1230   | No file  | `2400f7698098`  |
| 1226   | No file  | `2400f7698098`  |
| 1220   | No file  | `2400f7698098`  |
| 1217   | No file  | `2400f7698098`  |
| 1211   | No file  | `2400f7698098`  |
| 1210   | No file  | `2400f7698098`  |
| 1208   | No file  | `2400f7698098`  |
| 1203   | No file  | `2400f7698098`  |
| 1197   | No file  | `2400f7698098`  |
| 1194   | No file  | `2400f7698098`  |
| 1192   | No file  | `2400f7698098`  |
| 1187   | No file  | `2400f7698098`  |
| 1183   | No file  | `2400f7698098`  |
| 1177   | No file  | `2400f7698098`  |
| 1173   | No file  | `2400f7698098`  |
| 1167   | No file  | `2400f7698098`  |
| 1164   | No file  | `2400f7698098`  |
| 1156   | No file  | `2400f7698098`  |
| 1149   | No file  | `2400f7698098`  |
| 1144   | No file  | `2400f7698098`  |
| 1137   | No file  | `2400f7698098`  |
| 1132   | No file  | `2400f7698098`  |
| 1127   | No file  | `2400f7698098`  |
| 1122   | No file  | `2400f7698098`  |
| 1118   | No file  | `2400f7698098`  |
| 1114   | No file  | `2400f7698098`  |
| 1109   | No file  | `2400f7698098`  |
| 1102   | No file  | `2400f7698098`  |
| 1096   | No file  | `2400f7698098`  |
| 1088   | No file  | `2400f7698098`  |
| 1081   | No file  | `2400f7698098`  |
| 1076   | No file  | `2400f7698098`  |
| 1069   | No file  | `2400f7698098`  |
| 1064   | No file  | `2400f7698098`  |
| 1058   | No file  | `2400f7698098`  |
| 1051   | No file  | `2400f7698098`  |
| 1044   | No file  | `2400f7698098`  |
| 1036   | No file  | `2400f7698098`  |
| 1026   | No file  | `2400f7698098`  |
| 1016   | No file  | `2400f7698098`  |
| 1009   | No file  | `2400f7698098`  |
| 1005   | No file  | `2400f7698098`  |
| 1000   | No file  | `2400f7698098`  |
| 998    | No file  | `2400f7698098`  |
| 990    | No file  | `2400f7698098`  |
| 979    | No file  | `2400f7698098`  |
| 972    | No file  | `2400f7698098`  |
| 963    | No file  | `2400f7698098`  |
| 955    | No file  | `2400f7698098`  |
| 946    | No file  | `2400f7698098`  |
| 938    | No file  | `2400f7698098`  |
| 927    | No file  | `2400f7698098`  |
| 911    | No file  | `2400f7698098`  |
| 904    | No file  | `2400f7698098`  |
| 899    | No file  | `2400f7698098`  |
| 894    | No file  | `2400f7698098`  |
| 885    | No file  | `2400f7698098`  |
| 879    | No file  | `2400f7698098`  |
| 872    | No file  | `2400f7698098`  |
| 864    | No file  | `2400f7698098`  |
| 855    | No file  | `2400f7698098`  |
| 853    | No file  | `2400f7698098`  |
| 845    | No file  | `2400f7698098`  |
| 837    | No file  | `2400f7698098`  |
| 829    | No file  | `2400f7698098`  |
| 822    | No file  | `2400f7698098`  |
| 814    | No file  | `2400f7698098`  |
| 805    | No file  | `2400f7698098`  |
| 794    | No file  | `2400f7698098`  |
| 787    | No file  | `2400f7698098`  |
| 780    | No file  | `2400f7698098`  |
| 771    | No file  | `2400f7698098`  |
| 760    | No file  | `2400f7698098`  |
| 748    | No file  | `2400f7698098`  |
| 741    | No file  | `2400f7698098`  |
| 736    | No file  | `2400f7698098`  |
| 731    | No file  | `2400f7698098`  |
| 723    | No file  | `2400f7698098`  |
| 711    | No file  | `2400f7698098`  |
| 707    | No file  | `2400f7698098`  |
| 697    | No file  | `2400f7698098`  |
| 689    | No file  | `2400f7698098`  |
| 683    | No file  | `2400f7698098`  |
| 678    | No file  | `2400f7698098`  |
| 670    | No file  | `2400f7698098`  |
| 661    | No file  | `2400f7698098`  |
| 656    | No file  | `2400f7698098`  |
| 652    | No file  | `2400f7698098`  |
| 643    | No file  | `2400f7698098`  |
| 637    | No file  | `2400f7698098`  |
| 630    | No file  | `2400f7698098`  |
| 627    | No file  | `2400f7698098`  |
| 621    | No file  | `2400f7698098`  |
| 617    | No file  | `2400f7698098`  |
| 615    | No file  | `2400f7698098`  |
| 606    | No file  | `2400f7698098`  |
| 599    | No file  | `2400f7698098`  |
| 592    | No file  | `2400f7698098`  |
| 586    | No file  | `2400f7698098`  |
| 577    | No file  | `2400f7698098`  |
| 569    | No file  | `2400f7698098`  |
| 561    | No file  | `2400f7698098`  |
| 554    | No file  | `2400f7698098`  |
| 542    | No file  | `2400f7698098`  |
| 532    | No file  | `2400f7698098`  |
| 531    | No file  | `2400f7698098`  |
| 526    | No file  | `2400f7698098`  |
| 521    | No file  | `2400f7698098`  |
| 517    | No file  | `2400f7698098`  |
| 510    | No file  | `2400f7698098`  |
| 508    | No file  | `2400f7698098`  |
| 504    | No file  | `2400f7698098`  |
| 497    | No file  | `2400f7698098`  |
| 491    | No file  | `2400f7698098`  |
| 485    | No file  | `2400f7698098`  |
| 478    | No file  | `2400f7698098`  |
| 472    | No file  | `2400f7698098`  |
| 466    | No file  | `2400f7698098`  |
| 457    | No file  | `2400f7698098`  |
| 452    | No file  | `2400f7698098`  |
| 449    | No file  | `2400f7698098`  |
| 435    | No file  | `2400f7698098`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                               |
| --------------------- | -------- | ------------------------------------------------------------------ |
| `boss_spawnlevel.bss` | Optional | The boss character of each key, for the Boss column               |
| `languagedata_en.loc` | Optional | Character names (LOC type 6)                                       |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type       | Field | Notes          |
| ------- | ---------- | ----- | -------------- |
| `+0x00` | u32        | count | Number of rows |
| `+0x04` | Row[count] | rows  | See Row        |

### Row (24 bytes)

| Offset  | Type | Field              | Notes                                                          |
| ------- | ---- | ------------------ | -------------------------------------------------------------- |
| `+0x00` | u32  | boss_spawn_key     | A `boss_spawn.bss` key; `8` down to `1` on client 3474          |
| `+0x04` | f32  | x                  | World position, in the units of the `boss_spawn.bss` point     |
| `+0x08` | f32  | y                  | Height                                                         |
| `+0x0C` | f32  | z                  |                                                                |
| `+0x10` | u32  | boss_spawn_key_dup | Equal to `boss_spawn_key`                                      |
| `+0x14` | f32  | unknown_14         | `20000` on every row of client 3474                            |

The positions on client 3474, against the `boss_spawn.bss` spawn point of
the same key:

| Key | Boss          | x       | z        | Distance to the spawn point (x, z) |
| --- | ------------- | ------- | -------- | ---------------------------------- |
| 8   | Gumiho        | -64376  | 53858    | 0                                  |
| 5   | Khan          | -89743  | 602896   | 12,222                             |
| 4   | Org           | -50574  | -124111  | 1                                  |
| 3   | Giant Mudster | 32259   | -112131  | 0                                  |
| 2   | Moghulis      | 241677  | 15375    | 6,813                              |
| 1   | Ferrid        | 275038  | -29073   | 0                                  |

## Field Names

`boss_spawn_key` is the `bossKey` of the Lua calls above: all 6 keys of
client 3474 are `boss_spawn.bss` keys, and 4 of the 6 points lie within
1 unit of that boss's spawn point (x and z). The file is not in client
1784, and no sheet of a private server's `DataSheets.bexcel` on client 1784
holds it; the 2016 client's debug symbols have no guild boss field type.

## Open Questions

### unknown_14

`20000` on all 6 rows, a f32 after the key's copy. The two points that are
off their spawn point (Khan 12,222 units, Moghulis 6,813) are still within
20,000 units of it, so it may be the radius `ToClient_IsInGuildBossFieldPos`
checks; no Lua reads the value.
