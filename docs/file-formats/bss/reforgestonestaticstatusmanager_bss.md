# `reforgestonestaticstatusmanager.bss` Format

## Purpose

The reforge stones of the Reforge Stone preset window
(`panel_window_reforgestonepreset_all`): one row per stone, each a list of
levels with the level's item and the material that upgrades a stone to
it. The row position is the stone index the Lua passes to
`ToClient_GetReforgeStoneItemEnchantKey(index, stoneLevel)`. On client
3483 the 11 rows have two levels each: level 0 a Reforge Stone (`820953`
Reforge Stone - All AP to `820963` Reforge Stone - Black Spirit's Rage
Recovery), level 1 the HAN Reforge Stone of the same effect (`821260` to
`821270`), which takes one of that HAN Reforge Stone as its material.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                                  | Bytes | Records          | Row bytes |
| ------ | -------------- | ------------------------------------- | ----- | ---------------- | --------- |
| 1      | 3412 and later | `reforgestonestaticstatusmanager.bss` | 592   | 22 Level, 11 Row | 24        |

| Layout | File                                  | Known         | Unknown      |
| ------ | ------------------------------------- | ------------- | ------------ |
| 1      | `reforgestonestaticstatusmanager.bss` | 504 B (85.1%) | 88 B (14.9%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `cc1fbb8a19a0`  |
| 3482   | Layout 1 | `cc1fbb8a19a0`  |
| 3474   | Layout 1 | `cc1fbb8a19a0`  |
| 3473   | Layout 1 | `cc1fbb8a19a0`  |
| 3464   | Layout 1 | `cc1fbb8a19a0`  |
| 3458   | Layout 1 | `cc1fbb8a19a0`  |
| 3454   | Layout 1 | `cc1fbb8a19a0`  |
| 3444   | Layout 1 | `cc1fbb8a19a0`  |
| 3435   | Layout 1 | `cc1fbb8a19a0`  |
| 3426   | Layout 1 | `cc1fbb8a19a0`  |
| 3418   | Layout 1 | `cc1fbb8a19a0`  |
| 3412   | Layout 1 | `cc1fbb8a19a0`  |
| 3402   | No file  | `cc1fbb8a19a0`  |
| 3396   | No file  | `cc1fbb8a19a0`  |
| 3387   | No file  | `cc1fbb8a19a0`  |
| 3381   | No file  | `cc1fbb8a19a0`  |
| 3373   | No file  | `cc1fbb8a19a0`  |
| 3364   | No file  | `cc1fbb8a19a0`  |
| 3356   | No file  | `cc1fbb8a19a0`  |
| 3349   | No file  | `cc1fbb8a19a0`  |
| 3342   | No file  | `cc1fbb8a19a0`  |
| 3335   | No file  | `cc1fbb8a19a0`  |
| 3326   | No file  | `cc1fbb8a19a0`  |
| 3321   | No file  | `cc1fbb8a19a0`  |
| 3314   | No file  | `cc1fbb8a19a0`  |
| 3303   | No file  | `cc1fbb8a19a0`  |
| 3302   | No file  | `cc1fbb8a19a0`  |
| 3293   | No file  | `cc1fbb8a19a0`  |
| 3283   | No file  | `cc1fbb8a19a0`  |
| 3275   | No file  | `cc1fbb8a19a0`  |
| 3267   | No file  | `cc1fbb8a19a0`  |
| 3258   | No file  | `cc1fbb8a19a0`  |
| 3251   | No file  | `cc1fbb8a19a0`  |
| 3242   | No file  | `cc1fbb8a19a0`  |
| 3235   | No file  | `cc1fbb8a19a0`  |
| 3229   | No file  | `cc1fbb8a19a0`  |
| 3212   | No file  | `cc1fbb8a19a0`  |
| 3203   | No file  | `cc1fbb8a19a0`  |
| 3193   | No file  | `cc1fbb8a19a0`  |
| 3186   | No file  | `cc1fbb8a19a0`  |
| 3177   | No file  | `cc1fbb8a19a0`  |
| 3169   | No file  | `cc1fbb8a19a0`  |
| 3158   | No file  | `cc1fbb8a19a0`  |
| 3151   | No file  | `cc1fbb8a19a0`  |
| 3144   | No file  | `cc1fbb8a19a0`  |
| 3133   | No file  | `cc1fbb8a19a0`  |
| 3125   | No file  | `cc1fbb8a19a0`  |
| 3118   | No file  | `cc1fbb8a19a0`  |
| 3111   | No file  | `cc1fbb8a19a0`  |
| 3103   | No file  | `cc1fbb8a19a0`  |
| 3095   | No file  | `cc1fbb8a19a0`  |
| 3086   | No file  | `cc1fbb8a19a0`  |
| 3072   | No file  | `cc1fbb8a19a0`  |
| 3062   | No file  | `cc1fbb8a19a0`  |
| 3052   | No file  | `cc1fbb8a19a0`  |
| 3045   | No file  | `cc1fbb8a19a0`  |
| 3037   | No file  | `cc1fbb8a19a0`  |
| 3030   | No file  | `cc1fbb8a19a0`  |
| 3021   | No file  | `cc1fbb8a19a0`  |
| 3012   | No file  | `cc1fbb8a19a0`  |
| 3002   | No file  | `cc1fbb8a19a0`  |
| 2995   | No file  | `cc1fbb8a19a0`  |
| 2987   | No file  | `cc1fbb8a19a0`  |
| 2978   | No file  | `cc1fbb8a19a0`  |
| 2970   | No file  | `cc1fbb8a19a0`  |
| 2959   | No file  | `cc1fbb8a19a0`  |
| 2951   | No file  | `cc1fbb8a19a0`  |
| 2942   | No file  | `cc1fbb8a19a0`  |
| 2935   | No file  | `cc1fbb8a19a0`  |
| 2932   | No file  | `cc1fbb8a19a0`  |
| 2923   | No file  | `cc1fbb8a19a0`  |
| 2919   | No file  | `cc1fbb8a19a0`  |
| 2907   | No file  | `cc1fbb8a19a0`  |
| 2900   | No file  | `cc1fbb8a19a0`  |
| 2891   | No file  | `cc1fbb8a19a0`  |
| 2882   | No file  | `cc1fbb8a19a0`  |
| 2872   | No file  | `cc1fbb8a19a0`  |
| 2863   | No file  | `cc1fbb8a19a0`  |
| 2855   | No file  | `cc1fbb8a19a0`  |
| 2849   | No file  | `cc1fbb8a19a0`  |
| 2844   | No file  | `cc1fbb8a19a0`  |
| 2834   | No file  | `cc1fbb8a19a0`  |
| 2825   | No file  | `cc1fbb8a19a0`  |
| 2819   | No file  | `cc1fbb8a19a0`  |
| 2811   | No file  | `cc1fbb8a19a0`  |
| 2803   | No file  | `cc1fbb8a19a0`  |
| 2794   | No file  | `cc1fbb8a19a0`  |
| 2783   | No file  | `cc1fbb8a19a0`  |
| 2774   | No file  | `cc1fbb8a19a0`  |
| 2765   | No file  | `cc1fbb8a19a0`  |
| 2756   | No file  | `cc1fbb8a19a0`  |
| 2750   | No file  | `cc1fbb8a19a0`  |
| 2743   | No file  | `cc1fbb8a19a0`  |
| 2736   | No file  | `cc1fbb8a19a0`  |
| 2726   | No file  | `cc1fbb8a19a0`  |
| 2717   | No file  | `cc1fbb8a19a0`  |
| 2709   | No file  | `cc1fbb8a19a0`  |
| 2703   | No file  | `cc1fbb8a19a0`  |
| 2695   | No file  | `cc1fbb8a19a0`  |
| 2684   | No file  | `cc1fbb8a19a0`  |
| 2672   | No file  | `cc1fbb8a19a0`  |
| 2665   | No file  | `cc1fbb8a19a0`  |
| 2657   | No file  | `cc1fbb8a19a0`  |
| 2649   | No file  | `cc1fbb8a19a0`  |
| 2644   | No file  | `cc1fbb8a19a0`  |
| 2637   | No file  | `cc1fbb8a19a0`  |
| 2629   | No file  | `cc1fbb8a19a0`  |
| 2619   | No file  | `cc1fbb8a19a0`  |
| 2612   | No file  | `cc1fbb8a19a0`  |
| 2606   | No file  | `cc1fbb8a19a0`  |
| 2602   | No file  | `cc1fbb8a19a0`  |
| 2601   | No file  | `cc1fbb8a19a0`  |
| 2592   | No file  | `cc1fbb8a19a0`  |
| 2583   | No file  | `cc1fbb8a19a0`  |
| 2575   | No file  | `cc1fbb8a19a0`  |
| 2567   | No file  | `cc1fbb8a19a0`  |
| 2560   | No file  | `cc1fbb8a19a0`  |
| 2553   | No file  | `cc1fbb8a19a0`  |
| 2545   | No file  | `cc1fbb8a19a0`  |
| 2538   | No file  | `cc1fbb8a19a0`  |
| 2529   | No file  | `cc1fbb8a19a0`  |
| 2519   | No file  | `cc1fbb8a19a0`  |
| 2513   | No file  | `cc1fbb8a19a0`  |
| 2510   | No file  | `cc1fbb8a19a0`  |
| 2507   | No file  | `cc1fbb8a19a0`  |
| 2503   | No file  | `cc1fbb8a19a0`  |
| 2498   | No file  | `cc1fbb8a19a0`  |
| 2492   | No file  | `cc1fbb8a19a0`  |
| 2487   | No file  | `cc1fbb8a19a0`  |
| 2480   | No file  | `cc1fbb8a19a0`  |
| 2474   | No file  | `cc1fbb8a19a0`  |
| 2468   | No file  | `cc1fbb8a19a0`  |
| 2460   | No file  | `cc1fbb8a19a0`  |
| 2453   | No file  | `cc1fbb8a19a0`  |
| 2444   | No file  | `cc1fbb8a19a0`  |
| 2438   | No file  | `cc1fbb8a19a0`  |
| 2434   | No file  | `cc1fbb8a19a0`  |
| 2429   | No file  | `cc1fbb8a19a0`  |
| 2421   | No file  | `cc1fbb8a19a0`  |
| 2414   | No file  | `cc1fbb8a19a0`  |
| 2407   | No file  | `cc1fbb8a19a0`  |
| 2401   | No file  | `cc1fbb8a19a0`  |
| 2397   | No file  | `cc1fbb8a19a0`  |
| 2393   | No file  | `cc1fbb8a19a0`  |
| 2384   | No file  | `cc1fbb8a19a0`  |
| 2378   | No file  | `cc1fbb8a19a0`  |
| 2372   | No file  | `cc1fbb8a19a0`  |
| 2358   | No file  | `cc1fbb8a19a0`  |
| 2352   | No file  | `cc1fbb8a19a0`  |
| 2347   | No file  | `cc1fbb8a19a0`  |
| 2343   | No file  | `cc1fbb8a19a0`  |
| 2335   | No file  | `cc1fbb8a19a0`  |
| 2327   | No file  | `cc1fbb8a19a0`  |
| 2324   | No file  | `cc1fbb8a19a0`  |
| 2319   | No file  | `cc1fbb8a19a0`  |
| 2313   | No file  | `cc1fbb8a19a0`  |
| 2308   | No file  | `cc1fbb8a19a0`  |
| 2302   | No file  | `cc1fbb8a19a0`  |
| 2295   | No file  | `cc1fbb8a19a0`  |
| 2290   | No file  | `cc1fbb8a19a0`  |
| 2284   | No file  | `cc1fbb8a19a0`  |
| 2276   | No file  | `cc1fbb8a19a0`  |
| 2269   | No file  | `cc1fbb8a19a0`  |
| 2259   | No file  | `cc1fbb8a19a0`  |
| 2250   | No file  | `cc1fbb8a19a0`  |
| 2243   | No file  | `cc1fbb8a19a0`  |
| 2235   | No file  | `cc1fbb8a19a0`  |
| 2229   | No file  | `cc1fbb8a19a0`  |
| 2224   | No file  | `cc1fbb8a19a0`  |
| 2218   | No file  | `cc1fbb8a19a0`  |
| 2215   | No file  | `cc1fbb8a19a0`  |
| 2207   | No file  | `cc1fbb8a19a0`  |
| 2203   | No file  | `cc1fbb8a19a0`  |
| 2196   | No file  | `cc1fbb8a19a0`  |
| 2192   | No file  | `cc1fbb8a19a0`  |
| 2189   | No file  | `cc1fbb8a19a0`  |
| 2183   | No file  | `cc1fbb8a19a0`  |
| 2179   | No file  | `cc1fbb8a19a0`  |
| 2171   | No file  | `cc1fbb8a19a0`  |
| 2163   | No file  | `cc1fbb8a19a0`  |
| 2156   | No file  | `cc1fbb8a19a0`  |
| 2151   | No file  | `cc1fbb8a19a0`  |
| 2147   | No file  | `cc1fbb8a19a0`  |
| 2142   | No file  | `cc1fbb8a19a0`  |
| 2138   | No file  | `cc1fbb8a19a0`  |
| 2134   | No file  | `cc1fbb8a19a0`  |
| 2130   | No file  | `cc1fbb8a19a0`  |
| 2122   | No file  | `cc1fbb8a19a0`  |
| 2107   | No file  | `cc1fbb8a19a0`  |
| 2098   | No file  | `cc1fbb8a19a0`  |
| 2089   | No file  | `cc1fbb8a19a0`  |
| 2081   | No file  | `cc1fbb8a19a0`  |
| 2073   | No file  | `cc1fbb8a19a0`  |
| 2067   | No file  | `cc1fbb8a19a0`  |
| 2063   | No file  | `cc1fbb8a19a0`  |
| 2059   | No file  | `cc1fbb8a19a0`  |
| 2052   | No file  | `cc1fbb8a19a0`  |
| 2044   | No file  | `cc1fbb8a19a0`  |
| 2039   | No file  | `cc1fbb8a19a0`  |
| 2032   | No file  | `cc1fbb8a19a0`  |
| 2025   | No file  | `cc1fbb8a19a0`  |
| 2011   | No file  | `cc1fbb8a19a0`  |
| 2005   | No file  | `cc1fbb8a19a0`  |
| 2000   | No file  | `cc1fbb8a19a0`  |
| 1996   | No file  | `cc1fbb8a19a0`  |
| 1991   | No file  | `cc1fbb8a19a0`  |
| 1985   | No file  | `cc1fbb8a19a0`  |
| 1980   | No file  | `cc1fbb8a19a0`  |
| 1969   | No file  | `cc1fbb8a19a0`  |
| 1964   | No file  | `cc1fbb8a19a0`  |
| 1958   | No file  | `cc1fbb8a19a0`  |
| 1950   | No file  | `cc1fbb8a19a0`  |
| 1945   | No file  | `cc1fbb8a19a0`  |
| 1937   | No file  | `cc1fbb8a19a0`  |
| 1933   | No file  | `cc1fbb8a19a0`  |
| 1927   | No file  | `cc1fbb8a19a0`  |
| 1921   | No file  | `cc1fbb8a19a0`  |
| 1914   | No file  | `cc1fbb8a19a0`  |
| 1908   | No file  | `cc1fbb8a19a0`  |
| 1897   | No file  | `cc1fbb8a19a0`  |
| 1892   | No file  | `cc1fbb8a19a0`  |
| 1886   | No file  | `cc1fbb8a19a0`  |
| 1881   | No file  | `cc1fbb8a19a0`  |
| 1871   | No file  | `cc1fbb8a19a0`  |
| 1866   | No file  | `cc1fbb8a19a0`  |
| 1862   | No file  | `cc1fbb8a19a0`  |
| 1854   | No file  | `cc1fbb8a19a0`  |
| 1846   | No file  | `cc1fbb8a19a0`  |
| 1838   | No file  | `cc1fbb8a19a0`  |
| 1832   | No file  | `cc1fbb8a19a0`  |
| 1826   | No file  | `cc1fbb8a19a0`  |
| 1822   | No file  | `cc1fbb8a19a0`  |
| 1818   | No file  | `cc1fbb8a19a0`  |
| 1804   | No file  | `cc1fbb8a19a0`  |
| 1794   | No file  | `cc1fbb8a19a0`  |
| 1790   | No file  | `cc1fbb8a19a0`  |
| 1784   | No file  | `cc1fbb8a19a0`  |
| 1774   | No file  | `cc1fbb8a19a0`  |
| 1771   | No file  | `cc1fbb8a19a0`  |
| 1762   | No file  | `cc1fbb8a19a0`  |
| 1759   | No file  | `cc1fbb8a19a0`  |
| 1754   | No file  | `cc1fbb8a19a0`  |
| 1749   | No file  | `cc1fbb8a19a0`  |
| 1743   | No file  | `cc1fbb8a19a0`  |
| 1737   | No file  | `cc1fbb8a19a0`  |
| 1731   | No file  | `cc1fbb8a19a0`  |
| 1725   | No file  | `cc1fbb8a19a0`  |
| 1717   | No file  | `cc1fbb8a19a0`  |
| 1710   | No file  | `cc1fbb8a19a0`  |
| 1704   | No file  | `cc1fbb8a19a0`  |
| 1698   | No file  | `cc1fbb8a19a0`  |
| 1690   | No file  | `cc1fbb8a19a0`  |
| 1685   | No file  | `cc1fbb8a19a0`  |
| 1680   | No file  | `cc1fbb8a19a0`  |
| 1674   | No file  | `cc1fbb8a19a0`  |
| 1668   | No file  | `cc1fbb8a19a0`  |
| 1659   | No file  | `cc1fbb8a19a0`  |
| 1649   | No file  | `cc1fbb8a19a0`  |
| 1642   | No file  | `cc1fbb8a19a0`  |
| 1636   | No file  | `cc1fbb8a19a0`  |
| 1628   | No file  | `cc1fbb8a19a0`  |
| 1622   | No file  | `cc1fbb8a19a0`  |
| 1614   | No file  | `cc1fbb8a19a0`  |
| 1608   | No file  | `cc1fbb8a19a0`  |
| 1602   | No file  | `cc1fbb8a19a0`  |
| 1598   | No file  | `cc1fbb8a19a0`  |
| 1594   | No file  | `cc1fbb8a19a0`  |
| 1590   | No file  | `cc1fbb8a19a0`  |
| 1587   | No file  | `cc1fbb8a19a0`  |
| 1584   | No file  | `cc1fbb8a19a0`  |
| 1579   | No file  | `cc1fbb8a19a0`  |
| 1572   | No file  | `cc1fbb8a19a0`  |
| 1565   | No file  | `cc1fbb8a19a0`  |
| 1559   | No file  | `cc1fbb8a19a0`  |
| 1554   | No file  | `cc1fbb8a19a0`  |
| 1547   | No file  | `cc1fbb8a19a0`  |
| 1537   | No file  | `cc1fbb8a19a0`  |
| 1529   | No file  | `cc1fbb8a19a0`  |
| 1524   | No file  | `cc1fbb8a19a0`  |
| 1519   | No file  | `cc1fbb8a19a0`  |
| 1509   | No file  | `cc1fbb8a19a0`  |
| 1506   | No file  | `cc1fbb8a19a0`  |
| 1504   | No file  | `cc1fbb8a19a0`  |
| 1500   | No file  | `cc1fbb8a19a0`  |
| 1493   | No file  | `cc1fbb8a19a0`  |
| 1489   | No file  | `cc1fbb8a19a0`  |
| 1485   | No file  | `cc1fbb8a19a0`  |
| 1481   | No file  | `cc1fbb8a19a0`  |
| 1474   | No file  | `cc1fbb8a19a0`  |
| 1466   | No file  | `cc1fbb8a19a0`  |
| 1462   | No file  | `cc1fbb8a19a0`  |
| 1459   | No file  | `cc1fbb8a19a0`  |
| 1453   | No file  | `cc1fbb8a19a0`  |
| 1450   | No file  | `cc1fbb8a19a0`  |
| 1445   | No file  | `cc1fbb8a19a0`  |
| 1439   | No file  | `cc1fbb8a19a0`  |
| 1433   | No file  | `cc1fbb8a19a0`  |
| 1430   | No file  | `cc1fbb8a19a0`  |
| 1426   | No file  | `cc1fbb8a19a0`  |
| 1421   | No file  | `cc1fbb8a19a0`  |
| 1417   | No file  | `cc1fbb8a19a0`  |
| 1416   | No file  | `cc1fbb8a19a0`  |
| 1409   | No file  | `cc1fbb8a19a0`  |
| 1405   | No file  | `cc1fbb8a19a0`  |
| 1401   | No file  | `cc1fbb8a19a0`  |
| 1396   | No file  | `cc1fbb8a19a0`  |
| 1391   | No file  | `cc1fbb8a19a0`  |
| 1390   | No file  | `cc1fbb8a19a0`  |
| 1386   | No file  | `cc1fbb8a19a0`  |
| 1381   | No file  | `cc1fbb8a19a0`  |
| 1379   | No file  | `cc1fbb8a19a0`  |
| 1372   | No file  | `cc1fbb8a19a0`  |
| 1366   | No file  | `cc1fbb8a19a0`  |
| 1364   | No file  | `cc1fbb8a19a0`  |
| 1363   | No file  | `cc1fbb8a19a0`  |
| 1360   | No file  | `cc1fbb8a19a0`  |
| 1358   | No file  | `cc1fbb8a19a0`  |
| 1355   | No file  | `cc1fbb8a19a0`  |
| 1351   | No file  | `cc1fbb8a19a0`  |
| 1348   | No file  | `cc1fbb8a19a0`  |
| 1346   | No file  | `cc1fbb8a19a0`  |
| 1341   | No file  | `cc1fbb8a19a0`  |
| 1340   | No file  | `cc1fbb8a19a0`  |
| 1338   | No file  | `cc1fbb8a19a0`  |
| 1335   | No file  | `cc1fbb8a19a0`  |
| 1333   | No file  | `cc1fbb8a19a0`  |
| 1329   | No file  | `cc1fbb8a19a0`  |
| 1327   | No file  | `cc1fbb8a19a0`  |
| 1324   | No file  | `cc1fbb8a19a0`  |
| 1321   | No file  | `cc1fbb8a19a0`  |
| 1319   | No file  | `cc1fbb8a19a0`  |
| 1318   | No file  | `cc1fbb8a19a0`  |
| 1316   | No file  | `cc1fbb8a19a0`  |
| 1313   | No file  | `cc1fbb8a19a0`  |
| 1311   | No file  | `cc1fbb8a19a0`  |
| 1309   | No file  | `cc1fbb8a19a0`  |
| 1304   | No file  | `cc1fbb8a19a0`  |
| 1292   | No file  | `cc1fbb8a19a0`  |
| 1286   | No file  | `cc1fbb8a19a0`  |
| 1280   | No file  | `cc1fbb8a19a0`  |
| 1276   | No file  | `cc1fbb8a19a0`  |
| 1267   | No file  | `cc1fbb8a19a0`  |
| 1261   | No file  | `cc1fbb8a19a0`  |
| 1256   | No file  | `cc1fbb8a19a0`  |
| 1250   | No file  | `cc1fbb8a19a0`  |
| 1246   | No file  | `cc1fbb8a19a0`  |
| 1239   | No file  | `cc1fbb8a19a0`  |
| 1230   | No file  | `cc1fbb8a19a0`  |
| 1226   | No file  | `cc1fbb8a19a0`  |
| 1220   | No file  | `cc1fbb8a19a0`  |
| 1217   | No file  | `cc1fbb8a19a0`  |
| 1211   | No file  | `cc1fbb8a19a0`  |
| 1210   | No file  | `cc1fbb8a19a0`  |
| 1208   | No file  | `cc1fbb8a19a0`  |
| 1203   | No file  | `cc1fbb8a19a0`  |
| 1197   | No file  | `cc1fbb8a19a0`  |
| 1194   | No file  | `cc1fbb8a19a0`  |
| 1192   | No file  | `cc1fbb8a19a0`  |
| 1187   | No file  | `cc1fbb8a19a0`  |
| 1183   | No file  | `cc1fbb8a19a0`  |
| 1177   | No file  | `cc1fbb8a19a0`  |
| 1173   | No file  | `cc1fbb8a19a0`  |
| 1167   | No file  | `cc1fbb8a19a0`  |
| 1164   | No file  | `cc1fbb8a19a0`  |
| 1156   | No file  | `cc1fbb8a19a0`  |
| 1149   | No file  | `cc1fbb8a19a0`  |
| 1144   | No file  | `cc1fbb8a19a0`  |
| 1137   | No file  | `cc1fbb8a19a0`  |
| 1132   | No file  | `cc1fbb8a19a0`  |
| 1127   | No file  | `cc1fbb8a19a0`  |
| 1122   | No file  | `cc1fbb8a19a0`  |
| 1118   | No file  | `cc1fbb8a19a0`  |
| 1114   | No file  | `cc1fbb8a19a0`  |
| 1109   | No file  | `cc1fbb8a19a0`  |
| 1102   | No file  | `cc1fbb8a19a0`  |
| 1096   | No file  | `cc1fbb8a19a0`  |
| 1088   | No file  | `cc1fbb8a19a0`  |
| 1081   | No file  | `cc1fbb8a19a0`  |
| 1076   | No file  | `cc1fbb8a19a0`  |
| 1069   | No file  | `cc1fbb8a19a0`  |
| 1064   | No file  | `cc1fbb8a19a0`  |
| 1058   | No file  | `cc1fbb8a19a0`  |
| 1051   | No file  | `cc1fbb8a19a0`  |
| 1044   | No file  | `cc1fbb8a19a0`  |
| 1036   | No file  | `cc1fbb8a19a0`  |
| 1026   | No file  | `cc1fbb8a19a0`  |
| 1016   | No file  | `cc1fbb8a19a0`  |
| 1009   | No file  | `cc1fbb8a19a0`  |
| 1005   | No file  | `cc1fbb8a19a0`  |
| 1000   | No file  | `cc1fbb8a19a0`  |
| 998    | No file  | `cc1fbb8a19a0`  |
| 990    | No file  | `cc1fbb8a19a0`  |
| 979    | No file  | `cc1fbb8a19a0`  |
| 972    | No file  | `cc1fbb8a19a0`  |
| 963    | No file  | `cc1fbb8a19a0`  |
| 955    | No file  | `cc1fbb8a19a0`  |
| 946    | No file  | `cc1fbb8a19a0`  |
| 938    | No file  | `cc1fbb8a19a0`  |
| 927    | No file  | `cc1fbb8a19a0`  |
| 911    | No file  | `cc1fbb8a19a0`  |
| 904    | No file  | `cc1fbb8a19a0`  |
| 899    | No file  | `cc1fbb8a19a0`  |
| 894    | No file  | `cc1fbb8a19a0`  |
| 885    | No file  | `cc1fbb8a19a0`  |
| 879    | No file  | `cc1fbb8a19a0`  |
| 872    | No file  | `cc1fbb8a19a0`  |
| 864    | No file  | `cc1fbb8a19a0`  |
| 855    | No file  | `cc1fbb8a19a0`  |
| 853    | No file  | `cc1fbb8a19a0`  |
| 845    | No file  | `cc1fbb8a19a0`  |
| 837    | No file  | `cc1fbb8a19a0`  |
| 829    | No file  | `cc1fbb8a19a0`  |
| 822    | No file  | `cc1fbb8a19a0`  |
| 814    | No file  | `cc1fbb8a19a0`  |
| 805    | No file  | `cc1fbb8a19a0`  |
| 794    | No file  | `cc1fbb8a19a0`  |
| 787    | No file  | `cc1fbb8a19a0`  |
| 780    | No file  | `cc1fbb8a19a0`  |
| 771    | No file  | `cc1fbb8a19a0`  |
| 760    | No file  | `cc1fbb8a19a0`  |
| 748    | No file  | `cc1fbb8a19a0`  |
| 741    | No file  | `cc1fbb8a19a0`  |
| 736    | No file  | `cc1fbb8a19a0`  |
| 731    | No file  | `cc1fbb8a19a0`  |
| 723    | No file  | `cc1fbb8a19a0`  |
| 711    | No file  | `cc1fbb8a19a0`  |
| 707    | No file  | `cc1fbb8a19a0`  |
| 697    | No file  | `cc1fbb8a19a0`  |
| 689    | No file  | `cc1fbb8a19a0`  |
| 683    | No file  | `cc1fbb8a19a0`  |
| 678    | No file  | `cc1fbb8a19a0`  |
| 670    | No file  | `cc1fbb8a19a0`  |
| 661    | No file  | `cc1fbb8a19a0`  |
| 656    | No file  | `cc1fbb8a19a0`  |
| 652    | No file  | `cc1fbb8a19a0`  |
| 643    | No file  | `cc1fbb8a19a0`  |
| 637    | No file  | `cc1fbb8a19a0`  |
| 630    | No file  | `cc1fbb8a19a0`  |
| 627    | No file  | `cc1fbb8a19a0`  |
| 621    | No file  | `cc1fbb8a19a0`  |
| 617    | No file  | `cc1fbb8a19a0`  |
| 615    | No file  | `cc1fbb8a19a0`  |
| 606    | No file  | `cc1fbb8a19a0`  |
| 599    | No file  | `cc1fbb8a19a0`  |
| 592    | No file  | `cc1fbb8a19a0`  |
| 586    | No file  | `cc1fbb8a19a0`  |
| 577    | No file  | `cc1fbb8a19a0`  |
| 569    | No file  | `cc1fbb8a19a0`  |
| 561    | No file  | `cc1fbb8a19a0`  |
| 554    | No file  | `cc1fbb8a19a0`  |
| 542    | No file  | `cc1fbb8a19a0`  |
| 532    | No file  | `cc1fbb8a19a0`  |
| 531    | No file  | `cc1fbb8a19a0`  |
| 526    | No file  | `cc1fbb8a19a0`  |
| 521    | No file  | `cc1fbb8a19a0`  |
| 517    | No file  | `cc1fbb8a19a0`  |
| 510    | No file  | `cc1fbb8a19a0`  |
| 508    | No file  | `cc1fbb8a19a0`  |
| 504    | No file  | `cc1fbb8a19a0`  |
| 497    | No file  | `cc1fbb8a19a0`  |
| 491    | No file  | `cc1fbb8a19a0`  |
| 485    | No file  | `cc1fbb8a19a0`  |
| 478    | No file  | `cc1fbb8a19a0`  |
| 472    | No file  | `cc1fbb8a19a0`  |
| 466    | No file  | `cc1fbb8a19a0`  |
| 457    | No file  | `cc1fbb8a19a0`  |
| 452    | No file  | `cc1fbb8a19a0`  |
| 449    | No file  | `cc1fbb8a19a0`  |
| 435    | No file  | `cc1fbb8a19a0`  |

<!-- versions:end -->

## Companion Files

None. The handler names each item with LOC type 0 from
`languagedata_*.loc` when it is loaded.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of stones                              |
| `+0x08`             | Row[row_count] | rows         | See Row; byte-packed                          |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 4 bytes + levels)

| Offset  | Type               | Field       | Notes                                                        |
| ------- | ------------------ | ----------- | ------------------------------------------------------------ |
| `+0x00` | u32                | level_count | Number of `levels`; `2` on every row of client 3483          |
| `+0x04` | Level[level_count] | levels      | See Level; level 0 first                                     |

### Level (24 bytes)

| Offset  | Type     | Field                     | Notes                                                                 |
| ------- | -------- | ------------------------- | --------------------------------------------------------------------- |
| `+0x00` | u32      | item_enchant_key          | The stone at this level: `enchant_level << 24 \| item_id`, level `0` on every row |
| `+0x04` | u32      | unknown_04                | `0` on every level of client 3483                                     |
| `+0x08` | u32      | material_item_enchant_key | The item an upgrade to this level consumes; `0` on level 0           |
| `+0x0C` | bytes[4] | padding_0c                | Alignment of `material_item_count` to 8 bytes; see Notes              |
| `+0x10` | u64      | material_item_count       | Count of the material; left-over bytes on level 0, see Notes          |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                   |
| ------- | ------------------ | ------------ | ----------------------- |
| `+0x00` | u32                | string_count | Number of strings       |
| `+0x04` | pstr[string_count] | strings      | No field reads a string |

## Stones

The 11 rows of client 3483: the stone index (row position), the level 0
Reforge Stone and the level 1 HAN Reforge Stone, `+307` keys above it.
The level 1 material is the level 1 stone itself, count 1, on every row.

| Index | Level 0  | Level 1  | Effect                        |
| ----- | -------- | -------- | ----------------------------- |
| 0     | 820953   | 821260   | All AP                        |
| 1     | 820954   | 821261   | All Accuracy                  |
| 2     | 820955   | 821262   | All Damage Reduction          |
| 3     | 820956   | 821263   | All Evasion                   |
| 4     | 820957   | 821264   | Max HP                        |
| 5     | 820958   | 821265   | Critical Hit Rate             |
| 6     | 820959   | 821266   | Back Attack Extra Damage      |
| 7     | 820960   | 821267   | Down Attack Extra Damage      |
| 8     | 820961   | 821268   | Air Attack Extra Damage       |
| 9     | 820962   | 821269   | Critical Hit Extra Damage     |
| 10    | 820963   | 821270   | Black Spirit's Rage Recovery  |

The four Reforge Stones that ignore a resistance (`820964` to `820967`)
have no row and no HAN version in LOC type 0.

## Field Names

The file is newer than client 1784: it is not in that client's archives,
and no sheet of a private server's `DataSheets.bexcel` on that client has
`Reforge` in its name. The names follow the getters of the client Lua
(client 3482, `panel_window_reforgestonepreset_all_1` and `_2`):

- `ToClient_GetReforgeStoneItemEnchantKey(index, stoneLevel)` returns the
  item key the window looks up in the inventory and passes to
  `getItemEnchantStaticStatus`; it is `item_enchant_key`.
- `ToClient_GetReforgeStoneMaterialItemEnchantKey(index, nextStoneLevel)`
  and `ToClient_GetReforgeStoneMaterialItemCount(index, nextStoneLevel)`
  fill the upgrade tooltip `LUA_REFORGESTONE_UPGRADE_TOOLTIP_DESC` ("Use
  {itemName} x{count} in your inventory as material to enhance a Reforge
  Stone."). The Lua asks for level `stoneLevel + 1`, so the material sits
  on the level an upgrade reaches, and level 0 has none.

## Notes

- `padding_0c` is the alignment gap before the u64 count. It holds
  left-over bytes, the same in every level of one file: `ce 00 00 00` on
  client 3483 and `bf 00 00 00` on client 3474 for the same rows.
- On level 0, where `material_item_enchant_key` is `0`,
  `material_item_count` is never set: it holds `0x00007FFC5E2E5722` on every
  row of clients 3474 and 3483, an x64 stack address.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/enchantshop_tables.py`:
  the stone index, then each level as item name and key, with the material
  and its count when the level has one.

## Open Questions

### What `unknown_04` Holds

`unknown_04` is `0` on all 22 levels of clients 3474 and 3483. The Lua of
client 3482 reads three values of a level (the item key, the material key
and the material count), so no getter names it.
