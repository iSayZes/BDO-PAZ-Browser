# `yachtgameboardinfo.bss` Format

## Purpose

The game boards (modes) of a Yar! match between two players, picked in the
invite window (`panel_window_minigame_yachtdice_invite_1.luac`). Each row is
one board: the [`yachthandrank.bss`](yachthandrank_bss.md) hand ranks it
plays, how many rolls a turn allows, its difficulty level (stars), its
Korean description, its icon textures and whether it uses matchmaking. The
plain PABR file holds the rows, then the string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                     | Bytes | Records | Row bytes               |
| ------ | -------------- | ------------------------ | ----- | ------- | ----------------------- |
| 2      | 2855 and later | `yachtgameboardinfo.bss` | 2,523 | 9 Row   | 54 to 90, 68 on average |
| 1      | 1762 to 2849   | `yachtgameboardinfo.bss` | 2,220 | 8 Row   | 53 to 89, 64 on average |

| Layout | File                     | Known            | Unknown    |
| ------ | ------------------------ | ---------------- | ---------- |
| 2      | `yachtgameboardinfo.bss` | 2,523 B (100.0%) | 0 B (0.0%) |
| 1      | `yachtgameboardinfo.bss` | 2,220 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `aecd47ff219f`  |
| 3482   | Layout 2             | `aecd47ff219f`  |
| 3474   | Layout 2             | `aecd47ff219f`  |
| 3473   | Layout 2             | `aecd47ff219f`  |
| 3464   | Layout 2             | `aecd47ff219f`  |
| 3458   | Layout 2             | `aecd47ff219f`  |
| 3454   | Layout 2             | `aecd47ff219f`  |
| 3444   | Layout 2             | `aecd47ff219f`  |
| 3435   | Layout 2             | `aecd47ff219f`  |
| 3426   | Layout 2             | `aecd47ff219f`  |
| 3418   | Layout 2             | `aecd47ff219f`  |
| 3412   | Layout 2             | `aecd47ff219f`  |
| 3402   | Layout 2             | `aecd47ff219f`  |
| 3396   | Layout 2             | `aecd47ff219f`  |
| 3387   | Layout 2             | `aecd47ff219f`  |
| 3381   | Layout 2             | `aecd47ff219f`  |
| 3373   | Layout 2             | `aecd47ff219f`  |
| 3364   | Layout 2             | `aecd47ff219f`  |
| 3356   | Layout 2             | `aecd47ff219f`  |
| 3349   | Layout 2             | `aecd47ff219f`  |
| 3342   | Layout 2             | `aecd47ff219f`  |
| 3335   | Layout 2             | `aecd47ff219f`  |
| 3326   | Layout 2             | `aecd47ff219f`  |
| 3321   | Layout 2             | `aecd47ff219f`  |
| 3314   | Layout 2             | `aecd47ff219f`  |
| 3303   | Layout 2             | `aecd47ff219f`  |
| 3302   | Layout 2             | `aecd47ff219f`  |
| 3293   | Layout 2             | `aecd47ff219f`  |
| 3283   | Layout 2             | `aecd47ff219f`  |
| 3275   | Layout 2             | `aecd47ff219f`  |
| 3267   | Layout 2             | `aecd47ff219f`  |
| 3258   | Layout 2             | `aecd47ff219f`  |
| 3251   | Layout 2             | `aecd47ff219f`  |
| 3242   | Layout 2             | `aecd47ff219f`  |
| 3235   | Layout 2             | `aecd47ff219f`  |
| 3229   | Layout 2             | `aecd47ff219f`  |
| 3212   | Layout 2             | `aecd47ff219f`  |
| 3203   | Layout 2             | `aecd47ff219f`  |
| 3193   | Layout 2             | `aecd47ff219f`  |
| 3186   | Layout 2             | `aecd47ff219f`  |
| 3177   | Layout 2             | `aecd47ff219f`  |
| 3169   | Layout 2             | `aecd47ff219f`  |
| 3158   | Layout 2             | `aecd47ff219f`  |
| 3151   | Layout 2             | `aecd47ff219f`  |
| 3144   | Layout 2             | `aecd47ff219f`  |
| 3133   | Layout 2             | `aecd47ff219f`  |
| 3125   | Layout 2             | `aecd47ff219f`  |
| 3118   | Layout 2             | `aecd47ff219f`  |
| 3111   | Layout 2             | `aecd47ff219f`  |
| 3103   | Layout 2             | `aecd47ff219f`  |
| 3095   | Layout 2             | `aecd47ff219f`  |
| 3086   | Layout 2             | `aecd47ff219f`  |
| 3072   | Layout 2             | `aecd47ff219f`  |
| 3062   | Layout 2             | `aecd47ff219f`  |
| 3052   | Layout 2             | `aecd47ff219f`  |
| 3045   | Layout 2             | `aecd47ff219f`  |
| 3037   | Layout 2             | `aecd47ff219f`  |
| 3030   | Layout 2             | `aecd47ff219f`  |
| 3021   | Layout 2             | `aecd47ff219f`  |
| 3012   | Layout 2             | `aecd47ff219f`  |
| 3002   | Layout 2             | `aecd47ff219f`  |
| 2995   | Layout 2             | `aecd47ff219f`  |
| 2987   | Layout 2             | `aecd47ff219f`  |
| 2978   | Layout 2             | `aecd47ff219f`  |
| 2970   | Layout 2             | `aecd47ff219f`  |
| 2959   | Layout 2             | `aecd47ff219f`  |
| 2951   | Layout 2             | `aecd47ff219f`  |
| 2942   | Layout 2             | `aecd47ff219f`  |
| 2935   | Layout 2             | `aecd47ff219f`  |
| 2932   | Layout 2             | `aecd47ff219f`  |
| 2923   | Layout 2             | `aecd47ff219f`  |
| 2919   | Layout 2             | `aecd47ff219f`  |
| 2907   | Layout 2             | `aecd47ff219f`  |
| 2900   | Layout 2             | `aecd47ff219f`  |
| 2891   | Layout 2             | `aecd47ff219f`  |
| 2882   | Layout 2             | `aecd47ff219f`  |
| 2872   | Layout 2             | `aecd47ff219f`  |
| 2863   | Layout 2             | `aecd47ff219f`  |
| 2855   | Layout 2             | `aecd47ff219f`  |
| 2849   | Layout 1             | `aecd47ff219f`  |
| 2844   | Layout 1             | `aecd47ff219f`  |
| 2834   | Layout 1             | `aecd47ff219f`  |
| 2825   | Layout 1             | `aecd47ff219f`  |
| 2819   | Layout 1             | `aecd47ff219f`  |
| 2811   | Layout 1             | `aecd47ff219f`  |
| 2803   | Layout 1             | `aecd47ff219f`  |
| 2794   | Layout 1             | `aecd47ff219f`  |
| 2783   | Layout 1             | `aecd47ff219f`  |
| 2774   | Layout 1             | `aecd47ff219f`  |
| 2765   | Layout 1             | `aecd47ff219f`  |
| 2756   | Layout 1             | `aecd47ff219f`  |
| 2750   | Layout 1             | `aecd47ff219f`  |
| 2743   | Layout 1             | `aecd47ff219f`  |
| 2736   | Layout 1             | `aecd47ff219f`  |
| 2726   | Layout 1             | `aecd47ff219f`  |
| 2717   | Layout 1             | `aecd47ff219f`  |
| 2709   | Layout 1             | `aecd47ff219f`  |
| 2703   | Layout 1             | `aecd47ff219f`  |
| 2695   | Layout 1             | `aecd47ff219f`  |
| 2684   | Layout 1             | `aecd47ff219f`  |
| 2672   | Layout 1             | `aecd47ff219f`  |
| 2665   | Layout 1             | `aecd47ff219f`  |
| 2657   | Layout 1             | `aecd47ff219f`  |
| 2649   | Layout 1             | `aecd47ff219f`  |
| 2644   | Layout 1             | `aecd47ff219f`  |
| 2637   | Layout 1             | `aecd47ff219f`  |
| 2629   | Layout 1             | `aecd47ff219f`  |
| 2619   | Layout 1             | `aecd47ff219f`  |
| 2612   | Layout 1             | `aecd47ff219f`  |
| 2606   | Layout 1             | `aecd47ff219f`  |
| 2602   | Layout 1             | `aecd47ff219f`  |
| 2601   | Layout 1             | `aecd47ff219f`  |
| 2592   | Layout 1             | `aecd47ff219f`  |
| 2583   | Layout 1             | `aecd47ff219f`  |
| 2575   | Layout 1             | `aecd47ff219f`  |
| 2567   | Layout 1             | `aecd47ff219f`  |
| 2560   | Layout 1             | `aecd47ff219f`  |
| 2553   | Layout 1             | `aecd47ff219f`  |
| 2545   | Layout 1             | `aecd47ff219f`  |
| 2538   | Layout 1             | `aecd47ff219f`  |
| 2529   | Layout 1             | `aecd47ff219f`  |
| 2519   | Layout 1             | `aecd47ff219f`  |
| 2513   | Layout 1             | `aecd47ff219f`  |
| 2510   | Layout 1             | `aecd47ff219f`  |
| 2507   | Layout 1             | `aecd47ff219f`  |
| 2503   | Layout 1             | `aecd47ff219f`  |
| 2498   | Layout 1             | `aecd47ff219f`  |
| 2492   | Layout 1             | `aecd47ff219f`  |
| 2487   | Layout 1             | `aecd47ff219f`  |
| 2480   | Layout 1             | `aecd47ff219f`  |
| 2474   | Layout 1             | `aecd47ff219f`  |
| 2468   | Layout 1             | `aecd47ff219f`  |
| 2460   | Layout 1             | `aecd47ff219f`  |
| 2453   | Layout 1             | `aecd47ff219f`  |
| 2444   | Layout 1             | `aecd47ff219f`  |
| 2438   | Layout 1             | `aecd47ff219f`  |
| 2434   | Layout 1             | `aecd47ff219f`  |
| 2429   | Layout 1             | `aecd47ff219f`  |
| 2421   | Layout 1             | `aecd47ff219f`  |
| 2414   | Layout 1             | `aecd47ff219f`  |
| 2407   | Layout 1             | `aecd47ff219f`  |
| 2401   | Layout 1             | `aecd47ff219f`  |
| 2397   | Layout 1             | `aecd47ff219f`  |
| 2393   | Layout 1             | `aecd47ff219f`  |
| 2384   | Layout 1             | `aecd47ff219f`  |
| 2378   | Layout 1             | `aecd47ff219f`  |
| 2372   | Layout 1             | `aecd47ff219f`  |
| 2358   | Layout 1             | `aecd47ff219f`  |
| 2352   | Layout 1             | `aecd47ff219f`  |
| 2347   | Layout 1             | `aecd47ff219f`  |
| 2343   | Layout 1             | `aecd47ff219f`  |
| 2335   | Layout 1             | `aecd47ff219f`  |
| 2327   | Layout 1             | `aecd47ff219f`  |
| 2324   | Layout 1             | `aecd47ff219f`  |
| 2319   | Layout 1             | `aecd47ff219f`  |
| 2313   | Layout 1             | `aecd47ff219f`  |
| 2308   | Layout 1             | `aecd47ff219f`  |
| 2302   | Layout 1             | `aecd47ff219f`  |
| 2295   | Layout 1             | `aecd47ff219f`  |
| 2290   | Layout 1             | `aecd47ff219f`  |
| 2284   | Layout 1             | `aecd47ff219f`  |
| 2276   | Layout 1             | `aecd47ff219f`  |
| 2269   | Layout 1             | `aecd47ff219f`  |
| 2259   | Layout 1             | `aecd47ff219f`  |
| 2250   | Layout 1             | `aecd47ff219f`  |
| 2243   | Layout 1             | `aecd47ff219f`  |
| 2235   | Layout 1             | `aecd47ff219f`  |
| 2229   | Layout 1             | `aecd47ff219f`  |
| 2224   | Layout 1             | `aecd47ff219f`  |
| 2218   | Layout 1             | `aecd47ff219f`  |
| 2215   | Layout 1             | `aecd47ff219f`  |
| 2207   | Layout 1             | `aecd47ff219f`  |
| 2203   | Layout 1             | `aecd47ff219f`  |
| 2196   | Layout 1             | `aecd47ff219f`  |
| 2192   | Layout 1             | `aecd47ff219f`  |
| 2189   | Layout 1             | `aecd47ff219f`  |
| 2183   | Layout 1             | `aecd47ff219f`  |
| 2179   | Layout 1             | `aecd47ff219f`  |
| 2171   | Layout 1             | `aecd47ff219f`  |
| 2163   | Layout 1             | `aecd47ff219f`  |
| 2156   | Layout 1             | `aecd47ff219f`  |
| 2151   | Layout 1             | `aecd47ff219f`  |
| 2147   | Layout 1             | `aecd47ff219f`  |
| 2142   | Layout 1             | `aecd47ff219f`  |
| 2138   | Layout 1             | `aecd47ff219f`  |
| 2134   | Layout 1             | `aecd47ff219f`  |
| 2130   | Layout 1             | `aecd47ff219f`  |
| 2122   | Layout 1             | `aecd47ff219f`  |
| 2107   | Layout 1             | `aecd47ff219f`  |
| 2098   | Layout 1             | `aecd47ff219f`  |
| 2089   | Layout 1             | `aecd47ff219f`  |
| 2081   | Layout 1             | `aecd47ff219f`  |
| 2073   | Layout 1             | `aecd47ff219f`  |
| 2067   | Layout 1             | `aecd47ff219f`  |
| 2063   | Layout 1             | `aecd47ff219f`  |
| 2059   | Layout 1             | `aecd47ff219f`  |
| 2052   | Layout 1             | `aecd47ff219f`  |
| 2044   | Layout 1             | `aecd47ff219f`  |
| 2039   | Layout 1             | `aecd47ff219f`  |
| 2032   | Layout 1             | `aecd47ff219f`  |
| 2025   | Layout 1             | `aecd47ff219f`  |
| 2011   | Layout 1             | `aecd47ff219f`  |
| 2005   | Layout 1             | `aecd47ff219f`  |
| 2000   | Layout 1             | `aecd47ff219f`  |
| 1996   | Layout 1             | `aecd47ff219f`  |
| 1991   | Layout 1             | `aecd47ff219f`  |
| 1985   | Layout 1             | `aecd47ff219f`  |
| 1980   | Layout 1             | `aecd47ff219f`  |
| 1969   | Layout 1             | `aecd47ff219f`  |
| 1964   | Layout 1             | `aecd47ff219f`  |
| 1958   | Layout 1             | `aecd47ff219f`  |
| 1950   | Layout 1             | `aecd47ff219f`  |
| 1945   | Layout 1             | `aecd47ff219f`  |
| 1937   | Layout 1             | `aecd47ff219f`  |
| 1933   | Layout 1             | `aecd47ff219f`  |
| 1927   | Layout 1             | `aecd47ff219f`  |
| 1921   | Layout 1             | `aecd47ff219f`  |
| 1914   | Layout 1             | `aecd47ff219f`  |
| 1908   | Layout 1             | `aecd47ff219f`  |
| 1897   | Layout 1             | `aecd47ff219f`  |
| 1892   | Layout 1             | `aecd47ff219f`  |
| 1886   | Layout 1             | `aecd47ff219f`  |
| 1881   | Layout 1             | `aecd47ff219f`  |
| 1871   | Layout 1             | `aecd47ff219f`  |
| 1866   | Layout 1             | `aecd47ff219f`  |
| 1862   | Layout 1             | `aecd47ff219f`  |
| 1854   | Layout 1             | `aecd47ff219f`  |
| 1846   | Layout 1             | `aecd47ff219f`  |
| 1838   | Layout 1             | `aecd47ff219f`  |
| 1832   | Layout 1             | `aecd47ff219f`  |
| 1826   | Layout 1             | `aecd47ff219f`  |
| 1822   | Layout 1             | `aecd47ff219f`  |
| 1818   | Layout 1             | `aecd47ff219f`  |
| 1804   | Layout 1             | `aecd47ff219f`  |
| 1794   | Layout 1             | `aecd47ff219f`  |
| 1790   | Layout 1             | `aecd47ff219f`  |
| 1784   | Layout 1             | `aecd47ff219f`  |
| 1774   | Layout 1             | `aecd47ff219f`  |
| 1771   | Layout 1             | `aecd47ff219f`  |
| 1762   | Layout 1             | `aecd47ff219f`  |
| 1759   | No documented layout | `aecd47ff219f`  |
| 1754   | No documented layout | `aecd47ff219f`  |
| 1749   | No documented layout | `aecd47ff219f`  |
| 1743   | No documented layout | `aecd47ff219f`  |
| 1737   | No file              | `aecd47ff219f`  |
| 1731   | No file              | `aecd47ff219f`  |
| 1725   | No file              | `aecd47ff219f`  |
| 1717   | No file              | `aecd47ff219f`  |
| 1710   | No file              | `aecd47ff219f`  |
| 1704   | No file              | `aecd47ff219f`  |
| 1698   | No file              | `aecd47ff219f`  |
| 1690   | No file              | `aecd47ff219f`  |
| 1685   | No file              | `aecd47ff219f`  |
| 1680   | No file              | `aecd47ff219f`  |
| 1674   | No file              | `aecd47ff219f`  |
| 1668   | No file              | `aecd47ff219f`  |
| 1659   | No file              | `aecd47ff219f`  |
| 1649   | No file              | `aecd47ff219f`  |
| 1642   | No file              | `aecd47ff219f`  |
| 1636   | No file              | `aecd47ff219f`  |
| 1628   | No file              | `aecd47ff219f`  |
| 1622   | No file              | `aecd47ff219f`  |
| 1614   | No file              | `aecd47ff219f`  |
| 1608   | No file              | `aecd47ff219f`  |
| 1602   | No file              | `aecd47ff219f`  |
| 1598   | No file              | `aecd47ff219f`  |
| 1594   | No file              | `aecd47ff219f`  |
| 1590   | No file              | `aecd47ff219f`  |
| 1587   | No file              | `aecd47ff219f`  |
| 1584   | No file              | `aecd47ff219f`  |
| 1579   | No file              | `aecd47ff219f`  |
| 1572   | No file              | `aecd47ff219f`  |
| 1565   | No file              | `aecd47ff219f`  |
| 1559   | No file              | `aecd47ff219f`  |
| 1554   | No file              | `aecd47ff219f`  |
| 1547   | No file              | `aecd47ff219f`  |
| 1537   | No file              | `aecd47ff219f`  |
| 1529   | No file              | `aecd47ff219f`  |
| 1524   | No file              | `aecd47ff219f`  |
| 1519   | No file              | `aecd47ff219f`  |
| 1509   | No file              | `aecd47ff219f`  |
| 1506   | No file              | `aecd47ff219f`  |
| 1504   | No file              | `aecd47ff219f`  |
| 1500   | No file              | `aecd47ff219f`  |
| 1493   | No file              | `aecd47ff219f`  |
| 1489   | No file              | `aecd47ff219f`  |
| 1485   | No file              | `aecd47ff219f`  |
| 1481   | No file              | `aecd47ff219f`  |
| 1474   | No file              | `aecd47ff219f`  |
| 1466   | No file              | `aecd47ff219f`  |
| 1462   | No file              | `aecd47ff219f`  |
| 1459   | No file              | `aecd47ff219f`  |
| 1453   | No file              | `aecd47ff219f`  |
| 1450   | No file              | `aecd47ff219f`  |
| 1445   | No file              | `aecd47ff219f`  |
| 1439   | No file              | `aecd47ff219f`  |
| 1433   | No file              | `aecd47ff219f`  |
| 1430   | No file              | `aecd47ff219f`  |
| 1426   | No file              | `aecd47ff219f`  |
| 1421   | No file              | `aecd47ff219f`  |
| 1417   | No file              | `aecd47ff219f`  |
| 1416   | No file              | `aecd47ff219f`  |
| 1409   | No file              | `aecd47ff219f`  |
| 1405   | No file              | `aecd47ff219f`  |
| 1401   | No file              | `aecd47ff219f`  |
| 1396   | No file              | `aecd47ff219f`  |
| 1391   | No file              | `aecd47ff219f`  |
| 1390   | No file              | `aecd47ff219f`  |
| 1386   | No file              | `aecd47ff219f`  |
| 1381   | No file              | `aecd47ff219f`  |
| 1379   | No file              | `aecd47ff219f`  |
| 1372   | No file              | `aecd47ff219f`  |
| 1366   | No file              | `aecd47ff219f`  |
| 1364   | No file              | `aecd47ff219f`  |
| 1363   | No file              | `aecd47ff219f`  |
| 1360   | No file              | `aecd47ff219f`  |
| 1358   | No file              | `aecd47ff219f`  |
| 1355   | No file              | `aecd47ff219f`  |
| 1351   | No file              | `aecd47ff219f`  |
| 1348   | No file              | `aecd47ff219f`  |
| 1346   | No file              | `aecd47ff219f`  |
| 1341   | No file              | `aecd47ff219f`  |
| 1340   | No file              | `aecd47ff219f`  |
| 1338   | No file              | `aecd47ff219f`  |
| 1335   | No file              | `aecd47ff219f`  |
| 1333   | No file              | `aecd47ff219f`  |
| 1329   | No file              | `aecd47ff219f`  |
| 1327   | No file              | `aecd47ff219f`  |
| 1324   | No file              | `aecd47ff219f`  |
| 1321   | No file              | `aecd47ff219f`  |
| 1319   | No file              | `aecd47ff219f`  |
| 1318   | No file              | `aecd47ff219f`  |
| 1316   | No file              | `aecd47ff219f`  |
| 1313   | No file              | `aecd47ff219f`  |
| 1311   | No file              | `aecd47ff219f`  |
| 1309   | No file              | `aecd47ff219f`  |
| 1304   | No file              | `aecd47ff219f`  |
| 1292   | No file              | `aecd47ff219f`  |
| 1286   | No file              | `aecd47ff219f`  |
| 1280   | No file              | `aecd47ff219f`  |
| 1276   | No file              | `aecd47ff219f`  |
| 1267   | No file              | `aecd47ff219f`  |
| 1261   | No file              | `aecd47ff219f`  |
| 1256   | No file              | `aecd47ff219f`  |
| 1250   | No file              | `aecd47ff219f`  |
| 1246   | No file              | `aecd47ff219f`  |
| 1239   | No file              | `aecd47ff219f`  |
| 1230   | No file              | `aecd47ff219f`  |
| 1226   | No file              | `aecd47ff219f`  |
| 1220   | No file              | `aecd47ff219f`  |
| 1217   | No file              | `aecd47ff219f`  |
| 1211   | No file              | `aecd47ff219f`  |
| 1210   | No file              | `aecd47ff219f`  |
| 1208   | No file              | `aecd47ff219f`  |
| 1203   | No file              | `aecd47ff219f`  |
| 1197   | No file              | `aecd47ff219f`  |
| 1194   | No file              | `aecd47ff219f`  |
| 1192   | No file              | `aecd47ff219f`  |
| 1187   | No file              | `aecd47ff219f`  |
| 1183   | No file              | `aecd47ff219f`  |
| 1177   | No file              | `aecd47ff219f`  |
| 1173   | No file              | `aecd47ff219f`  |
| 1167   | No file              | `aecd47ff219f`  |
| 1164   | No file              | `aecd47ff219f`  |
| 1156   | No file              | `aecd47ff219f`  |
| 1149   | No file              | `aecd47ff219f`  |
| 1144   | No file              | `aecd47ff219f`  |
| 1137   | No file              | `aecd47ff219f`  |
| 1132   | No file              | `aecd47ff219f`  |
| 1127   | No file              | `aecd47ff219f`  |
| 1122   | No file              | `aecd47ff219f`  |
| 1118   | No file              | `aecd47ff219f`  |
| 1114   | No file              | `aecd47ff219f`  |
| 1109   | No file              | `aecd47ff219f`  |
| 1102   | No file              | `aecd47ff219f`  |
| 1096   | No file              | `aecd47ff219f`  |
| 1088   | No file              | `aecd47ff219f`  |
| 1081   | No file              | `aecd47ff219f`  |
| 1076   | No file              | `aecd47ff219f`  |
| 1069   | No file              | `aecd47ff219f`  |
| 1064   | No file              | `aecd47ff219f`  |
| 1058   | No file              | `aecd47ff219f`  |
| 1051   | No file              | `aecd47ff219f`  |
| 1044   | No file              | `aecd47ff219f`  |
| 1036   | No file              | `aecd47ff219f`  |
| 1026   | No file              | `aecd47ff219f`  |
| 1016   | No file              | `aecd47ff219f`  |
| 1009   | No file              | `aecd47ff219f`  |
| 1005   | No file              | `aecd47ff219f`  |
| 1000   | No file              | `aecd47ff219f`  |
| 998    | No file              | `aecd47ff219f`  |
| 990    | No file              | `aecd47ff219f`  |
| 979    | No file              | `aecd47ff219f`  |
| 972    | No file              | `aecd47ff219f`  |
| 963    | No file              | `aecd47ff219f`  |
| 955    | No file              | `aecd47ff219f`  |
| 946    | No file              | `aecd47ff219f`  |
| 938    | No file              | `aecd47ff219f`  |
| 927    | No file              | `aecd47ff219f`  |
| 911    | No file              | `aecd47ff219f`  |
| 904    | No file              | `aecd47ff219f`  |
| 899    | No file              | `aecd47ff219f`  |
| 894    | No file              | `aecd47ff219f`  |
| 885    | No file              | `aecd47ff219f`  |
| 879    | No file              | `aecd47ff219f`  |
| 872    | No file              | `aecd47ff219f`  |
| 864    | No file              | `aecd47ff219f`  |
| 855    | No file              | `aecd47ff219f`  |
| 853    | No file              | `aecd47ff219f`  |
| 845    | No file              | `aecd47ff219f`  |
| 837    | No file              | `aecd47ff219f`  |
| 829    | No file              | `aecd47ff219f`  |
| 822    | No file              | `aecd47ff219f`  |
| 814    | No file              | `aecd47ff219f`  |
| 805    | No file              | `aecd47ff219f`  |
| 794    | No file              | `aecd47ff219f`  |
| 787    | No file              | `aecd47ff219f`  |
| 780    | No file              | `aecd47ff219f`  |
| 771    | No file              | `aecd47ff219f`  |
| 760    | No file              | `aecd47ff219f`  |
| 748    | No file              | `aecd47ff219f`  |
| 741    | No file              | `aecd47ff219f`  |
| 736    | No file              | `aecd47ff219f`  |
| 731    | No file              | `aecd47ff219f`  |
| 723    | No file              | `aecd47ff219f`  |
| 711    | No file              | `aecd47ff219f`  |
| 707    | No file              | `aecd47ff219f`  |
| 697    | No file              | `aecd47ff219f`  |
| 689    | No file              | `aecd47ff219f`  |
| 683    | No file              | `aecd47ff219f`  |
| 678    | No file              | `aecd47ff219f`  |
| 670    | No file              | `aecd47ff219f`  |
| 661    | No file              | `aecd47ff219f`  |
| 656    | No file              | `aecd47ff219f`  |
| 652    | No file              | `aecd47ff219f`  |
| 643    | No file              | `aecd47ff219f`  |
| 637    | No file              | `aecd47ff219f`  |
| 630    | No file              | `aecd47ff219f`  |
| 627    | No file              | `aecd47ff219f`  |
| 621    | No file              | `aecd47ff219f`  |
| 617    | No file              | `aecd47ff219f`  |
| 615    | No file              | `aecd47ff219f`  |
| 606    | No file              | `aecd47ff219f`  |
| 599    | No file              | `aecd47ff219f`  |
| 592    | No file              | `aecd47ff219f`  |
| 586    | No file              | `aecd47ff219f`  |
| 577    | No file              | `aecd47ff219f`  |
| 569    | No file              | `aecd47ff219f`  |
| 561    | No file              | `aecd47ff219f`  |
| 554    | No file              | `aecd47ff219f`  |
| 542    | No file              | `aecd47ff219f`  |
| 532    | No file              | `aecd47ff219f`  |
| 531    | No file              | `aecd47ff219f`  |
| 526    | No file              | `aecd47ff219f`  |
| 521    | No file              | `aecd47ff219f`  |
| 517    | No file              | `aecd47ff219f`  |
| 510    | No file              | `aecd47ff219f`  |
| 508    | No file              | `aecd47ff219f`  |
| 504    | No file              | `aecd47ff219f`  |
| 497    | No file              | `aecd47ff219f`  |
| 491    | No file              | `aecd47ff219f`  |
| 485    | No file              | `aecd47ff219f`  |
| 478    | No file              | `aecd47ff219f`  |
| 472    | No file              | `aecd47ff219f`  |
| 466    | No file              | `aecd47ff219f`  |
| 457    | No file              | `aecd47ff219f`  |
| 452    | No file              | `aecd47ff219f`  |
| 449    | No file              | `aecd47ff219f`  |
| 435    | No file              | `aecd47ff219f`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                                     |
| --------------------- | -------- | ---------------------------------------------------------------------------------------- |
| `yachthandrank.bss`   | Optional | Korean hand rank names, where LOC has none                                               |
| `languagedata_en.loc` | Optional | Board descriptions (LOC type 109, `str_id1=game_board_key`), hand rank names (LOC type 105) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type         | Field              | Notes                                        |
| ------------------- | ------------ | ------------------ | -------------------------------------------- |
| `+0x00`             | char[4]      | magic              | ASCII `PABR`                                 |
| `+0x04`             | u32          | count              | Number of rows                               |
| `+0x08`             | Row[count]   | rows               | Variable-size rows, back to back; see Row    |
| `rows+0x00`         | String Table | string_table       | See String Table                             |
| `string_table+0x00` | u32          | string_table_start | Offset of `string_count`, where the rows end |
| `string_table+0x04` | u32          | zero               | Always `0`                                   |

The string table has the shape `exploration.bss` and `npcsimply.bss` use
(`_common/pabr_strings.py`). Walking `count` rows ends exactly at
`string_table_start`.

### Row (variable: 30 bytes + hand ranks)

| Offset                | Type                 | Field              | Notes                                                              |
| --------------------- | -------------------- | ------------------ | ------------------------------------------------------------------ |
| `+0x00`               | u32                  | game_board_key     | Unique row key, LOC type 109 `str_id1`                             |
| `+0x04`               | u64                  | hand_rank_count    | Number of hand ranks                                               |
| `+0x0C`               | u32[hand_rank_count] | hand_rank_keys     | Keys of `yachthandrank.bss`, in sheet order (not always ascending) |
| `hand_rank_keys+0x00` | u8                   | roll_count_max     | Rolls per turn; `3` or `4` (client 3474)                           |
| `hand_rank_keys+0x01` | u32                  | desc_kr_index      | String table index of the Korean description                       |
| `hand_rank_keys+0x05` | u32                  | icon_texture_index | String table index of the icon's texture ID (`Combine_ETC_MiniGame_Ya_pvp_Card01`) |
| `hand_rank_keys+0x09` | u32                  | big_texture_index  | String table index of the large picture's texture ID (`Combine_ETC_MiniGame_Ya_pvp_Big_Card01`) |
| `hand_rank_keys+0x0D` | u32                  | level              | Difficulty, drawn as that many stars; `1` to `5`                   |
| `hand_rank_keys+0x11` | u8                   | is_use_matching    | `1` when the board offers matchmaking against a stranger           |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                       |
| ------- | ------------------ | ------------ | ----------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; three per row (27 on client 3474)        |
| `+0x04` | pstr[string_count] | strings      | Per row its description (UTF-16) and two texture IDs (UTF-8) |

## Layout 1

Client 1784 rows have no `is_use_matching`.

### Row (variable: 29 bytes + hand ranks)

| Offset                | Type                 | Field              | Notes                                      |
| --------------------- | -------------------- | ------------------ | ------------------------------------------ |
| `+0x00`               | u32                  | game_board_key     | Unique row key                             |
| `+0x04`               | u64                  | hand_rank_count    | Number of hand ranks                       |
| `+0x0C`               | u32[hand_rank_count] | hand_rank_keys     | Keys of `yachthandrank.bss`                |
| `hand_rank_keys+0x00` | u8                   | roll_count_max     | Rolls per turn                             |
| `hand_rank_keys+0x01` | u32                  | desc_kr_index      | String table index of the Korean description |
| `hand_rank_keys+0x05` | u32                  | icon_texture_index | String table index of the icon's texture ID |
| `hand_rank_keys+0x09` | u32                  | big_texture_index  | String table index of the large picture's texture ID |
| `hand_rank_keys+0x0D` | u32                  | level              | Difficulty, drawn as that many stars       |

## Game Boards

On client 3474 the file holds 9 rows. The descriptions are the first
sentence of the LOC type 109 English text.

| Key | Level | Hand ranks               | Rolls | Matchmaking | Description                                     |
| --- | ----- | ------------------------ | ----- | ----------- | ----------------------------------------------- |
| 1   | 1     | 1 to 6, 15               | 3     | No          | The most basic mode.                            |
| 2   | 2     | 1, 3, 5, 8, 14, 15       | 3     | No          | A mode with only odd-numbered hands.            |
| 3   | 2     | 2, 4, 6, 7, 9, 13, 15    | 3     | No          | A mode with only even-numbered hands.           |
| 4   | 3     | 1 to 6, 10, 11, 15       | 3     | No          | A mode with numbered hands, Double Trouble, and Den of Wolves. |
| 5   | 3     | 1 to 3, 10, 11, 13 to 15 | 3     | No          | A mode that values low-numbered hands.          |
| 6   | 4     | 1 to 6, 13 to 15         | 4     | No          | A mode with numbered hands, Broken Arrow, and Straight Shot. |
| 7   | 4     | 7 to 11, 13 to 15, 12    | 4     | No          | A mode without single-numbered hands.           |
| 8   | 5     | 1 to 11, 13 to 15, 12    | 4     | No          | A mode with all Yar! hands available.           |
| 9   | 5     | 1 to 11, 13 to 15, 12    | 4     | Yes         | A mode with all Yar! hands available.           |

Rows 7 to 9 list hand rank `12` last. Row 9 differs from row 8 only in
`is_use_matching` and its second description line, "Select this when you
want to battle a stranger."

## Field Names

The `PVP_GameBoard` sheet of a private server's `datasheet_minigame.xlsm`
on client 1784 has the columns `GameBoardKey` (`game_board_key`),
`HandRankKeyList` (`hand_rank_keys`, one comma-separated list),
`RollCountMax` (`roll_count_max`), `~Name`, `Level` (`level`), `~Desc`,
`IconTexture` and `BigTexture`. Its 8 rows match rows 1 to 8 of clients
1784 and 3474 in every named column and in the description and texture
strings, hand rank order included. `~Name` holds the level as star text
(`★★<PAColor0xff6c6c6c>☆☆☆<PAOldColor>`) and is not in the file. The file
writes `~Desc` before the textures and `Level` after them.

The client Lua (`panel_window_minigame_yachtdice_invite_1.luac`) reads a
board through `ToClient_getYachtGameBoardStaticStatusWrapperByIndex()` and
`...ByKey()`: `getKey()`, `getLevel()` (the star count), `getDesc()`,
`getHandRankCount()`, `isHaveHandRankKey()`, `getBigTextureId()`,
`getIconNormalTextureId()`, `getIconOverTextureId()` and
`getIconClickTextureId()` (three states of the board button, from the one
`icon_texture_index` string), and `isUseMatching()`, which shows the
matchmaking button.

## Notes

- Client 1784 has rows 1 to 8 and no `is_use_matching`. Client 3474 adds
  row 9 and the byte; row 9 is the only row with `1`.
