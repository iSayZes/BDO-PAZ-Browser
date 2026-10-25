# `musiclevel.dbss` Format

## Purpose

The music (instrument play) levels: per level the music EXP it takes, the
bar and note counts the composer allows at that level and the rank letter
the Music Board shows. The Music Board Lua (`panel_window_musicboard_all_1.luac`)
reads the player's state with `ToClient_GetMusicLevel()` and
`ToClient_GetMusicRank()`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                    | Bytes | Records          | Row bytes               |
| ------ | -------------- | ----------------------- | ----- | ---------------- | ----------------------- |
| 1      | 1346 and later | `musiclevel.dbss`       | 572   | 16 Row, 16 Entry | 30 to 32, 31 on average |
| 1      | 1346 and later | `musicleveloffset.dbss` | 196   | 16 Offset Row    | 12                      |

| Layout | File                    | Known          | Unknown    |
| ------ | ----------------------- | -------------- | ---------- |
| 1      | `musiclevel.dbss`       | 568 B (99.3%)  | 4 B (0.7%) |
| 1      | `musicleveloffset.dbss` | 196 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `71746a3a0ae5`  |
| 3482   | Layout 1 | `71746a3a0ae5`  |
| 3474   | Layout 1 | `71746a3a0ae5`  |
| 3473   | Layout 1 | `71746a3a0ae5`  |
| 3464   | Layout 1 | `71746a3a0ae5`  |
| 3458   | Layout 1 | `71746a3a0ae5`  |
| 3454   | Layout 1 | `71746a3a0ae5`  |
| 3444   | Layout 1 | `71746a3a0ae5`  |
| 3435   | Layout 1 | `71746a3a0ae5`  |
| 3426   | Layout 1 | `71746a3a0ae5`  |
| 3418   | Layout 1 | `71746a3a0ae5`  |
| 3412   | Layout 1 | `71746a3a0ae5`  |
| 3402   | Layout 1 | `71746a3a0ae5`  |
| 3396   | Layout 1 | `71746a3a0ae5`  |
| 3387   | Layout 1 | `71746a3a0ae5`  |
| 3381   | Layout 1 | `71746a3a0ae5`  |
| 3373   | Layout 1 | `71746a3a0ae5`  |
| 3364   | Layout 1 | `71746a3a0ae5`  |
| 3356   | Layout 1 | `71746a3a0ae5`  |
| 3349   | Layout 1 | `71746a3a0ae5`  |
| 3342   | Layout 1 | `71746a3a0ae5`  |
| 3335   | Layout 1 | `71746a3a0ae5`  |
| 3326   | Layout 1 | `71746a3a0ae5`  |
| 3321   | Layout 1 | `71746a3a0ae5`  |
| 3314   | Layout 1 | `71746a3a0ae5`  |
| 3303   | Layout 1 | `71746a3a0ae5`  |
| 3302   | Layout 1 | `71746a3a0ae5`  |
| 3293   | Layout 1 | `71746a3a0ae5`  |
| 3283   | Layout 1 | `71746a3a0ae5`  |
| 3275   | Layout 1 | `71746a3a0ae5`  |
| 3267   | Layout 1 | `71746a3a0ae5`  |
| 3258   | Layout 1 | `71746a3a0ae5`  |
| 3251   | Layout 1 | `71746a3a0ae5`  |
| 3242   | Layout 1 | `71746a3a0ae5`  |
| 3235   | Layout 1 | `71746a3a0ae5`  |
| 3229   | Layout 1 | `71746a3a0ae5`  |
| 3212   | Layout 1 | `71746a3a0ae5`  |
| 3203   | Layout 1 | `71746a3a0ae5`  |
| 3193   | Layout 1 | `71746a3a0ae5`  |
| 3186   | Layout 1 | `71746a3a0ae5`  |
| 3177   | Layout 1 | `71746a3a0ae5`  |
| 3169   | Layout 1 | `71746a3a0ae5`  |
| 3158   | Layout 1 | `71746a3a0ae5`  |
| 3151   | Layout 1 | `71746a3a0ae5`  |
| 3144   | Layout 1 | `71746a3a0ae5`  |
| 3133   | Layout 1 | `71746a3a0ae5`  |
| 3125   | Layout 1 | `71746a3a0ae5`  |
| 3118   | Layout 1 | `71746a3a0ae5`  |
| 3111   | Layout 1 | `71746a3a0ae5`  |
| 3103   | Layout 1 | `71746a3a0ae5`  |
| 3095   | Layout 1 | `71746a3a0ae5`  |
| 3086   | Layout 1 | `71746a3a0ae5`  |
| 3072   | Layout 1 | `71746a3a0ae5`  |
| 3062   | Layout 1 | `71746a3a0ae5`  |
| 3052   | Layout 1 | `71746a3a0ae5`  |
| 3045   | Layout 1 | `71746a3a0ae5`  |
| 3037   | Layout 1 | `71746a3a0ae5`  |
| 3030   | Layout 1 | `71746a3a0ae5`  |
| 3021   | Layout 1 | `71746a3a0ae5`  |
| 3012   | Layout 1 | `71746a3a0ae5`  |
| 3002   | Layout 1 | `71746a3a0ae5`  |
| 2995   | Layout 1 | `71746a3a0ae5`  |
| 2987   | Layout 1 | `71746a3a0ae5`  |
| 2978   | Layout 1 | `71746a3a0ae5`  |
| 2970   | Layout 1 | `71746a3a0ae5`  |
| 2959   | Layout 1 | `71746a3a0ae5`  |
| 2951   | Layout 1 | `71746a3a0ae5`  |
| 2942   | Layout 1 | `71746a3a0ae5`  |
| 2935   | Layout 1 | `71746a3a0ae5`  |
| 2932   | Layout 1 | `71746a3a0ae5`  |
| 2923   | Layout 1 | `71746a3a0ae5`  |
| 2919   | Layout 1 | `71746a3a0ae5`  |
| 2907   | Layout 1 | `71746a3a0ae5`  |
| 2900   | Layout 1 | `71746a3a0ae5`  |
| 2891   | Layout 1 | `71746a3a0ae5`  |
| 2882   | Layout 1 | `71746a3a0ae5`  |
| 2872   | Layout 1 | `71746a3a0ae5`  |
| 2863   | Layout 1 | `71746a3a0ae5`  |
| 2855   | Layout 1 | `71746a3a0ae5`  |
| 2849   | Layout 1 | `71746a3a0ae5`  |
| 2844   | Layout 1 | `71746a3a0ae5`  |
| 2834   | Layout 1 | `71746a3a0ae5`  |
| 2825   | Layout 1 | `71746a3a0ae5`  |
| 2819   | Layout 1 | `71746a3a0ae5`  |
| 2811   | Layout 1 | `71746a3a0ae5`  |
| 2803   | Layout 1 | `71746a3a0ae5`  |
| 2794   | Layout 1 | `71746a3a0ae5`  |
| 2783   | Layout 1 | `71746a3a0ae5`  |
| 2774   | Layout 1 | `71746a3a0ae5`  |
| 2765   | Layout 1 | `71746a3a0ae5`  |
| 2756   | Layout 1 | `71746a3a0ae5`  |
| 2750   | Layout 1 | `71746a3a0ae5`  |
| 2743   | Layout 1 | `71746a3a0ae5`  |
| 2736   | Layout 1 | `71746a3a0ae5`  |
| 2726   | Layout 1 | `71746a3a0ae5`  |
| 2717   | Layout 1 | `71746a3a0ae5`  |
| 2709   | Layout 1 | `71746a3a0ae5`  |
| 2703   | Layout 1 | `71746a3a0ae5`  |
| 2695   | Layout 1 | `71746a3a0ae5`  |
| 2684   | Layout 1 | `71746a3a0ae5`  |
| 2672   | Layout 1 | `71746a3a0ae5`  |
| 2665   | Layout 1 | `71746a3a0ae5`  |
| 2657   | Layout 1 | `71746a3a0ae5`  |
| 2649   | Layout 1 | `71746a3a0ae5`  |
| 2644   | Layout 1 | `71746a3a0ae5`  |
| 2637   | Layout 1 | `71746a3a0ae5`  |
| 2629   | Layout 1 | `71746a3a0ae5`  |
| 2619   | Layout 1 | `71746a3a0ae5`  |
| 2612   | Layout 1 | `71746a3a0ae5`  |
| 2606   | Layout 1 | `71746a3a0ae5`  |
| 2602   | Layout 1 | `71746a3a0ae5`  |
| 2601   | Layout 1 | `71746a3a0ae5`  |
| 2592   | Layout 1 | `71746a3a0ae5`  |
| 2583   | Layout 1 | `71746a3a0ae5`  |
| 2575   | Layout 1 | `71746a3a0ae5`  |
| 2567   | Layout 1 | `71746a3a0ae5`  |
| 2560   | Layout 1 | `71746a3a0ae5`  |
| 2553   | Layout 1 | `71746a3a0ae5`  |
| 2545   | Layout 1 | `71746a3a0ae5`  |
| 2538   | Layout 1 | `71746a3a0ae5`  |
| 2529   | Layout 1 | `71746a3a0ae5`  |
| 2519   | Layout 1 | `71746a3a0ae5`  |
| 2513   | Layout 1 | `71746a3a0ae5`  |
| 2510   | Layout 1 | `71746a3a0ae5`  |
| 2507   | Layout 1 | `71746a3a0ae5`  |
| 2503   | Layout 1 | `71746a3a0ae5`  |
| 2498   | Layout 1 | `71746a3a0ae5`  |
| 2492   | Layout 1 | `71746a3a0ae5`  |
| 2487   | Layout 1 | `71746a3a0ae5`  |
| 2480   | Layout 1 | `71746a3a0ae5`  |
| 2474   | Layout 1 | `71746a3a0ae5`  |
| 2468   | Layout 1 | `71746a3a0ae5`  |
| 2460   | Layout 1 | `71746a3a0ae5`  |
| 2453   | Layout 1 | `71746a3a0ae5`  |
| 2444   | Layout 1 | `71746a3a0ae5`  |
| 2438   | Layout 1 | `71746a3a0ae5`  |
| 2434   | Layout 1 | `71746a3a0ae5`  |
| 2429   | Layout 1 | `71746a3a0ae5`  |
| 2421   | Layout 1 | `71746a3a0ae5`  |
| 2414   | Layout 1 | `71746a3a0ae5`  |
| 2407   | Layout 1 | `71746a3a0ae5`  |
| 2401   | Layout 1 | `71746a3a0ae5`  |
| 2397   | Layout 1 | `71746a3a0ae5`  |
| 2393   | Layout 1 | `71746a3a0ae5`  |
| 2384   | Layout 1 | `71746a3a0ae5`  |
| 2378   | Layout 1 | `71746a3a0ae5`  |
| 2372   | Layout 1 | `71746a3a0ae5`  |
| 2358   | Layout 1 | `71746a3a0ae5`  |
| 2352   | Layout 1 | `71746a3a0ae5`  |
| 2347   | Layout 1 | `71746a3a0ae5`  |
| 2343   | Layout 1 | `71746a3a0ae5`  |
| 2335   | Layout 1 | `71746a3a0ae5`  |
| 2327   | Layout 1 | `71746a3a0ae5`  |
| 2324   | Layout 1 | `71746a3a0ae5`  |
| 2319   | Layout 1 | `71746a3a0ae5`  |
| 2313   | Layout 1 | `71746a3a0ae5`  |
| 2308   | Layout 1 | `71746a3a0ae5`  |
| 2302   | Layout 1 | `71746a3a0ae5`  |
| 2295   | Layout 1 | `71746a3a0ae5`  |
| 2290   | Layout 1 | `71746a3a0ae5`  |
| 2284   | Layout 1 | `71746a3a0ae5`  |
| 2276   | Layout 1 | `71746a3a0ae5`  |
| 2269   | Layout 1 | `71746a3a0ae5`  |
| 2259   | Layout 1 | `71746a3a0ae5`  |
| 2250   | Layout 1 | `71746a3a0ae5`  |
| 2243   | Layout 1 | `71746a3a0ae5`  |
| 2235   | Layout 1 | `71746a3a0ae5`  |
| 2229   | Layout 1 | `71746a3a0ae5`  |
| 2224   | Layout 1 | `71746a3a0ae5`  |
| 2218   | Layout 1 | `71746a3a0ae5`  |
| 2215   | Layout 1 | `71746a3a0ae5`  |
| 2207   | Layout 1 | `71746a3a0ae5`  |
| 2203   | Layout 1 | `71746a3a0ae5`  |
| 2196   | Layout 1 | `71746a3a0ae5`  |
| 2192   | Layout 1 | `71746a3a0ae5`  |
| 2189   | Layout 1 | `71746a3a0ae5`  |
| 2183   | Layout 1 | `71746a3a0ae5`  |
| 2179   | Layout 1 | `71746a3a0ae5`  |
| 2171   | Layout 1 | `71746a3a0ae5`  |
| 2163   | Layout 1 | `71746a3a0ae5`  |
| 2156   | Layout 1 | `71746a3a0ae5`  |
| 2151   | Layout 1 | `71746a3a0ae5`  |
| 2147   | Layout 1 | `71746a3a0ae5`  |
| 2142   | Layout 1 | `71746a3a0ae5`  |
| 2138   | Layout 1 | `71746a3a0ae5`  |
| 2134   | Layout 1 | `71746a3a0ae5`  |
| 2130   | Layout 1 | `71746a3a0ae5`  |
| 2122   | Layout 1 | `71746a3a0ae5`  |
| 2107   | Layout 1 | `71746a3a0ae5`  |
| 2098   | Layout 1 | `71746a3a0ae5`  |
| 2089   | Layout 1 | `71746a3a0ae5`  |
| 2081   | Layout 1 | `71746a3a0ae5`  |
| 2073   | Layout 1 | `71746a3a0ae5`  |
| 2067   | Layout 1 | `71746a3a0ae5`  |
| 2063   | Layout 1 | `71746a3a0ae5`  |
| 2059   | Layout 1 | `71746a3a0ae5`  |
| 2052   | Layout 1 | `71746a3a0ae5`  |
| 2044   | Layout 1 | `71746a3a0ae5`  |
| 2039   | Layout 1 | `71746a3a0ae5`  |
| 2032   | Layout 1 | `71746a3a0ae5`  |
| 2025   | Layout 1 | `71746a3a0ae5`  |
| 2011   | Layout 1 | `71746a3a0ae5`  |
| 2005   | Layout 1 | `71746a3a0ae5`  |
| 2000   | Layout 1 | `71746a3a0ae5`  |
| 1996   | Layout 1 | `71746a3a0ae5`  |
| 1991   | Layout 1 | `71746a3a0ae5`  |
| 1985   | Layout 1 | `71746a3a0ae5`  |
| 1980   | Layout 1 | `71746a3a0ae5`  |
| 1969   | Layout 1 | `71746a3a0ae5`  |
| 1964   | Layout 1 | `71746a3a0ae5`  |
| 1958   | Layout 1 | `71746a3a0ae5`  |
| 1950   | Layout 1 | `71746a3a0ae5`  |
| 1945   | Layout 1 | `71746a3a0ae5`  |
| 1937   | Layout 1 | `71746a3a0ae5`  |
| 1933   | Layout 1 | `71746a3a0ae5`  |
| 1927   | Layout 1 | `71746a3a0ae5`  |
| 1921   | Layout 1 | `71746a3a0ae5`  |
| 1914   | Layout 1 | `71746a3a0ae5`  |
| 1908   | Layout 1 | `71746a3a0ae5`  |
| 1897   | Layout 1 | `71746a3a0ae5`  |
| 1892   | Layout 1 | `71746a3a0ae5`  |
| 1886   | Layout 1 | `71746a3a0ae5`  |
| 1881   | Layout 1 | `71746a3a0ae5`  |
| 1871   | Layout 1 | `71746a3a0ae5`  |
| 1866   | Layout 1 | `71746a3a0ae5`  |
| 1862   | Layout 1 | `71746a3a0ae5`  |
| 1854   | Layout 1 | `71746a3a0ae5`  |
| 1846   | Layout 1 | `71746a3a0ae5`  |
| 1838   | Layout 1 | `71746a3a0ae5`  |
| 1832   | Layout 1 | `71746a3a0ae5`  |
| 1826   | Layout 1 | `71746a3a0ae5`  |
| 1822   | Layout 1 | `71746a3a0ae5`  |
| 1818   | Layout 1 | `71746a3a0ae5`  |
| 1804   | Layout 1 | `71746a3a0ae5`  |
| 1794   | Layout 1 | `71746a3a0ae5`  |
| 1790   | Layout 1 | `71746a3a0ae5`  |
| 1784   | Layout 1 | `71746a3a0ae5`  |
| 1774   | Layout 1 | `71746a3a0ae5`  |
| 1771   | Layout 1 | `71746a3a0ae5`  |
| 1762   | Layout 1 | `71746a3a0ae5`  |
| 1759   | Layout 1 | `71746a3a0ae5`  |
| 1754   | Layout 1 | `71746a3a0ae5`  |
| 1749   | Layout 1 | `71746a3a0ae5`  |
| 1743   | Layout 1 | `71746a3a0ae5`  |
| 1737   | Layout 1 | `71746a3a0ae5`  |
| 1731   | Layout 1 | `71746a3a0ae5`  |
| 1725   | Layout 1 | `71746a3a0ae5`  |
| 1717   | Layout 1 | `71746a3a0ae5`  |
| 1710   | Layout 1 | `71746a3a0ae5`  |
| 1704   | Layout 1 | `71746a3a0ae5`  |
| 1698   | Layout 1 | `71746a3a0ae5`  |
| 1690   | Layout 1 | `71746a3a0ae5`  |
| 1685   | Layout 1 | `71746a3a0ae5`  |
| 1680   | Layout 1 | `71746a3a0ae5`  |
| 1674   | Layout 1 | `71746a3a0ae5`  |
| 1668   | Layout 1 | `71746a3a0ae5`  |
| 1659   | Layout 1 | `71746a3a0ae5`  |
| 1649   | Layout 1 | `71746a3a0ae5`  |
| 1642   | Layout 1 | `71746a3a0ae5`  |
| 1636   | Layout 1 | `71746a3a0ae5`  |
| 1628   | Layout 1 | `71746a3a0ae5`  |
| 1622   | Layout 1 | `71746a3a0ae5`  |
| 1614   | Layout 1 | `71746a3a0ae5`  |
| 1608   | Layout 1 | `71746a3a0ae5`  |
| 1602   | Layout 1 | `71746a3a0ae5`  |
| 1598   | Layout 1 | `71746a3a0ae5`  |
| 1594   | Layout 1 | `71746a3a0ae5`  |
| 1590   | Layout 1 | `71746a3a0ae5`  |
| 1587   | Layout 1 | `71746a3a0ae5`  |
| 1584   | Layout 1 | `71746a3a0ae5`  |
| 1579   | Layout 1 | `71746a3a0ae5`  |
| 1572   | Layout 1 | `71746a3a0ae5`  |
| 1565   | Layout 1 | `71746a3a0ae5`  |
| 1559   | Layout 1 | `71746a3a0ae5`  |
| 1554   | Layout 1 | `71746a3a0ae5`  |
| 1547   | Layout 1 | `71746a3a0ae5`  |
| 1537   | Layout 1 | `71746a3a0ae5`  |
| 1529   | Layout 1 | `71746a3a0ae5`  |
| 1524   | Layout 1 | `71746a3a0ae5`  |
| 1519   | Layout 1 | `71746a3a0ae5`  |
| 1509   | Layout 1 | `71746a3a0ae5`  |
| 1506   | Layout 1 | `71746a3a0ae5`  |
| 1504   | Layout 1 | `71746a3a0ae5`  |
| 1500   | Layout 1 | `71746a3a0ae5`  |
| 1493   | Layout 1 | `71746a3a0ae5`  |
| 1489   | Layout 1 | `71746a3a0ae5`  |
| 1485   | Layout 1 | `71746a3a0ae5`  |
| 1481   | Layout 1 | `71746a3a0ae5`  |
| 1474   | Layout 1 | `71746a3a0ae5`  |
| 1466   | Layout 1 | `71746a3a0ae5`  |
| 1462   | Layout 1 | `71746a3a0ae5`  |
| 1459   | Layout 1 | `71746a3a0ae5`  |
| 1453   | Layout 1 | `71746a3a0ae5`  |
| 1450   | Layout 1 | `71746a3a0ae5`  |
| 1445   | Layout 1 | `71746a3a0ae5`  |
| 1439   | Layout 1 | `71746a3a0ae5`  |
| 1433   | Layout 1 | `71746a3a0ae5`  |
| 1430   | Layout 1 | `71746a3a0ae5`  |
| 1426   | Layout 1 | `71746a3a0ae5`  |
| 1421   | Layout 1 | `71746a3a0ae5`  |
| 1417   | Layout 1 | `71746a3a0ae5`  |
| 1416   | Layout 1 | `71746a3a0ae5`  |
| 1409   | Layout 1 | `71746a3a0ae5`  |
| 1405   | Layout 1 | `71746a3a0ae5`  |
| 1401   | Layout 1 | `71746a3a0ae5`  |
| 1396   | Layout 1 | `71746a3a0ae5`  |
| 1391   | Layout 1 | `71746a3a0ae5`  |
| 1390   | Layout 1 | `71746a3a0ae5`  |
| 1386   | Layout 1 | `71746a3a0ae5`  |
| 1381   | Layout 1 | `71746a3a0ae5`  |
| 1379   | Layout 1 | `71746a3a0ae5`  |
| 1372   | Layout 1 | `71746a3a0ae5`  |
| 1366   | Layout 1 | `71746a3a0ae5`  |
| 1364   | Layout 1 | `71746a3a0ae5`  |
| 1363   | Layout 1 | `71746a3a0ae5`  |
| 1360   | Layout 1 | `71746a3a0ae5`  |
| 1358   | Layout 1 | `71746a3a0ae5`  |
| 1355   | Layout 1 | `71746a3a0ae5`  |
| 1351   | Layout 1 | `71746a3a0ae5`  |
| 1348   | Layout 1 | `71746a3a0ae5`  |
| 1346   | Layout 1 | `71746a3a0ae5`  |
| 1341   | No file  | `71746a3a0ae5`  |
| 1340   | No file  | `71746a3a0ae5`  |
| 1338   | No file  | `71746a3a0ae5`  |
| 1335   | No file  | `71746a3a0ae5`  |
| 1333   | No file  | `71746a3a0ae5`  |
| 1329   | No file  | `71746a3a0ae5`  |
| 1327   | No file  | `71746a3a0ae5`  |
| 1324   | No file  | `71746a3a0ae5`  |
| 1321   | No file  | `71746a3a0ae5`  |
| 1319   | No file  | `71746a3a0ae5`  |
| 1318   | No file  | `71746a3a0ae5`  |
| 1316   | No file  | `71746a3a0ae5`  |
| 1313   | No file  | `71746a3a0ae5`  |
| 1311   | No file  | `71746a3a0ae5`  |
| 1309   | No file  | `71746a3a0ae5`  |
| 1304   | No file  | `71746a3a0ae5`  |
| 1292   | No file  | `71746a3a0ae5`  |
| 1286   | No file  | `71746a3a0ae5`  |
| 1280   | No file  | `71746a3a0ae5`  |
| 1276   | No file  | `71746a3a0ae5`  |
| 1267   | No file  | `71746a3a0ae5`  |
| 1261   | No file  | `71746a3a0ae5`  |
| 1256   | No file  | `71746a3a0ae5`  |
| 1250   | No file  | `71746a3a0ae5`  |
| 1246   | No file  | `71746a3a0ae5`  |
| 1239   | No file  | `71746a3a0ae5`  |
| 1230   | No file  | `71746a3a0ae5`  |
| 1226   | No file  | `71746a3a0ae5`  |
| 1220   | No file  | `71746a3a0ae5`  |
| 1217   | No file  | `71746a3a0ae5`  |
| 1211   | No file  | `71746a3a0ae5`  |
| 1210   | No file  | `71746a3a0ae5`  |
| 1208   | No file  | `71746a3a0ae5`  |
| 1203   | No file  | `71746a3a0ae5`  |
| 1197   | No file  | `71746a3a0ae5`  |
| 1194   | No file  | `71746a3a0ae5`  |
| 1192   | No file  | `71746a3a0ae5`  |
| 1187   | No file  | `71746a3a0ae5`  |
| 1183   | No file  | `71746a3a0ae5`  |
| 1177   | No file  | `71746a3a0ae5`  |
| 1173   | No file  | `71746a3a0ae5`  |
| 1167   | No file  | `71746a3a0ae5`  |
| 1164   | No file  | `71746a3a0ae5`  |
| 1156   | No file  | `71746a3a0ae5`  |
| 1149   | No file  | `71746a3a0ae5`  |
| 1144   | No file  | `71746a3a0ae5`  |
| 1137   | No file  | `71746a3a0ae5`  |
| 1132   | No file  | `71746a3a0ae5`  |
| 1127   | No file  | `71746a3a0ae5`  |
| 1122   | No file  | `71746a3a0ae5`  |
| 1118   | No file  | `71746a3a0ae5`  |
| 1114   | No file  | `71746a3a0ae5`  |
| 1109   | No file  | `71746a3a0ae5`  |
| 1102   | No file  | `71746a3a0ae5`  |
| 1096   | No file  | `71746a3a0ae5`  |
| 1088   | No file  | `71746a3a0ae5`  |
| 1081   | No file  | `71746a3a0ae5`  |
| 1076   | No file  | `71746a3a0ae5`  |
| 1069   | No file  | `71746a3a0ae5`  |
| 1064   | No file  | `71746a3a0ae5`  |
| 1058   | No file  | `71746a3a0ae5`  |
| 1051   | No file  | `71746a3a0ae5`  |
| 1044   | No file  | `71746a3a0ae5`  |
| 1036   | No file  | `71746a3a0ae5`  |
| 1026   | No file  | `71746a3a0ae5`  |
| 1016   | No file  | `71746a3a0ae5`  |
| 1009   | No file  | `71746a3a0ae5`  |
| 1005   | No file  | `71746a3a0ae5`  |
| 1000   | No file  | `71746a3a0ae5`  |
| 998    | No file  | `71746a3a0ae5`  |
| 990    | No file  | `71746a3a0ae5`  |
| 979    | No file  | `71746a3a0ae5`  |
| 972    | No file  | `71746a3a0ae5`  |
| 963    | No file  | `71746a3a0ae5`  |
| 955    | No file  | `71746a3a0ae5`  |
| 946    | No file  | `71746a3a0ae5`  |
| 938    | No file  | `71746a3a0ae5`  |
| 927    | No file  | `71746a3a0ae5`  |
| 911    | No file  | `71746a3a0ae5`  |
| 904    | No file  | `71746a3a0ae5`  |
| 899    | No file  | `71746a3a0ae5`  |
| 894    | No file  | `71746a3a0ae5`  |
| 885    | No file  | `71746a3a0ae5`  |
| 879    | No file  | `71746a3a0ae5`  |
| 872    | No file  | `71746a3a0ae5`  |
| 864    | No file  | `71746a3a0ae5`  |
| 855    | No file  | `71746a3a0ae5`  |
| 853    | No file  | `71746a3a0ae5`  |
| 845    | No file  | `71746a3a0ae5`  |
| 837    | No file  | `71746a3a0ae5`  |
| 829    | No file  | `71746a3a0ae5`  |
| 822    | No file  | `71746a3a0ae5`  |
| 814    | No file  | `71746a3a0ae5`  |
| 805    | No file  | `71746a3a0ae5`  |
| 794    | No file  | `71746a3a0ae5`  |
| 787    | No file  | `71746a3a0ae5`  |
| 780    | No file  | `71746a3a0ae5`  |
| 771    | No file  | `71746a3a0ae5`  |
| 760    | No file  | `71746a3a0ae5`  |
| 748    | No file  | `71746a3a0ae5`  |
| 741    | No file  | `71746a3a0ae5`  |
| 736    | No file  | `71746a3a0ae5`  |
| 731    | No file  | `71746a3a0ae5`  |
| 723    | No file  | `71746a3a0ae5`  |
| 711    | No file  | `71746a3a0ae5`  |
| 707    | No file  | `71746a3a0ae5`  |
| 697    | No file  | `71746a3a0ae5`  |
| 689    | No file  | `71746a3a0ae5`  |
| 683    | No file  | `71746a3a0ae5`  |
| 678    | No file  | `71746a3a0ae5`  |
| 670    | No file  | `71746a3a0ae5`  |
| 661    | No file  | `71746a3a0ae5`  |
| 656    | No file  | `71746a3a0ae5`  |
| 652    | No file  | `71746a3a0ae5`  |
| 643    | No file  | `71746a3a0ae5`  |
| 637    | No file  | `71746a3a0ae5`  |
| 630    | No file  | `71746a3a0ae5`  |
| 627    | No file  | `71746a3a0ae5`  |
| 621    | No file  | `71746a3a0ae5`  |
| 617    | No file  | `71746a3a0ae5`  |
| 615    | No file  | `71746a3a0ae5`  |
| 606    | No file  | `71746a3a0ae5`  |
| 599    | No file  | `71746a3a0ae5`  |
| 592    | No file  | `71746a3a0ae5`  |
| 586    | No file  | `71746a3a0ae5`  |
| 577    | No file  | `71746a3a0ae5`  |
| 569    | No file  | `71746a3a0ae5`  |
| 561    | No file  | `71746a3a0ae5`  |
| 554    | No file  | `71746a3a0ae5`  |
| 542    | No file  | `71746a3a0ae5`  |
| 532    | No file  | `71746a3a0ae5`  |
| 531    | No file  | `71746a3a0ae5`  |
| 526    | No file  | `71746a3a0ae5`  |
| 521    | No file  | `71746a3a0ae5`  |
| 517    | No file  | `71746a3a0ae5`  |
| 510    | No file  | `71746a3a0ae5`  |
| 508    | No file  | `71746a3a0ae5`  |
| 504    | No file  | `71746a3a0ae5`  |
| 497    | No file  | `71746a3a0ae5`  |
| 491    | No file  | `71746a3a0ae5`  |
| 485    | No file  | `71746a3a0ae5`  |
| 478    | No file  | `71746a3a0ae5`  |
| 472    | No file  | `71746a3a0ae5`  |
| 466    | No file  | `71746a3a0ae5`  |
| 457    | No file  | `71746a3a0ae5`  |
| 452    | No file  | `71746a3a0ae5`  |
| 449    | No file  | `71746a3a0ae5`  |
| 435    | No file  | `71746a3a0ae5`  |

<!-- versions:end -->

## Companion Files

| File                    | Required | Role                                                                                    |
| ----------------------- | -------- | --------------------------------------------------------------------------------------- |
| `musicleveloffset.dbss` | Optional | `music_level -> (data_offset, data_size)` of every row; the parser walks the main file without it |

All multi-byte values are little-endian.

## Layout 1

### File Layout

No `PABR` magic. Two counts, then the entries back to back to the end of
the file.

| Offset  | Type         | Field      | Notes                                                              |
| ------- | ------------ | ---------- | ------------------------------------------------------------------ |
| `+0x00` | u32          | count      | Number of entries                                                  |
| `+0x04` | u32          | unknown_04 | Equals `count` and the highest `music_level` on clients 1784 and 3482 |
| `+0x08` | Entry[count] | entries    | See Entry                                                          |

### Entry (variable: 4 bytes + row)

| Offset  | Type | Field       | Notes                                                                      |
| ------- | ---- | ----------- | -------------------------------------------------------------------------- |
| `+0x00` | u32  | key_prefix  | Equals the row's `music_level`; the offset index points past it           |
| `+0x04` | Row  | row         | See Row                                                                    |

### Row (variable: 28 bytes + rank text)

| Offset  | Type  | Field                   | Notes                                                                 |
| ------- | ----- | ----------------------- | --------------------------------------------------------------------- |
| `+0x00` | u32   | music_level             | Row key, `1` to `16` in order on client 3482                          |
| `+0x04` | u64   | music_level_exp         | Music EXP of the level                                                |
| `+0x0C` | u32   | increasing_bar_number   | `30` at level 1 to `100` at level 6 (clients 1784 and 3482)           |
| `+0x10` | u32   | increasing_note_number  | `500` at level 1 to `1200` at level 6 (clients 1784 and 3482)         |
| `+0x14` | str16 | music_rank              | Rank letter (`F`, `D-`, `C`, `S+`)                                    |

### `musicleveloffset.dbss`

No `PABR` magic and no trailer: a count, then one row per level.

| Offset  | Type              | Field | Notes                       |
| ------- | ----------------- | ----- | --------------------------- |
| `+0x00` | u32               | count | Equals `musiclevel.dbss` count |
| `+0x04` | Offset Row[count] | rows  | See Offset Row              |

### Offset Row (12 bytes)

| Offset  | Type | Field       | Notes                                                        |
| ------- | ---- | ----------- | ------------------------------------------------------------ |
| `+0x00` | u32  | music_level | Row key                                                      |
| `+0x04` | u32  | data_offset | Where the Row starts in `musiclevel.dbss`, past `key_prefix` |
| `+0x08` | u32  | data_size   | Length of the Row                                            |

## Levels

Client 3482 holds 16 levels, client 1784 the first six with the same
values:

| Level | EXP           | Bars | Notes | Rank |
| ----- | ------------- | ---- | ----- | ---- |
| 1     | 72            | 30   | 500   | F    |
| 2     | 108           | 34   | 555   | D-   |
| 3     | 162           | 42   | 665   | D    |
| 4     | 243           | 54   | 830   | D+   |
| 5     | 364           | 70   | 1050  | C-   |
| 6     | 546           | 100  | 1200  | C    |
| 7     | 546,750       | 101  | 1201  | C+   |
| 8     | 1,366,875     | 102  | 1202  | B-   |
| 9     | 3,417,187     | 103  | 1203  | B    |
| 10    | 8,542,968     | 104  | 1204  | B+   |
| 11    | 17,085,937    | 105  | 1205  | A-   |
| 12    | 34,171,875    | 106  | 1206  | A    |
| 13    | 68,343,750    | 107  | 1207  | A+   |
| 14    | 136,687,500   | 108  | 1208  | S-   |
| 15    | 273,375,000   | 109  | 1209  | S    |
| 16    | 546,750,000   | 110  | 1210  | S+   |

Level 7 holds 1,000 times the sheet value of level 6 (`546.75`); levels 8
to 10 take 2.5 times the level before, levels 11 to 16 twice (rounded
down).

## Field Names

The `MusicLevel` sheet of a private server's `DataSheets.bexcel` on client
1784 has the columns `MusicLevel`, `MusicLevelEXPTable`,
`IncreasingBarNumber`, `IncreasingNoteNumber` and `MusicRank`, one row per
level. All five match on 6 of 6 levels (client 1784) and on the same six
levels of client 3482. The sheet writes `364.5` and `546.75` for levels 5
and 6; the file holds the integer part.

## Open Questions

### Second Count

`unknown_04` equals `count` and the highest level on both clients. A file
with a gap in its levels would tell a count from a maximum level.
