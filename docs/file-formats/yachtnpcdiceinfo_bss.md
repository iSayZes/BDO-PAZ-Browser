# `yachtnpcdiceinfo.bss` Format

## Purpose

The NPC opponents of Yar!, a dice minigame (`panel_window_minigame_yachtdice` in the client Lua) that a client 3474 quest text describes as "inspired by Poker and Yacht". Each row is one game setup for one NPC: the dice preset the NPC plays, the hand ranks (scoring combinations) the game offers, the NPC's knowledge entry, the deck limit and how many rolls a turn allows. An NPC can have more than one row. The plain PABR file holds the rows, then an empty string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                   | Bytes | Records | Row bytes               |
| ------ | -------------- | ---------------------- | ----- | ------- | ----------------------- |
| 1      | 1790 and later | `yachtnpcdiceinfo.bss` | 560   | 11 Row  | 44 to 60, 49 on average |

| Layout | File                   | Known          | Unknown    |
| ------ | ---------------------- | -------------- | ---------- |
| 1      | `yachtnpcdiceinfo.bss` | 560 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `b6d079311da1`  |
| 3482   | Layout 1 | `b6d079311da1`  |
| 3474   | Layout 1 | `b6d079311da1`  |
| 3473   | Layout 1 | `b6d079311da1`  |
| 3464   | Layout 1 | `b6d079311da1`  |
| 3458   | Layout 1 | `b6d079311da1`  |
| 3454   | Layout 1 | `b6d079311da1`  |
| 3444   | Layout 1 | `b6d079311da1`  |
| 3435   | Layout 1 | `b6d079311da1`  |
| 3426   | Layout 1 | `b6d079311da1`  |
| 3418   | Layout 1 | `b6d079311da1`  |
| 3412   | Layout 1 | `b6d079311da1`  |
| 3402   | Layout 1 | `b6d079311da1`  |
| 3396   | Layout 1 | `b6d079311da1`  |
| 3387   | Layout 1 | `b6d079311da1`  |
| 3381   | Layout 1 | `b6d079311da1`  |
| 3373   | Layout 1 | `b6d079311da1`  |
| 3364   | Layout 1 | `b6d079311da1`  |
| 3356   | Layout 1 | `b6d079311da1`  |
| 3349   | Layout 1 | `b6d079311da1`  |
| 3342   | Layout 1 | `b6d079311da1`  |
| 3335   | Layout 1 | `b6d079311da1`  |
| 3326   | Layout 1 | `b6d079311da1`  |
| 3321   | Layout 1 | `b6d079311da1`  |
| 3314   | Layout 1 | `b6d079311da1`  |
| 3303   | Layout 1 | `b6d079311da1`  |
| 3302   | Layout 1 | `b6d079311da1`  |
| 3293   | Layout 1 | `b6d079311da1`  |
| 3283   | Layout 1 | `b6d079311da1`  |
| 3275   | Layout 1 | `b6d079311da1`  |
| 3267   | Layout 1 | `b6d079311da1`  |
| 3258   | Layout 1 | `b6d079311da1`  |
| 3251   | Layout 1 | `b6d079311da1`  |
| 3242   | Layout 1 | `b6d079311da1`  |
| 3235   | Layout 1 | `b6d079311da1`  |
| 3229   | Layout 1 | `b6d079311da1`  |
| 3212   | Layout 1 | `b6d079311da1`  |
| 3203   | Layout 1 | `b6d079311da1`  |
| 3193   | Layout 1 | `b6d079311da1`  |
| 3186   | Layout 1 | `b6d079311da1`  |
| 3177   | Layout 1 | `b6d079311da1`  |
| 3169   | Layout 1 | `b6d079311da1`  |
| 3158   | Layout 1 | `b6d079311da1`  |
| 3151   | Layout 1 | `b6d079311da1`  |
| 3144   | Layout 1 | `b6d079311da1`  |
| 3133   | Layout 1 | `b6d079311da1`  |
| 3125   | Layout 1 | `b6d079311da1`  |
| 3118   | Layout 1 | `b6d079311da1`  |
| 3111   | Layout 1 | `b6d079311da1`  |
| 3103   | Layout 1 | `b6d079311da1`  |
| 3095   | Layout 1 | `b6d079311da1`  |
| 3086   | Layout 1 | `b6d079311da1`  |
| 3072   | Layout 1 | `b6d079311da1`  |
| 3062   | Layout 1 | `b6d079311da1`  |
| 3052   | Layout 1 | `b6d079311da1`  |
| 3045   | Layout 1 | `b6d079311da1`  |
| 3037   | Layout 1 | `b6d079311da1`  |
| 3030   | Layout 1 | `b6d079311da1`  |
| 3021   | Layout 1 | `b6d079311da1`  |
| 3012   | Layout 1 | `b6d079311da1`  |
| 3002   | Layout 1 | `b6d079311da1`  |
| 2995   | Layout 1 | `b6d079311da1`  |
| 2987   | Layout 1 | `b6d079311da1`  |
| 2978   | Layout 1 | `b6d079311da1`  |
| 2970   | Layout 1 | `b6d079311da1`  |
| 2959   | Layout 1 | `b6d079311da1`  |
| 2951   | Layout 1 | `b6d079311da1`  |
| 2942   | Layout 1 | `b6d079311da1`  |
| 2935   | Layout 1 | `b6d079311da1`  |
| 2932   | Layout 1 | `b6d079311da1`  |
| 2923   | Layout 1 | `b6d079311da1`  |
| 2919   | Layout 1 | `b6d079311da1`  |
| 2907   | Layout 1 | `b6d079311da1`  |
| 2900   | Layout 1 | `b6d079311da1`  |
| 2891   | Layout 1 | `b6d079311da1`  |
| 2882   | Layout 1 | `b6d079311da1`  |
| 2872   | Layout 1 | `b6d079311da1`  |
| 2863   | Layout 1 | `b6d079311da1`  |
| 2855   | Layout 1 | `b6d079311da1`  |
| 2849   | Layout 1 | `b6d079311da1`  |
| 2844   | Layout 1 | `b6d079311da1`  |
| 2834   | Layout 1 | `b6d079311da1`  |
| 2825   | Layout 1 | `b6d079311da1`  |
| 2819   | Layout 1 | `b6d079311da1`  |
| 2811   | Layout 1 | `b6d079311da1`  |
| 2803   | Layout 1 | `b6d079311da1`  |
| 2794   | Layout 1 | `b6d079311da1`  |
| 2783   | Layout 1 | `b6d079311da1`  |
| 2774   | Layout 1 | `b6d079311da1`  |
| 2765   | Layout 1 | `b6d079311da1`  |
| 2756   | Layout 1 | `b6d079311da1`  |
| 2750   | Layout 1 | `b6d079311da1`  |
| 2743   | Layout 1 | `b6d079311da1`  |
| 2736   | Layout 1 | `b6d079311da1`  |
| 2726   | Layout 1 | `b6d079311da1`  |
| 2717   | Layout 1 | `b6d079311da1`  |
| 2709   | Layout 1 | `b6d079311da1`  |
| 2703   | Layout 1 | `b6d079311da1`  |
| 2695   | Layout 1 | `b6d079311da1`  |
| 2684   | Layout 1 | `b6d079311da1`  |
| 2672   | Layout 1 | `b6d079311da1`  |
| 2665   | Layout 1 | `b6d079311da1`  |
| 2657   | Layout 1 | `b6d079311da1`  |
| 2649   | Layout 1 | `b6d079311da1`  |
| 2644   | Layout 1 | `b6d079311da1`  |
| 2637   | Layout 1 | `b6d079311da1`  |
| 2629   | Layout 1 | `b6d079311da1`  |
| 2619   | Layout 1 | `b6d079311da1`  |
| 2612   | Layout 1 | `b6d079311da1`  |
| 2606   | Layout 1 | `b6d079311da1`  |
| 2602   | Layout 1 | `b6d079311da1`  |
| 2601   | Layout 1 | `b6d079311da1`  |
| 2592   | Layout 1 | `b6d079311da1`  |
| 2583   | Layout 1 | `b6d079311da1`  |
| 2575   | Layout 1 | `b6d079311da1`  |
| 2567   | Layout 1 | `b6d079311da1`  |
| 2560   | Layout 1 | `b6d079311da1`  |
| 2553   | Layout 1 | `b6d079311da1`  |
| 2545   | Layout 1 | `b6d079311da1`  |
| 2538   | Layout 1 | `b6d079311da1`  |
| 2529   | Layout 1 | `b6d079311da1`  |
| 2519   | Layout 1 | `b6d079311da1`  |
| 2513   | Layout 1 | `b6d079311da1`  |
| 2510   | Layout 1 | `b6d079311da1`  |
| 2507   | Layout 1 | `b6d079311da1`  |
| 2503   | Layout 1 | `b6d079311da1`  |
| 2498   | Layout 1 | `b6d079311da1`  |
| 2492   | Layout 1 | `b6d079311da1`  |
| 2487   | Layout 1 | `b6d079311da1`  |
| 2480   | Layout 1 | `b6d079311da1`  |
| 2474   | Layout 1 | `b6d079311da1`  |
| 2468   | Layout 1 | `b6d079311da1`  |
| 2460   | Layout 1 | `b6d079311da1`  |
| 2453   | Layout 1 | `b6d079311da1`  |
| 2444   | Layout 1 | `b6d079311da1`  |
| 2438   | Layout 1 | `b6d079311da1`  |
| 2434   | Layout 1 | `b6d079311da1`  |
| 2429   | Layout 1 | `b6d079311da1`  |
| 2421   | Layout 1 | `b6d079311da1`  |
| 2414   | Layout 1 | `b6d079311da1`  |
| 2407   | Layout 1 | `b6d079311da1`  |
| 2401   | Layout 1 | `b6d079311da1`  |
| 2397   | Layout 1 | `b6d079311da1`  |
| 2393   | Layout 1 | `b6d079311da1`  |
| 2384   | Layout 1 | `b6d079311da1`  |
| 2378   | Layout 1 | `b6d079311da1`  |
| 2372   | Layout 1 | `b6d079311da1`  |
| 2358   | Layout 1 | `b6d079311da1`  |
| 2352   | Layout 1 | `b6d079311da1`  |
| 2347   | Layout 1 | `b6d079311da1`  |
| 2343   | Layout 1 | `b6d079311da1`  |
| 2335   | Layout 1 | `b6d079311da1`  |
| 2327   | Layout 1 | `b6d079311da1`  |
| 2324   | Layout 1 | `b6d079311da1`  |
| 2319   | Layout 1 | `b6d079311da1`  |
| 2313   | Layout 1 | `b6d079311da1`  |
| 2308   | Layout 1 | `b6d079311da1`  |
| 2302   | Layout 1 | `b6d079311da1`  |
| 2295   | Layout 1 | `b6d079311da1`  |
| 2290   | Layout 1 | `b6d079311da1`  |
| 2284   | Layout 1 | `b6d079311da1`  |
| 2276   | Layout 1 | `b6d079311da1`  |
| 2269   | Layout 1 | `b6d079311da1`  |
| 2259   | Layout 1 | `b6d079311da1`  |
| 2250   | Layout 1 | `b6d079311da1`  |
| 2243   | Layout 1 | `b6d079311da1`  |
| 2235   | Layout 1 | `b6d079311da1`  |
| 2229   | Layout 1 | `b6d079311da1`  |
| 2224   | Layout 1 | `b6d079311da1`  |
| 2218   | Layout 1 | `b6d079311da1`  |
| 2215   | Layout 1 | `b6d079311da1`  |
| 2207   | Layout 1 | `b6d079311da1`  |
| 2203   | Layout 1 | `b6d079311da1`  |
| 2196   | Layout 1 | `b6d079311da1`  |
| 2192   | Layout 1 | `b6d079311da1`  |
| 2189   | Layout 1 | `b6d079311da1`  |
| 2183   | Layout 1 | `b6d079311da1`  |
| 2179   | Layout 1 | `b6d079311da1`  |
| 2171   | Layout 1 | `b6d079311da1`  |
| 2163   | Layout 1 | `b6d079311da1`  |
| 2156   | Layout 1 | `b6d079311da1`  |
| 2151   | Layout 1 | `b6d079311da1`  |
| 2147   | Layout 1 | `b6d079311da1`  |
| 2142   | Layout 1 | `b6d079311da1`  |
| 2138   | Layout 1 | `b6d079311da1`  |
| 2134   | Layout 1 | `b6d079311da1`  |
| 2130   | Layout 1 | `b6d079311da1`  |
| 2122   | Layout 1 | `b6d079311da1`  |
| 2107   | Layout 1 | `b6d079311da1`  |
| 2098   | Layout 1 | `b6d079311da1`  |
| 2089   | Layout 1 | `b6d079311da1`  |
| 2081   | Layout 1 | `b6d079311da1`  |
| 2073   | Layout 1 | `b6d079311da1`  |
| 2067   | Layout 1 | `b6d079311da1`  |
| 2063   | Layout 1 | `b6d079311da1`  |
| 2059   | Layout 1 | `b6d079311da1`  |
| 2052   | Layout 1 | `b6d079311da1`  |
| 2044   | Layout 1 | `b6d079311da1`  |
| 2039   | Layout 1 | `b6d079311da1`  |
| 2032   | Layout 1 | `b6d079311da1`  |
| 2025   | Layout 1 | `b6d079311da1`  |
| 2011   | Layout 1 | `b6d079311da1`  |
| 2005   | Layout 1 | `b6d079311da1`  |
| 2000   | Layout 1 | `b6d079311da1`  |
| 1996   | Layout 1 | `b6d079311da1`  |
| 1991   | Layout 1 | `b6d079311da1`  |
| 1985   | Layout 1 | `b6d079311da1`  |
| 1980   | Layout 1 | `b6d079311da1`  |
| 1969   | Layout 1 | `b6d079311da1`  |
| 1964   | Layout 1 | `b6d079311da1`  |
| 1958   | Layout 1 | `b6d079311da1`  |
| 1950   | Layout 1 | `b6d079311da1`  |
| 1945   | Layout 1 | `b6d079311da1`  |
| 1937   | Layout 1 | `b6d079311da1`  |
| 1933   | Layout 1 | `b6d079311da1`  |
| 1927   | Layout 1 | `b6d079311da1`  |
| 1921   | Layout 1 | `b6d079311da1`  |
| 1914   | Layout 1 | `b6d079311da1`  |
| 1908   | Layout 1 | `b6d079311da1`  |
| 1897   | Layout 1 | `b6d079311da1`  |
| 1892   | Layout 1 | `b6d079311da1`  |
| 1886   | Layout 1 | `b6d079311da1`  |
| 1881   | Layout 1 | `b6d079311da1`  |
| 1871   | Layout 1 | `b6d079311da1`  |
| 1866   | Layout 1 | `b6d079311da1`  |
| 1862   | Layout 1 | `b6d079311da1`  |
| 1854   | Layout 1 | `b6d079311da1`  |
| 1846   | Layout 1 | `b6d079311da1`  |
| 1838   | Layout 1 | `b6d079311da1`  |
| 1832   | Layout 1 | `b6d079311da1`  |
| 1826   | Layout 1 | `b6d079311da1`  |
| 1822   | Layout 1 | `b6d079311da1`  |
| 1818   | Layout 1 | `b6d079311da1`  |
| 1804   | Layout 1 | `b6d079311da1`  |
| 1794   | Layout 1 | `b6d079311da1`  |
| 1790   | Layout 1 | `b6d079311da1`  |
| 1784   | No file  | `b6d079311da1`  |
| 1774   | No file  | `b6d079311da1`  |
| 1771   | No file  | `b6d079311da1`  |
| 1762   | No file  | `b6d079311da1`  |
| 1759   | No file  | `b6d079311da1`  |
| 1754   | No file  | `b6d079311da1`  |
| 1749   | No file  | `b6d079311da1`  |
| 1743   | No file  | `b6d079311da1`  |
| 1737   | No file  | `b6d079311da1`  |
| 1731   | No file  | `b6d079311da1`  |
| 1725   | No file  | `b6d079311da1`  |
| 1717   | No file  | `b6d079311da1`  |
| 1710   | No file  | `b6d079311da1`  |
| 1704   | No file  | `b6d079311da1`  |
| 1698   | No file  | `b6d079311da1`  |
| 1690   | No file  | `b6d079311da1`  |
| 1685   | No file  | `b6d079311da1`  |
| 1680   | No file  | `b6d079311da1`  |
| 1674   | No file  | `b6d079311da1`  |
| 1668   | No file  | `b6d079311da1`  |
| 1659   | No file  | `b6d079311da1`  |
| 1649   | No file  | `b6d079311da1`  |
| 1642   | No file  | `b6d079311da1`  |
| 1636   | No file  | `b6d079311da1`  |
| 1628   | No file  | `b6d079311da1`  |
| 1622   | No file  | `b6d079311da1`  |
| 1614   | No file  | `b6d079311da1`  |
| 1608   | No file  | `b6d079311da1`  |
| 1602   | No file  | `b6d079311da1`  |
| 1598   | No file  | `b6d079311da1`  |
| 1594   | No file  | `b6d079311da1`  |
| 1590   | No file  | `b6d079311da1`  |
| 1587   | No file  | `b6d079311da1`  |
| 1584   | No file  | `b6d079311da1`  |
| 1579   | No file  | `b6d079311da1`  |
| 1572   | No file  | `b6d079311da1`  |
| 1565   | No file  | `b6d079311da1`  |
| 1559   | No file  | `b6d079311da1`  |
| 1554   | No file  | `b6d079311da1`  |
| 1547   | No file  | `b6d079311da1`  |
| 1537   | No file  | `b6d079311da1`  |
| 1529   | No file  | `b6d079311da1`  |
| 1524   | No file  | `b6d079311da1`  |
| 1519   | No file  | `b6d079311da1`  |
| 1509   | No file  | `b6d079311da1`  |
| 1506   | No file  | `b6d079311da1`  |
| 1504   | No file  | `b6d079311da1`  |
| 1500   | No file  | `b6d079311da1`  |
| 1493   | No file  | `b6d079311da1`  |
| 1489   | No file  | `b6d079311da1`  |
| 1485   | No file  | `b6d079311da1`  |
| 1481   | No file  | `b6d079311da1`  |
| 1474   | No file  | `b6d079311da1`  |
| 1466   | No file  | `b6d079311da1`  |
| 1462   | No file  | `b6d079311da1`  |
| 1459   | No file  | `b6d079311da1`  |
| 1453   | No file  | `b6d079311da1`  |
| 1450   | No file  | `b6d079311da1`  |
| 1445   | No file  | `b6d079311da1`  |
| 1439   | No file  | `b6d079311da1`  |
| 1433   | No file  | `b6d079311da1`  |
| 1430   | No file  | `b6d079311da1`  |
| 1426   | No file  | `b6d079311da1`  |
| 1421   | No file  | `b6d079311da1`  |
| 1417   | No file  | `b6d079311da1`  |
| 1416   | No file  | `b6d079311da1`  |
| 1409   | No file  | `b6d079311da1`  |
| 1405   | No file  | `b6d079311da1`  |
| 1401   | No file  | `b6d079311da1`  |
| 1396   | No file  | `b6d079311da1`  |
| 1391   | No file  | `b6d079311da1`  |
| 1390   | No file  | `b6d079311da1`  |
| 1386   | No file  | `b6d079311da1`  |
| 1381   | No file  | `b6d079311da1`  |
| 1379   | No file  | `b6d079311da1`  |
| 1372   | No file  | `b6d079311da1`  |
| 1366   | No file  | `b6d079311da1`  |
| 1364   | No file  | `b6d079311da1`  |
| 1363   | No file  | `b6d079311da1`  |
| 1360   | No file  | `b6d079311da1`  |
| 1358   | No file  | `b6d079311da1`  |
| 1355   | No file  | `b6d079311da1`  |
| 1351   | No file  | `b6d079311da1`  |
| 1348   | No file  | `b6d079311da1`  |
| 1346   | No file  | `b6d079311da1`  |
| 1341   | No file  | `b6d079311da1`  |
| 1340   | No file  | `b6d079311da1`  |
| 1338   | No file  | `b6d079311da1`  |
| 1335   | No file  | `b6d079311da1`  |
| 1333   | No file  | `b6d079311da1`  |
| 1329   | No file  | `b6d079311da1`  |
| 1327   | No file  | `b6d079311da1`  |
| 1324   | No file  | `b6d079311da1`  |
| 1321   | No file  | `b6d079311da1`  |
| 1319   | No file  | `b6d079311da1`  |
| 1318   | No file  | `b6d079311da1`  |
| 1316   | No file  | `b6d079311da1`  |
| 1313   | No file  | `b6d079311da1`  |
| 1311   | No file  | `b6d079311da1`  |
| 1309   | No file  | `b6d079311da1`  |
| 1304   | No file  | `b6d079311da1`  |
| 1292   | No file  | `b6d079311da1`  |
| 1286   | No file  | `b6d079311da1`  |
| 1280   | No file  | `b6d079311da1`  |
| 1276   | No file  | `b6d079311da1`  |
| 1267   | No file  | `b6d079311da1`  |
| 1261   | No file  | `b6d079311da1`  |
| 1256   | No file  | `b6d079311da1`  |
| 1250   | No file  | `b6d079311da1`  |
| 1246   | No file  | `b6d079311da1`  |
| 1239   | No file  | `b6d079311da1`  |
| 1230   | No file  | `b6d079311da1`  |
| 1226   | No file  | `b6d079311da1`  |
| 1220   | No file  | `b6d079311da1`  |
| 1217   | No file  | `b6d079311da1`  |
| 1211   | No file  | `b6d079311da1`  |
| 1210   | No file  | `b6d079311da1`  |
| 1208   | No file  | `b6d079311da1`  |
| 1203   | No file  | `b6d079311da1`  |
| 1197   | No file  | `b6d079311da1`  |
| 1194   | No file  | `b6d079311da1`  |
| 1192   | No file  | `b6d079311da1`  |
| 1187   | No file  | `b6d079311da1`  |
| 1183   | No file  | `b6d079311da1`  |
| 1177   | No file  | `b6d079311da1`  |
| 1173   | No file  | `b6d079311da1`  |
| 1167   | No file  | `b6d079311da1`  |
| 1164   | No file  | `b6d079311da1`  |
| 1156   | No file  | `b6d079311da1`  |
| 1149   | No file  | `b6d079311da1`  |
| 1144   | No file  | `b6d079311da1`  |
| 1137   | No file  | `b6d079311da1`  |
| 1132   | No file  | `b6d079311da1`  |
| 1127   | No file  | `b6d079311da1`  |
| 1122   | No file  | `b6d079311da1`  |
| 1118   | No file  | `b6d079311da1`  |
| 1114   | No file  | `b6d079311da1`  |
| 1109   | No file  | `b6d079311da1`  |
| 1102   | No file  | `b6d079311da1`  |
| 1096   | No file  | `b6d079311da1`  |
| 1088   | No file  | `b6d079311da1`  |
| 1081   | No file  | `b6d079311da1`  |
| 1076   | No file  | `b6d079311da1`  |
| 1069   | No file  | `b6d079311da1`  |
| 1064   | No file  | `b6d079311da1`  |
| 1058   | No file  | `b6d079311da1`  |
| 1051   | No file  | `b6d079311da1`  |
| 1044   | No file  | `b6d079311da1`  |
| 1036   | No file  | `b6d079311da1`  |
| 1026   | No file  | `b6d079311da1`  |
| 1016   | No file  | `b6d079311da1`  |
| 1009   | No file  | `b6d079311da1`  |
| 1005   | No file  | `b6d079311da1`  |
| 1000   | No file  | `b6d079311da1`  |
| 998    | No file  | `b6d079311da1`  |
| 990    | No file  | `b6d079311da1`  |
| 979    | No file  | `b6d079311da1`  |
| 972    | No file  | `b6d079311da1`  |
| 963    | No file  | `b6d079311da1`  |
| 955    | No file  | `b6d079311da1`  |
| 946    | No file  | `b6d079311da1`  |
| 938    | No file  | `b6d079311da1`  |
| 927    | No file  | `b6d079311da1`  |
| 911    | No file  | `b6d079311da1`  |
| 904    | No file  | `b6d079311da1`  |
| 899    | No file  | `b6d079311da1`  |
| 894    | No file  | `b6d079311da1`  |
| 885    | No file  | `b6d079311da1`  |
| 879    | No file  | `b6d079311da1`  |
| 872    | No file  | `b6d079311da1`  |
| 864    | No file  | `b6d079311da1`  |
| 855    | No file  | `b6d079311da1`  |
| 853    | No file  | `b6d079311da1`  |
| 845    | No file  | `b6d079311da1`  |
| 837    | No file  | `b6d079311da1`  |
| 829    | No file  | `b6d079311da1`  |
| 822    | No file  | `b6d079311da1`  |
| 814    | No file  | `b6d079311da1`  |
| 805    | No file  | `b6d079311da1`  |
| 794    | No file  | `b6d079311da1`  |
| 787    | No file  | `b6d079311da1`  |
| 780    | No file  | `b6d079311da1`  |
| 771    | No file  | `b6d079311da1`  |
| 760    | No file  | `b6d079311da1`  |
| 748    | No file  | `b6d079311da1`  |
| 741    | No file  | `b6d079311da1`  |
| 736    | No file  | `b6d079311da1`  |
| 731    | No file  | `b6d079311da1`  |
| 723    | No file  | `b6d079311da1`  |
| 711    | No file  | `b6d079311da1`  |
| 707    | No file  | `b6d079311da1`  |
| 697    | No file  | `b6d079311da1`  |
| 689    | No file  | `b6d079311da1`  |
| 683    | No file  | `b6d079311da1`  |
| 678    | No file  | `b6d079311da1`  |
| 670    | No file  | `b6d079311da1`  |
| 661    | No file  | `b6d079311da1`  |
| 656    | No file  | `b6d079311da1`  |
| 652    | No file  | `b6d079311da1`  |
| 643    | No file  | `b6d079311da1`  |
| 637    | No file  | `b6d079311da1`  |
| 630    | No file  | `b6d079311da1`  |
| 627    | No file  | `b6d079311da1`  |
| 621    | No file  | `b6d079311da1`  |
| 617    | No file  | `b6d079311da1`  |
| 615    | No file  | `b6d079311da1`  |
| 606    | No file  | `b6d079311da1`  |
| 599    | No file  | `b6d079311da1`  |
| 592    | No file  | `b6d079311da1`  |
| 586    | No file  | `b6d079311da1`  |
| 577    | No file  | `b6d079311da1`  |
| 569    | No file  | `b6d079311da1`  |
| 561    | No file  | `b6d079311da1`  |
| 554    | No file  | `b6d079311da1`  |
| 542    | No file  | `b6d079311da1`  |
| 532    | No file  | `b6d079311da1`  |
| 531    | No file  | `b6d079311da1`  |
| 526    | No file  | `b6d079311da1`  |
| 521    | No file  | `b6d079311da1`  |
| 517    | No file  | `b6d079311da1`  |
| 510    | No file  | `b6d079311da1`  |
| 508    | No file  | `b6d079311da1`  |
| 504    | No file  | `b6d079311da1`  |
| 497    | No file  | `b6d079311da1`  |
| 491    | No file  | `b6d079311da1`  |
| 485    | No file  | `b6d079311da1`  |
| 478    | No file  | `b6d079311da1`  |
| 472    | No file  | `b6d079311da1`  |
| 466    | No file  | `b6d079311da1`  |
| 457    | No file  | `b6d079311da1`  |
| 452    | No file  | `b6d079311da1`  |
| 449    | No file  | `b6d079311da1`  |
| 435    | No file  | `b6d079311da1`  |

<!-- versions:end -->

## Companion Files

| File                   | Required | Role                                                                                 |
| ---------------------- | -------- | ------------------------------------------------------------------------------------ |
| `yachthandrank.bss`    | Optional | Korean hand rank names, where LOC has none ([`yachthandrank.bss`](yachthandrank_bss.md)) |
| `yachtdicepreset.dbss` | Optional | The five dice of each `dice_preset_key` ([`yachtdicepreset.dbss`](yachtdicepreset_dbss.md)) |
| `languagedata_en.loc`  | Optional | NPC names (LOC type 6 at `str_id1=npc_key`), knowledge names (LOC type 34 at `str_id1=knowledge_key`), hand rank names (LOC type 105 at `str_id1=hand_rank_key`) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type         | Field              | Notes                                         |
| ------------------- | ------------ | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32          | count              | Number of rows                                |
| `+0x08`             | Row[count]   | rows               | Variable-size rows, back to back; see Row     |
| `rows+0x00`         | String Table | string_table       | See String Table                              |
| `string_table+0x00` | u32          | string_table_start | Offset of `string_count`, where the rows end  |
| `string_table+0x04` | u32          | zero               | Always `0`                                    |

The string table has the shape `exploration.bss` and `npcsimply.bss` use (`_common/pabr_strings.py`). Walking `count` rows ends exactly at `string_table_start`.

### Row (variable: 24 bytes + hand ranks)

| Offset            | Type                 | Field             | Notes                                                                   |
| ----------------- | -------------------- | ----------------- | ----------------------------------------------------------------------- |
| `+0x00`           | u32                  | npc_dice_info_key | Unique row key                                                          |
| `+0x04`           | u16                  | npc_key           | Character key of the NPC, LOC type 6 `str_id1`                          |
| `+0x06`           | u32                  | dice_preset_key   | A key of `yachtdicepreset.dbss` (keys 1 to 31 on client 3474)           |
| `+0x0A`           | u64                  | hand_rank_count   | Number of hand ranks                                                    |
| `+0x12`           | u32[hand_rank_count] | hand_rank_keys    | Keys of `yachthandrank.bss` (15 hand ranks on client 3474); ascending on every row (client 3474) |
| `hand_rank_keys+0x00` | u32              | knowledge_key     | The NPC's knowledge entry, LOC type 34 `str_id1`                        |
| `hand_rank_keys+0x04` | u8               | deck_limit        | `150` on every row (client 3474)                                        |
| `hand_rank_keys+0x05` | u8               | roll_count_max    | Rolls per turn; `3` or `4` (client 3474)                                |

`npc_key` sits at `+0x04` with no padding, so `dice_preset_key` and the hand rank list are not 4-byte aligned.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on client 3474          |
| `+0x04` | pstr[string_count] | strings      | No row reads a string                          |

## Rows

On client 3474 the file holds 11 rows for 8 NPCs:

| Key | NPC (`npc_key`)       | Dice preset | Hand ranks | Knowledge (`knowledge_key`) | Rolls |
| --- | --------------------- | ----------- | ---------- | --------------------------- | ----- |
| 1   | Eileen (40063)        | 26          | 1 to 6     | Eileen (45)                 | 3     |
| 2   | Eileen (40063)        | 25          | 1 to 4, 7  | Eileen (45)                 | 3     |
| 3   | Islin Bartali (40001) | 26          | 2, 3, 5, 6, 7 | Islin Bartali (1)        | 3     |
| 4   | Islin Bartali (40001) | 26          | 1, 3, 4, 5, 8 | Islin Bartali (1)        | 3     |
| 5   | Crio (40012)          | 1           | 2 to 5, 7  | Crio (12)                   | 3     |
| 6   | Crio (40012)          | 26          | 1 to 7     | Crio (12)                   | 4     |
| 7   | Igor Bartali (40017)  | 31          | 1 to 6     | Igor Bartali (18)           | 3     |
| 8   | Narangerel (50857)    | 31          | 1 to 4, 6, 7 | Narangerel (1678)         | 3     |
| 9   | Kakuo (59739)         | 31          | 1 to 6     | Kakuo (11155)               | 4     |
| 10  | Shakatu (45120)       | 26          | 1 to 9     | Shakatu (894)               | 4     |
| 11  | Nolbu (47240)         | 26          | 1 to 9     | Nolbu (2003)                | 4     |

On every row the knowledge entry's English name (LOC type 34) is the NPC's English name (LOC type 6).

## Field Names

The `NPC_DiceList` sheet of a private server's `datasheet_minigame.xlsm` on client 1784 has the columns `NpcDiceInfoKey` (`npc_dice_info_key`), `NPCKey` (`npc_key`), `PresetList` (`dice_preset_key`), `HandRankKeyList` (`hand_rank_keys`, one comma-separated list), `DeckLimit` (`deck_limit`), `MentalCardKey` (`knowledge_key`) and `RollCountMax` (`roll_count_max`). Its 7 compiled rows (keys 1 to 7) match rows 1 to 7 of the client 3474 file in every column; the file writes `MentalCardKey` before `DeckLimit`. `PresetList` holds one value per row, the `PresetIndex` of the same workbook's `DicePreset` sheet, and the file stores it as one u32. `HandRankKeyList` names the `HandRankKey` of the `HandRanking` sheet (Ones, Twos, ..., Two of a kind, Full House). The sheet has 10 more rows, commented out with `<주석>`, for NPCs that are not in either client's file.

## Notes

- The client Lua reads the hand ranks through `ToClient_getYachtHandRankKeyList` and the roll limit through `ToClient_getMiniGameYachtCurrentGameRollCountMax` (`panel_window_minigame_yachtdice_1.luac`).
- Every `dice_preset_key` on client 3474 is a key of `yachtdicepresetoffset.dbss`; `test_handler.py` checks it.
- The quote in Purpose is LOC type 37 text from a Narangerel quest: "Yar! is a minigame inspired by Poker and Yacht, and you can challenge various NPCs in the world of Black Desert."
- Client 1784 has no `yachtnpcdiceinfo.bss`. It ships `yachtnpcdiceinfo.dbss` with `yachtnpcdiceinfooffset.dbss` instead: a u32 count, then each row as here with a u32 copy of its key in front, in reverse key order (7 down to 1). The offset file lists key, offset and size per row (`0x30` for row 7, the size this doc's Row gives for 6 hand ranks). Its 7 rows hold the same values as rows 1 to 7 of the client 3474 file.
