# `yachtautobubbletextinfo.bss` Format

## Purpose

The speech bubbles of a Yar! match: what the player character and each
NPC opponent of [`yachtnpcdiceinfo.bss`](yachtnpcdiceinfo_bss.md) say when
something happens in the game. Each row is one trigger, either a game event
(scoring zero, winning, a turn passing) or a
[`yachthandrank.bss`](yachthandrank_bss.md) hand rank, with up to six
Korean lines. The plain PABR file holds the player's rows, then the NPCs'
rows, then the string table.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                          | Bytes  | Records | Row bytes |
| ------ | -------------- | ----------------------------- | ------ | ------- | --------- |
| 1      | 1762 and later | `yachtautobubbletextinfo.bss` | 10,529 | 61 Row  | 36        |

| Layout | File                          | Known            | Unknown     |
| ------ | ----------------------------- | ---------------- | ----------- |
| 1      | `yachtautobubbletextinfo.bss` | 10,468 B (99.4%) | 61 B (0.6%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `31d5a6ef2aa8`  |
| 3482   | Layout 1             | `31d5a6ef2aa8`  |
| 3474   | Layout 1             | `31d5a6ef2aa8`  |
| 3473   | Layout 1             | `31d5a6ef2aa8`  |
| 3464   | Layout 1             | `31d5a6ef2aa8`  |
| 3458   | Layout 1             | `31d5a6ef2aa8`  |
| 3454   | Layout 1             | `31d5a6ef2aa8`  |
| 3444   | Layout 1             | `31d5a6ef2aa8`  |
| 3435   | Layout 1             | `31d5a6ef2aa8`  |
| 3426   | Layout 1             | `31d5a6ef2aa8`  |
| 3418   | Layout 1             | `31d5a6ef2aa8`  |
| 3412   | Layout 1             | `31d5a6ef2aa8`  |
| 3402   | Layout 1             | `31d5a6ef2aa8`  |
| 3396   | Layout 1             | `31d5a6ef2aa8`  |
| 3387   | Layout 1             | `31d5a6ef2aa8`  |
| 3381   | Layout 1             | `31d5a6ef2aa8`  |
| 3373   | Layout 1             | `31d5a6ef2aa8`  |
| 3364   | Layout 1             | `31d5a6ef2aa8`  |
| 3356   | Layout 1             | `31d5a6ef2aa8`  |
| 3349   | Layout 1             | `31d5a6ef2aa8`  |
| 3342   | Layout 1             | `31d5a6ef2aa8`  |
| 3335   | Layout 1             | `31d5a6ef2aa8`  |
| 3326   | Layout 1             | `31d5a6ef2aa8`  |
| 3321   | Layout 1             | `31d5a6ef2aa8`  |
| 3314   | Layout 1             | `31d5a6ef2aa8`  |
| 3303   | Layout 1             | `31d5a6ef2aa8`  |
| 3302   | Layout 1             | `31d5a6ef2aa8`  |
| 3293   | Layout 1             | `31d5a6ef2aa8`  |
| 3283   | Layout 1             | `31d5a6ef2aa8`  |
| 3275   | Layout 1             | `31d5a6ef2aa8`  |
| 3267   | Layout 1             | `31d5a6ef2aa8`  |
| 3258   | Layout 1             | `31d5a6ef2aa8`  |
| 3251   | Layout 1             | `31d5a6ef2aa8`  |
| 3242   | Layout 1             | `31d5a6ef2aa8`  |
| 3235   | Layout 1             | `31d5a6ef2aa8`  |
| 3229   | Layout 1             | `31d5a6ef2aa8`  |
| 3212   | Layout 1             | `31d5a6ef2aa8`  |
| 3203   | Layout 1             | `31d5a6ef2aa8`  |
| 3193   | Layout 1             | `31d5a6ef2aa8`  |
| 3186   | Layout 1             | `31d5a6ef2aa8`  |
| 3177   | Layout 1             | `31d5a6ef2aa8`  |
| 3169   | Layout 1             | `31d5a6ef2aa8`  |
| 3158   | Layout 1             | `31d5a6ef2aa8`  |
| 3151   | Layout 1             | `31d5a6ef2aa8`  |
| 3144   | Layout 1             | `31d5a6ef2aa8`  |
| 3133   | Layout 1             | `31d5a6ef2aa8`  |
| 3125   | Layout 1             | `31d5a6ef2aa8`  |
| 3118   | Layout 1             | `31d5a6ef2aa8`  |
| 3111   | Layout 1             | `31d5a6ef2aa8`  |
| 3103   | Layout 1             | `31d5a6ef2aa8`  |
| 3095   | Layout 1             | `31d5a6ef2aa8`  |
| 3086   | Layout 1             | `31d5a6ef2aa8`  |
| 3072   | Layout 1             | `31d5a6ef2aa8`  |
| 3062   | Layout 1             | `31d5a6ef2aa8`  |
| 3052   | Layout 1             | `31d5a6ef2aa8`  |
| 3045   | Layout 1             | `31d5a6ef2aa8`  |
| 3037   | Layout 1             | `31d5a6ef2aa8`  |
| 3030   | Layout 1             | `31d5a6ef2aa8`  |
| 3021   | Layout 1             | `31d5a6ef2aa8`  |
| 3012   | Layout 1             | `31d5a6ef2aa8`  |
| 3002   | Layout 1             | `31d5a6ef2aa8`  |
| 2995   | Layout 1             | `31d5a6ef2aa8`  |
| 2987   | Layout 1             | `31d5a6ef2aa8`  |
| 2978   | Layout 1             | `31d5a6ef2aa8`  |
| 2970   | Layout 1             | `31d5a6ef2aa8`  |
| 2959   | Layout 1             | `31d5a6ef2aa8`  |
| 2951   | Layout 1             | `31d5a6ef2aa8`  |
| 2942   | Layout 1             | `31d5a6ef2aa8`  |
| 2935   | Layout 1             | `31d5a6ef2aa8`  |
| 2932   | Layout 1             | `31d5a6ef2aa8`  |
| 2923   | Layout 1             | `31d5a6ef2aa8`  |
| 2919   | Layout 1             | `31d5a6ef2aa8`  |
| 2907   | Layout 1             | `31d5a6ef2aa8`  |
| 2900   | Layout 1             | `31d5a6ef2aa8`  |
| 2891   | Layout 1             | `31d5a6ef2aa8`  |
| 2882   | Layout 1             | `31d5a6ef2aa8`  |
| 2872   | Layout 1             | `31d5a6ef2aa8`  |
| 2863   | Layout 1             | `31d5a6ef2aa8`  |
| 2855   | Layout 1             | `31d5a6ef2aa8`  |
| 2849   | Layout 1             | `31d5a6ef2aa8`  |
| 2844   | Layout 1             | `31d5a6ef2aa8`  |
| 2834   | Layout 1             | `31d5a6ef2aa8`  |
| 2825   | Layout 1             | `31d5a6ef2aa8`  |
| 2819   | Layout 1             | `31d5a6ef2aa8`  |
| 2811   | Layout 1             | `31d5a6ef2aa8`  |
| 2803   | Layout 1             | `31d5a6ef2aa8`  |
| 2794   | Layout 1             | `31d5a6ef2aa8`  |
| 2783   | Layout 1             | `31d5a6ef2aa8`  |
| 2774   | Layout 1             | `31d5a6ef2aa8`  |
| 2765   | Layout 1             | `31d5a6ef2aa8`  |
| 2756   | Layout 1             | `31d5a6ef2aa8`  |
| 2750   | Layout 1             | `31d5a6ef2aa8`  |
| 2743   | Layout 1             | `31d5a6ef2aa8`  |
| 2736   | Layout 1             | `31d5a6ef2aa8`  |
| 2726   | Layout 1             | `31d5a6ef2aa8`  |
| 2717   | Layout 1             | `31d5a6ef2aa8`  |
| 2709   | Layout 1             | `31d5a6ef2aa8`  |
| 2703   | Layout 1             | `31d5a6ef2aa8`  |
| 2695   | Layout 1             | `31d5a6ef2aa8`  |
| 2684   | Layout 1             | `31d5a6ef2aa8`  |
| 2672   | Layout 1             | `31d5a6ef2aa8`  |
| 2665   | Layout 1             | `31d5a6ef2aa8`  |
| 2657   | Layout 1             | `31d5a6ef2aa8`  |
| 2649   | Layout 1             | `31d5a6ef2aa8`  |
| 2644   | Layout 1             | `31d5a6ef2aa8`  |
| 2637   | Layout 1             | `31d5a6ef2aa8`  |
| 2629   | Layout 1             | `31d5a6ef2aa8`  |
| 2619   | Layout 1             | `31d5a6ef2aa8`  |
| 2612   | Layout 1             | `31d5a6ef2aa8`  |
| 2606   | Layout 1             | `31d5a6ef2aa8`  |
| 2602   | Layout 1             | `31d5a6ef2aa8`  |
| 2601   | Layout 1             | `31d5a6ef2aa8`  |
| 2592   | Layout 1             | `31d5a6ef2aa8`  |
| 2583   | Layout 1             | `31d5a6ef2aa8`  |
| 2575   | Layout 1             | `31d5a6ef2aa8`  |
| 2567   | Layout 1             | `31d5a6ef2aa8`  |
| 2560   | Layout 1             | `31d5a6ef2aa8`  |
| 2553   | Layout 1             | `31d5a6ef2aa8`  |
| 2545   | Layout 1             | `31d5a6ef2aa8`  |
| 2538   | Layout 1             | `31d5a6ef2aa8`  |
| 2529   | Layout 1             | `31d5a6ef2aa8`  |
| 2519   | Layout 1             | `31d5a6ef2aa8`  |
| 2513   | Layout 1             | `31d5a6ef2aa8`  |
| 2510   | Layout 1             | `31d5a6ef2aa8`  |
| 2507   | Layout 1             | `31d5a6ef2aa8`  |
| 2503   | Layout 1             | `31d5a6ef2aa8`  |
| 2498   | Layout 1             | `31d5a6ef2aa8`  |
| 2492   | Layout 1             | `31d5a6ef2aa8`  |
| 2487   | Layout 1             | `31d5a6ef2aa8`  |
| 2480   | Layout 1             | `31d5a6ef2aa8`  |
| 2474   | Layout 1             | `31d5a6ef2aa8`  |
| 2468   | Layout 1             | `31d5a6ef2aa8`  |
| 2460   | Layout 1             | `31d5a6ef2aa8`  |
| 2453   | Layout 1             | `31d5a6ef2aa8`  |
| 2444   | Layout 1             | `31d5a6ef2aa8`  |
| 2438   | Layout 1             | `31d5a6ef2aa8`  |
| 2434   | Layout 1             | `31d5a6ef2aa8`  |
| 2429   | Layout 1             | `31d5a6ef2aa8`  |
| 2421   | Layout 1             | `31d5a6ef2aa8`  |
| 2414   | Layout 1             | `31d5a6ef2aa8`  |
| 2407   | Layout 1             | `31d5a6ef2aa8`  |
| 2401   | Layout 1             | `31d5a6ef2aa8`  |
| 2397   | Layout 1             | `31d5a6ef2aa8`  |
| 2393   | Layout 1             | `31d5a6ef2aa8`  |
| 2384   | Layout 1             | `31d5a6ef2aa8`  |
| 2378   | Layout 1             | `31d5a6ef2aa8`  |
| 2372   | Layout 1             | `31d5a6ef2aa8`  |
| 2358   | Layout 1             | `31d5a6ef2aa8`  |
| 2352   | Layout 1             | `31d5a6ef2aa8`  |
| 2347   | Layout 1             | `31d5a6ef2aa8`  |
| 2343   | Layout 1             | `31d5a6ef2aa8`  |
| 2335   | Layout 1             | `31d5a6ef2aa8`  |
| 2327   | Layout 1             | `31d5a6ef2aa8`  |
| 2324   | Layout 1             | `31d5a6ef2aa8`  |
| 2319   | Layout 1             | `31d5a6ef2aa8`  |
| 2313   | Layout 1             | `31d5a6ef2aa8`  |
| 2308   | Layout 1             | `31d5a6ef2aa8`  |
| 2302   | Layout 1             | `31d5a6ef2aa8`  |
| 2295   | Layout 1             | `31d5a6ef2aa8`  |
| 2290   | Layout 1             | `31d5a6ef2aa8`  |
| 2284   | Layout 1             | `31d5a6ef2aa8`  |
| 2276   | Layout 1             | `31d5a6ef2aa8`  |
| 2269   | Layout 1             | `31d5a6ef2aa8`  |
| 2259   | Layout 1             | `31d5a6ef2aa8`  |
| 2250   | Layout 1             | `31d5a6ef2aa8`  |
| 2243   | Layout 1             | `31d5a6ef2aa8`  |
| 2235   | Layout 1             | `31d5a6ef2aa8`  |
| 2229   | Layout 1             | `31d5a6ef2aa8`  |
| 2224   | Layout 1             | `31d5a6ef2aa8`  |
| 2218   | Layout 1             | `31d5a6ef2aa8`  |
| 2215   | Layout 1             | `31d5a6ef2aa8`  |
| 2207   | Layout 1             | `31d5a6ef2aa8`  |
| 2203   | Layout 1             | `31d5a6ef2aa8`  |
| 2196   | Layout 1             | `31d5a6ef2aa8`  |
| 2192   | Layout 1             | `31d5a6ef2aa8`  |
| 2189   | Layout 1             | `31d5a6ef2aa8`  |
| 2183   | Layout 1             | `31d5a6ef2aa8`  |
| 2179   | Layout 1             | `31d5a6ef2aa8`  |
| 2171   | Layout 1             | `31d5a6ef2aa8`  |
| 2163   | Layout 1             | `31d5a6ef2aa8`  |
| 2156   | Layout 1             | `31d5a6ef2aa8`  |
| 2151   | Layout 1             | `31d5a6ef2aa8`  |
| 2147   | Layout 1             | `31d5a6ef2aa8`  |
| 2142   | Layout 1             | `31d5a6ef2aa8`  |
| 2138   | Layout 1             | `31d5a6ef2aa8`  |
| 2134   | Layout 1             | `31d5a6ef2aa8`  |
| 2130   | Layout 1             | `31d5a6ef2aa8`  |
| 2122   | Layout 1             | `31d5a6ef2aa8`  |
| 2107   | Layout 1             | `31d5a6ef2aa8`  |
| 2098   | Layout 1             | `31d5a6ef2aa8`  |
| 2089   | Layout 1             | `31d5a6ef2aa8`  |
| 2081   | Layout 1             | `31d5a6ef2aa8`  |
| 2073   | Layout 1             | `31d5a6ef2aa8`  |
| 2067   | Layout 1             | `31d5a6ef2aa8`  |
| 2063   | Layout 1             | `31d5a6ef2aa8`  |
| 2059   | Layout 1             | `31d5a6ef2aa8`  |
| 2052   | Layout 1             | `31d5a6ef2aa8`  |
| 2044   | Layout 1             | `31d5a6ef2aa8`  |
| 2039   | Layout 1             | `31d5a6ef2aa8`  |
| 2032   | Layout 1             | `31d5a6ef2aa8`  |
| 2025   | Layout 1             | `31d5a6ef2aa8`  |
| 2011   | Layout 1             | `31d5a6ef2aa8`  |
| 2005   | Layout 1             | `31d5a6ef2aa8`  |
| 2000   | Layout 1             | `31d5a6ef2aa8`  |
| 1996   | Layout 1             | `31d5a6ef2aa8`  |
| 1991   | Layout 1             | `31d5a6ef2aa8`  |
| 1985   | Layout 1             | `31d5a6ef2aa8`  |
| 1980   | Layout 1             | `31d5a6ef2aa8`  |
| 1969   | Layout 1             | `31d5a6ef2aa8`  |
| 1964   | Layout 1             | `31d5a6ef2aa8`  |
| 1958   | Layout 1             | `31d5a6ef2aa8`  |
| 1950   | Layout 1             | `31d5a6ef2aa8`  |
| 1945   | Layout 1             | `31d5a6ef2aa8`  |
| 1937   | Layout 1             | `31d5a6ef2aa8`  |
| 1933   | Layout 1             | `31d5a6ef2aa8`  |
| 1927   | Layout 1             | `31d5a6ef2aa8`  |
| 1921   | Layout 1             | `31d5a6ef2aa8`  |
| 1914   | Layout 1             | `31d5a6ef2aa8`  |
| 1908   | Layout 1             | `31d5a6ef2aa8`  |
| 1897   | Layout 1             | `31d5a6ef2aa8`  |
| 1892   | Layout 1             | `31d5a6ef2aa8`  |
| 1886   | Layout 1             | `31d5a6ef2aa8`  |
| 1881   | Layout 1             | `31d5a6ef2aa8`  |
| 1871   | Layout 1             | `31d5a6ef2aa8`  |
| 1866   | Layout 1             | `31d5a6ef2aa8`  |
| 1862   | Layout 1             | `31d5a6ef2aa8`  |
| 1854   | Layout 1             | `31d5a6ef2aa8`  |
| 1846   | Layout 1             | `31d5a6ef2aa8`  |
| 1838   | Layout 1             | `31d5a6ef2aa8`  |
| 1832   | Layout 1             | `31d5a6ef2aa8`  |
| 1826   | Layout 1             | `31d5a6ef2aa8`  |
| 1822   | Layout 1             | `31d5a6ef2aa8`  |
| 1818   | Layout 1             | `31d5a6ef2aa8`  |
| 1804   | Layout 1             | `31d5a6ef2aa8`  |
| 1794   | Layout 1             | `31d5a6ef2aa8`  |
| 1790   | Layout 1             | `31d5a6ef2aa8`  |
| 1784   | Layout 1             | `31d5a6ef2aa8`  |
| 1774   | Layout 1             | `31d5a6ef2aa8`  |
| 1771   | Layout 1             | `31d5a6ef2aa8`  |
| 1762   | Layout 1             | `31d5a6ef2aa8`  |
| 1759   | No documented layout | `31d5a6ef2aa8`  |
| 1754   | No file              | `31d5a6ef2aa8`  |
| 1749   | No file              | `31d5a6ef2aa8`  |
| 1743   | No file              | `31d5a6ef2aa8`  |
| 1737   | No file              | `31d5a6ef2aa8`  |
| 1731   | No file              | `31d5a6ef2aa8`  |
| 1725   | No file              | `31d5a6ef2aa8`  |
| 1717   | No file              | `31d5a6ef2aa8`  |
| 1710   | No file              | `31d5a6ef2aa8`  |
| 1704   | No file              | `31d5a6ef2aa8`  |
| 1698   | No file              | `31d5a6ef2aa8`  |
| 1690   | No file              | `31d5a6ef2aa8`  |
| 1685   | No file              | `31d5a6ef2aa8`  |
| 1680   | No file              | `31d5a6ef2aa8`  |
| 1674   | No file              | `31d5a6ef2aa8`  |
| 1668   | No file              | `31d5a6ef2aa8`  |
| 1659   | No file              | `31d5a6ef2aa8`  |
| 1649   | No file              | `31d5a6ef2aa8`  |
| 1642   | No file              | `31d5a6ef2aa8`  |
| 1636   | No file              | `31d5a6ef2aa8`  |
| 1628   | No file              | `31d5a6ef2aa8`  |
| 1622   | No file              | `31d5a6ef2aa8`  |
| 1614   | No file              | `31d5a6ef2aa8`  |
| 1608   | No file              | `31d5a6ef2aa8`  |
| 1602   | No file              | `31d5a6ef2aa8`  |
| 1598   | No file              | `31d5a6ef2aa8`  |
| 1594   | No file              | `31d5a6ef2aa8`  |
| 1590   | No file              | `31d5a6ef2aa8`  |
| 1587   | No file              | `31d5a6ef2aa8`  |
| 1584   | No file              | `31d5a6ef2aa8`  |
| 1579   | No file              | `31d5a6ef2aa8`  |
| 1572   | No file              | `31d5a6ef2aa8`  |
| 1565   | No file              | `31d5a6ef2aa8`  |
| 1559   | No file              | `31d5a6ef2aa8`  |
| 1554   | No file              | `31d5a6ef2aa8`  |
| 1547   | No file              | `31d5a6ef2aa8`  |
| 1537   | No file              | `31d5a6ef2aa8`  |
| 1529   | No file              | `31d5a6ef2aa8`  |
| 1524   | No file              | `31d5a6ef2aa8`  |
| 1519   | No file              | `31d5a6ef2aa8`  |
| 1509   | No file              | `31d5a6ef2aa8`  |
| 1506   | No file              | `31d5a6ef2aa8`  |
| 1504   | No file              | `31d5a6ef2aa8`  |
| 1500   | No file              | `31d5a6ef2aa8`  |
| 1493   | No file              | `31d5a6ef2aa8`  |
| 1489   | No file              | `31d5a6ef2aa8`  |
| 1485   | No file              | `31d5a6ef2aa8`  |
| 1481   | No file              | `31d5a6ef2aa8`  |
| 1474   | No file              | `31d5a6ef2aa8`  |
| 1466   | No file              | `31d5a6ef2aa8`  |
| 1462   | No file              | `31d5a6ef2aa8`  |
| 1459   | No file              | `31d5a6ef2aa8`  |
| 1453   | No file              | `31d5a6ef2aa8`  |
| 1450   | No file              | `31d5a6ef2aa8`  |
| 1445   | No file              | `31d5a6ef2aa8`  |
| 1439   | No file              | `31d5a6ef2aa8`  |
| 1433   | No file              | `31d5a6ef2aa8`  |
| 1430   | No file              | `31d5a6ef2aa8`  |
| 1426   | No file              | `31d5a6ef2aa8`  |
| 1421   | No file              | `31d5a6ef2aa8`  |
| 1417   | No file              | `31d5a6ef2aa8`  |
| 1416   | No file              | `31d5a6ef2aa8`  |
| 1409   | No file              | `31d5a6ef2aa8`  |
| 1405   | No file              | `31d5a6ef2aa8`  |
| 1401   | No file              | `31d5a6ef2aa8`  |
| 1396   | No file              | `31d5a6ef2aa8`  |
| 1391   | No file              | `31d5a6ef2aa8`  |
| 1390   | No file              | `31d5a6ef2aa8`  |
| 1386   | No file              | `31d5a6ef2aa8`  |
| 1381   | No file              | `31d5a6ef2aa8`  |
| 1379   | No file              | `31d5a6ef2aa8`  |
| 1372   | No file              | `31d5a6ef2aa8`  |
| 1366   | No file              | `31d5a6ef2aa8`  |
| 1364   | No file              | `31d5a6ef2aa8`  |
| 1363   | No file              | `31d5a6ef2aa8`  |
| 1360   | No file              | `31d5a6ef2aa8`  |
| 1358   | No file              | `31d5a6ef2aa8`  |
| 1355   | No file              | `31d5a6ef2aa8`  |
| 1351   | No file              | `31d5a6ef2aa8`  |
| 1348   | No file              | `31d5a6ef2aa8`  |
| 1346   | No file              | `31d5a6ef2aa8`  |
| 1341   | No file              | `31d5a6ef2aa8`  |
| 1340   | No file              | `31d5a6ef2aa8`  |
| 1338   | No file              | `31d5a6ef2aa8`  |
| 1335   | No file              | `31d5a6ef2aa8`  |
| 1333   | No file              | `31d5a6ef2aa8`  |
| 1329   | No file              | `31d5a6ef2aa8`  |
| 1327   | No file              | `31d5a6ef2aa8`  |
| 1324   | No file              | `31d5a6ef2aa8`  |
| 1321   | No file              | `31d5a6ef2aa8`  |
| 1319   | No file              | `31d5a6ef2aa8`  |
| 1318   | No file              | `31d5a6ef2aa8`  |
| 1316   | No file              | `31d5a6ef2aa8`  |
| 1313   | No file              | `31d5a6ef2aa8`  |
| 1311   | No file              | `31d5a6ef2aa8`  |
| 1309   | No file              | `31d5a6ef2aa8`  |
| 1304   | No file              | `31d5a6ef2aa8`  |
| 1292   | No file              | `31d5a6ef2aa8`  |
| 1286   | No file              | `31d5a6ef2aa8`  |
| 1280   | No file              | `31d5a6ef2aa8`  |
| 1276   | No file              | `31d5a6ef2aa8`  |
| 1267   | No file              | `31d5a6ef2aa8`  |
| 1261   | No file              | `31d5a6ef2aa8`  |
| 1256   | No file              | `31d5a6ef2aa8`  |
| 1250   | No file              | `31d5a6ef2aa8`  |
| 1246   | No file              | `31d5a6ef2aa8`  |
| 1239   | No file              | `31d5a6ef2aa8`  |
| 1230   | No file              | `31d5a6ef2aa8`  |
| 1226   | No file              | `31d5a6ef2aa8`  |
| 1220   | No file              | `31d5a6ef2aa8`  |
| 1217   | No file              | `31d5a6ef2aa8`  |
| 1211   | No file              | `31d5a6ef2aa8`  |
| 1210   | No file              | `31d5a6ef2aa8`  |
| 1208   | No file              | `31d5a6ef2aa8`  |
| 1203   | No file              | `31d5a6ef2aa8`  |
| 1197   | No file              | `31d5a6ef2aa8`  |
| 1194   | No file              | `31d5a6ef2aa8`  |
| 1192   | No file              | `31d5a6ef2aa8`  |
| 1187   | No file              | `31d5a6ef2aa8`  |
| 1183   | No file              | `31d5a6ef2aa8`  |
| 1177   | No file              | `31d5a6ef2aa8`  |
| 1173   | No file              | `31d5a6ef2aa8`  |
| 1167   | No file              | `31d5a6ef2aa8`  |
| 1164   | No file              | `31d5a6ef2aa8`  |
| 1156   | No file              | `31d5a6ef2aa8`  |
| 1149   | No file              | `31d5a6ef2aa8`  |
| 1144   | No file              | `31d5a6ef2aa8`  |
| 1137   | No file              | `31d5a6ef2aa8`  |
| 1132   | No file              | `31d5a6ef2aa8`  |
| 1127   | No file              | `31d5a6ef2aa8`  |
| 1122   | No file              | `31d5a6ef2aa8`  |
| 1118   | No file              | `31d5a6ef2aa8`  |
| 1114   | No file              | `31d5a6ef2aa8`  |
| 1109   | No file              | `31d5a6ef2aa8`  |
| 1102   | No file              | `31d5a6ef2aa8`  |
| 1096   | No file              | `31d5a6ef2aa8`  |
| 1088   | No file              | `31d5a6ef2aa8`  |
| 1081   | No file              | `31d5a6ef2aa8`  |
| 1076   | No file              | `31d5a6ef2aa8`  |
| 1069   | No file              | `31d5a6ef2aa8`  |
| 1064   | No file              | `31d5a6ef2aa8`  |
| 1058   | No file              | `31d5a6ef2aa8`  |
| 1051   | No file              | `31d5a6ef2aa8`  |
| 1044   | No file              | `31d5a6ef2aa8`  |
| 1036   | No file              | `31d5a6ef2aa8`  |
| 1026   | No file              | `31d5a6ef2aa8`  |
| 1016   | No file              | `31d5a6ef2aa8`  |
| 1009   | No file              | `31d5a6ef2aa8`  |
| 1005   | No file              | `31d5a6ef2aa8`  |
| 1000   | No file              | `31d5a6ef2aa8`  |
| 998    | No file              | `31d5a6ef2aa8`  |
| 990    | No file              | `31d5a6ef2aa8`  |
| 979    | No file              | `31d5a6ef2aa8`  |
| 972    | No file              | `31d5a6ef2aa8`  |
| 963    | No file              | `31d5a6ef2aa8`  |
| 955    | No file              | `31d5a6ef2aa8`  |
| 946    | No file              | `31d5a6ef2aa8`  |
| 938    | No file              | `31d5a6ef2aa8`  |
| 927    | No file              | `31d5a6ef2aa8`  |
| 911    | No file              | `31d5a6ef2aa8`  |
| 904    | No file              | `31d5a6ef2aa8`  |
| 899    | No file              | `31d5a6ef2aa8`  |
| 894    | No file              | `31d5a6ef2aa8`  |
| 885    | No file              | `31d5a6ef2aa8`  |
| 879    | No file              | `31d5a6ef2aa8`  |
| 872    | No file              | `31d5a6ef2aa8`  |
| 864    | No file              | `31d5a6ef2aa8`  |
| 855    | No file              | `31d5a6ef2aa8`  |
| 853    | No file              | `31d5a6ef2aa8`  |
| 845    | No file              | `31d5a6ef2aa8`  |
| 837    | No file              | `31d5a6ef2aa8`  |
| 829    | No file              | `31d5a6ef2aa8`  |
| 822    | No file              | `31d5a6ef2aa8`  |
| 814    | No file              | `31d5a6ef2aa8`  |
| 805    | No file              | `31d5a6ef2aa8`  |
| 794    | No file              | `31d5a6ef2aa8`  |
| 787    | No file              | `31d5a6ef2aa8`  |
| 780    | No file              | `31d5a6ef2aa8`  |
| 771    | No file              | `31d5a6ef2aa8`  |
| 760    | No file              | `31d5a6ef2aa8`  |
| 748    | No file              | `31d5a6ef2aa8`  |
| 741    | No file              | `31d5a6ef2aa8`  |
| 736    | No file              | `31d5a6ef2aa8`  |
| 731    | No file              | `31d5a6ef2aa8`  |
| 723    | No file              | `31d5a6ef2aa8`  |
| 711    | No file              | `31d5a6ef2aa8`  |
| 707    | No file              | `31d5a6ef2aa8`  |
| 697    | No file              | `31d5a6ef2aa8`  |
| 689    | No file              | `31d5a6ef2aa8`  |
| 683    | No file              | `31d5a6ef2aa8`  |
| 678    | No file              | `31d5a6ef2aa8`  |
| 670    | No file              | `31d5a6ef2aa8`  |
| 661    | No file              | `31d5a6ef2aa8`  |
| 656    | No file              | `31d5a6ef2aa8`  |
| 652    | No file              | `31d5a6ef2aa8`  |
| 643    | No file              | `31d5a6ef2aa8`  |
| 637    | No file              | `31d5a6ef2aa8`  |
| 630    | No file              | `31d5a6ef2aa8`  |
| 627    | No file              | `31d5a6ef2aa8`  |
| 621    | No file              | `31d5a6ef2aa8`  |
| 617    | No file              | `31d5a6ef2aa8`  |
| 615    | No file              | `31d5a6ef2aa8`  |
| 606    | No file              | `31d5a6ef2aa8`  |
| 599    | No file              | `31d5a6ef2aa8`  |
| 592    | No file              | `31d5a6ef2aa8`  |
| 586    | No file              | `31d5a6ef2aa8`  |
| 577    | No file              | `31d5a6ef2aa8`  |
| 569    | No file              | `31d5a6ef2aa8`  |
| 561    | No file              | `31d5a6ef2aa8`  |
| 554    | No file              | `31d5a6ef2aa8`  |
| 542    | No file              | `31d5a6ef2aa8`  |
| 532    | No file              | `31d5a6ef2aa8`  |
| 531    | No file              | `31d5a6ef2aa8`  |
| 526    | No file              | `31d5a6ef2aa8`  |
| 521    | No file              | `31d5a6ef2aa8`  |
| 517    | No file              | `31d5a6ef2aa8`  |
| 510    | No file              | `31d5a6ef2aa8`  |
| 508    | No file              | `31d5a6ef2aa8`  |
| 504    | No file              | `31d5a6ef2aa8`  |
| 497    | No file              | `31d5a6ef2aa8`  |
| 491    | No file              | `31d5a6ef2aa8`  |
| 485    | No file              | `31d5a6ef2aa8`  |
| 478    | No file              | `31d5a6ef2aa8`  |
| 472    | No file              | `31d5a6ef2aa8`  |
| 466    | No file              | `31d5a6ef2aa8`  |
| 457    | No file              | `31d5a6ef2aa8`  |
| 452    | No file              | `31d5a6ef2aa8`  |
| 449    | No file              | `31d5a6ef2aa8`  |
| 435    | No file              | `31d5a6ef2aa8`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                                                 |
| --------------------- | -------- | ---------------------------------------------------------------------------------------------------- |
| `yachthandrank.bss`   | Optional | Korean hand rank names, where LOC has none                                                           |
| `languagedata_en.loc` | Optional | Lines (LOC type 112, `str_id1=bubble_text_key`, `str_id4` = line slot `0` to `5`), NPC names (LOC type 6), hand rank names (LOC type 105) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type            | Field              | Notes                                         |
| ------------------- | --------------- | ------------------ | --------------------------------------------- |
| `+0x00`             | char[4]         | magic              | ASCII `PABR`                                  |
| `+0x04`             | u32             | pc_count           | Number of player rows                         |
| `+0x08`             | Row[pc_count]   | pc_rows            | Rows with `character_key` `0`; see Row        |
| `pc_rows+0x00`      | u32             | npc_count          | Number of NPC rows                            |
| `pc_rows+0x04`      | Row[npc_count]  | npc_rows           | Rows with an NPC's `character_key`; see Row   |
| `npc_rows+0x00`     | String Table    | string_table       | See String Table                              |
| `string_table+0x00` | u32             | string_table_start | Offset of `string_count`, where the rows end  |
| `string_table+0x04` | u32             | zero               | Always `0`                                    |

The string table has the shape `exploration.bss` and `npcsimply.bss` use
(`_common/pabr_strings.py`). The NPC rows end exactly at
`string_table_start`.

### Row (36 bytes)

| Offset  | Type   | Field            | Notes                                                                       |
| ------- | ------ | ---------------- | --------------------------------------------------------------------------- |
| `+0x00` | u32    | bubble_text_key  | Unique key over both groups, LOC type 112 `str_id1`                         |
| `+0x04` | u16    | character_key    | The NPC who speaks; `0` in every player row                                 |
| `+0x06` | u32    | hand_rank_key    | The `yachthandrank.bss` hand that triggers the row; `0` when `condition` does |
| `+0x0A` | u32[6] | text_kr_indexes  | String table index of each Korean line; unused slots point at an empty string |
| `+0x22` | u8     | condition        | The game event that triggers the row, see Conditions; `0` when `hand_rank_key` does |
| `+0x23` | u8     | unknown_23       | `1` in every player row, `0` in every NPC row (clients 1784 and 3474)       |

The two groups share the key range: on client 3474 the player rows hold
keys 1 to 5 and the NPC rows 6 to 61.

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                        |
| ------- | ------------------ | ------------ | ------------------------------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings (185 on client 3474)                       |
| `+0x04` | pstr[string_count] | strings      | UTF-16 lines, each once: rows with the same line share its index |

## Conditions

The names come from the developer note on the `Condition` column in the
`#참조` sheet of a private server's `datasheet_minigame.xlsm` on client
1784; the speaker is the row's NPC, or the player in a player row.

| Value | Trigger                                  |
| ----- | ---------------------------------------- |
| `0`   | None; the row has a `hand_rank_key`      |
| `1`   | The speaker scores 0 points              |
| `2`   | The speaker scores more than the opponent |
| `3`   | The game starts                          |
| `4`   | The speaker wins                         |
| `5`   | The speaker loses                        |
| `6`   | 10 seconds are left in the turn          |
| `7`   | The turn passes to the speaker           |

On client 3474 the 5 player rows are conditions `1` and `2` and hand ranks
`11`, `12` and `14`. Each of the 8 NPCs of `yachtnpcdiceinfo.bss` has 7
rows, conditions `1` to `7` in order; condition `7` has six lines, every
other row three.

## Field Names

The `YachtBubbleText` sheet of a private server's `datasheet_minigame.xlsm`
on client 1784 has the columns `Index` (`bubble_text_key`), `CharacterKey`
(`character_key`), `Condition` (`condition`), `HandRankKey`
(`hand_rank_key`) and `~Desc_1` to `~Desc_6` (`text_kr_indexes`, in slot
order). Its 33 rows match the 33 rows of client 1784 and rows 1 to 33 of
client 3474 in every column and line. The sheet has no column for
`unknown_23` and no grouping: the file puts the rows without an NPC first,
which the `#참조` sheet marks as the player (`<null> = PC`).

## Notes

- Client 1784 holds the 5 player rows and 28 NPC rows (keys 6 to 33, the
  first four NPCs). Client 3474 adds keys 34 to 61 for Narangerel, Kakuo,
  Shakatu and Nolbu.
- Kakuo (`59739`) reuses Crio's (`40012`) Korean lines, one line aside, so
  their rows share string indexes. LOC type 112 gives each its own English
  text: slot 2 of Crio's key 20 reads "Were these cards hidden up your
  sleeve? Queek?", slot 2 of Kakuo's key 41 "Were these cards hidden up yer
  sleeve? Queek?".
- The client Lua calls no getter of this table. The match window
  (`panel_window_minigame_yachtdice_2.luac`) gets each bubble through the
  event `FromClient_processYachtGameBubbleText(isPlayer, bubbleText)` and
  shows it only in a game against an NPC
  (`__eMiniGameDBType_YachtDice_PVE`).

## Open Questions

### What `unknown_23` Is

The byte is `1` in the 5 player rows and `0` in the NPC rows on both
clients, so it repeats which group a row is in. No sheet column holds it.
The bubble event passes an `isPlayer` flag, which the byte may feed; a
player row with `0`, or an NPC row with `1`, would tell whether it is a
separate flag.
