# `minigamefind.bss` Format

## Purpose

The Lakiaro digging minigame (`Panel_MiniGame_Find_All`): one row per game
type with its grid size, the hoes it takes, its rates, its six reward items
and the [`minigamefindpattern.dbss`](../dbss/minigamefindpattern_dbss.md) slot groups
it draws from, then a second table with one row per Lakiaro character and
dig depth. On client 3482 the file holds 18 game types in four chains (1 to
5, 6 to 10, 11 to 15, 16 to 18) and 19 Lakiaro rows.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients       | File               | Bytes | Records                          | Row bytes |
| ------ | ------------- | ------------------ | ----- | -------------------------------- | --------- |
| 1      | 805 and later | `minigamefind.bss` | 2,296 | 18 Type Row, 19 Collect Rate Row | 26        |

| Layout | File               | Known           | Unknown     |
| ------ | ------------------ | --------------- | ----------- |
| 1      | `minigamefind.bss` | 2,220 B (96.7%) | 76 B (3.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `426bf7b32ef4`  |
| 3482   | Layout 1             | `426bf7b32ef4`  |
| 3474   | Layout 1             | `426bf7b32ef4`  |
| 3473   | Layout 1             | `426bf7b32ef4`  |
| 3464   | Layout 1             | `426bf7b32ef4`  |
| 3458   | Layout 1             | `426bf7b32ef4`  |
| 3454   | Layout 1             | `426bf7b32ef4`  |
| 3444   | Layout 1             | `426bf7b32ef4`  |
| 3435   | Layout 1             | `426bf7b32ef4`  |
| 3426   | Layout 1             | `426bf7b32ef4`  |
| 3418   | Layout 1             | `426bf7b32ef4`  |
| 3412   | Layout 1             | `426bf7b32ef4`  |
| 3402   | Layout 1             | `426bf7b32ef4`  |
| 3396   | Layout 1             | `426bf7b32ef4`  |
| 3387   | Layout 1             | `426bf7b32ef4`  |
| 3381   | Layout 1             | `426bf7b32ef4`  |
| 3373   | Layout 1             | `426bf7b32ef4`  |
| 3364   | Layout 1             | `426bf7b32ef4`  |
| 3356   | Layout 1             | `426bf7b32ef4`  |
| 3349   | Layout 1             | `426bf7b32ef4`  |
| 3342   | Layout 1             | `426bf7b32ef4`  |
| 3335   | Layout 1             | `426bf7b32ef4`  |
| 3326   | Layout 1             | `426bf7b32ef4`  |
| 3321   | Layout 1             | `426bf7b32ef4`  |
| 3314   | Layout 1             | `426bf7b32ef4`  |
| 3303   | Layout 1             | `426bf7b32ef4`  |
| 3302   | Layout 1             | `426bf7b32ef4`  |
| 3293   | Layout 1             | `426bf7b32ef4`  |
| 3283   | Layout 1             | `426bf7b32ef4`  |
| 3275   | Layout 1             | `426bf7b32ef4`  |
| 3267   | Layout 1             | `426bf7b32ef4`  |
| 3258   | Layout 1             | `426bf7b32ef4`  |
| 3251   | Layout 1             | `426bf7b32ef4`  |
| 3242   | Layout 1             | `426bf7b32ef4`  |
| 3235   | Layout 1             | `426bf7b32ef4`  |
| 3229   | Layout 1             | `426bf7b32ef4`  |
| 3212   | Layout 1             | `426bf7b32ef4`  |
| 3203   | Layout 1             | `426bf7b32ef4`  |
| 3193   | Layout 1             | `426bf7b32ef4`  |
| 3186   | Layout 1             | `426bf7b32ef4`  |
| 3177   | Layout 1             | `426bf7b32ef4`  |
| 3169   | Layout 1             | `426bf7b32ef4`  |
| 3158   | Layout 1             | `426bf7b32ef4`  |
| 3151   | Layout 1             | `426bf7b32ef4`  |
| 3144   | Layout 1             | `426bf7b32ef4`  |
| 3133   | Layout 1             | `426bf7b32ef4`  |
| 3125   | Layout 1             | `426bf7b32ef4`  |
| 3118   | Layout 1             | `426bf7b32ef4`  |
| 3111   | Layout 1             | `426bf7b32ef4`  |
| 3103   | Layout 1             | `426bf7b32ef4`  |
| 3095   | Layout 1             | `426bf7b32ef4`  |
| 3086   | Layout 1             | `426bf7b32ef4`  |
| 3072   | Layout 1             | `426bf7b32ef4`  |
| 3062   | Layout 1             | `426bf7b32ef4`  |
| 3052   | Layout 1             | `426bf7b32ef4`  |
| 3045   | Layout 1             | `426bf7b32ef4`  |
| 3037   | Layout 1             | `426bf7b32ef4`  |
| 3030   | Layout 1             | `426bf7b32ef4`  |
| 3021   | Layout 1             | `426bf7b32ef4`  |
| 3012   | Layout 1             | `426bf7b32ef4`  |
| 3002   | Layout 1             | `426bf7b32ef4`  |
| 2995   | Layout 1             | `426bf7b32ef4`  |
| 2987   | Layout 1             | `426bf7b32ef4`  |
| 2978   | Layout 1             | `426bf7b32ef4`  |
| 2970   | Layout 1             | `426bf7b32ef4`  |
| 2959   | Layout 1             | `426bf7b32ef4`  |
| 2951   | Layout 1             | `426bf7b32ef4`  |
| 2942   | Layout 1             | `426bf7b32ef4`  |
| 2935   | Layout 1             | `426bf7b32ef4`  |
| 2932   | Layout 1             | `426bf7b32ef4`  |
| 2923   | Layout 1             | `426bf7b32ef4`  |
| 2919   | Layout 1             | `426bf7b32ef4`  |
| 2907   | Layout 1             | `426bf7b32ef4`  |
| 2900   | Layout 1             | `426bf7b32ef4`  |
| 2891   | Layout 1             | `426bf7b32ef4`  |
| 2882   | Layout 1             | `426bf7b32ef4`  |
| 2872   | Layout 1             | `426bf7b32ef4`  |
| 2863   | Layout 1             | `426bf7b32ef4`  |
| 2855   | Layout 1             | `426bf7b32ef4`  |
| 2849   | Layout 1             | `426bf7b32ef4`  |
| 2844   | Layout 1             | `426bf7b32ef4`  |
| 2834   | Layout 1             | `426bf7b32ef4`  |
| 2825   | Layout 1             | `426bf7b32ef4`  |
| 2819   | Layout 1             | `426bf7b32ef4`  |
| 2811   | Layout 1             | `426bf7b32ef4`  |
| 2803   | Layout 1             | `426bf7b32ef4`  |
| 2794   | Layout 1             | `426bf7b32ef4`  |
| 2783   | Layout 1             | `426bf7b32ef4`  |
| 2774   | Layout 1             | `426bf7b32ef4`  |
| 2765   | Layout 1             | `426bf7b32ef4`  |
| 2756   | Layout 1             | `426bf7b32ef4`  |
| 2750   | Layout 1             | `426bf7b32ef4`  |
| 2743   | Layout 1             | `426bf7b32ef4`  |
| 2736   | Layout 1             | `426bf7b32ef4`  |
| 2726   | Layout 1             | `426bf7b32ef4`  |
| 2717   | Layout 1             | `426bf7b32ef4`  |
| 2709   | Layout 1             | `426bf7b32ef4`  |
| 2703   | Layout 1             | `426bf7b32ef4`  |
| 2695   | Layout 1             | `426bf7b32ef4`  |
| 2684   | Layout 1             | `426bf7b32ef4`  |
| 2672   | Layout 1             | `426bf7b32ef4`  |
| 2665   | Layout 1             | `426bf7b32ef4`  |
| 2657   | Layout 1             | `426bf7b32ef4`  |
| 2649   | Layout 1             | `426bf7b32ef4`  |
| 2644   | Layout 1             | `426bf7b32ef4`  |
| 2637   | Layout 1             | `426bf7b32ef4`  |
| 2629   | Layout 1             | `426bf7b32ef4`  |
| 2619   | Layout 1             | `426bf7b32ef4`  |
| 2612   | Layout 1             | `426bf7b32ef4`  |
| 2606   | Layout 1             | `426bf7b32ef4`  |
| 2602   | Layout 1             | `426bf7b32ef4`  |
| 2601   | Layout 1             | `426bf7b32ef4`  |
| 2592   | Layout 1             | `426bf7b32ef4`  |
| 2583   | Layout 1             | `426bf7b32ef4`  |
| 2575   | Layout 1             | `426bf7b32ef4`  |
| 2567   | Layout 1             | `426bf7b32ef4`  |
| 2560   | Layout 1             | `426bf7b32ef4`  |
| 2553   | Layout 1             | `426bf7b32ef4`  |
| 2545   | Layout 1             | `426bf7b32ef4`  |
| 2538   | Layout 1             | `426bf7b32ef4`  |
| 2529   | Layout 1             | `426bf7b32ef4`  |
| 2519   | Layout 1             | `426bf7b32ef4`  |
| 2513   | Layout 1             | `426bf7b32ef4`  |
| 2510   | Layout 1             | `426bf7b32ef4`  |
| 2507   | Layout 1             | `426bf7b32ef4`  |
| 2503   | Layout 1             | `426bf7b32ef4`  |
| 2498   | Layout 1             | `426bf7b32ef4`  |
| 2492   | Layout 1             | `426bf7b32ef4`  |
| 2487   | Layout 1             | `426bf7b32ef4`  |
| 2480   | Layout 1             | `426bf7b32ef4`  |
| 2474   | Layout 1             | `426bf7b32ef4`  |
| 2468   | Layout 1             | `426bf7b32ef4`  |
| 2460   | Layout 1             | `426bf7b32ef4`  |
| 2453   | Layout 1             | `426bf7b32ef4`  |
| 2444   | Layout 1             | `426bf7b32ef4`  |
| 2438   | Layout 1             | `426bf7b32ef4`  |
| 2434   | Layout 1             | `426bf7b32ef4`  |
| 2429   | Layout 1             | `426bf7b32ef4`  |
| 2421   | Layout 1             | `426bf7b32ef4`  |
| 2414   | Layout 1             | `426bf7b32ef4`  |
| 2407   | Layout 1             | `426bf7b32ef4`  |
| 2401   | Layout 1             | `426bf7b32ef4`  |
| 2397   | Layout 1             | `426bf7b32ef4`  |
| 2393   | Layout 1             | `426bf7b32ef4`  |
| 2384   | Layout 1             | `426bf7b32ef4`  |
| 2378   | Layout 1             | `426bf7b32ef4`  |
| 2372   | Layout 1             | `426bf7b32ef4`  |
| 2358   | Layout 1             | `426bf7b32ef4`  |
| 2352   | Layout 1             | `426bf7b32ef4`  |
| 2347   | Layout 1             | `426bf7b32ef4`  |
| 2343   | Layout 1             | `426bf7b32ef4`  |
| 2335   | Layout 1             | `426bf7b32ef4`  |
| 2327   | Layout 1             | `426bf7b32ef4`  |
| 2324   | Layout 1             | `426bf7b32ef4`  |
| 2319   | Layout 1             | `426bf7b32ef4`  |
| 2313   | Layout 1             | `426bf7b32ef4`  |
| 2308   | Layout 1             | `426bf7b32ef4`  |
| 2302   | Layout 1             | `426bf7b32ef4`  |
| 2295   | Layout 1             | `426bf7b32ef4`  |
| 2290   | Layout 1             | `426bf7b32ef4`  |
| 2284   | Layout 1             | `426bf7b32ef4`  |
| 2276   | Layout 1             | `426bf7b32ef4`  |
| 2269   | Layout 1             | `426bf7b32ef4`  |
| 2259   | Layout 1             | `426bf7b32ef4`  |
| 2250   | Layout 1             | `426bf7b32ef4`  |
| 2243   | Layout 1             | `426bf7b32ef4`  |
| 2235   | Layout 1             | `426bf7b32ef4`  |
| 2229   | Layout 1             | `426bf7b32ef4`  |
| 2224   | Layout 1             | `426bf7b32ef4`  |
| 2218   | Layout 1             | `426bf7b32ef4`  |
| 2215   | Layout 1             | `426bf7b32ef4`  |
| 2207   | Layout 1             | `426bf7b32ef4`  |
| 2203   | Layout 1             | `426bf7b32ef4`  |
| 2196   | Layout 1             | `426bf7b32ef4`  |
| 2192   | Layout 1             | `426bf7b32ef4`  |
| 2189   | Layout 1             | `426bf7b32ef4`  |
| 2183   | Layout 1             | `426bf7b32ef4`  |
| 2179   | Layout 1             | `426bf7b32ef4`  |
| 2171   | Layout 1             | `426bf7b32ef4`  |
| 2163   | Layout 1             | `426bf7b32ef4`  |
| 2156   | Layout 1             | `426bf7b32ef4`  |
| 2151   | Layout 1             | `426bf7b32ef4`  |
| 2147   | Layout 1             | `426bf7b32ef4`  |
| 2142   | Layout 1             | `426bf7b32ef4`  |
| 2138   | Layout 1             | `426bf7b32ef4`  |
| 2134   | Layout 1             | `426bf7b32ef4`  |
| 2130   | Layout 1             | `426bf7b32ef4`  |
| 2122   | Layout 1             | `426bf7b32ef4`  |
| 2107   | Layout 1             | `426bf7b32ef4`  |
| 2098   | Layout 1             | `426bf7b32ef4`  |
| 2089   | Layout 1             | `426bf7b32ef4`  |
| 2081   | Layout 1             | `426bf7b32ef4`  |
| 2073   | Layout 1             | `426bf7b32ef4`  |
| 2067   | Layout 1             | `426bf7b32ef4`  |
| 2063   | Layout 1             | `426bf7b32ef4`  |
| 2059   | Layout 1             | `426bf7b32ef4`  |
| 2052   | Layout 1             | `426bf7b32ef4`  |
| 2044   | Layout 1             | `426bf7b32ef4`  |
| 2039   | Layout 1             | `426bf7b32ef4`  |
| 2032   | Layout 1             | `426bf7b32ef4`  |
| 2025   | Layout 1             | `426bf7b32ef4`  |
| 2011   | Layout 1             | `426bf7b32ef4`  |
| 2005   | Layout 1             | `426bf7b32ef4`  |
| 2000   | Layout 1             | `426bf7b32ef4`  |
| 1996   | Layout 1             | `426bf7b32ef4`  |
| 1991   | Layout 1             | `426bf7b32ef4`  |
| 1985   | Layout 1             | `426bf7b32ef4`  |
| 1980   | Layout 1             | `426bf7b32ef4`  |
| 1969   | Layout 1             | `426bf7b32ef4`  |
| 1964   | Layout 1             | `426bf7b32ef4`  |
| 1958   | Layout 1             | `426bf7b32ef4`  |
| 1950   | Layout 1             | `426bf7b32ef4`  |
| 1945   | Layout 1             | `426bf7b32ef4`  |
| 1937   | Layout 1             | `426bf7b32ef4`  |
| 1933   | Layout 1             | `426bf7b32ef4`  |
| 1927   | Layout 1             | `426bf7b32ef4`  |
| 1921   | Layout 1             | `426bf7b32ef4`  |
| 1914   | Layout 1             | `426bf7b32ef4`  |
| 1908   | Layout 1             | `426bf7b32ef4`  |
| 1897   | Layout 1             | `426bf7b32ef4`  |
| 1892   | Layout 1             | `426bf7b32ef4`  |
| 1886   | Layout 1             | `426bf7b32ef4`  |
| 1881   | Layout 1             | `426bf7b32ef4`  |
| 1871   | Layout 1             | `426bf7b32ef4`  |
| 1866   | Layout 1             | `426bf7b32ef4`  |
| 1862   | Layout 1             | `426bf7b32ef4`  |
| 1854   | Layout 1             | `426bf7b32ef4`  |
| 1846   | Layout 1             | `426bf7b32ef4`  |
| 1838   | Layout 1             | `426bf7b32ef4`  |
| 1832   | Layout 1             | `426bf7b32ef4`  |
| 1826   | Layout 1             | `426bf7b32ef4`  |
| 1822   | Layout 1             | `426bf7b32ef4`  |
| 1818   | Layout 1             | `426bf7b32ef4`  |
| 1804   | Layout 1             | `426bf7b32ef4`  |
| 1794   | Layout 1             | `426bf7b32ef4`  |
| 1790   | Layout 1             | `426bf7b32ef4`  |
| 1784   | Layout 1             | `426bf7b32ef4`  |
| 1774   | Layout 1             | `426bf7b32ef4`  |
| 1771   | Layout 1             | `426bf7b32ef4`  |
| 1762   | Layout 1             | `426bf7b32ef4`  |
| 1759   | Layout 1             | `426bf7b32ef4`  |
| 1754   | Layout 1             | `426bf7b32ef4`  |
| 1749   | Layout 1             | `426bf7b32ef4`  |
| 1743   | Layout 1             | `426bf7b32ef4`  |
| 1737   | Layout 1             | `426bf7b32ef4`  |
| 1731   | Layout 1             | `426bf7b32ef4`  |
| 1725   | Layout 1             | `426bf7b32ef4`  |
| 1717   | Layout 1             | `426bf7b32ef4`  |
| 1710   | Layout 1             | `426bf7b32ef4`  |
| 1704   | Layout 1             | `426bf7b32ef4`  |
| 1698   | Layout 1             | `426bf7b32ef4`  |
| 1690   | Layout 1             | `426bf7b32ef4`  |
| 1685   | Layout 1             | `426bf7b32ef4`  |
| 1680   | Layout 1             | `426bf7b32ef4`  |
| 1674   | Layout 1             | `426bf7b32ef4`  |
| 1668   | Layout 1             | `426bf7b32ef4`  |
| 1659   | Layout 1             | `426bf7b32ef4`  |
| 1649   | Layout 1             | `426bf7b32ef4`  |
| 1642   | Layout 1             | `426bf7b32ef4`  |
| 1636   | Layout 1             | `426bf7b32ef4`  |
| 1628   | Layout 1             | `426bf7b32ef4`  |
| 1622   | Layout 1             | `426bf7b32ef4`  |
| 1614   | Layout 1             | `426bf7b32ef4`  |
| 1608   | Layout 1             | `426bf7b32ef4`  |
| 1602   | Layout 1             | `426bf7b32ef4`  |
| 1598   | Layout 1             | `426bf7b32ef4`  |
| 1594   | Layout 1             | `426bf7b32ef4`  |
| 1590   | Layout 1             | `426bf7b32ef4`  |
| 1587   | Layout 1             | `426bf7b32ef4`  |
| 1584   | Layout 1             | `426bf7b32ef4`  |
| 1579   | Layout 1             | `426bf7b32ef4`  |
| 1572   | Layout 1             | `426bf7b32ef4`  |
| 1565   | Layout 1             | `426bf7b32ef4`  |
| 1559   | Layout 1             | `426bf7b32ef4`  |
| 1554   | Layout 1             | `426bf7b32ef4`  |
| 1547   | Layout 1             | `426bf7b32ef4`  |
| 1537   | Layout 1             | `426bf7b32ef4`  |
| 1529   | Layout 1             | `426bf7b32ef4`  |
| 1524   | Layout 1             | `426bf7b32ef4`  |
| 1519   | Layout 1             | `426bf7b32ef4`  |
| 1509   | Layout 1             | `426bf7b32ef4`  |
| 1506   | Layout 1             | `426bf7b32ef4`  |
| 1504   | Layout 1             | `426bf7b32ef4`  |
| 1500   | Layout 1             | `426bf7b32ef4`  |
| 1493   | Layout 1             | `426bf7b32ef4`  |
| 1489   | Layout 1             | `426bf7b32ef4`  |
| 1485   | Layout 1             | `426bf7b32ef4`  |
| 1481   | Layout 1             | `426bf7b32ef4`  |
| 1474   | Layout 1             | `426bf7b32ef4`  |
| 1466   | Layout 1             | `426bf7b32ef4`  |
| 1462   | Layout 1             | `426bf7b32ef4`  |
| 1459   | Layout 1             | `426bf7b32ef4`  |
| 1453   | Layout 1             | `426bf7b32ef4`  |
| 1450   | Layout 1             | `426bf7b32ef4`  |
| 1445   | Layout 1             | `426bf7b32ef4`  |
| 1439   | Layout 1             | `426bf7b32ef4`  |
| 1433   | Layout 1             | `426bf7b32ef4`  |
| 1430   | Layout 1             | `426bf7b32ef4`  |
| 1426   | Layout 1             | `426bf7b32ef4`  |
| 1421   | Layout 1             | `426bf7b32ef4`  |
| 1417   | Layout 1             | `426bf7b32ef4`  |
| 1416   | Layout 1             | `426bf7b32ef4`  |
| 1409   | Layout 1             | `426bf7b32ef4`  |
| 1405   | Layout 1             | `426bf7b32ef4`  |
| 1401   | Layout 1             | `426bf7b32ef4`  |
| 1396   | Layout 1             | `426bf7b32ef4`  |
| 1391   | Layout 1             | `426bf7b32ef4`  |
| 1390   | Layout 1             | `426bf7b32ef4`  |
| 1386   | Layout 1             | `426bf7b32ef4`  |
| 1381   | Layout 1             | `426bf7b32ef4`  |
| 1379   | Layout 1             | `426bf7b32ef4`  |
| 1372   | Layout 1             | `426bf7b32ef4`  |
| 1366   | Layout 1             | `426bf7b32ef4`  |
| 1364   | Layout 1             | `426bf7b32ef4`  |
| 1363   | Layout 1             | `426bf7b32ef4`  |
| 1360   | Layout 1             | `426bf7b32ef4`  |
| 1358   | Layout 1             | `426bf7b32ef4`  |
| 1355   | Layout 1             | `426bf7b32ef4`  |
| 1351   | Layout 1             | `426bf7b32ef4`  |
| 1348   | Layout 1             | `426bf7b32ef4`  |
| 1346   | Layout 1             | `426bf7b32ef4`  |
| 1341   | Layout 1             | `426bf7b32ef4`  |
| 1340   | Layout 1             | `426bf7b32ef4`  |
| 1338   | Layout 1             | `426bf7b32ef4`  |
| 1335   | Layout 1             | `426bf7b32ef4`  |
| 1333   | Layout 1             | `426bf7b32ef4`  |
| 1329   | Layout 1             | `426bf7b32ef4`  |
| 1327   | Layout 1             | `426bf7b32ef4`  |
| 1324   | Layout 1             | `426bf7b32ef4`  |
| 1321   | Layout 1             | `426bf7b32ef4`  |
| 1319   | Layout 1             | `426bf7b32ef4`  |
| 1318   | Layout 1             | `426bf7b32ef4`  |
| 1316   | Layout 1             | `426bf7b32ef4`  |
| 1313   | Layout 1             | `426bf7b32ef4`  |
| 1311   | Layout 1             | `426bf7b32ef4`  |
| 1309   | Layout 1             | `426bf7b32ef4`  |
| 1304   | Layout 1             | `426bf7b32ef4`  |
| 1292   | Layout 1             | `426bf7b32ef4`  |
| 1286   | Layout 1             | `426bf7b32ef4`  |
| 1280   | Layout 1             | `426bf7b32ef4`  |
| 1276   | Layout 1             | `426bf7b32ef4`  |
| 1267   | Layout 1             | `426bf7b32ef4`  |
| 1261   | Layout 1             | `426bf7b32ef4`  |
| 1256   | Layout 1             | `426bf7b32ef4`  |
| 1250   | Layout 1             | `426bf7b32ef4`  |
| 1246   | Layout 1             | `426bf7b32ef4`  |
| 1239   | Layout 1             | `426bf7b32ef4`  |
| 1230   | Layout 1             | `426bf7b32ef4`  |
| 1226   | Layout 1             | `426bf7b32ef4`  |
| 1220   | Layout 1             | `426bf7b32ef4`  |
| 1217   | Layout 1             | `426bf7b32ef4`  |
| 1211   | Layout 1             | `426bf7b32ef4`  |
| 1210   | Layout 1             | `426bf7b32ef4`  |
| 1208   | Layout 1             | `426bf7b32ef4`  |
| 1203   | Layout 1             | `426bf7b32ef4`  |
| 1197   | Layout 1             | `426bf7b32ef4`  |
| 1194   | Layout 1             | `426bf7b32ef4`  |
| 1192   | Layout 1             | `426bf7b32ef4`  |
| 1187   | Layout 1             | `426bf7b32ef4`  |
| 1183   | Layout 1             | `426bf7b32ef4`  |
| 1177   | Layout 1             | `426bf7b32ef4`  |
| 1173   | Layout 1             | `426bf7b32ef4`  |
| 1167   | Layout 1             | `426bf7b32ef4`  |
| 1164   | Layout 1             | `426bf7b32ef4`  |
| 1156   | Layout 1             | `426bf7b32ef4`  |
| 1149   | Layout 1             | `426bf7b32ef4`  |
| 1144   | Layout 1             | `426bf7b32ef4`  |
| 1137   | Layout 1             | `426bf7b32ef4`  |
| 1132   | Layout 1             | `426bf7b32ef4`  |
| 1127   | Layout 1             | `426bf7b32ef4`  |
| 1122   | Layout 1             | `426bf7b32ef4`  |
| 1118   | Layout 1             | `426bf7b32ef4`  |
| 1114   | Layout 1             | `426bf7b32ef4`  |
| 1109   | Layout 1             | `426bf7b32ef4`  |
| 1102   | Layout 1             | `426bf7b32ef4`  |
| 1096   | Layout 1             | `426bf7b32ef4`  |
| 1088   | Layout 1             | `426bf7b32ef4`  |
| 1081   | Layout 1             | `426bf7b32ef4`  |
| 1076   | Layout 1             | `426bf7b32ef4`  |
| 1069   | Layout 1             | `426bf7b32ef4`  |
| 1064   | Layout 1             | `426bf7b32ef4`  |
| 1058   | Layout 1             | `426bf7b32ef4`  |
| 1051   | Layout 1             | `426bf7b32ef4`  |
| 1044   | Layout 1             | `426bf7b32ef4`  |
| 1036   | Layout 1             | `426bf7b32ef4`  |
| 1026   | Layout 1             | `426bf7b32ef4`  |
| 1016   | Layout 1             | `426bf7b32ef4`  |
| 1009   | Layout 1             | `426bf7b32ef4`  |
| 1005   | Layout 1             | `426bf7b32ef4`  |
| 1000   | Layout 1             | `426bf7b32ef4`  |
| 998    | Layout 1             | `426bf7b32ef4`  |
| 990    | Layout 1             | `426bf7b32ef4`  |
| 979    | Layout 1             | `426bf7b32ef4`  |
| 972    | Layout 1             | `426bf7b32ef4`  |
| 963    | Layout 1             | `426bf7b32ef4`  |
| 955    | Layout 1             | `426bf7b32ef4`  |
| 946    | Layout 1             | `426bf7b32ef4`  |
| 938    | Layout 1             | `426bf7b32ef4`  |
| 927    | Layout 1             | `426bf7b32ef4`  |
| 911    | Layout 1             | `426bf7b32ef4`  |
| 904    | Layout 1             | `426bf7b32ef4`  |
| 899    | Layout 1             | `426bf7b32ef4`  |
| 894    | Layout 1             | `426bf7b32ef4`  |
| 885    | Layout 1             | `426bf7b32ef4`  |
| 879    | Layout 1             | `426bf7b32ef4`  |
| 872    | Layout 1             | `426bf7b32ef4`  |
| 864    | Layout 1             | `426bf7b32ef4`  |
| 855    | Layout 1             | `426bf7b32ef4`  |
| 853    | Layout 1             | `426bf7b32ef4`  |
| 845    | Layout 1             | `426bf7b32ef4`  |
| 837    | Layout 1             | `426bf7b32ef4`  |
| 829    | Layout 1             | `426bf7b32ef4`  |
| 822    | Layout 1             | `426bf7b32ef4`  |
| 814    | Layout 1             | `426bf7b32ef4`  |
| 805    | Layout 1             | `426bf7b32ef4`  |
| 794    | No documented layout | `426bf7b32ef4`  |
| 787    | No documented layout | `426bf7b32ef4`  |
| 780    | No documented layout | `426bf7b32ef4`  |
| 771    | No documented layout | `426bf7b32ef4`  |
| 760    | No documented layout | `426bf7b32ef4`  |
| 748    | No documented layout | `426bf7b32ef4`  |
| 741    | No documented layout | `426bf7b32ef4`  |
| 736    | No documented layout | `426bf7b32ef4`  |
| 731    | No documented layout | `426bf7b32ef4`  |
| 723    | No documented layout | `426bf7b32ef4`  |
| 711    | No documented layout | `426bf7b32ef4`  |
| 707    | No documented layout | `426bf7b32ef4`  |
| 697    | No documented layout | `426bf7b32ef4`  |
| 689    | No documented layout | `426bf7b32ef4`  |
| 683    | No documented layout | `426bf7b32ef4`  |
| 678    | No documented layout | `426bf7b32ef4`  |
| 670    | No documented layout | `426bf7b32ef4`  |
| 661    | No documented layout | `426bf7b32ef4`  |
| 656    | No documented layout | `426bf7b32ef4`  |
| 652    | No documented layout | `426bf7b32ef4`  |
| 643    | No documented layout | `426bf7b32ef4`  |
| 637    | No documented layout | `426bf7b32ef4`  |
| 630    | No documented layout | `426bf7b32ef4`  |
| 627    | No documented layout | `426bf7b32ef4`  |
| 621    | No documented layout | `426bf7b32ef4`  |
| 617    | No documented layout | `426bf7b32ef4`  |
| 615    | No documented layout | `426bf7b32ef4`  |
| 606    | No file              | `426bf7b32ef4`  |
| 599    | No file              | `426bf7b32ef4`  |
| 592    | No file              | `426bf7b32ef4`  |
| 586    | No file              | `426bf7b32ef4`  |
| 577    | No file              | `426bf7b32ef4`  |
| 569    | No file              | `426bf7b32ef4`  |
| 561    | No file              | `426bf7b32ef4`  |
| 554    | No file              | `426bf7b32ef4`  |
| 542    | No file              | `426bf7b32ef4`  |
| 532    | No file              | `426bf7b32ef4`  |
| 531    | No file              | `426bf7b32ef4`  |
| 526    | No file              | `426bf7b32ef4`  |
| 521    | No file              | `426bf7b32ef4`  |
| 517    | No file              | `426bf7b32ef4`  |
| 510    | No file              | `426bf7b32ef4`  |
| 508    | No file              | `426bf7b32ef4`  |
| 504    | No file              | `426bf7b32ef4`  |
| 497    | No file              | `426bf7b32ef4`  |
| 491    | No file              | `426bf7b32ef4`  |
| 485    | No file              | `426bf7b32ef4`  |
| 478    | No file              | `426bf7b32ef4`  |
| 472    | No file              | `426bf7b32ef4`  |
| 466    | No file              | `426bf7b32ef4`  |
| 457    | No file              | `426bf7b32ef4`  |
| 452    | No file              | `426bf7b32ef4`  |
| 449    | No file              | `426bf7b32ef4`  |
| 435    | No file              | `426bf7b32ef4`  |

<!-- versions:end -->

## Companion Files

None. Item names come from LOC type 0 and character names from LOC type 6.

All multi-byte values are little-endian.

## Layout 1

### File Layout

PABR with two counted tables back to back, then the counted string table and
8-byte trailer of [`npcsimply.bss`](npcsimply_bss.md#string-table-variable-4-bytes--strings)
(`_common/pabr_strings.py`). The string table holds the two image paths the
Lakiaro rows name.

| Offset                   | Type                                 | Field              | Notes                                         |
| ------------------------ | ------------------------------------ | ------------------ | --------------------------------------------- |
| `+0x00`                  | char[4]                              | magic              | ASCII `PABR`                                  |
| `+0x04`                  | u32                                  | type_count         | Number of game types; 18 on client 3482       |
| `+0x08`                  | Type Row[type_count]                 | type_rows          | See Type Row                                  |
| `type_rows+0x00`         | u32                                  | collect_rate_count | Number of Lakiaro rows; 19 on client 3482     |
| `type_rows+0x04`         | Collect Rate Row[collect_rate_count] | collect_rate_rows  | See Collect Rate Row                          |
| `collect_rate_rows+0x00` | String Table                         | string_table       | See String Table                              |
| `string_table+0x00`      | u32                                  | string_table_start | Offset of the string table, where the rows end |
| `string_table+0x04`      | u32                                  | zero               | Always `0`                                    |

On client 3482 the file is 8 + 18 x 92 + 4 + 19 x 26 + 130 + 8 = 2,296
bytes.

### Type Row (92 bytes)

| Offset  | Type   | Field               | Notes                                                                    |
| ------- | ------ | ------------------- | ------------------------------------------------------------------------ |
| `+0x00` | u8     | game_type           | Row key, `1` to `18`                                                     |
| `+0x01` | u8     | game_type_dup       | Equal to `game_type` on every row                                        |
| `+0x02` | u8     | next_game           | `game_type` of the next game in the chain; `255` on the last one         |
| `+0x03` | u32    | min_damage_rate     | `1000000` on every row with a next game, `0` on the last ones            |
| `+0x07` | u32    | next_rate           | `1000000` on every row with a next game, `0` on the last ones            |
| `+0x0B` | u8     | life_type           | `0` on every row (clients 1784 and 3482)                                 |
| `+0x0C` | u32    | life_rate           | `5000` on every row (clients 1784 and 3482)                              |
| `+0x10` | u32[5] | tool_item_keys      | Hoes the game takes; `0` in a free slot                                  |
| `+0x24` | u32    | tool_rate           | `10000` on every row (clients 1784 and 3482)                             |
| `+0x28` | u32    | stone_rate          | `50000` to `300000` on client 3482, rising along each chain              |
| `+0x2C` | u32    | stone_drop_item_key | `4006` Rough Stone on every row (clients 1784 and 3482)                  |
| `+0x30` | u8     | col                 | Grid width: `12` or `14`; equal to `row` on every row                    |
| `+0x31` | u8     | row                 | Grid height: `12` or `14`                                                |
| `+0x32` | u8[4]  | start_pos           | `0, 0, 4, 4` on every row (clients 1784 and 3482)                        |
| `+0x36` | u8[6]  | min_root_count      | `7, 7, 4, 3, 3, 0` on the 12 x 12 games, `9, 9, 6, 5, 5, 0` on the 14 x 14 ones |
| `+0x3C` | u8[4]  | begin_root_count    | One count per side in Left, Right, Top, Bottom order (see Directions)    |
| `+0x40` | u8[4]  | use_slot_indexes    | `slot_index` groups of `minigamefindpattern.dbss`; `0` in a free slot    |
| `+0x44` | u32[6] | reward_item_keys    | Reward items, slot 0 first (see Rewards)                                 |

The rows are stored in key order 15 down to 1, then 18, 17, 16 (clients
1784 and 3482).

### Collect Rate Row (26 bytes)

| Offset  | Type   | Field           | Notes                                                                    |
| ------- | ------ | --------------- | ------------------------------------------------------------------------ |
| `+0x00` | u16    | character_key   | Row key: a Lakiaro character (LOC type 6), unique                        |
| `+0x02` | u32    | unknown_02      | `1` on every row (clients 1784 and 3482); see Open Questions             |
| `+0x06` | u16[4] | slot_coordinate | Pixel rectangle (x1, y1, x2, y2) in `image_ref`'s image                  |
| `+0x0E` | u32    | image_ref       | String table index of the image path                                     |
| `+0x12` | u8     | main_game_type  | `game_type` that opens the chain: `1`, `6` or `11` on client 3482        |
| `+0x13` | u32    | collect_rate    | `1000000` on every row (clients 1784 and 3482)                           |
| `+0x17` | u8     | depth           | `1` to `5`                                                               |
| `+0x18` | u16    | vary_wp         | `0`, `20`, `30`, `40` or `50` on client 3482                             |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                          |
| ------- | ------------------ | ------------ | ------------------------------ |
| `+0x00` | u32                | string_count | `2` on clients 1784 and 3482   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries            |

The two strings are `New_UI_Common_forLua\Window\MiniGame\MiniGameFind_03.dds`
(index 0) and `MiniGameFind_01.dds` (index 1) in the same folder, which is
`ui_texture/new_ui_common_forlua/window/minigame/` in the PAZ index.

## Directions

`begin_root_count` holds one count per side in the order of the
`minigamefindpattern.dbss` direction values: Left, Right, Top, Bottom. The
order comes from the sheet (see Field Names): its `BeginRootCount_Left`,
`_Top`, `_Right` and `_Bottom` columns match bytes 0, 2, 1 and 3 on 18 of 18
rows (client 1784).

## Rewards

The minigame window Lua (`panel_minigame_find_all_1`, `getRewardIndex`)
highlights one of the six reward slots by the share it shows: slot 0 at
100%, otherwise slot 5 up to 20%, slot 4 up to 40%, slot 3 up to 60%, slot 2
up to 80% and slot 1 above. `FromClient_MiniGameFindSetReward` fills the
slots from a list of item keys.

On client 3482 chains 1 to 5 and 16 to 18 give Lakiaro sacks (`761251`
Young Lakiaro Sack to `761260` Primitive Lakiaro Sack) and chain 6 to 10 the
Lush ones (`761261` to `761270`); game type 16 also gives `720112` Wild
Grass Sack and `5439` Wild Grass. Chain 11 to 15 gives `720111` Wild Grass
Sack, `5439` Wild Grass and `5600` Weeds, as on client 1784.

## Field Names

The type rows are the `MiniGameFindType` sheet and the Lakiaro rows the
`MiniGameFindCollectRate` sheet of a private server's `DataSheets.bexcel` on
client 1784. Matched by key on the client 1784 file:

| Field                                 | Column                         | Same value (client 1784) |
| ------------------------------------- | ------------------------------ | ------------------------ |
| `game_type`                           | `GameType`                     | 18 of 18                 |
| `next_game` (`<null>` as `255`)       | `NextGame`                     | 18 of 18                 |
| `min_damage_rate`, `next_rate`        | `MinDamageRate`, `NextRate`    | 18 of 18                 |
| `life_type`, `life_rate`              | `LifeType`, `LifeRate`         | 18 of 18                 |
| `tool_item_keys`                      | `ToolIndex`                    | 18 of 18                 |
| `tool_rate`                           | `ToolRate`                     | 18 of 18                 |
| `stone_rate`, `stone_drop_item_key`   | `StoneRate`, `StoneDropKey`    | 18 of 18                 |
| `col`, `row`                          | `Col`, `Row`                   | 18 of 18                 |
| `start_pos`                           | `StartPos`                     | 18 of 18                 |
| `min_root_count`                      | `MinRootCount`                 | 18 of 18                 |
| `begin_root_count`                    | `BeginRootCount_*`             | 18 of 18                 |
| `use_slot_indexes`                    | `UseSlotIndexList`             | 18 of 18                 |
| `reward_item_keys`                    | `Reward_0` to `Reward_5`       | 18 of 18                 |
| `character_key`                       | `CharacterKey`                 | 12 of 14                 |
| `slot_coordinate`, `image_ref`        | `SlotCoordinate`, `ImageFile`  | 12 of 12                 |
| `main_game_type`, `collect_rate`      | `MainGameType`, `CollectRate`  | 12 of 12                 |
| `depth`, `vary_wp` (`<null>` as `0`)  | `Depth`, `VaryWp`              | 12 of 12                 |

The two sheet rows the client 1784 file lacks are `27635` and `27636`, the
only ones with `MainGameType` `16`. On client 3482 the same columns match 18
of 18 type keys except `begin_root_count` (17, game type 8 now ends in `1`)
and `reward_item_keys` (5, the new sack items), and 12 of 12 Lakiaro keys.
The sheet has no column for `unknown_02`. `col` and `row` are equal on every
row, so their order follows the sheet, not the data.

## Notes

- The tools on client 3482 are `16479` Manos Hoe, `16480` Dostter Hoe,
  `16540` Dostter Steel Hoe and `65496` QA Lakiaro Hoe on game types 1 to
  15, and `16652` [Event] Ahr Hoe and `65496` on 16 to 18.
- The Lakiaro characters are `27621` to `27630` and `27637`, `27638` (as on
  client 1784), and `24885` to `24889`, `25197` and `25198` (client 3482
  only); LOC type 6 names them all Lakiaro, `27626` to `27630` "... Lakiaro
  for Research".
- `slot_coordinate` and the image are the Lakiaro's picture: the Lua
  receives a texture path and a UV rectangle for the grid
  (`FromClient_Minigame_Find_All_DefaultImage`). The rectangles are 221 x
  221 pixels on every row of client 3482.
- The window Lua reads the damage share as `damageRate / 10000`, so rates
  in this minigame count `1000000` as 100%.

## Open Questions

### What `unknown_02` Holds

The u32 after `character_key` is `1` on every Lakiaro row of clients 1784
and 3482, and the `MiniGameFindCollectRate` sheet has no column left for
it.
