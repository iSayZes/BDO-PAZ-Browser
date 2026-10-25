# `icefisingstaticstatus.bss` Format

## Purpose

The settings of the ice fishing mini-game, one row per mini-game group:
wait and game times, the fish's HP and the HP a hit and a critical hit
take, block, speed and durability values and the reward drop group. [`icefisingregionstaticstatus.bss`](icefisingregionstaticstatus_bss.md)
gives each ice fishing region its group. The client Lua opens the game
through `Panel_MiniGame_IceFishing_All` behind
`_ContentsGroup_IceFishingGame` and shows the time left as
`LUA_ICEFISHING_TIME` ("Remaining: {time} sec"); it reads none of these
values.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                        | Bytes | Records               | Row bytes |
| ------ | -------------- | --------------------------- | ----- | --------------------- | --------- |
| 2      | 2726 and later | `icefisingstaticstatus.bss` | 240   | 2 Row                 | 110       |
| 1      | 1784 to 2717   | `icefisingstaticstatus.bss` | 128   | 1 Row, 1 String Table | 108       |

| Layout | File                        | Known          | Unknown    |
| ------ | --------------------------- | -------------- | ---------- |
| 2      | `icefisingstaticstatus.bss` | 240 B (100.0%) | 0 B (0.0%) |
| 1      | `icefisingstaticstatus.bss` | 128 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `e1d0c8f03c81`  |
| 3482   | Layout 2 | `e1d0c8f03c81`  |
| 3474   | Layout 2 | `e1d0c8f03c81`  |
| 3473   | Layout 2 | `e1d0c8f03c81`  |
| 3464   | Layout 2 | `e1d0c8f03c81`  |
| 3458   | Layout 2 | `e1d0c8f03c81`  |
| 3454   | Layout 2 | `e1d0c8f03c81`  |
| 3444   | Layout 2 | `e1d0c8f03c81`  |
| 3435   | Layout 2 | `e1d0c8f03c81`  |
| 3426   | Layout 2 | `e1d0c8f03c81`  |
| 3418   | Layout 2 | `e1d0c8f03c81`  |
| 3412   | Layout 2 | `e1d0c8f03c81`  |
| 3402   | Layout 2 | `e1d0c8f03c81`  |
| 3396   | Layout 2 | `e1d0c8f03c81`  |
| 3387   | Layout 2 | `e1d0c8f03c81`  |
| 3381   | Layout 2 | `e1d0c8f03c81`  |
| 3373   | Layout 2 | `e1d0c8f03c81`  |
| 3364   | Layout 2 | `e1d0c8f03c81`  |
| 3356   | Layout 2 | `e1d0c8f03c81`  |
| 3349   | Layout 2 | `e1d0c8f03c81`  |
| 3342   | Layout 2 | `e1d0c8f03c81`  |
| 3335   | Layout 2 | `e1d0c8f03c81`  |
| 3326   | Layout 2 | `e1d0c8f03c81`  |
| 3321   | Layout 2 | `e1d0c8f03c81`  |
| 3314   | Layout 2 | `e1d0c8f03c81`  |
| 3303   | Layout 2 | `e1d0c8f03c81`  |
| 3302   | Layout 2 | `e1d0c8f03c81`  |
| 3293   | Layout 2 | `e1d0c8f03c81`  |
| 3283   | Layout 2 | `e1d0c8f03c81`  |
| 3275   | Layout 2 | `e1d0c8f03c81`  |
| 3267   | Layout 2 | `e1d0c8f03c81`  |
| 3258   | Layout 2 | `e1d0c8f03c81`  |
| 3251   | Layout 2 | `e1d0c8f03c81`  |
| 3242   | Layout 2 | `e1d0c8f03c81`  |
| 3235   | Layout 2 | `e1d0c8f03c81`  |
| 3229   | Layout 2 | `e1d0c8f03c81`  |
| 3212   | Layout 2 | `e1d0c8f03c81`  |
| 3203   | Layout 2 | `e1d0c8f03c81`  |
| 3193   | Layout 2 | `e1d0c8f03c81`  |
| 3186   | Layout 2 | `e1d0c8f03c81`  |
| 3177   | Layout 2 | `e1d0c8f03c81`  |
| 3169   | Layout 2 | `e1d0c8f03c81`  |
| 3158   | Layout 2 | `e1d0c8f03c81`  |
| 3151   | Layout 2 | `e1d0c8f03c81`  |
| 3144   | Layout 2 | `e1d0c8f03c81`  |
| 3133   | Layout 2 | `e1d0c8f03c81`  |
| 3125   | Layout 2 | `e1d0c8f03c81`  |
| 3118   | Layout 2 | `e1d0c8f03c81`  |
| 3111   | Layout 2 | `e1d0c8f03c81`  |
| 3103   | Layout 2 | `e1d0c8f03c81`  |
| 3095   | Layout 2 | `e1d0c8f03c81`  |
| 3086   | Layout 2 | `e1d0c8f03c81`  |
| 3072   | Layout 2 | `e1d0c8f03c81`  |
| 3062   | Layout 2 | `e1d0c8f03c81`  |
| 3052   | Layout 2 | `e1d0c8f03c81`  |
| 3045   | Layout 2 | `e1d0c8f03c81`  |
| 3037   | Layout 2 | `e1d0c8f03c81`  |
| 3030   | Layout 2 | `e1d0c8f03c81`  |
| 3021   | Layout 2 | `e1d0c8f03c81`  |
| 3012   | Layout 2 | `e1d0c8f03c81`  |
| 3002   | Layout 2 | `e1d0c8f03c81`  |
| 2995   | Layout 2 | `e1d0c8f03c81`  |
| 2987   | Layout 2 | `e1d0c8f03c81`  |
| 2978   | Layout 2 | `e1d0c8f03c81`  |
| 2970   | Layout 2 | `e1d0c8f03c81`  |
| 2959   | Layout 2 | `e1d0c8f03c81`  |
| 2951   | Layout 2 | `e1d0c8f03c81`  |
| 2942   | Layout 2 | `e1d0c8f03c81`  |
| 2935   | Layout 2 | `e1d0c8f03c81`  |
| 2932   | Layout 2 | `e1d0c8f03c81`  |
| 2923   | Layout 2 | `e1d0c8f03c81`  |
| 2919   | Layout 2 | `e1d0c8f03c81`  |
| 2907   | Layout 2 | `e1d0c8f03c81`  |
| 2900   | Layout 2 | `e1d0c8f03c81`  |
| 2891   | Layout 2 | `e1d0c8f03c81`  |
| 2882   | Layout 2 | `e1d0c8f03c81`  |
| 2872   | Layout 2 | `e1d0c8f03c81`  |
| 2863   | Layout 2 | `e1d0c8f03c81`  |
| 2855   | Layout 2 | `e1d0c8f03c81`  |
| 2849   | Layout 2 | `e1d0c8f03c81`  |
| 2844   | Layout 2 | `e1d0c8f03c81`  |
| 2834   | Layout 2 | `e1d0c8f03c81`  |
| 2825   | Layout 2 | `e1d0c8f03c81`  |
| 2819   | Layout 2 | `e1d0c8f03c81`  |
| 2811   | Layout 2 | `e1d0c8f03c81`  |
| 2803   | Layout 2 | `e1d0c8f03c81`  |
| 2794   | Layout 2 | `e1d0c8f03c81`  |
| 2783   | Layout 2 | `e1d0c8f03c81`  |
| 2774   | Layout 2 | `e1d0c8f03c81`  |
| 2765   | Layout 2 | `e1d0c8f03c81`  |
| 2756   | Layout 2 | `e1d0c8f03c81`  |
| 2750   | Layout 2 | `e1d0c8f03c81`  |
| 2743   | Layout 2 | `e1d0c8f03c81`  |
| 2736   | Layout 2 | `e1d0c8f03c81`  |
| 2726   | Layout 2 | `e1d0c8f03c81`  |
| 2717   | Layout 1 | `e1d0c8f03c81`  |
| 2709   | Layout 1 | `e1d0c8f03c81`  |
| 2703   | Layout 1 | `e1d0c8f03c81`  |
| 2695   | Layout 1 | `e1d0c8f03c81`  |
| 2684   | Layout 1 | `e1d0c8f03c81`  |
| 2672   | Layout 1 | `e1d0c8f03c81`  |
| 2665   | Layout 1 | `e1d0c8f03c81`  |
| 2657   | Layout 1 | `e1d0c8f03c81`  |
| 2649   | Layout 1 | `e1d0c8f03c81`  |
| 2644   | Layout 1 | `e1d0c8f03c81`  |
| 2637   | Layout 1 | `e1d0c8f03c81`  |
| 2629   | Layout 1 | `e1d0c8f03c81`  |
| 2619   | Layout 1 | `e1d0c8f03c81`  |
| 2612   | Layout 1 | `e1d0c8f03c81`  |
| 2606   | Layout 1 | `e1d0c8f03c81`  |
| 2602   | Layout 1 | `e1d0c8f03c81`  |
| 2601   | Layout 1 | `e1d0c8f03c81`  |
| 2592   | Layout 1 | `e1d0c8f03c81`  |
| 2583   | Layout 1 | `e1d0c8f03c81`  |
| 2575   | Layout 1 | `e1d0c8f03c81`  |
| 2567   | Layout 1 | `e1d0c8f03c81`  |
| 2560   | Layout 1 | `e1d0c8f03c81`  |
| 2553   | Layout 1 | `e1d0c8f03c81`  |
| 2545   | Layout 1 | `e1d0c8f03c81`  |
| 2538   | Layout 1 | `e1d0c8f03c81`  |
| 2529   | Layout 1 | `e1d0c8f03c81`  |
| 2519   | Layout 1 | `e1d0c8f03c81`  |
| 2513   | Layout 1 | `e1d0c8f03c81`  |
| 2510   | Layout 1 | `e1d0c8f03c81`  |
| 2507   | Layout 1 | `e1d0c8f03c81`  |
| 2503   | Layout 1 | `e1d0c8f03c81`  |
| 2498   | Layout 1 | `e1d0c8f03c81`  |
| 2492   | Layout 1 | `e1d0c8f03c81`  |
| 2487   | Layout 1 | `e1d0c8f03c81`  |
| 2480   | Layout 1 | `e1d0c8f03c81`  |
| 2474   | Layout 1 | `e1d0c8f03c81`  |
| 2468   | Layout 1 | `e1d0c8f03c81`  |
| 2460   | Layout 1 | `e1d0c8f03c81`  |
| 2453   | Layout 1 | `e1d0c8f03c81`  |
| 2444   | Layout 1 | `e1d0c8f03c81`  |
| 2438   | Layout 1 | `e1d0c8f03c81`  |
| 2434   | Layout 1 | `e1d0c8f03c81`  |
| 2429   | Layout 1 | `e1d0c8f03c81`  |
| 2421   | Layout 1 | `e1d0c8f03c81`  |
| 2414   | Layout 1 | `e1d0c8f03c81`  |
| 2407   | Layout 1 | `e1d0c8f03c81`  |
| 2401   | Layout 1 | `e1d0c8f03c81`  |
| 2397   | Layout 1 | `e1d0c8f03c81`  |
| 2393   | Layout 1 | `e1d0c8f03c81`  |
| 2384   | Layout 1 | `e1d0c8f03c81`  |
| 2378   | Layout 1 | `e1d0c8f03c81`  |
| 2372   | Layout 1 | `e1d0c8f03c81`  |
| 2358   | Layout 1 | `e1d0c8f03c81`  |
| 2352   | Layout 1 | `e1d0c8f03c81`  |
| 2347   | Layout 1 | `e1d0c8f03c81`  |
| 2343   | Layout 1 | `e1d0c8f03c81`  |
| 2335   | Layout 1 | `e1d0c8f03c81`  |
| 2327   | Layout 1 | `e1d0c8f03c81`  |
| 2324   | Layout 1 | `e1d0c8f03c81`  |
| 2319   | Layout 1 | `e1d0c8f03c81`  |
| 2313   | Layout 1 | `e1d0c8f03c81`  |
| 2308   | Layout 1 | `e1d0c8f03c81`  |
| 2302   | Layout 1 | `e1d0c8f03c81`  |
| 2295   | Layout 1 | `e1d0c8f03c81`  |
| 2290   | Layout 1 | `e1d0c8f03c81`  |
| 2284   | Layout 1 | `e1d0c8f03c81`  |
| 2276   | Layout 1 | `e1d0c8f03c81`  |
| 2269   | Layout 1 | `e1d0c8f03c81`  |
| 2259   | Layout 1 | `e1d0c8f03c81`  |
| 2250   | Layout 1 | `e1d0c8f03c81`  |
| 2243   | Layout 1 | `e1d0c8f03c81`  |
| 2235   | Layout 1 | `e1d0c8f03c81`  |
| 2229   | Layout 1 | `e1d0c8f03c81`  |
| 2224   | Layout 1 | `e1d0c8f03c81`  |
| 2218   | Layout 1 | `e1d0c8f03c81`  |
| 2215   | Layout 1 | `e1d0c8f03c81`  |
| 2207   | Layout 1 | `e1d0c8f03c81`  |
| 2203   | Layout 1 | `e1d0c8f03c81`  |
| 2196   | Layout 1 | `e1d0c8f03c81`  |
| 2192   | Layout 1 | `e1d0c8f03c81`  |
| 2189   | Layout 1 | `e1d0c8f03c81`  |
| 2183   | Layout 1 | `e1d0c8f03c81`  |
| 2179   | Layout 1 | `e1d0c8f03c81`  |
| 2171   | Layout 1 | `e1d0c8f03c81`  |
| 2163   | Layout 1 | `e1d0c8f03c81`  |
| 2156   | Layout 1 | `e1d0c8f03c81`  |
| 2151   | Layout 1 | `e1d0c8f03c81`  |
| 2147   | Layout 1 | `e1d0c8f03c81`  |
| 2142   | Layout 1 | `e1d0c8f03c81`  |
| 2138   | Layout 1 | `e1d0c8f03c81`  |
| 2134   | Layout 1 | `e1d0c8f03c81`  |
| 2130   | Layout 1 | `e1d0c8f03c81`  |
| 2122   | Layout 1 | `e1d0c8f03c81`  |
| 2107   | Layout 1 | `e1d0c8f03c81`  |
| 2098   | Layout 1 | `e1d0c8f03c81`  |
| 2089   | Layout 1 | `e1d0c8f03c81`  |
| 2081   | Layout 1 | `e1d0c8f03c81`  |
| 2073   | Layout 1 | `e1d0c8f03c81`  |
| 2067   | Layout 1 | `e1d0c8f03c81`  |
| 2063   | Layout 1 | `e1d0c8f03c81`  |
| 2059   | Layout 1 | `e1d0c8f03c81`  |
| 2052   | Layout 1 | `e1d0c8f03c81`  |
| 2044   | Layout 1 | `e1d0c8f03c81`  |
| 2039   | Layout 1 | `e1d0c8f03c81`  |
| 2032   | Layout 1 | `e1d0c8f03c81`  |
| 2025   | Layout 1 | `e1d0c8f03c81`  |
| 2011   | Layout 1 | `e1d0c8f03c81`  |
| 2005   | Layout 1 | `e1d0c8f03c81`  |
| 2000   | Layout 1 | `e1d0c8f03c81`  |
| 1996   | Layout 1 | `e1d0c8f03c81`  |
| 1991   | Layout 1 | `e1d0c8f03c81`  |
| 1985   | Layout 1 | `e1d0c8f03c81`  |
| 1980   | Layout 1 | `e1d0c8f03c81`  |
| 1969   | Layout 1 | `e1d0c8f03c81`  |
| 1964   | Layout 1 | `e1d0c8f03c81`  |
| 1958   | Layout 1 | `e1d0c8f03c81`  |
| 1950   | Layout 1 | `e1d0c8f03c81`  |
| 1945   | Layout 1 | `e1d0c8f03c81`  |
| 1937   | Layout 1 | `e1d0c8f03c81`  |
| 1933   | Layout 1 | `e1d0c8f03c81`  |
| 1927   | Layout 1 | `e1d0c8f03c81`  |
| 1921   | Layout 1 | `e1d0c8f03c81`  |
| 1914   | Layout 1 | `e1d0c8f03c81`  |
| 1908   | Layout 1 | `e1d0c8f03c81`  |
| 1897   | Layout 1 | `e1d0c8f03c81`  |
| 1892   | Layout 1 | `e1d0c8f03c81`  |
| 1886   | Layout 1 | `e1d0c8f03c81`  |
| 1881   | Layout 1 | `e1d0c8f03c81`  |
| 1871   | Layout 1 | `e1d0c8f03c81`  |
| 1866   | Layout 1 | `e1d0c8f03c81`  |
| 1862   | Layout 1 | `e1d0c8f03c81`  |
| 1854   | Layout 1 | `e1d0c8f03c81`  |
| 1846   | Layout 1 | `e1d0c8f03c81`  |
| 1838   | Layout 1 | `e1d0c8f03c81`  |
| 1832   | Layout 1 | `e1d0c8f03c81`  |
| 1826   | Layout 1 | `e1d0c8f03c81`  |
| 1822   | Layout 1 | `e1d0c8f03c81`  |
| 1818   | Layout 1 | `e1d0c8f03c81`  |
| 1804   | Layout 1 | `e1d0c8f03c81`  |
| 1794   | Layout 1 | `e1d0c8f03c81`  |
| 1790   | Layout 1 | `e1d0c8f03c81`  |
| 1784   | Layout 1 | `e1d0c8f03c81`  |
| 1774   | No file  | `e1d0c8f03c81`  |
| 1771   | No file  | `e1d0c8f03c81`  |
| 1762   | No file  | `e1d0c8f03c81`  |
| 1759   | No file  | `e1d0c8f03c81`  |
| 1754   | No file  | `e1d0c8f03c81`  |
| 1749   | No file  | `e1d0c8f03c81`  |
| 1743   | No file  | `e1d0c8f03c81`  |
| 1737   | No file  | `e1d0c8f03c81`  |
| 1731   | No file  | `e1d0c8f03c81`  |
| 1725   | No file  | `e1d0c8f03c81`  |
| 1717   | No file  | `e1d0c8f03c81`  |
| 1710   | No file  | `e1d0c8f03c81`  |
| 1704   | No file  | `e1d0c8f03c81`  |
| 1698   | No file  | `e1d0c8f03c81`  |
| 1690   | No file  | `e1d0c8f03c81`  |
| 1685   | No file  | `e1d0c8f03c81`  |
| 1680   | No file  | `e1d0c8f03c81`  |
| 1674   | No file  | `e1d0c8f03c81`  |
| 1668   | No file  | `e1d0c8f03c81`  |
| 1659   | No file  | `e1d0c8f03c81`  |
| 1649   | No file  | `e1d0c8f03c81`  |
| 1642   | No file  | `e1d0c8f03c81`  |
| 1636   | No file  | `e1d0c8f03c81`  |
| 1628   | No file  | `e1d0c8f03c81`  |
| 1622   | No file  | `e1d0c8f03c81`  |
| 1614   | No file  | `e1d0c8f03c81`  |
| 1608   | No file  | `e1d0c8f03c81`  |
| 1602   | No file  | `e1d0c8f03c81`  |
| 1598   | No file  | `e1d0c8f03c81`  |
| 1594   | No file  | `e1d0c8f03c81`  |
| 1590   | No file  | `e1d0c8f03c81`  |
| 1587   | No file  | `e1d0c8f03c81`  |
| 1584   | No file  | `e1d0c8f03c81`  |
| 1579   | No file  | `e1d0c8f03c81`  |
| 1572   | No file  | `e1d0c8f03c81`  |
| 1565   | No file  | `e1d0c8f03c81`  |
| 1559   | No file  | `e1d0c8f03c81`  |
| 1554   | No file  | `e1d0c8f03c81`  |
| 1547   | No file  | `e1d0c8f03c81`  |
| 1537   | No file  | `e1d0c8f03c81`  |
| 1529   | No file  | `e1d0c8f03c81`  |
| 1524   | No file  | `e1d0c8f03c81`  |
| 1519   | No file  | `e1d0c8f03c81`  |
| 1509   | No file  | `e1d0c8f03c81`  |
| 1506   | No file  | `e1d0c8f03c81`  |
| 1504   | No file  | `e1d0c8f03c81`  |
| 1500   | No file  | `e1d0c8f03c81`  |
| 1493   | No file  | `e1d0c8f03c81`  |
| 1489   | No file  | `e1d0c8f03c81`  |
| 1485   | No file  | `e1d0c8f03c81`  |
| 1481   | No file  | `e1d0c8f03c81`  |
| 1474   | No file  | `e1d0c8f03c81`  |
| 1466   | No file  | `e1d0c8f03c81`  |
| 1462   | No file  | `e1d0c8f03c81`  |
| 1459   | No file  | `e1d0c8f03c81`  |
| 1453   | No file  | `e1d0c8f03c81`  |
| 1450   | No file  | `e1d0c8f03c81`  |
| 1445   | No file  | `e1d0c8f03c81`  |
| 1439   | No file  | `e1d0c8f03c81`  |
| 1433   | No file  | `e1d0c8f03c81`  |
| 1430   | No file  | `e1d0c8f03c81`  |
| 1426   | No file  | `e1d0c8f03c81`  |
| 1421   | No file  | `e1d0c8f03c81`  |
| 1417   | No file  | `e1d0c8f03c81`  |
| 1416   | No file  | `e1d0c8f03c81`  |
| 1409   | No file  | `e1d0c8f03c81`  |
| 1405   | No file  | `e1d0c8f03c81`  |
| 1401   | No file  | `e1d0c8f03c81`  |
| 1396   | No file  | `e1d0c8f03c81`  |
| 1391   | No file  | `e1d0c8f03c81`  |
| 1390   | No file  | `e1d0c8f03c81`  |
| 1386   | No file  | `e1d0c8f03c81`  |
| 1381   | No file  | `e1d0c8f03c81`  |
| 1379   | No file  | `e1d0c8f03c81`  |
| 1372   | No file  | `e1d0c8f03c81`  |
| 1366   | No file  | `e1d0c8f03c81`  |
| 1364   | No file  | `e1d0c8f03c81`  |
| 1363   | No file  | `e1d0c8f03c81`  |
| 1360   | No file  | `e1d0c8f03c81`  |
| 1358   | No file  | `e1d0c8f03c81`  |
| 1355   | No file  | `e1d0c8f03c81`  |
| 1351   | No file  | `e1d0c8f03c81`  |
| 1348   | No file  | `e1d0c8f03c81`  |
| 1346   | No file  | `e1d0c8f03c81`  |
| 1341   | No file  | `e1d0c8f03c81`  |
| 1340   | No file  | `e1d0c8f03c81`  |
| 1338   | No file  | `e1d0c8f03c81`  |
| 1335   | No file  | `e1d0c8f03c81`  |
| 1333   | No file  | `e1d0c8f03c81`  |
| 1329   | No file  | `e1d0c8f03c81`  |
| 1327   | No file  | `e1d0c8f03c81`  |
| 1324   | No file  | `e1d0c8f03c81`  |
| 1321   | No file  | `e1d0c8f03c81`  |
| 1319   | No file  | `e1d0c8f03c81`  |
| 1318   | No file  | `e1d0c8f03c81`  |
| 1316   | No file  | `e1d0c8f03c81`  |
| 1313   | No file  | `e1d0c8f03c81`  |
| 1311   | No file  | `e1d0c8f03c81`  |
| 1309   | No file  | `e1d0c8f03c81`  |
| 1304   | No file  | `e1d0c8f03c81`  |
| 1292   | No file  | `e1d0c8f03c81`  |
| 1286   | No file  | `e1d0c8f03c81`  |
| 1280   | No file  | `e1d0c8f03c81`  |
| 1276   | No file  | `e1d0c8f03c81`  |
| 1267   | No file  | `e1d0c8f03c81`  |
| 1261   | No file  | `e1d0c8f03c81`  |
| 1256   | No file  | `e1d0c8f03c81`  |
| 1250   | No file  | `e1d0c8f03c81`  |
| 1246   | No file  | `e1d0c8f03c81`  |
| 1239   | No file  | `e1d0c8f03c81`  |
| 1230   | No file  | `e1d0c8f03c81`  |
| 1226   | No file  | `e1d0c8f03c81`  |
| 1220   | No file  | `e1d0c8f03c81`  |
| 1217   | No file  | `e1d0c8f03c81`  |
| 1211   | No file  | `e1d0c8f03c81`  |
| 1210   | No file  | `e1d0c8f03c81`  |
| 1208   | No file  | `e1d0c8f03c81`  |
| 1203   | No file  | `e1d0c8f03c81`  |
| 1197   | No file  | `e1d0c8f03c81`  |
| 1194   | No file  | `e1d0c8f03c81`  |
| 1192   | No file  | `e1d0c8f03c81`  |
| 1187   | No file  | `e1d0c8f03c81`  |
| 1183   | No file  | `e1d0c8f03c81`  |
| 1177   | No file  | `e1d0c8f03c81`  |
| 1173   | No file  | `e1d0c8f03c81`  |
| 1167   | No file  | `e1d0c8f03c81`  |
| 1164   | No file  | `e1d0c8f03c81`  |
| 1156   | No file  | `e1d0c8f03c81`  |
| 1149   | No file  | `e1d0c8f03c81`  |
| 1144   | No file  | `e1d0c8f03c81`  |
| 1137   | No file  | `e1d0c8f03c81`  |
| 1132   | No file  | `e1d0c8f03c81`  |
| 1127   | No file  | `e1d0c8f03c81`  |
| 1122   | No file  | `e1d0c8f03c81`  |
| 1118   | No file  | `e1d0c8f03c81`  |
| 1114   | No file  | `e1d0c8f03c81`  |
| 1109   | No file  | `e1d0c8f03c81`  |
| 1102   | No file  | `e1d0c8f03c81`  |
| 1096   | No file  | `e1d0c8f03c81`  |
| 1088   | No file  | `e1d0c8f03c81`  |
| 1081   | No file  | `e1d0c8f03c81`  |
| 1076   | No file  | `e1d0c8f03c81`  |
| 1069   | No file  | `e1d0c8f03c81`  |
| 1064   | No file  | `e1d0c8f03c81`  |
| 1058   | No file  | `e1d0c8f03c81`  |
| 1051   | No file  | `e1d0c8f03c81`  |
| 1044   | No file  | `e1d0c8f03c81`  |
| 1036   | No file  | `e1d0c8f03c81`  |
| 1026   | No file  | `e1d0c8f03c81`  |
| 1016   | No file  | `e1d0c8f03c81`  |
| 1009   | No file  | `e1d0c8f03c81`  |
| 1005   | No file  | `e1d0c8f03c81`  |
| 1000   | No file  | `e1d0c8f03c81`  |
| 998    | No file  | `e1d0c8f03c81`  |
| 990    | No file  | `e1d0c8f03c81`  |
| 979    | No file  | `e1d0c8f03c81`  |
| 972    | No file  | `e1d0c8f03c81`  |
| 963    | No file  | `e1d0c8f03c81`  |
| 955    | No file  | `e1d0c8f03c81`  |
| 946    | No file  | `e1d0c8f03c81`  |
| 938    | No file  | `e1d0c8f03c81`  |
| 927    | No file  | `e1d0c8f03c81`  |
| 911    | No file  | `e1d0c8f03c81`  |
| 904    | No file  | `e1d0c8f03c81`  |
| 899    | No file  | `e1d0c8f03c81`  |
| 894    | No file  | `e1d0c8f03c81`  |
| 885    | No file  | `e1d0c8f03c81`  |
| 879    | No file  | `e1d0c8f03c81`  |
| 872    | No file  | `e1d0c8f03c81`  |
| 864    | No file  | `e1d0c8f03c81`  |
| 855    | No file  | `e1d0c8f03c81`  |
| 853    | No file  | `e1d0c8f03c81`  |
| 845    | No file  | `e1d0c8f03c81`  |
| 837    | No file  | `e1d0c8f03c81`  |
| 829    | No file  | `e1d0c8f03c81`  |
| 822    | No file  | `e1d0c8f03c81`  |
| 814    | No file  | `e1d0c8f03c81`  |
| 805    | No file  | `e1d0c8f03c81`  |
| 794    | No file  | `e1d0c8f03c81`  |
| 787    | No file  | `e1d0c8f03c81`  |
| 780    | No file  | `e1d0c8f03c81`  |
| 771    | No file  | `e1d0c8f03c81`  |
| 760    | No file  | `e1d0c8f03c81`  |
| 748    | No file  | `e1d0c8f03c81`  |
| 741    | No file  | `e1d0c8f03c81`  |
| 736    | No file  | `e1d0c8f03c81`  |
| 731    | No file  | `e1d0c8f03c81`  |
| 723    | No file  | `e1d0c8f03c81`  |
| 711    | No file  | `e1d0c8f03c81`  |
| 707    | No file  | `e1d0c8f03c81`  |
| 697    | No file  | `e1d0c8f03c81`  |
| 689    | No file  | `e1d0c8f03c81`  |
| 683    | No file  | `e1d0c8f03c81`  |
| 678    | No file  | `e1d0c8f03c81`  |
| 670    | No file  | `e1d0c8f03c81`  |
| 661    | No file  | `e1d0c8f03c81`  |
| 656    | No file  | `e1d0c8f03c81`  |
| 652    | No file  | `e1d0c8f03c81`  |
| 643    | No file  | `e1d0c8f03c81`  |
| 637    | No file  | `e1d0c8f03c81`  |
| 630    | No file  | `e1d0c8f03c81`  |
| 627    | No file  | `e1d0c8f03c81`  |
| 621    | No file  | `e1d0c8f03c81`  |
| 617    | No file  | `e1d0c8f03c81`  |
| 615    | No file  | `e1d0c8f03c81`  |
| 606    | No file  | `e1d0c8f03c81`  |
| 599    | No file  | `e1d0c8f03c81`  |
| 592    | No file  | `e1d0c8f03c81`  |
| 586    | No file  | `e1d0c8f03c81`  |
| 577    | No file  | `e1d0c8f03c81`  |
| 569    | No file  | `e1d0c8f03c81`  |
| 561    | No file  | `e1d0c8f03c81`  |
| 554    | No file  | `e1d0c8f03c81`  |
| 542    | No file  | `e1d0c8f03c81`  |
| 532    | No file  | `e1d0c8f03c81`  |
| 531    | No file  | `e1d0c8f03c81`  |
| 526    | No file  | `e1d0c8f03c81`  |
| 521    | No file  | `e1d0c8f03c81`  |
| 517    | No file  | `e1d0c8f03c81`  |
| 510    | No file  | `e1d0c8f03c81`  |
| 508    | No file  | `e1d0c8f03c81`  |
| 504    | No file  | `e1d0c8f03c81`  |
| 497    | No file  | `e1d0c8f03c81`  |
| 491    | No file  | `e1d0c8f03c81`  |
| 485    | No file  | `e1d0c8f03c81`  |
| 478    | No file  | `e1d0c8f03c81`  |
| 472    | No file  | `e1d0c8f03c81`  |
| 466    | No file  | `e1d0c8f03c81`  |
| 457    | No file  | `e1d0c8f03c81`  |
| 452    | No file  | `e1d0c8f03c81`  |
| 449    | No file  | `e1d0c8f03c81`  |
| 435    | No file  | `e1d0c8f03c81`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of mini-game groups                    |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (110 bytes)

| Offset  | Type | Field                | Notes                                                                    |
| ------- | ---- | -------------------- | ------------------------------------------------------------------------ |
| `+0x00` | u16  | mini_game_group      | Group key; `icefisingregionstaticstatus.bss` `mini_game_group_index`      |
| `+0x02` | u64  | min_wait_time        | Sheet `MinWaitTime`                                                      |
| `+0x0A` | u64  | max_wait_time        | Sheet `MaxWaitTime`                                                      |
| `+0x12` | u64  | game_total_time      | Sheet `GameTotalTime`                                                    |
| `+0x1A` | u64  | game_min_time        | Sheet `GameMinTime`; see Field Names                                     |
| `+0x22` | u64  | game_max_time        | Sheet `GameMaxTime`; see Field Names                                     |
| `+0x2A` | u32  | fish_hp              | Sheet `FishHP`                                                           |
| `+0x2E` | u32  | decrease_hp          | Sheet `DecreaseHP`                                                       |
| `+0x32` | u64  | time_per_tick        | Sheet `TimePerTick`                                                      |
| `+0x3A` | u32  | critical_percent     | Sheet `CriticalPercent`                                                  |
| `+0x3E` | u32  | critical_decrease_hp | Sheet `CriticalDecreaseHP`, a whole number                               |
| `+0x42` | u32  | possible_percent     | Sheet `PossiblePercent`                                                  |
| `+0x46` | u32  | total_block          | Sheet `TotalBlock`                                                       |
| `+0x4A` | u64  | minigame_time        | Sheet `MinigameTime`                                                     |
| `+0x52` | u64  | random_minigame_time | Sheet `RandomMinigameTime`                                               |
| `+0x5A` | u32  | fish_speed           | Sheet `FishSpeed`                                                        |
| `+0x5E` | u32  | random_fish_speed    | Sheet `RandomFishSpeed`                                                  |
| `+0x62` | u32  | player_move_speed    | Sheet `PlayerMoveSpeed`                                                  |
| `+0x66` | u32  | endurance_decrease   | Sheet `EnduranceDecrease`                                                |
| `+0x6A` | u32  | reward_drop_group    | Sheet `RewardDropGroup`                                                  |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Layout 1

`reward_drop_group` is a u16, so the row is 2 bytes shorter. Only the Row
differs from Layout 2.

### Row (108 bytes)

| Offset  | Type | Field                | Notes                                                                    |
| ------- | ---- | -------------------- | ------------------------------------------------------------------------ |
| `+0x00` | u16  | mini_game_group      |                                                                          |
| `+0x02` | u64  | min_wait_time        |                                                                          |
| `+0x0A` | u64  | max_wait_time        |                                                                          |
| `+0x12` | u64  | game_total_time      |                                                                          |
| `+0x1A` | u64  | game_min_time        |                                                                          |
| `+0x22` | u64  | game_max_time        |                                                                          |
| `+0x2A` | u32  | fish_hp              |                                                                          |
| `+0x2E` | u32  | decrease_hp          |                                                                          |
| `+0x32` | u64  | time_per_tick        |                                                                          |
| `+0x3A` | u32  | critical_percent     |                                                                          |
| `+0x3E` | u32  | critical_decrease_hp |                                                                          |
| `+0x42` | u32  | possible_percent     |                                                                          |
| `+0x46` | u32  | total_block          |                                                                          |
| `+0x4A` | u64  | minigame_time        |                                                                          |
| `+0x52` | u64  | random_minigame_time |                                                                          |
| `+0x5A` | u32  | fish_speed           |                                                                          |
| `+0x5E` | u32  | random_fish_speed    |                                                                          |
| `+0x62` | u32  | player_move_speed    |                                                                          |
| `+0x66` | u32  | endurance_decrease   |                                                                          |
| `+0x6A` | u16  | reward_drop_group    | `19840` on client 1784                                                   |

## Groups

The rows on the clients read, against the `IceFishing` sheet row of a
private server on client 1784 (its values are edited, see Field Names):

| Field                  | Sheet (1784) | Client 1784 | Client 3482, groups `2` and `1` |
| ---------------------- | ------------ | ----------- | ------------------------------- |
| `mini_game_group`      | `1`          | `1`         | `2`, `1`                        |
| `min_wait_time`        | `10000`      | `10`        | `10`                            |
| `max_wait_time`        | `20000`      | `20`        | `20`                            |
| `game_total_time`      | `30000`      | `30`        | `30`                            |
| `game_min_time`        | `10000`      | `3`         | `3`                             |
| `game_max_time`        | `20000`      | `100`       | `100`                           |
| `fish_hp`              | `100`        | `100`       | `100`                           |
| `decrease_hp`          | `5`          | `10`        | `10`                            |
| `time_per_tick`        | `500`        | `1`         | `1`                             |
| `critical_percent`     | `30`         | `30`        | `30`                            |
| `critical_decrease_hp` | `7.5`        | `15`        | `15`                            |
| `possible_percent`     | `30`         | `30`        | `30`                            |
| `total_block`          | `20`         | `20`        | `20`                            |
| `minigame_time`        | `3000`       | `3`         | `3`                             |
| `random_minigame_time` | `2000`       | `2`         | `2`                             |
| `fish_speed`           | `4`          | `4`         | `4`                             |
| `random_fish_speed`    | `3`          | `3`         | `3`                             |
| `player_move_speed`    | `1`          | `1`         | `1`                             |
| `endurance_decrease`   | `3`          | `3`         | `3`                             |
| `reward_drop_group`    | `19840`      | `19840`     | `16444` on both rows            |

The two rows of client 3482 differ in `mini_game_group` only.

## Field Names

The names follow the `IceFishing` sheet of a private server's
`DataSheets.bexcel` on client 1784, also in that server's
`datasheet_minigame_2.xlsm`: 20 columns from `MiniGameGroup` to
`GameMaxTime`, one row. That server's `binary/icefisingstaticstatus.bss`,
compiled from the sheet, has the 108-byte row of Layout 1 and holds each
sheet value at one offset: `10000` and `20000` at `+0x02` and `+0x0A`
and again at `+0x1A` and `+0x22`, `30000` at `+0x12`, `500` at `+0x32`,
`7` (the sheet's `7.5`, cut to a whole number) at `+0x3E`, `3000` and
`2000` at `+0x4A` and `+0x52`, `19840` at `+0x6A`, the others as in the
table above.

Four pairs of offsets hold equal sheet values (`10000`, `20000`, `30`
and `3`), so the values alone do not place them. The server dump of the
same build places them: its `IceFishing` loader reads `MiniGameGroup`,
`MinWaitTime`, `MaxWaitTime`, `GameTotalTime`, `FishHP`, `DecreaseHP`,
`TimePerTick`, `CriticalPercent`, `CriticalDecreaseHP`,
`PossiblePercent`, `TotalBlock`, `MinigameTime`, `RandomMinigameTime`,
`FishSpeed`, `RandomFishSpeed`, `PlayerMoveSpeed`, `EnduranceDecrease`
and `RewardDropGroup` in this order, which is the file's field order, and
keeps `RewardDropGroup` as a 16-bit value, as Layout 1 stores it. That
places `CriticalPercent` before `PossiblePercent`, `RandomFishSpeed`
before `EnduranceDecrease` and the wait times at `+0x02` and `+0x0A`.
The loader does not read `GameMinTime` or `GameMaxTime`, so those two
take the u64 fields left after `GameTotalTime`, the only other place the
sheet values `10000` and `20000` occupy.

The sheet writes the times in milliseconds (`MinWaitTime` `10000`); the
client files store `10` where the sheet has `10000` and `3` where it has
`3000`.

## Notes

- `icefising` is the client's spelling.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/lifeskill_tables.py`, one
  row per mini-game group.

## Open Questions

### What game_min_time and game_max_time Limit

On client 3482 both rows store `3` and `100` there, next to a
`game_total_time` of `30`. Which time of the game they bound, and in which
unit, is not known; neither the dump's loader nor the client Lua reads
them.
