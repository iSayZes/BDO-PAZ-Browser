# `guildmatchexp.bss` Format

## Purpose

The Combat EXP a Guild League match gives by character level: two rows of
100 values each, value `N` for level `N + 1`. Clients 2519 to 3251 fill
them; row 0 holds the lower values (421,740 on levels 1 to 20) and row 1
the higher (705,375). Both change in steps up to level 40, fall from level
41 and hold `31` from level 68 on. On client 3474 every value is `0`. The ranks are in
[guildmatchrank](guildmatchrank_bss.md), the rewards in
[guildmatchoption](guildmatchoption_bss.md).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                | Bytes | Records | Row bytes |
| ------ | -------------- | ------------------- | ----- | ------- | --------- |
| 1      | 2444 and later | `guildmatchexp.bss` | 828   | 2 Row   | 404       |

| Layout | File                | Known          | Unknown    |
| ------ | ------------------- | -------------- | ---------- |
| 1      | `guildmatchexp.bss` | 828 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `fecd11f7732c`  |
| 3482   | Layout 1 | `fecd11f7732c`  |
| 3474   | Layout 1 | `fecd11f7732c`  |
| 3473   | Layout 1 | `fecd11f7732c`  |
| 3464   | Layout 1 | `fecd11f7732c`  |
| 3458   | Layout 1 | `fecd11f7732c`  |
| 3454   | Layout 1 | `fecd11f7732c`  |
| 3444   | Layout 1 | `fecd11f7732c`  |
| 3435   | Layout 1 | `fecd11f7732c`  |
| 3426   | Layout 1 | `fecd11f7732c`  |
| 3418   | Layout 1 | `fecd11f7732c`  |
| 3412   | Layout 1 | `fecd11f7732c`  |
| 3402   | Layout 1 | `fecd11f7732c`  |
| 3396   | Layout 1 | `fecd11f7732c`  |
| 3387   | Layout 1 | `fecd11f7732c`  |
| 3381   | Layout 1 | `fecd11f7732c`  |
| 3373   | Layout 1 | `fecd11f7732c`  |
| 3364   | Layout 1 | `fecd11f7732c`  |
| 3356   | Layout 1 | `fecd11f7732c`  |
| 3349   | Layout 1 | `fecd11f7732c`  |
| 3342   | Layout 1 | `fecd11f7732c`  |
| 3335   | Layout 1 | `fecd11f7732c`  |
| 3326   | Layout 1 | `fecd11f7732c`  |
| 3321   | Layout 1 | `fecd11f7732c`  |
| 3314   | Layout 1 | `fecd11f7732c`  |
| 3303   | Layout 1 | `fecd11f7732c`  |
| 3302   | Layout 1 | `fecd11f7732c`  |
| 3293   | Layout 1 | `fecd11f7732c`  |
| 3283   | Layout 1 | `fecd11f7732c`  |
| 3275   | Layout 1 | `fecd11f7732c`  |
| 3267   | Layout 1 | `fecd11f7732c`  |
| 3258   | Layout 1 | `fecd11f7732c`  |
| 3251   | Layout 1 | `fecd11f7732c`  |
| 3242   | Layout 1 | `fecd11f7732c`  |
| 3235   | Layout 1 | `fecd11f7732c`  |
| 3229   | Layout 1 | `fecd11f7732c`  |
| 3212   | Layout 1 | `fecd11f7732c`  |
| 3203   | Layout 1 | `fecd11f7732c`  |
| 3193   | Layout 1 | `fecd11f7732c`  |
| 3186   | Layout 1 | `fecd11f7732c`  |
| 3177   | Layout 1 | `fecd11f7732c`  |
| 3169   | Layout 1 | `fecd11f7732c`  |
| 3158   | Layout 1 | `fecd11f7732c`  |
| 3151   | Layout 1 | `fecd11f7732c`  |
| 3144   | Layout 1 | `fecd11f7732c`  |
| 3133   | Layout 1 | `fecd11f7732c`  |
| 3125   | Layout 1 | `fecd11f7732c`  |
| 3118   | Layout 1 | `fecd11f7732c`  |
| 3111   | Layout 1 | `fecd11f7732c`  |
| 3103   | Layout 1 | `fecd11f7732c`  |
| 3095   | Layout 1 | `fecd11f7732c`  |
| 3086   | Layout 1 | `fecd11f7732c`  |
| 3072   | Layout 1 | `fecd11f7732c`  |
| 3062   | Layout 1 | `fecd11f7732c`  |
| 3052   | Layout 1 | `fecd11f7732c`  |
| 3045   | Layout 1 | `fecd11f7732c`  |
| 3037   | Layout 1 | `fecd11f7732c`  |
| 3030   | Layout 1 | `fecd11f7732c`  |
| 3021   | Layout 1 | `fecd11f7732c`  |
| 3012   | Layout 1 | `fecd11f7732c`  |
| 3002   | Layout 1 | `fecd11f7732c`  |
| 2995   | Layout 1 | `fecd11f7732c`  |
| 2987   | Layout 1 | `fecd11f7732c`  |
| 2978   | Layout 1 | `fecd11f7732c`  |
| 2970   | Layout 1 | `fecd11f7732c`  |
| 2959   | Layout 1 | `fecd11f7732c`  |
| 2951   | Layout 1 | `fecd11f7732c`  |
| 2942   | Layout 1 | `fecd11f7732c`  |
| 2935   | Layout 1 | `fecd11f7732c`  |
| 2932   | Layout 1 | `fecd11f7732c`  |
| 2923   | Layout 1 | `fecd11f7732c`  |
| 2919   | Layout 1 | `fecd11f7732c`  |
| 2907   | Layout 1 | `fecd11f7732c`  |
| 2900   | Layout 1 | `fecd11f7732c`  |
| 2891   | Layout 1 | `fecd11f7732c`  |
| 2882   | Layout 1 | `fecd11f7732c`  |
| 2872   | Layout 1 | `fecd11f7732c`  |
| 2863   | Layout 1 | `fecd11f7732c`  |
| 2855   | Layout 1 | `fecd11f7732c`  |
| 2849   | Layout 1 | `fecd11f7732c`  |
| 2844   | Layout 1 | `fecd11f7732c`  |
| 2834   | Layout 1 | `fecd11f7732c`  |
| 2825   | Layout 1 | `fecd11f7732c`  |
| 2819   | Layout 1 | `fecd11f7732c`  |
| 2811   | Layout 1 | `fecd11f7732c`  |
| 2803   | Layout 1 | `fecd11f7732c`  |
| 2794   | Layout 1 | `fecd11f7732c`  |
| 2783   | Layout 1 | `fecd11f7732c`  |
| 2774   | Layout 1 | `fecd11f7732c`  |
| 2765   | Layout 1 | `fecd11f7732c`  |
| 2756   | Layout 1 | `fecd11f7732c`  |
| 2750   | Layout 1 | `fecd11f7732c`  |
| 2743   | Layout 1 | `fecd11f7732c`  |
| 2736   | Layout 1 | `fecd11f7732c`  |
| 2726   | Layout 1 | `fecd11f7732c`  |
| 2717   | Layout 1 | `fecd11f7732c`  |
| 2709   | Layout 1 | `fecd11f7732c`  |
| 2703   | Layout 1 | `fecd11f7732c`  |
| 2695   | Layout 1 | `fecd11f7732c`  |
| 2684   | Layout 1 | `fecd11f7732c`  |
| 2672   | Layout 1 | `fecd11f7732c`  |
| 2665   | Layout 1 | `fecd11f7732c`  |
| 2657   | Layout 1 | `fecd11f7732c`  |
| 2649   | Layout 1 | `fecd11f7732c`  |
| 2644   | Layout 1 | `fecd11f7732c`  |
| 2637   | Layout 1 | `fecd11f7732c`  |
| 2629   | Layout 1 | `fecd11f7732c`  |
| 2619   | Layout 1 | `fecd11f7732c`  |
| 2612   | Layout 1 | `fecd11f7732c`  |
| 2606   | Layout 1 | `fecd11f7732c`  |
| 2602   | Layout 1 | `fecd11f7732c`  |
| 2601   | Layout 1 | `fecd11f7732c`  |
| 2592   | Layout 1 | `fecd11f7732c`  |
| 2583   | Layout 1 | `fecd11f7732c`  |
| 2575   | Layout 1 | `fecd11f7732c`  |
| 2567   | Layout 1 | `fecd11f7732c`  |
| 2560   | Layout 1 | `fecd11f7732c`  |
| 2553   | Layout 1 | `fecd11f7732c`  |
| 2545   | Layout 1 | `fecd11f7732c`  |
| 2538   | Layout 1 | `fecd11f7732c`  |
| 2529   | Layout 1 | `fecd11f7732c`  |
| 2519   | Layout 1 | `fecd11f7732c`  |
| 2513   | Layout 1 | `fecd11f7732c`  |
| 2510   | Layout 1 | `fecd11f7732c`  |
| 2507   | Layout 1 | `fecd11f7732c`  |
| 2503   | Layout 1 | `fecd11f7732c`  |
| 2498   | Layout 1 | `fecd11f7732c`  |
| 2492   | Layout 1 | `fecd11f7732c`  |
| 2487   | Layout 1 | `fecd11f7732c`  |
| 2480   | Layout 1 | `fecd11f7732c`  |
| 2474   | Layout 1 | `fecd11f7732c`  |
| 2468   | Layout 1 | `fecd11f7732c`  |
| 2460   | Layout 1 | `fecd11f7732c`  |
| 2453   | Layout 1 | `fecd11f7732c`  |
| 2444   | Layout 1 | `fecd11f7732c`  |
| 2438   | No file  | `fecd11f7732c`  |
| 2434   | No file  | `fecd11f7732c`  |
| 2429   | No file  | `fecd11f7732c`  |
| 2421   | No file  | `fecd11f7732c`  |
| 2414   | No file  | `fecd11f7732c`  |
| 2407   | No file  | `fecd11f7732c`  |
| 2401   | No file  | `fecd11f7732c`  |
| 2397   | No file  | `fecd11f7732c`  |
| 2393   | No file  | `fecd11f7732c`  |
| 2384   | No file  | `fecd11f7732c`  |
| 2378   | No file  | `fecd11f7732c`  |
| 2372   | No file  | `fecd11f7732c`  |
| 2358   | No file  | `fecd11f7732c`  |
| 2352   | No file  | `fecd11f7732c`  |
| 2347   | No file  | `fecd11f7732c`  |
| 2343   | No file  | `fecd11f7732c`  |
| 2335   | No file  | `fecd11f7732c`  |
| 2327   | No file  | `fecd11f7732c`  |
| 2324   | No file  | `fecd11f7732c`  |
| 2319   | No file  | `fecd11f7732c`  |
| 2313   | No file  | `fecd11f7732c`  |
| 2308   | No file  | `fecd11f7732c`  |
| 2302   | No file  | `fecd11f7732c`  |
| 2295   | No file  | `fecd11f7732c`  |
| 2290   | No file  | `fecd11f7732c`  |
| 2284   | No file  | `fecd11f7732c`  |
| 2276   | No file  | `fecd11f7732c`  |
| 2269   | No file  | `fecd11f7732c`  |
| 2259   | No file  | `fecd11f7732c`  |
| 2250   | No file  | `fecd11f7732c`  |
| 2243   | No file  | `fecd11f7732c`  |
| 2235   | No file  | `fecd11f7732c`  |
| 2229   | No file  | `fecd11f7732c`  |
| 2224   | No file  | `fecd11f7732c`  |
| 2218   | No file  | `fecd11f7732c`  |
| 2215   | No file  | `fecd11f7732c`  |
| 2207   | No file  | `fecd11f7732c`  |
| 2203   | No file  | `fecd11f7732c`  |
| 2196   | No file  | `fecd11f7732c`  |
| 2192   | No file  | `fecd11f7732c`  |
| 2189   | No file  | `fecd11f7732c`  |
| 2183   | No file  | `fecd11f7732c`  |
| 2179   | No file  | `fecd11f7732c`  |
| 2171   | No file  | `fecd11f7732c`  |
| 2163   | No file  | `fecd11f7732c`  |
| 2156   | No file  | `fecd11f7732c`  |
| 2151   | No file  | `fecd11f7732c`  |
| 2147   | No file  | `fecd11f7732c`  |
| 2142   | No file  | `fecd11f7732c`  |
| 2138   | No file  | `fecd11f7732c`  |
| 2134   | No file  | `fecd11f7732c`  |
| 2130   | No file  | `fecd11f7732c`  |
| 2122   | No file  | `fecd11f7732c`  |
| 2107   | No file  | `fecd11f7732c`  |
| 2098   | No file  | `fecd11f7732c`  |
| 2089   | No file  | `fecd11f7732c`  |
| 2081   | No file  | `fecd11f7732c`  |
| 2073   | No file  | `fecd11f7732c`  |
| 2067   | No file  | `fecd11f7732c`  |
| 2063   | No file  | `fecd11f7732c`  |
| 2059   | No file  | `fecd11f7732c`  |
| 2052   | No file  | `fecd11f7732c`  |
| 2044   | No file  | `fecd11f7732c`  |
| 2039   | No file  | `fecd11f7732c`  |
| 2032   | No file  | `fecd11f7732c`  |
| 2025   | No file  | `fecd11f7732c`  |
| 2011   | No file  | `fecd11f7732c`  |
| 2005   | No file  | `fecd11f7732c`  |
| 2000   | No file  | `fecd11f7732c`  |
| 1996   | No file  | `fecd11f7732c`  |
| 1991   | No file  | `fecd11f7732c`  |
| 1985   | No file  | `fecd11f7732c`  |
| 1980   | No file  | `fecd11f7732c`  |
| 1969   | No file  | `fecd11f7732c`  |
| 1964   | No file  | `fecd11f7732c`  |
| 1958   | No file  | `fecd11f7732c`  |
| 1950   | No file  | `fecd11f7732c`  |
| 1945   | No file  | `fecd11f7732c`  |
| 1937   | No file  | `fecd11f7732c`  |
| 1933   | No file  | `fecd11f7732c`  |
| 1927   | No file  | `fecd11f7732c`  |
| 1921   | No file  | `fecd11f7732c`  |
| 1914   | No file  | `fecd11f7732c`  |
| 1908   | No file  | `fecd11f7732c`  |
| 1897   | No file  | `fecd11f7732c`  |
| 1892   | No file  | `fecd11f7732c`  |
| 1886   | No file  | `fecd11f7732c`  |
| 1881   | No file  | `fecd11f7732c`  |
| 1871   | No file  | `fecd11f7732c`  |
| 1866   | No file  | `fecd11f7732c`  |
| 1862   | No file  | `fecd11f7732c`  |
| 1854   | No file  | `fecd11f7732c`  |
| 1846   | No file  | `fecd11f7732c`  |
| 1838   | No file  | `fecd11f7732c`  |
| 1832   | No file  | `fecd11f7732c`  |
| 1826   | No file  | `fecd11f7732c`  |
| 1822   | No file  | `fecd11f7732c`  |
| 1818   | No file  | `fecd11f7732c`  |
| 1804   | No file  | `fecd11f7732c`  |
| 1794   | No file  | `fecd11f7732c`  |
| 1790   | No file  | `fecd11f7732c`  |
| 1784   | No file  | `fecd11f7732c`  |
| 1774   | No file  | `fecd11f7732c`  |
| 1771   | No file  | `fecd11f7732c`  |
| 1762   | No file  | `fecd11f7732c`  |
| 1759   | No file  | `fecd11f7732c`  |
| 1754   | No file  | `fecd11f7732c`  |
| 1749   | No file  | `fecd11f7732c`  |
| 1743   | No file  | `fecd11f7732c`  |
| 1737   | No file  | `fecd11f7732c`  |
| 1731   | No file  | `fecd11f7732c`  |
| 1725   | No file  | `fecd11f7732c`  |
| 1717   | No file  | `fecd11f7732c`  |
| 1710   | No file  | `fecd11f7732c`  |
| 1704   | No file  | `fecd11f7732c`  |
| 1698   | No file  | `fecd11f7732c`  |
| 1690   | No file  | `fecd11f7732c`  |
| 1685   | No file  | `fecd11f7732c`  |
| 1680   | No file  | `fecd11f7732c`  |
| 1674   | No file  | `fecd11f7732c`  |
| 1668   | No file  | `fecd11f7732c`  |
| 1659   | No file  | `fecd11f7732c`  |
| 1649   | No file  | `fecd11f7732c`  |
| 1642   | No file  | `fecd11f7732c`  |
| 1636   | No file  | `fecd11f7732c`  |
| 1628   | No file  | `fecd11f7732c`  |
| 1622   | No file  | `fecd11f7732c`  |
| 1614   | No file  | `fecd11f7732c`  |
| 1608   | No file  | `fecd11f7732c`  |
| 1602   | No file  | `fecd11f7732c`  |
| 1598   | No file  | `fecd11f7732c`  |
| 1594   | No file  | `fecd11f7732c`  |
| 1590   | No file  | `fecd11f7732c`  |
| 1587   | No file  | `fecd11f7732c`  |
| 1584   | No file  | `fecd11f7732c`  |
| 1579   | No file  | `fecd11f7732c`  |
| 1572   | No file  | `fecd11f7732c`  |
| 1565   | No file  | `fecd11f7732c`  |
| 1559   | No file  | `fecd11f7732c`  |
| 1554   | No file  | `fecd11f7732c`  |
| 1547   | No file  | `fecd11f7732c`  |
| 1537   | No file  | `fecd11f7732c`  |
| 1529   | No file  | `fecd11f7732c`  |
| 1524   | No file  | `fecd11f7732c`  |
| 1519   | No file  | `fecd11f7732c`  |
| 1509   | No file  | `fecd11f7732c`  |
| 1506   | No file  | `fecd11f7732c`  |
| 1504   | No file  | `fecd11f7732c`  |
| 1500   | No file  | `fecd11f7732c`  |
| 1493   | No file  | `fecd11f7732c`  |
| 1489   | No file  | `fecd11f7732c`  |
| 1485   | No file  | `fecd11f7732c`  |
| 1481   | No file  | `fecd11f7732c`  |
| 1474   | No file  | `fecd11f7732c`  |
| 1466   | No file  | `fecd11f7732c`  |
| 1462   | No file  | `fecd11f7732c`  |
| 1459   | No file  | `fecd11f7732c`  |
| 1453   | No file  | `fecd11f7732c`  |
| 1450   | No file  | `fecd11f7732c`  |
| 1445   | No file  | `fecd11f7732c`  |
| 1439   | No file  | `fecd11f7732c`  |
| 1433   | No file  | `fecd11f7732c`  |
| 1430   | No file  | `fecd11f7732c`  |
| 1426   | No file  | `fecd11f7732c`  |
| 1421   | No file  | `fecd11f7732c`  |
| 1417   | No file  | `fecd11f7732c`  |
| 1416   | No file  | `fecd11f7732c`  |
| 1409   | No file  | `fecd11f7732c`  |
| 1405   | No file  | `fecd11f7732c`  |
| 1401   | No file  | `fecd11f7732c`  |
| 1396   | No file  | `fecd11f7732c`  |
| 1391   | No file  | `fecd11f7732c`  |
| 1390   | No file  | `fecd11f7732c`  |
| 1386   | No file  | `fecd11f7732c`  |
| 1381   | No file  | `fecd11f7732c`  |
| 1379   | No file  | `fecd11f7732c`  |
| 1372   | No file  | `fecd11f7732c`  |
| 1366   | No file  | `fecd11f7732c`  |
| 1364   | No file  | `fecd11f7732c`  |
| 1363   | No file  | `fecd11f7732c`  |
| 1360   | No file  | `fecd11f7732c`  |
| 1358   | No file  | `fecd11f7732c`  |
| 1355   | No file  | `fecd11f7732c`  |
| 1351   | No file  | `fecd11f7732c`  |
| 1348   | No file  | `fecd11f7732c`  |
| 1346   | No file  | `fecd11f7732c`  |
| 1341   | No file  | `fecd11f7732c`  |
| 1340   | No file  | `fecd11f7732c`  |
| 1338   | No file  | `fecd11f7732c`  |
| 1335   | No file  | `fecd11f7732c`  |
| 1333   | No file  | `fecd11f7732c`  |
| 1329   | No file  | `fecd11f7732c`  |
| 1327   | No file  | `fecd11f7732c`  |
| 1324   | No file  | `fecd11f7732c`  |
| 1321   | No file  | `fecd11f7732c`  |
| 1319   | No file  | `fecd11f7732c`  |
| 1318   | No file  | `fecd11f7732c`  |
| 1316   | No file  | `fecd11f7732c`  |
| 1313   | No file  | `fecd11f7732c`  |
| 1311   | No file  | `fecd11f7732c`  |
| 1309   | No file  | `fecd11f7732c`  |
| 1304   | No file  | `fecd11f7732c`  |
| 1292   | No file  | `fecd11f7732c`  |
| 1286   | No file  | `fecd11f7732c`  |
| 1280   | No file  | `fecd11f7732c`  |
| 1276   | No file  | `fecd11f7732c`  |
| 1267   | No file  | `fecd11f7732c`  |
| 1261   | No file  | `fecd11f7732c`  |
| 1256   | No file  | `fecd11f7732c`  |
| 1250   | No file  | `fecd11f7732c`  |
| 1246   | No file  | `fecd11f7732c`  |
| 1239   | No file  | `fecd11f7732c`  |
| 1230   | No file  | `fecd11f7732c`  |
| 1226   | No file  | `fecd11f7732c`  |
| 1220   | No file  | `fecd11f7732c`  |
| 1217   | No file  | `fecd11f7732c`  |
| 1211   | No file  | `fecd11f7732c`  |
| 1210   | No file  | `fecd11f7732c`  |
| 1208   | No file  | `fecd11f7732c`  |
| 1203   | No file  | `fecd11f7732c`  |
| 1197   | No file  | `fecd11f7732c`  |
| 1194   | No file  | `fecd11f7732c`  |
| 1192   | No file  | `fecd11f7732c`  |
| 1187   | No file  | `fecd11f7732c`  |
| 1183   | No file  | `fecd11f7732c`  |
| 1177   | No file  | `fecd11f7732c`  |
| 1173   | No file  | `fecd11f7732c`  |
| 1167   | No file  | `fecd11f7732c`  |
| 1164   | No file  | `fecd11f7732c`  |
| 1156   | No file  | `fecd11f7732c`  |
| 1149   | No file  | `fecd11f7732c`  |
| 1144   | No file  | `fecd11f7732c`  |
| 1137   | No file  | `fecd11f7732c`  |
| 1132   | No file  | `fecd11f7732c`  |
| 1127   | No file  | `fecd11f7732c`  |
| 1122   | No file  | `fecd11f7732c`  |
| 1118   | No file  | `fecd11f7732c`  |
| 1114   | No file  | `fecd11f7732c`  |
| 1109   | No file  | `fecd11f7732c`  |
| 1102   | No file  | `fecd11f7732c`  |
| 1096   | No file  | `fecd11f7732c`  |
| 1088   | No file  | `fecd11f7732c`  |
| 1081   | No file  | `fecd11f7732c`  |
| 1076   | No file  | `fecd11f7732c`  |
| 1069   | No file  | `fecd11f7732c`  |
| 1064   | No file  | `fecd11f7732c`  |
| 1058   | No file  | `fecd11f7732c`  |
| 1051   | No file  | `fecd11f7732c`  |
| 1044   | No file  | `fecd11f7732c`  |
| 1036   | No file  | `fecd11f7732c`  |
| 1026   | No file  | `fecd11f7732c`  |
| 1016   | No file  | `fecd11f7732c`  |
| 1009   | No file  | `fecd11f7732c`  |
| 1005   | No file  | `fecd11f7732c`  |
| 1000   | No file  | `fecd11f7732c`  |
| 998    | No file  | `fecd11f7732c`  |
| 990    | No file  | `fecd11f7732c`  |
| 979    | No file  | `fecd11f7732c`  |
| 972    | No file  | `fecd11f7732c`  |
| 963    | No file  | `fecd11f7732c`  |
| 955    | No file  | `fecd11f7732c`  |
| 946    | No file  | `fecd11f7732c`  |
| 938    | No file  | `fecd11f7732c`  |
| 927    | No file  | `fecd11f7732c`  |
| 911    | No file  | `fecd11f7732c`  |
| 904    | No file  | `fecd11f7732c`  |
| 899    | No file  | `fecd11f7732c`  |
| 894    | No file  | `fecd11f7732c`  |
| 885    | No file  | `fecd11f7732c`  |
| 879    | No file  | `fecd11f7732c`  |
| 872    | No file  | `fecd11f7732c`  |
| 864    | No file  | `fecd11f7732c`  |
| 855    | No file  | `fecd11f7732c`  |
| 853    | No file  | `fecd11f7732c`  |
| 845    | No file  | `fecd11f7732c`  |
| 837    | No file  | `fecd11f7732c`  |
| 829    | No file  | `fecd11f7732c`  |
| 822    | No file  | `fecd11f7732c`  |
| 814    | No file  | `fecd11f7732c`  |
| 805    | No file  | `fecd11f7732c`  |
| 794    | No file  | `fecd11f7732c`  |
| 787    | No file  | `fecd11f7732c`  |
| 780    | No file  | `fecd11f7732c`  |
| 771    | No file  | `fecd11f7732c`  |
| 760    | No file  | `fecd11f7732c`  |
| 748    | No file  | `fecd11f7732c`  |
| 741    | No file  | `fecd11f7732c`  |
| 736    | No file  | `fecd11f7732c`  |
| 731    | No file  | `fecd11f7732c`  |
| 723    | No file  | `fecd11f7732c`  |
| 711    | No file  | `fecd11f7732c`  |
| 707    | No file  | `fecd11f7732c`  |
| 697    | No file  | `fecd11f7732c`  |
| 689    | No file  | `fecd11f7732c`  |
| 683    | No file  | `fecd11f7732c`  |
| 678    | No file  | `fecd11f7732c`  |
| 670    | No file  | `fecd11f7732c`  |
| 661    | No file  | `fecd11f7732c`  |
| 656    | No file  | `fecd11f7732c`  |
| 652    | No file  | `fecd11f7732c`  |
| 643    | No file  | `fecd11f7732c`  |
| 637    | No file  | `fecd11f7732c`  |
| 630    | No file  | `fecd11f7732c`  |
| 627    | No file  | `fecd11f7732c`  |
| 621    | No file  | `fecd11f7732c`  |
| 617    | No file  | `fecd11f7732c`  |
| 615    | No file  | `fecd11f7732c`  |
| 606    | No file  | `fecd11f7732c`  |
| 599    | No file  | `fecd11f7732c`  |
| 592    | No file  | `fecd11f7732c`  |
| 586    | No file  | `fecd11f7732c`  |
| 577    | No file  | `fecd11f7732c`  |
| 569    | No file  | `fecd11f7732c`  |
| 561    | No file  | `fecd11f7732c`  |
| 554    | No file  | `fecd11f7732c`  |
| 542    | No file  | `fecd11f7732c`  |
| 532    | No file  | `fecd11f7732c`  |
| 531    | No file  | `fecd11f7732c`  |
| 526    | No file  | `fecd11f7732c`  |
| 521    | No file  | `fecd11f7732c`  |
| 517    | No file  | `fecd11f7732c`  |
| 510    | No file  | `fecd11f7732c`  |
| 508    | No file  | `fecd11f7732c`  |
| 504    | No file  | `fecd11f7732c`  |
| 497    | No file  | `fecd11f7732c`  |
| 491    | No file  | `fecd11f7732c`  |
| 485    | No file  | `fecd11f7732c`  |
| 478    | No file  | `fecd11f7732c`  |
| 472    | No file  | `fecd11f7732c`  |
| 466    | No file  | `fecd11f7732c`  |
| 457    | No file  | `fecd11f7732c`  |
| 452    | No file  | `fecd11f7732c`  |
| 449    | No file  | `fecd11f7732c`  |
| 435    | No file  | `fecd11f7732c`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows; `2` on every client checked   |
| `+0x08`             | Row[row_count] | rows         | See Row; no key                               |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 4 bytes + values)

| Offset  | Type              | Field       | Notes                                                       |
| ------- | ----------------- | ----------- | ----------------------------------------------------------- |
| `+0x00` | u32               | level_count | Number of values; `100` on every client checked             |
| `+0x04` | u32[level_count]  | combat_exp  | Combat EXP for character level `N + 1` at position `N`      |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The Guild League is newer than client 1784 and 2107, which do not ship the
file, so no sheet of a private server's `DataSheets.bexcel` covers it.
`combat_exp` follows the two reward items of clients 2519 to 3251 in
[guildmatchoption](guildmatchoption_bss.md): Guild League Victory Combat
EXP (56276) and Guild League Defeat Combat EXP (56277), whose LOC texts
read "Gain a certain amount of Combat EXP according to level for winning
(losing) in the Guild League". 100 values per row fit one per level, and
the values fall from level 41 on and reach their floor of `31` at level 68
(client 3251), which fits EXP by level; the EXP items' LOC text adds "EXP
gained diminishes from Lv. 60".

## Notes

- Clients 2519 to 3474 have the same 828 bytes, and clients 3002 and 3251
  the same values. Client 2519 matches them on levels 1 to 20 and 68 to
  100 only and is lower in between (row 0 at level 60 is 11,360 against
  49,200 on client 3251).
- Client 3474 replaced the two EXP items in the reward lists of
  [guildmatchoption](guildmatchoption_bss.md) and zeroed every value here.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the shared layout table in
  `_bss/pabr_values/guild_tables.py`, each row's 100 values in one cell.

## Open Questions

### Which Row Is the Victory

Row 1 is higher than row 0 at every level where both are above `31`,
which fits row 1 as the victory EXP and row 0 as the defeat EXP. Nothing
in the file or the Lua names the rows.
