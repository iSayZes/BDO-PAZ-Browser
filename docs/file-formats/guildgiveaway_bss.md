# `guildgiveaway.bss` Format

## Purpose

The items of each Guild Giveaway, the Pearl Shop gift a player buys for
their guild (Button_GuildPearlReward in the guild window): one row per
giveaway key with the items each guild member can collect. On client 3474
the file has 3 rows, keys `10`, `9` and `8`, each with one box
(`[Kind Gesture] Blacksmith's Workshop Box`, `[Kind Gesture] Hero's
Blessing Box` and `Choose Your Spotlight Dance Box`).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                | Bytes | Records       | Row bytes |
| ------ | -------------- | ------- | ------------------- | ----- | ------------- | --------- |
| 1      | 1500 and later | 3483    | `guildgiveaway.bss` | 80    | 3 Item, 3 Row | 12        |

| Layout | File                | Known         | Unknown    |
| ------ | ------------------- | ------------- | ---------- |
| 1      | `guildgiveaway.bss` | 80 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `b5624239b2ad`  |
| 3482   | Layout 1 | `b5624239b2ad`  |
| 3474   | Layout 1 | `b5624239b2ad`  |
| 3473   | Layout 1 | `b5624239b2ad`  |
| 3464   | Layout 1 | `b5624239b2ad`  |
| 3458   | Layout 1 | `b5624239b2ad`  |
| 3454   | Layout 1 | `b5624239b2ad`  |
| 3444   | Layout 1 | `b5624239b2ad`  |
| 3435   | Layout 1 | `b5624239b2ad`  |
| 3426   | Layout 1 | `b5624239b2ad`  |
| 3418   | Layout 1 | `b5624239b2ad`  |
| 3412   | Layout 1 | `b5624239b2ad`  |
| 3402   | Layout 1 | `b5624239b2ad`  |
| 3396   | Layout 1 | `b5624239b2ad`  |
| 3387   | Layout 1 | `b5624239b2ad`  |
| 3381   | Layout 1 | `b5624239b2ad`  |
| 3373   | Layout 1 | `b5624239b2ad`  |
| 3364   | Layout 1 | `b5624239b2ad`  |
| 3356   | Layout 1 | `b5624239b2ad`  |
| 3349   | Layout 1 | `b5624239b2ad`  |
| 3342   | Layout 1 | `b5624239b2ad`  |
| 3335   | Layout 1 | `b5624239b2ad`  |
| 3326   | Layout 1 | `b5624239b2ad`  |
| 3321   | Layout 1 | `b5624239b2ad`  |
| 3314   | Layout 1 | `b5624239b2ad`  |
| 3303   | Layout 1 | `b5624239b2ad`  |
| 3302   | Layout 1 | `b5624239b2ad`  |
| 3293   | Layout 1 | `b5624239b2ad`  |
| 3283   | Layout 1 | `b5624239b2ad`  |
| 3275   | Layout 1 | `b5624239b2ad`  |
| 3267   | Layout 1 | `b5624239b2ad`  |
| 3258   | Layout 1 | `b5624239b2ad`  |
| 3251   | Layout 1 | `b5624239b2ad`  |
| 3242   | Layout 1 | `b5624239b2ad`  |
| 3235   | Layout 1 | `b5624239b2ad`  |
| 3229   | Layout 1 | `b5624239b2ad`  |
| 3212   | Layout 1 | `b5624239b2ad`  |
| 3203   | Layout 1 | `b5624239b2ad`  |
| 3193   | Layout 1 | `b5624239b2ad`  |
| 3186   | Layout 1 | `b5624239b2ad`  |
| 3177   | Layout 1 | `b5624239b2ad`  |
| 3169   | Layout 1 | `b5624239b2ad`  |
| 3158   | Layout 1 | `b5624239b2ad`  |
| 3151   | Layout 1 | `b5624239b2ad`  |
| 3144   | Layout 1 | `b5624239b2ad`  |
| 3133   | Layout 1 | `b5624239b2ad`  |
| 3125   | Layout 1 | `b5624239b2ad`  |
| 3118   | Layout 1 | `b5624239b2ad`  |
| 3111   | Layout 1 | `b5624239b2ad`  |
| 3103   | Layout 1 | `b5624239b2ad`  |
| 3095   | Layout 1 | `b5624239b2ad`  |
| 3086   | Layout 1 | `b5624239b2ad`  |
| 3072   | Layout 1 | `b5624239b2ad`  |
| 3062   | Layout 1 | `b5624239b2ad`  |
| 3052   | Layout 1 | `b5624239b2ad`  |
| 3045   | Layout 1 | `b5624239b2ad`  |
| 3037   | Layout 1 | `b5624239b2ad`  |
| 3030   | Layout 1 | `b5624239b2ad`  |
| 3021   | Layout 1 | `b5624239b2ad`  |
| 3012   | Layout 1 | `b5624239b2ad`  |
| 3002   | Layout 1 | `b5624239b2ad`  |
| 2995   | Layout 1 | `b5624239b2ad`  |
| 2987   | Layout 1 | `b5624239b2ad`  |
| 2978   | Layout 1 | `b5624239b2ad`  |
| 2970   | Layout 1 | `b5624239b2ad`  |
| 2959   | Layout 1 | `b5624239b2ad`  |
| 2951   | Layout 1 | `b5624239b2ad`  |
| 2942   | Layout 1 | `b5624239b2ad`  |
| 2935   | Layout 1 | `b5624239b2ad`  |
| 2932   | Layout 1 | `b5624239b2ad`  |
| 2923   | Layout 1 | `b5624239b2ad`  |
| 2919   | Layout 1 | `b5624239b2ad`  |
| 2907   | Layout 1 | `b5624239b2ad`  |
| 2900   | Layout 1 | `b5624239b2ad`  |
| 2891   | Layout 1 | `b5624239b2ad`  |
| 2882   | Layout 1 | `b5624239b2ad`  |
| 2872   | Layout 1 | `b5624239b2ad`  |
| 2863   | Layout 1 | `b5624239b2ad`  |
| 2855   | Layout 1 | `b5624239b2ad`  |
| 2849   | Layout 1 | `b5624239b2ad`  |
| 2844   | Layout 1 | `b5624239b2ad`  |
| 2834   | Layout 1 | `b5624239b2ad`  |
| 2825   | Layout 1 | `b5624239b2ad`  |
| 2819   | Layout 1 | `b5624239b2ad`  |
| 2811   | Layout 1 | `b5624239b2ad`  |
| 2803   | Layout 1 | `b5624239b2ad`  |
| 2794   | Layout 1 | `b5624239b2ad`  |
| 2783   | Layout 1 | `b5624239b2ad`  |
| 2774   | Layout 1 | `b5624239b2ad`  |
| 2765   | Layout 1 | `b5624239b2ad`  |
| 2756   | Layout 1 | `b5624239b2ad`  |
| 2750   | Layout 1 | `b5624239b2ad`  |
| 2743   | Layout 1 | `b5624239b2ad`  |
| 2736   | Layout 1 | `b5624239b2ad`  |
| 2726   | Layout 1 | `b5624239b2ad`  |
| 2717   | Layout 1 | `b5624239b2ad`  |
| 2709   | Layout 1 | `b5624239b2ad`  |
| 2703   | Layout 1 | `b5624239b2ad`  |
| 2695   | Layout 1 | `b5624239b2ad`  |
| 2684   | Layout 1 | `b5624239b2ad`  |
| 2672   | Layout 1 | `b5624239b2ad`  |
| 2665   | Layout 1 | `b5624239b2ad`  |
| 2657   | Layout 1 | `b5624239b2ad`  |
| 2649   | Layout 1 | `b5624239b2ad`  |
| 2644   | Layout 1 | `b5624239b2ad`  |
| 2637   | Layout 1 | `b5624239b2ad`  |
| 2629   | Layout 1 | `b5624239b2ad`  |
| 2619   | Layout 1 | `b5624239b2ad`  |
| 2612   | Layout 1 | `b5624239b2ad`  |
| 2606   | Layout 1 | `b5624239b2ad`  |
| 2602   | Layout 1 | `b5624239b2ad`  |
| 2601   | Layout 1 | `b5624239b2ad`  |
| 2592   | Layout 1 | `b5624239b2ad`  |
| 2583   | Layout 1 | `b5624239b2ad`  |
| 2575   | Layout 1 | `b5624239b2ad`  |
| 2567   | Layout 1 | `b5624239b2ad`  |
| 2560   | Layout 1 | `b5624239b2ad`  |
| 2553   | Layout 1 | `b5624239b2ad`  |
| 2545   | Layout 1 | `b5624239b2ad`  |
| 2538   | Layout 1 | `b5624239b2ad`  |
| 2529   | Layout 1 | `b5624239b2ad`  |
| 2519   | Layout 1 | `b5624239b2ad`  |
| 2513   | Layout 1 | `b5624239b2ad`  |
| 2510   | Layout 1 | `b5624239b2ad`  |
| 2507   | Layout 1 | `b5624239b2ad`  |
| 2503   | Layout 1 | `b5624239b2ad`  |
| 2498   | Layout 1 | `b5624239b2ad`  |
| 2492   | Layout 1 | `b5624239b2ad`  |
| 2487   | Layout 1 | `b5624239b2ad`  |
| 2480   | Layout 1 | `b5624239b2ad`  |
| 2474   | Layout 1 | `b5624239b2ad`  |
| 2468   | Layout 1 | `b5624239b2ad`  |
| 2460   | Layout 1 | `b5624239b2ad`  |
| 2453   | Layout 1 | `b5624239b2ad`  |
| 2444   | Layout 1 | `b5624239b2ad`  |
| 2438   | Layout 1 | `b5624239b2ad`  |
| 2434   | Layout 1 | `b5624239b2ad`  |
| 2429   | Layout 1 | `b5624239b2ad`  |
| 2421   | Layout 1 | `b5624239b2ad`  |
| 2414   | Layout 1 | `b5624239b2ad`  |
| 2407   | Layout 1 | `b5624239b2ad`  |
| 2401   | Layout 1 | `b5624239b2ad`  |
| 2397   | Layout 1 | `b5624239b2ad`  |
| 2393   | Layout 1 | `b5624239b2ad`  |
| 2384   | Layout 1 | `b5624239b2ad`  |
| 2378   | Layout 1 | `b5624239b2ad`  |
| 2372   | Layout 1 | `b5624239b2ad`  |
| 2358   | Layout 1 | `b5624239b2ad`  |
| 2352   | Layout 1 | `b5624239b2ad`  |
| 2347   | Layout 1 | `b5624239b2ad`  |
| 2343   | Layout 1 | `b5624239b2ad`  |
| 2335   | Layout 1 | `b5624239b2ad`  |
| 2327   | Layout 1 | `b5624239b2ad`  |
| 2324   | Layout 1 | `b5624239b2ad`  |
| 2319   | Layout 1 | `b5624239b2ad`  |
| 2313   | Layout 1 | `b5624239b2ad`  |
| 2308   | Layout 1 | `b5624239b2ad`  |
| 2302   | Layout 1 | `b5624239b2ad`  |
| 2295   | Layout 1 | `b5624239b2ad`  |
| 2290   | Layout 1 | `b5624239b2ad`  |
| 2284   | Layout 1 | `b5624239b2ad`  |
| 2276   | Layout 1 | `b5624239b2ad`  |
| 2269   | Layout 1 | `b5624239b2ad`  |
| 2259   | Layout 1 | `b5624239b2ad`  |
| 2250   | Layout 1 | `b5624239b2ad`  |
| 2243   | Layout 1 | `b5624239b2ad`  |
| 2235   | Layout 1 | `b5624239b2ad`  |
| 2229   | Layout 1 | `b5624239b2ad`  |
| 2224   | Layout 1 | `b5624239b2ad`  |
| 2218   | Layout 1 | `b5624239b2ad`  |
| 2215   | Layout 1 | `b5624239b2ad`  |
| 2207   | Layout 1 | `b5624239b2ad`  |
| 2203   | Layout 1 | `b5624239b2ad`  |
| 2196   | Layout 1 | `b5624239b2ad`  |
| 2192   | Layout 1 | `b5624239b2ad`  |
| 2189   | Layout 1 | `b5624239b2ad`  |
| 2183   | Layout 1 | `b5624239b2ad`  |
| 2179   | Layout 1 | `b5624239b2ad`  |
| 2171   | Layout 1 | `b5624239b2ad`  |
| 2163   | Layout 1 | `b5624239b2ad`  |
| 2156   | Layout 1 | `b5624239b2ad`  |
| 2151   | Layout 1 | `b5624239b2ad`  |
| 2147   | Layout 1 | `b5624239b2ad`  |
| 2142   | Layout 1 | `b5624239b2ad`  |
| 2138   | Layout 1 | `b5624239b2ad`  |
| 2134   | Layout 1 | `b5624239b2ad`  |
| 2130   | Layout 1 | `b5624239b2ad`  |
| 2122   | Layout 1 | `b5624239b2ad`  |
| 2107   | Layout 1 | `b5624239b2ad`  |
| 2098   | Layout 1 | `b5624239b2ad`  |
| 2089   | Layout 1 | `b5624239b2ad`  |
| 2081   | Layout 1 | `b5624239b2ad`  |
| 2073   | Layout 1 | `b5624239b2ad`  |
| 2067   | Layout 1 | `b5624239b2ad`  |
| 2063   | Layout 1 | `b5624239b2ad`  |
| 2059   | Layout 1 | `b5624239b2ad`  |
| 2052   | Layout 1 | `b5624239b2ad`  |
| 2044   | Layout 1 | `b5624239b2ad`  |
| 2039   | Layout 1 | `b5624239b2ad`  |
| 2032   | Layout 1 | `b5624239b2ad`  |
| 2025   | Layout 1 | `b5624239b2ad`  |
| 2011   | Layout 1 | `b5624239b2ad`  |
| 2005   | Layout 1 | `b5624239b2ad`  |
| 2000   | Layout 1 | `b5624239b2ad`  |
| 1996   | Layout 1 | `b5624239b2ad`  |
| 1991   | Layout 1 | `b5624239b2ad`  |
| 1985   | Layout 1 | `b5624239b2ad`  |
| 1980   | Layout 1 | `b5624239b2ad`  |
| 1969   | Layout 1 | `b5624239b2ad`  |
| 1964   | Layout 1 | `b5624239b2ad`  |
| 1958   | Layout 1 | `b5624239b2ad`  |
| 1950   | Layout 1 | `b5624239b2ad`  |
| 1945   | Layout 1 | `b5624239b2ad`  |
| 1937   | Layout 1 | `b5624239b2ad`  |
| 1933   | Layout 1 | `b5624239b2ad`  |
| 1927   | Layout 1 | `b5624239b2ad`  |
| 1921   | Layout 1 | `b5624239b2ad`  |
| 1914   | Layout 1 | `b5624239b2ad`  |
| 1908   | Layout 1 | `b5624239b2ad`  |
| 1897   | Layout 1 | `b5624239b2ad`  |
| 1892   | Layout 1 | `b5624239b2ad`  |
| 1886   | Layout 1 | `b5624239b2ad`  |
| 1881   | Layout 1 | `b5624239b2ad`  |
| 1871   | Layout 1 | `b5624239b2ad`  |
| 1866   | Layout 1 | `b5624239b2ad`  |
| 1862   | Layout 1 | `b5624239b2ad`  |
| 1854   | Layout 1 | `b5624239b2ad`  |
| 1846   | Layout 1 | `b5624239b2ad`  |
| 1838   | Layout 1 | `b5624239b2ad`  |
| 1832   | Layout 1 | `b5624239b2ad`  |
| 1826   | Layout 1 | `b5624239b2ad`  |
| 1822   | Layout 1 | `b5624239b2ad`  |
| 1818   | Layout 1 | `b5624239b2ad`  |
| 1804   | Layout 1 | `b5624239b2ad`  |
| 1794   | Layout 1 | `b5624239b2ad`  |
| 1790   | Layout 1 | `b5624239b2ad`  |
| 1784   | Layout 1 | `b5624239b2ad`  |
| 1774   | Layout 1 | `b5624239b2ad`  |
| 1771   | Layout 1 | `b5624239b2ad`  |
| 1762   | Layout 1 | `b5624239b2ad`  |
| 1759   | Layout 1 | `b5624239b2ad`  |
| 1754   | Layout 1 | `b5624239b2ad`  |
| 1749   | Layout 1 | `b5624239b2ad`  |
| 1743   | Layout 1 | `b5624239b2ad`  |
| 1737   | Layout 1 | `b5624239b2ad`  |
| 1731   | Layout 1 | `b5624239b2ad`  |
| 1725   | Layout 1 | `b5624239b2ad`  |
| 1717   | Layout 1 | `b5624239b2ad`  |
| 1710   | Layout 1 | `b5624239b2ad`  |
| 1704   | Layout 1 | `b5624239b2ad`  |
| 1698   | Layout 1 | `b5624239b2ad`  |
| 1690   | Layout 1 | `b5624239b2ad`  |
| 1685   | Layout 1 | `b5624239b2ad`  |
| 1680   | Layout 1 | `b5624239b2ad`  |
| 1674   | Layout 1 | `b5624239b2ad`  |
| 1668   | Layout 1 | `b5624239b2ad`  |
| 1659   | Layout 1 | `b5624239b2ad`  |
| 1649   | Layout 1 | `b5624239b2ad`  |
| 1642   | Layout 1 | `b5624239b2ad`  |
| 1636   | Layout 1 | `b5624239b2ad`  |
| 1628   | Layout 1 | `b5624239b2ad`  |
| 1622   | Layout 1 | `b5624239b2ad`  |
| 1614   | Layout 1 | `b5624239b2ad`  |
| 1608   | Layout 1 | `b5624239b2ad`  |
| 1602   | Layout 1 | `b5624239b2ad`  |
| 1598   | Layout 1 | `b5624239b2ad`  |
| 1594   | Layout 1 | `b5624239b2ad`  |
| 1590   | Layout 1 | `b5624239b2ad`  |
| 1587   | Layout 1 | `b5624239b2ad`  |
| 1584   | Layout 1 | `b5624239b2ad`  |
| 1579   | Layout 1 | `b5624239b2ad`  |
| 1572   | Layout 1 | `b5624239b2ad`  |
| 1565   | Layout 1 | `b5624239b2ad`  |
| 1559   | Layout 1 | `b5624239b2ad`  |
| 1554   | Layout 1 | `b5624239b2ad`  |
| 1547   | Layout 1 | `b5624239b2ad`  |
| 1537   | Layout 1 | `b5624239b2ad`  |
| 1529   | Layout 1 | `b5624239b2ad`  |
| 1524   | Layout 1 | `b5624239b2ad`  |
| 1519   | Layout 1 | `b5624239b2ad`  |
| 1509   | Layout 1 | `b5624239b2ad`  |
| 1506   | Layout 1 | `b5624239b2ad`  |
| 1504   | Layout 1 | `b5624239b2ad`  |
| 1500   | Layout 1 | `b5624239b2ad`  |
| 1493   | No file  | `b5624239b2ad`  |
| 1489   | No file  | `b5624239b2ad`  |
| 1485   | No file  | `b5624239b2ad`  |
| 1481   | No file  | `b5624239b2ad`  |
| 1474   | No file  | `b5624239b2ad`  |
| 1466   | No file  | `b5624239b2ad`  |
| 1462   | No file  | `b5624239b2ad`  |
| 1459   | No file  | `b5624239b2ad`  |
| 1453   | No file  | `b5624239b2ad`  |
| 1450   | No file  | `b5624239b2ad`  |
| 1445   | No file  | `b5624239b2ad`  |
| 1439   | No file  | `b5624239b2ad`  |
| 1433   | No file  | `b5624239b2ad`  |
| 1430   | No file  | `b5624239b2ad`  |
| 1426   | No file  | `b5624239b2ad`  |
| 1421   | No file  | `b5624239b2ad`  |
| 1417   | No file  | `b5624239b2ad`  |
| 1416   | No file  | `b5624239b2ad`  |
| 1409   | No file  | `b5624239b2ad`  |
| 1405   | No file  | `b5624239b2ad`  |
| 1401   | No file  | `b5624239b2ad`  |
| 1396   | No file  | `b5624239b2ad`  |
| 1391   | No file  | `b5624239b2ad`  |
| 1390   | No file  | `b5624239b2ad`  |
| 1386   | No file  | `b5624239b2ad`  |
| 1381   | No file  | `b5624239b2ad`  |
| 1379   | No file  | `b5624239b2ad`  |
| 1372   | No file  | `b5624239b2ad`  |
| 1366   | No file  | `b5624239b2ad`  |
| 1364   | No file  | `b5624239b2ad`  |
| 1363   | No file  | `b5624239b2ad`  |
| 1360   | No file  | `b5624239b2ad`  |
| 1358   | No file  | `b5624239b2ad`  |
| 1355   | No file  | `b5624239b2ad`  |
| 1351   | No file  | `b5624239b2ad`  |
| 1348   | No file  | `b5624239b2ad`  |
| 1346   | No file  | `b5624239b2ad`  |
| 1341   | No file  | `b5624239b2ad`  |
| 1340   | No file  | `b5624239b2ad`  |
| 1338   | No file  | `b5624239b2ad`  |
| 1335   | No file  | `b5624239b2ad`  |
| 1333   | No file  | `b5624239b2ad`  |
| 1329   | No file  | `b5624239b2ad`  |
| 1327   | No file  | `b5624239b2ad`  |
| 1324   | No file  | `b5624239b2ad`  |
| 1321   | No file  | `b5624239b2ad`  |
| 1319   | No file  | `b5624239b2ad`  |
| 1318   | No file  | `b5624239b2ad`  |
| 1316   | No file  | `b5624239b2ad`  |
| 1313   | No file  | `b5624239b2ad`  |
| 1311   | No file  | `b5624239b2ad`  |
| 1309   | No file  | `b5624239b2ad`  |
| 1304   | No file  | `b5624239b2ad`  |
| 1292   | No file  | `b5624239b2ad`  |
| 1286   | No file  | `b5624239b2ad`  |
| 1280   | No file  | `b5624239b2ad`  |
| 1276   | No file  | `b5624239b2ad`  |
| 1267   | No file  | `b5624239b2ad`  |
| 1261   | No file  | `b5624239b2ad`  |
| 1256   | No file  | `b5624239b2ad`  |
| 1250   | No file  | `b5624239b2ad`  |
| 1246   | No file  | `b5624239b2ad`  |
| 1239   | No file  | `b5624239b2ad`  |
| 1230   | No file  | `b5624239b2ad`  |
| 1226   | No file  | `b5624239b2ad`  |
| 1220   | No file  | `b5624239b2ad`  |
| 1217   | No file  | `b5624239b2ad`  |
| 1211   | No file  | `b5624239b2ad`  |
| 1210   | No file  | `b5624239b2ad`  |
| 1208   | No file  | `b5624239b2ad`  |
| 1203   | No file  | `b5624239b2ad`  |
| 1197   | No file  | `b5624239b2ad`  |
| 1194   | No file  | `b5624239b2ad`  |
| 1192   | No file  | `b5624239b2ad`  |
| 1187   | No file  | `b5624239b2ad`  |
| 1183   | No file  | `b5624239b2ad`  |
| 1177   | No file  | `b5624239b2ad`  |
| 1173   | No file  | `b5624239b2ad`  |
| 1167   | No file  | `b5624239b2ad`  |
| 1164   | No file  | `b5624239b2ad`  |
| 1156   | No file  | `b5624239b2ad`  |
| 1149   | No file  | `b5624239b2ad`  |
| 1144   | No file  | `b5624239b2ad`  |
| 1137   | No file  | `b5624239b2ad`  |
| 1132   | No file  | `b5624239b2ad`  |
| 1127   | No file  | `b5624239b2ad`  |
| 1122   | No file  | `b5624239b2ad`  |
| 1118   | No file  | `b5624239b2ad`  |
| 1114   | No file  | `b5624239b2ad`  |
| 1109   | No file  | `b5624239b2ad`  |
| 1102   | No file  | `b5624239b2ad`  |
| 1096   | No file  | `b5624239b2ad`  |
| 1088   | No file  | `b5624239b2ad`  |
| 1081   | No file  | `b5624239b2ad`  |
| 1076   | No file  | `b5624239b2ad`  |
| 1069   | No file  | `b5624239b2ad`  |
| 1064   | No file  | `b5624239b2ad`  |
| 1058   | No file  | `b5624239b2ad`  |
| 1051   | No file  | `b5624239b2ad`  |
| 1044   | No file  | `b5624239b2ad`  |
| 1036   | No file  | `b5624239b2ad`  |
| 1026   | No file  | `b5624239b2ad`  |
| 1016   | No file  | `b5624239b2ad`  |
| 1009   | No file  | `b5624239b2ad`  |
| 1005   | No file  | `b5624239b2ad`  |
| 1000   | No file  | `b5624239b2ad`  |
| 998    | No file  | `b5624239b2ad`  |
| 990    | No file  | `b5624239b2ad`  |
| 979    | No file  | `b5624239b2ad`  |
| 972    | No file  | `b5624239b2ad`  |
| 963    | No file  | `b5624239b2ad`  |
| 955    | No file  | `b5624239b2ad`  |
| 946    | No file  | `b5624239b2ad`  |
| 938    | No file  | `b5624239b2ad`  |
| 927    | No file  | `b5624239b2ad`  |
| 911    | No file  | `b5624239b2ad`  |
| 904    | No file  | `b5624239b2ad`  |
| 899    | No file  | `b5624239b2ad`  |
| 894    | No file  | `b5624239b2ad`  |
| 885    | No file  | `b5624239b2ad`  |
| 879    | No file  | `b5624239b2ad`  |
| 872    | No file  | `b5624239b2ad`  |
| 864    | No file  | `b5624239b2ad`  |
| 855    | No file  | `b5624239b2ad`  |
| 853    | No file  | `b5624239b2ad`  |
| 845    | No file  | `b5624239b2ad`  |
| 837    | No file  | `b5624239b2ad`  |
| 829    | No file  | `b5624239b2ad`  |
| 822    | No file  | `b5624239b2ad`  |
| 814    | No file  | `b5624239b2ad`  |
| 805    | No file  | `b5624239b2ad`  |
| 794    | No file  | `b5624239b2ad`  |
| 787    | No file  | `b5624239b2ad`  |
| 780    | No file  | `b5624239b2ad`  |
| 771    | No file  | `b5624239b2ad`  |
| 760    | No file  | `b5624239b2ad`  |
| 748    | No file  | `b5624239b2ad`  |
| 741    | No file  | `b5624239b2ad`  |
| 736    | No file  | `b5624239b2ad`  |
| 731    | No file  | `b5624239b2ad`  |
| 723    | No file  | `b5624239b2ad`  |
| 711    | No file  | `b5624239b2ad`  |
| 707    | No file  | `b5624239b2ad`  |
| 697    | No file  | `b5624239b2ad`  |
| 689    | No file  | `b5624239b2ad`  |
| 683    | No file  | `b5624239b2ad`  |
| 678    | No file  | `b5624239b2ad`  |
| 670    | No file  | `b5624239b2ad`  |
| 661    | No file  | `b5624239b2ad`  |
| 656    | No file  | `b5624239b2ad`  |
| 652    | No file  | `b5624239b2ad`  |
| 643    | No file  | `b5624239b2ad`  |
| 637    | No file  | `b5624239b2ad`  |
| 630    | No file  | `b5624239b2ad`  |
| 627    | No file  | `b5624239b2ad`  |
| 621    | No file  | `b5624239b2ad`  |
| 617    | No file  | `b5624239b2ad`  |
| 615    | No file  | `b5624239b2ad`  |
| 606    | No file  | `b5624239b2ad`  |
| 599    | No file  | `b5624239b2ad`  |
| 592    | No file  | `b5624239b2ad`  |
| 586    | No file  | `b5624239b2ad`  |
| 577    | No file  | `b5624239b2ad`  |
| 569    | No file  | `b5624239b2ad`  |
| 561    | No file  | `b5624239b2ad`  |
| 554    | No file  | `b5624239b2ad`  |
| 542    | No file  | `b5624239b2ad`  |
| 532    | No file  | `b5624239b2ad`  |
| 531    | No file  | `b5624239b2ad`  |
| 526    | No file  | `b5624239b2ad`  |
| 521    | No file  | `b5624239b2ad`  |
| 517    | No file  | `b5624239b2ad`  |
| 510    | No file  | `b5624239b2ad`  |
| 508    | No file  | `b5624239b2ad`  |
| 504    | No file  | `b5624239b2ad`  |
| 497    | No file  | `b5624239b2ad`  |
| 491    | No file  | `b5624239b2ad`  |
| 485    | No file  | `b5624239b2ad`  |
| 478    | No file  | `b5624239b2ad`  |
| 472    | No file  | `b5624239b2ad`  |
| 466    | No file  | `b5624239b2ad`  |
| 457    | No file  | `b5624239b2ad`  |
| 452    | No file  | `b5624239b2ad`  |
| 449    | No file  | `b5624239b2ad`  |
| 435    | No file  | `b5624239b2ad`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                       |
| --------------------- | -------- | -------------------------- |
| `languagedata_en.loc` | Optional | Item names, LOC type 0     |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows; `0` on clients 1784 to 3002   |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 8 bytes + items)

| Offset  | Type                   | Field        | Notes                                                       |
| ------- | ---------------------- | ------------ | ----------------------------------------------------------- |
| `+0x00` | u32                    | giveaway_key | Row key; the `getKeyRaw()` of a giveaway in the Lua          |
| `+0x04` | u32                    | entry_count  | Number of items; `1` on every row (client 3474)              |
| `+0x08` | Item[entry_count]      | items        | See Item                                                    |

### Item (12 bytes)

| Offset  | Type | Field       | Notes                                                                       |
| ------- | ---- | ----------- | --------------------------------------------------------------------------- |
| `+0x00` | u32  | item_key    | `enchant_level << 24 \| item_id`, the key of [itemenchant](itemenchant_dbss.md); every level is `0` (client 3474) |
| `+0x04` | u64  | item_count  | Number of items; `1` on every row (client 3474)                              |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

No sheet of a private server's `DataSheets.bexcel` on client 1784 covers
the file; client 1784 ships it with 0 rows. The names follow the client Lua
of client 3474 (`panel_ingamecashshop_guildgiveaway_all_1.luac`): a
giveaway reads its row with `dataWrapper:getKeyRaw()`, then
`ToClient_getGuildGiveawaySelectedListSize(keyRaw)`, and per entry
`ToClient_getGuildGiveawaySelectedItemEnchantKey(keyRaw, i)` (passed to
`getItemEnchantStaticStatus`, so an item key with its level) and
`ToClient_getGuildGiveawaySelectedItemCount(keyRaw, i)`, a 64-bit count.
The window shows one item when the list holds one entry and a list
otherwise.

## Notes

- Client 1784, 2107, 2519 and 3002 ship the file with 0 rows (20 bytes);
  client 3251 has one row (key `8`, Choose Your Spotlight Dance Box), client
  3474 three.
- The giveaway window shows only with the `_ContentsGroup_GuildGiveaway`
  content flag, and says `LUA_GUILDGIVEAWAY_NO_REWARD` when the guild has
  no giveaway to collect.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/guild_tables.py`: the key and each item with its name
  and count.
