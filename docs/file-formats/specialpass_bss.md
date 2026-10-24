# `specialpass.bss` Format

## Purpose

The Special Pass events of the event window: per pass its period, the end
of the pass sale, string table indices of its Korean title, period text
and description, and its content type (Daily, Solare, Combat, Sailing or
Gathering Special). A reward track per pass follows the rows, 14 steps of
a basic item, a pass item and the Pass Points that unlock the step.
`panel_event_specialpass_all_1.luac` picks a pass through
`ToClient_GetCurrentSpecialPassKey(passType)` and reads it through
`ToClient_GetSpecialPassTitle`, `ToClient_GetSpecialPassPeriod`,
`ToClient_GetSpecialPassDesc`, `ToClient_GetSpecialPassItemEnchantKey(passKey,
isPass, index)`, `ToClient_GetSpecialPassItemCount(passKey, isPass, index)`
and `ToClient_GetSpecialPassItemRewardPoint(passKey, index)`, for index `0`
to `__eSPECIALPASS_MAX_COUNT - 1`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File              | Bytes  | Records                           | Row bytes |
| ------ | -------------- | ------- | ----------------- | ------ | --------------------------------- | --------- |
| 2      | 2844 and later | 3483    | `specialpass.bss` | 39,107 | 31 Row, 434 Step, 31 Reward Track | 34        |
| 1      | 2059 to 2834   | 2834    | `specialpass.bss` | 16,481 | 13 Row, 182 Step, 13 Reward Track | 26        |

| Layout | File              | Known            | Unknown      |
| ------ | ----------------- | ---------------- | ------------ |
| 2      | `specialpass.bss` | 38,908 B (99.5%) | 199 B (0.5%) |
| 1      | `specialpass.bss` | 16,429 B (99.7%) | 52 B (0.3%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 2             | `ccf7ddd0bac0`  |
| 3482   | Layout 2             | `ccf7ddd0bac0`  |
| 3474   | Layout 2             | `ccf7ddd0bac0`  |
| 3473   | Layout 2             | `ccf7ddd0bac0`  |
| 3464   | Layout 2             | `ccf7ddd0bac0`  |
| 3458   | Layout 2             | `ccf7ddd0bac0`  |
| 3454   | Layout 2             | `ccf7ddd0bac0`  |
| 3444   | Layout 2             | `ccf7ddd0bac0`  |
| 3435   | Layout 2             | `ccf7ddd0bac0`  |
| 3426   | Layout 2             | `ccf7ddd0bac0`  |
| 3418   | Layout 2             | `ccf7ddd0bac0`  |
| 3412   | Layout 2             | `ccf7ddd0bac0`  |
| 3402   | Layout 2             | `ccf7ddd0bac0`  |
| 3396   | Layout 2             | `ccf7ddd0bac0`  |
| 3387   | Layout 2             | `ccf7ddd0bac0`  |
| 3381   | Layout 2             | `ccf7ddd0bac0`  |
| 3373   | Layout 2             | `ccf7ddd0bac0`  |
| 3364   | Layout 2             | `ccf7ddd0bac0`  |
| 3356   | Layout 2             | `ccf7ddd0bac0`  |
| 3349   | Layout 2             | `ccf7ddd0bac0`  |
| 3342   | Layout 2             | `ccf7ddd0bac0`  |
| 3335   | Layout 2             | `ccf7ddd0bac0`  |
| 3326   | Layout 2             | `ccf7ddd0bac0`  |
| 3321   | Layout 2             | `ccf7ddd0bac0`  |
| 3314   | Layout 2             | `ccf7ddd0bac0`  |
| 3303   | Layout 2             | `ccf7ddd0bac0`  |
| 3302   | Layout 2             | `ccf7ddd0bac0`  |
| 3293   | Layout 2             | `ccf7ddd0bac0`  |
| 3283   | Layout 2             | `ccf7ddd0bac0`  |
| 3275   | Layout 2             | `ccf7ddd0bac0`  |
| 3267   | Layout 2             | `ccf7ddd0bac0`  |
| 3258   | Layout 2             | `ccf7ddd0bac0`  |
| 3251   | Layout 2             | `ccf7ddd0bac0`  |
| 3242   | Layout 2             | `ccf7ddd0bac0`  |
| 3235   | Layout 2             | `ccf7ddd0bac0`  |
| 3229   | Layout 2             | `ccf7ddd0bac0`  |
| 3212   | Layout 2             | `ccf7ddd0bac0`  |
| 3203   | Layout 2             | `ccf7ddd0bac0`  |
| 3193   | Layout 2             | `ccf7ddd0bac0`  |
| 3186   | Layout 2             | `ccf7ddd0bac0`  |
| 3177   | Layout 2             | `ccf7ddd0bac0`  |
| 3169   | Layout 2             | `ccf7ddd0bac0`  |
| 3158   | Layout 2             | `ccf7ddd0bac0`  |
| 3151   | Layout 2             | `ccf7ddd0bac0`  |
| 3144   | Layout 2             | `ccf7ddd0bac0`  |
| 3133   | Layout 2             | `ccf7ddd0bac0`  |
| 3125   | Layout 2             | `ccf7ddd0bac0`  |
| 3118   | Layout 2             | `ccf7ddd0bac0`  |
| 3111   | Layout 2             | `ccf7ddd0bac0`  |
| 3103   | Layout 2             | `ccf7ddd0bac0`  |
| 3095   | Layout 2             | `ccf7ddd0bac0`  |
| 3086   | Layout 2             | `ccf7ddd0bac0`  |
| 3072   | Layout 2             | `ccf7ddd0bac0`  |
| 3062   | Layout 2             | `ccf7ddd0bac0`  |
| 3052   | Layout 2             | `ccf7ddd0bac0`  |
| 3045   | Layout 2             | `ccf7ddd0bac0`  |
| 3037   | Layout 2             | `ccf7ddd0bac0`  |
| 3030   | Layout 2             | `ccf7ddd0bac0`  |
| 3021   | Layout 2             | `ccf7ddd0bac0`  |
| 3012   | Layout 2             | `ccf7ddd0bac0`  |
| 3002   | Layout 2             | `ccf7ddd0bac0`  |
| 2995   | Layout 2             | `ccf7ddd0bac0`  |
| 2987   | Layout 2             | `ccf7ddd0bac0`  |
| 2978   | Layout 2             | `ccf7ddd0bac0`  |
| 2970   | Layout 2             | `ccf7ddd0bac0`  |
| 2959   | Layout 2             | `ccf7ddd0bac0`  |
| 2951   | Layout 2             | `ccf7ddd0bac0`  |
| 2942   | Layout 2             | `ccf7ddd0bac0`  |
| 2935   | Layout 2             | `ccf7ddd0bac0`  |
| 2932   | Layout 2             | `ccf7ddd0bac0`  |
| 2923   | Layout 2             | `ccf7ddd0bac0`  |
| 2919   | Layout 2             | `ccf7ddd0bac0`  |
| 2907   | Layout 2             | `ccf7ddd0bac0`  |
| 2900   | Layout 2             | `ccf7ddd0bac0`  |
| 2891   | Layout 2             | `ccf7ddd0bac0`  |
| 2882   | Layout 2             | `ccf7ddd0bac0`  |
| 2872   | Layout 2             | `ccf7ddd0bac0`  |
| 2863   | Layout 2             | `ccf7ddd0bac0`  |
| 2855   | Layout 2             | `ccf7ddd0bac0`  |
| 2849   | Layout 2             | `ccf7ddd0bac0`  |
| 2844   | Layout 2             | `ccf7ddd0bac0`  |
| 2834   | Layout 1             | `ccf7ddd0bac0`  |
| 2825   | Layout 1             | `ccf7ddd0bac0`  |
| 2819   | Layout 1             | `ccf7ddd0bac0`  |
| 2811   | Layout 1             | `ccf7ddd0bac0`  |
| 2803   | Layout 1             | `ccf7ddd0bac0`  |
| 2794   | Layout 1             | `ccf7ddd0bac0`  |
| 2783   | Layout 1             | `ccf7ddd0bac0`  |
| 2774   | Layout 1             | `ccf7ddd0bac0`  |
| 2765   | Layout 1             | `ccf7ddd0bac0`  |
| 2756   | Layout 1             | `ccf7ddd0bac0`  |
| 2750   | Layout 1             | `ccf7ddd0bac0`  |
| 2743   | Layout 1             | `ccf7ddd0bac0`  |
| 2736   | Layout 1             | `ccf7ddd0bac0`  |
| 2726   | Layout 1             | `ccf7ddd0bac0`  |
| 2717   | Layout 1             | `ccf7ddd0bac0`  |
| 2709   | Layout 1             | `ccf7ddd0bac0`  |
| 2703   | Layout 1             | `ccf7ddd0bac0`  |
| 2695   | Layout 1             | `ccf7ddd0bac0`  |
| 2684   | Layout 1             | `ccf7ddd0bac0`  |
| 2672   | Layout 1             | `ccf7ddd0bac0`  |
| 2665   | Layout 1             | `ccf7ddd0bac0`  |
| 2657   | Layout 1             | `ccf7ddd0bac0`  |
| 2649   | Layout 1             | `ccf7ddd0bac0`  |
| 2644   | Layout 1             | `ccf7ddd0bac0`  |
| 2637   | Layout 1             | `ccf7ddd0bac0`  |
| 2629   | Layout 1             | `ccf7ddd0bac0`  |
| 2619   | Layout 1             | `ccf7ddd0bac0`  |
| 2612   | Layout 1             | `ccf7ddd0bac0`  |
| 2606   | Layout 1             | `ccf7ddd0bac0`  |
| 2602   | Layout 1             | `ccf7ddd0bac0`  |
| 2601   | Layout 1             | `ccf7ddd0bac0`  |
| 2592   | Layout 1             | `ccf7ddd0bac0`  |
| 2583   | Layout 1             | `ccf7ddd0bac0`  |
| 2575   | Layout 1             | `ccf7ddd0bac0`  |
| 2567   | Layout 1             | `ccf7ddd0bac0`  |
| 2560   | Layout 1             | `ccf7ddd0bac0`  |
| 2553   | Layout 1             | `ccf7ddd0bac0`  |
| 2545   | Layout 1             | `ccf7ddd0bac0`  |
| 2538   | Layout 1             | `ccf7ddd0bac0`  |
| 2529   | Layout 1             | `ccf7ddd0bac0`  |
| 2519   | Layout 1             | `ccf7ddd0bac0`  |
| 2513   | Layout 1             | `ccf7ddd0bac0`  |
| 2510   | Layout 1             | `ccf7ddd0bac0`  |
| 2507   | Layout 1             | `ccf7ddd0bac0`  |
| 2503   | Layout 1             | `ccf7ddd0bac0`  |
| 2498   | Layout 1             | `ccf7ddd0bac0`  |
| 2492   | Layout 1             | `ccf7ddd0bac0`  |
| 2487   | Layout 1             | `ccf7ddd0bac0`  |
| 2480   | Layout 1             | `ccf7ddd0bac0`  |
| 2474   | Layout 1             | `ccf7ddd0bac0`  |
| 2468   | Layout 1             | `ccf7ddd0bac0`  |
| 2460   | Layout 1             | `ccf7ddd0bac0`  |
| 2453   | Layout 1             | `ccf7ddd0bac0`  |
| 2444   | Layout 1             | `ccf7ddd0bac0`  |
| 2438   | Layout 1             | `ccf7ddd0bac0`  |
| 2434   | Layout 1             | `ccf7ddd0bac0`  |
| 2429   | Layout 1             | `ccf7ddd0bac0`  |
| 2421   | Layout 1             | `ccf7ddd0bac0`  |
| 2414   | Layout 1             | `ccf7ddd0bac0`  |
| 2407   | Layout 1             | `ccf7ddd0bac0`  |
| 2401   | Layout 1             | `ccf7ddd0bac0`  |
| 2397   | Layout 1             | `ccf7ddd0bac0`  |
| 2393   | Layout 1             | `ccf7ddd0bac0`  |
| 2384   | Layout 1             | `ccf7ddd0bac0`  |
| 2378   | Layout 1             | `ccf7ddd0bac0`  |
| 2372   | Layout 1             | `ccf7ddd0bac0`  |
| 2358   | Layout 1             | `ccf7ddd0bac0`  |
| 2352   | Layout 1             | `ccf7ddd0bac0`  |
| 2347   | Layout 1             | `ccf7ddd0bac0`  |
| 2343   | Layout 1             | `ccf7ddd0bac0`  |
| 2335   | Layout 1             | `ccf7ddd0bac0`  |
| 2327   | Layout 1             | `ccf7ddd0bac0`  |
| 2324   | Layout 1             | `ccf7ddd0bac0`  |
| 2319   | Layout 1             | `ccf7ddd0bac0`  |
| 2313   | Layout 1             | `ccf7ddd0bac0`  |
| 2308   | Layout 1             | `ccf7ddd0bac0`  |
| 2302   | Layout 1             | `ccf7ddd0bac0`  |
| 2295   | Layout 1             | `ccf7ddd0bac0`  |
| 2290   | Layout 1             | `ccf7ddd0bac0`  |
| 2284   | Layout 1             | `ccf7ddd0bac0`  |
| 2276   | Layout 1             | `ccf7ddd0bac0`  |
| 2269   | Layout 1             | `ccf7ddd0bac0`  |
| 2259   | Layout 1             | `ccf7ddd0bac0`  |
| 2250   | Layout 1             | `ccf7ddd0bac0`  |
| 2243   | Layout 1             | `ccf7ddd0bac0`  |
| 2235   | Layout 1             | `ccf7ddd0bac0`  |
| 2229   | Layout 1             | `ccf7ddd0bac0`  |
| 2224   | Layout 1             | `ccf7ddd0bac0`  |
| 2218   | Layout 1             | `ccf7ddd0bac0`  |
| 2215   | Layout 1             | `ccf7ddd0bac0`  |
| 2207   | Layout 1             | `ccf7ddd0bac0`  |
| 2203   | Layout 1             | `ccf7ddd0bac0`  |
| 2196   | Layout 1             | `ccf7ddd0bac0`  |
| 2192   | Layout 1             | `ccf7ddd0bac0`  |
| 2189   | Layout 1             | `ccf7ddd0bac0`  |
| 2183   | Layout 1             | `ccf7ddd0bac0`  |
| 2179   | Layout 1             | `ccf7ddd0bac0`  |
| 2171   | Layout 1             | `ccf7ddd0bac0`  |
| 2163   | Layout 1             | `ccf7ddd0bac0`  |
| 2156   | Layout 1             | `ccf7ddd0bac0`  |
| 2151   | Layout 1             | `ccf7ddd0bac0`  |
| 2147   | Layout 1             | `ccf7ddd0bac0`  |
| 2142   | Layout 1             | `ccf7ddd0bac0`  |
| 2138   | Layout 1             | `ccf7ddd0bac0`  |
| 2134   | Layout 1             | `ccf7ddd0bac0`  |
| 2130   | Layout 1             | `ccf7ddd0bac0`  |
| 2122   | Layout 1             | `ccf7ddd0bac0`  |
| 2107   | Layout 1             | `ccf7ddd0bac0`  |
| 2098   | Layout 1             | `ccf7ddd0bac0`  |
| 2089   | Layout 1             | `ccf7ddd0bac0`  |
| 2081   | Layout 1             | `ccf7ddd0bac0`  |
| 2073   | Layout 1             | `ccf7ddd0bac0`  |
| 2067   | Layout 1             | `ccf7ddd0bac0`  |
| 2063   | Layout 1             | `ccf7ddd0bac0`  |
| 2059   | Layout 1             | `ccf7ddd0bac0`  |
| 2052   | No documented layout | `ccf7ddd0bac0`  |
| 2044   | No file              | `ccf7ddd0bac0`  |
| 2039   | No file              | `ccf7ddd0bac0`  |
| 2032   | No file              | `ccf7ddd0bac0`  |
| 2025   | No file              | `ccf7ddd0bac0`  |
| 2011   | No file              | `ccf7ddd0bac0`  |
| 2005   | No file              | `ccf7ddd0bac0`  |
| 2000   | No file              | `ccf7ddd0bac0`  |
| 1996   | No file              | `ccf7ddd0bac0`  |
| 1991   | No file              | `ccf7ddd0bac0`  |
| 1985   | No file              | `ccf7ddd0bac0`  |
| 1980   | No file              | `ccf7ddd0bac0`  |
| 1969   | No file              | `ccf7ddd0bac0`  |
| 1964   | No file              | `ccf7ddd0bac0`  |
| 1958   | No file              | `ccf7ddd0bac0`  |
| 1950   | No file              | `ccf7ddd0bac0`  |
| 1945   | No file              | `ccf7ddd0bac0`  |
| 1937   | No file              | `ccf7ddd0bac0`  |
| 1933   | No file              | `ccf7ddd0bac0`  |
| 1927   | No file              | `ccf7ddd0bac0`  |
| 1921   | No file              | `ccf7ddd0bac0`  |
| 1914   | No file              | `ccf7ddd0bac0`  |
| 1908   | No file              | `ccf7ddd0bac0`  |
| 1897   | No file              | `ccf7ddd0bac0`  |
| 1892   | No file              | `ccf7ddd0bac0`  |
| 1886   | No file              | `ccf7ddd0bac0`  |
| 1881   | No file              | `ccf7ddd0bac0`  |
| 1871   | No file              | `ccf7ddd0bac0`  |
| 1866   | No file              | `ccf7ddd0bac0`  |
| 1862   | No file              | `ccf7ddd0bac0`  |
| 1854   | No file              | `ccf7ddd0bac0`  |
| 1846   | No file              | `ccf7ddd0bac0`  |
| 1838   | No file              | `ccf7ddd0bac0`  |
| 1832   | No file              | `ccf7ddd0bac0`  |
| 1826   | No file              | `ccf7ddd0bac0`  |
| 1822   | No file              | `ccf7ddd0bac0`  |
| 1818   | No file              | `ccf7ddd0bac0`  |
| 1804   | No file              | `ccf7ddd0bac0`  |
| 1794   | No file              | `ccf7ddd0bac0`  |
| 1790   | No file              | `ccf7ddd0bac0`  |
| 1784   | No file              | `ccf7ddd0bac0`  |
| 1774   | No file              | `ccf7ddd0bac0`  |
| 1771   | No file              | `ccf7ddd0bac0`  |
| 1762   | No file              | `ccf7ddd0bac0`  |
| 1759   | No file              | `ccf7ddd0bac0`  |
| 1754   | No file              | `ccf7ddd0bac0`  |
| 1749   | No file              | `ccf7ddd0bac0`  |
| 1743   | No file              | `ccf7ddd0bac0`  |
| 1737   | No file              | `ccf7ddd0bac0`  |
| 1731   | No file              | `ccf7ddd0bac0`  |
| 1725   | No file              | `ccf7ddd0bac0`  |
| 1717   | No file              | `ccf7ddd0bac0`  |
| 1710   | No file              | `ccf7ddd0bac0`  |
| 1704   | No file              | `ccf7ddd0bac0`  |
| 1698   | No file              | `ccf7ddd0bac0`  |
| 1690   | No file              | `ccf7ddd0bac0`  |
| 1685   | No file              | `ccf7ddd0bac0`  |
| 1680   | No file              | `ccf7ddd0bac0`  |
| 1674   | No file              | `ccf7ddd0bac0`  |
| 1668   | No file              | `ccf7ddd0bac0`  |
| 1659   | No file              | `ccf7ddd0bac0`  |
| 1649   | No file              | `ccf7ddd0bac0`  |
| 1642   | No file              | `ccf7ddd0bac0`  |
| 1636   | No file              | `ccf7ddd0bac0`  |
| 1628   | No file              | `ccf7ddd0bac0`  |
| 1622   | No file              | `ccf7ddd0bac0`  |
| 1614   | No file              | `ccf7ddd0bac0`  |
| 1608   | No file              | `ccf7ddd0bac0`  |
| 1602   | No file              | `ccf7ddd0bac0`  |
| 1598   | No file              | `ccf7ddd0bac0`  |
| 1594   | No file              | `ccf7ddd0bac0`  |
| 1590   | No file              | `ccf7ddd0bac0`  |
| 1587   | No file              | `ccf7ddd0bac0`  |
| 1584   | No file              | `ccf7ddd0bac0`  |
| 1579   | No file              | `ccf7ddd0bac0`  |
| 1572   | No file              | `ccf7ddd0bac0`  |
| 1565   | No file              | `ccf7ddd0bac0`  |
| 1559   | No file              | `ccf7ddd0bac0`  |
| 1554   | No file              | `ccf7ddd0bac0`  |
| 1547   | No file              | `ccf7ddd0bac0`  |
| 1537   | No file              | `ccf7ddd0bac0`  |
| 1529   | No file              | `ccf7ddd0bac0`  |
| 1524   | No file              | `ccf7ddd0bac0`  |
| 1519   | No file              | `ccf7ddd0bac0`  |
| 1509   | No file              | `ccf7ddd0bac0`  |
| 1506   | No file              | `ccf7ddd0bac0`  |
| 1504   | No file              | `ccf7ddd0bac0`  |
| 1500   | No file              | `ccf7ddd0bac0`  |
| 1493   | No file              | `ccf7ddd0bac0`  |
| 1489   | No file              | `ccf7ddd0bac0`  |
| 1485   | No file              | `ccf7ddd0bac0`  |
| 1481   | No file              | `ccf7ddd0bac0`  |
| 1474   | No file              | `ccf7ddd0bac0`  |
| 1466   | No file              | `ccf7ddd0bac0`  |
| 1462   | No file              | `ccf7ddd0bac0`  |
| 1459   | No file              | `ccf7ddd0bac0`  |
| 1453   | No file              | `ccf7ddd0bac0`  |
| 1450   | No file              | `ccf7ddd0bac0`  |
| 1445   | No file              | `ccf7ddd0bac0`  |
| 1439   | No file              | `ccf7ddd0bac0`  |
| 1433   | No file              | `ccf7ddd0bac0`  |
| 1430   | No file              | `ccf7ddd0bac0`  |
| 1426   | No file              | `ccf7ddd0bac0`  |
| 1421   | No file              | `ccf7ddd0bac0`  |
| 1417   | No file              | `ccf7ddd0bac0`  |
| 1416   | No file              | `ccf7ddd0bac0`  |
| 1409   | No file              | `ccf7ddd0bac0`  |
| 1405   | No file              | `ccf7ddd0bac0`  |
| 1401   | No file              | `ccf7ddd0bac0`  |
| 1396   | No file              | `ccf7ddd0bac0`  |
| 1391   | No file              | `ccf7ddd0bac0`  |
| 1390   | No file              | `ccf7ddd0bac0`  |
| 1386   | No file              | `ccf7ddd0bac0`  |
| 1381   | No file              | `ccf7ddd0bac0`  |
| 1379   | No file              | `ccf7ddd0bac0`  |
| 1372   | No file              | `ccf7ddd0bac0`  |
| 1366   | No file              | `ccf7ddd0bac0`  |
| 1364   | No file              | `ccf7ddd0bac0`  |
| 1363   | No file              | `ccf7ddd0bac0`  |
| 1360   | No file              | `ccf7ddd0bac0`  |
| 1358   | No file              | `ccf7ddd0bac0`  |
| 1355   | No file              | `ccf7ddd0bac0`  |
| 1351   | No file              | `ccf7ddd0bac0`  |
| 1348   | No file              | `ccf7ddd0bac0`  |
| 1346   | No file              | `ccf7ddd0bac0`  |
| 1341   | No file              | `ccf7ddd0bac0`  |
| 1340   | No file              | `ccf7ddd0bac0`  |
| 1338   | No file              | `ccf7ddd0bac0`  |
| 1335   | No file              | `ccf7ddd0bac0`  |
| 1333   | No file              | `ccf7ddd0bac0`  |
| 1329   | No file              | `ccf7ddd0bac0`  |
| 1327   | No file              | `ccf7ddd0bac0`  |
| 1324   | No file              | `ccf7ddd0bac0`  |
| 1321   | No file              | `ccf7ddd0bac0`  |
| 1319   | No file              | `ccf7ddd0bac0`  |
| 1318   | No file              | `ccf7ddd0bac0`  |
| 1316   | No file              | `ccf7ddd0bac0`  |
| 1313   | No file              | `ccf7ddd0bac0`  |
| 1311   | No file              | `ccf7ddd0bac0`  |
| 1309   | No file              | `ccf7ddd0bac0`  |
| 1304   | No file              | `ccf7ddd0bac0`  |
| 1292   | No file              | `ccf7ddd0bac0`  |
| 1286   | No file              | `ccf7ddd0bac0`  |
| 1280   | No file              | `ccf7ddd0bac0`  |
| 1276   | No file              | `ccf7ddd0bac0`  |
| 1267   | No file              | `ccf7ddd0bac0`  |
| 1261   | No file              | `ccf7ddd0bac0`  |
| 1256   | No file              | `ccf7ddd0bac0`  |
| 1250   | No file              | `ccf7ddd0bac0`  |
| 1246   | No file              | `ccf7ddd0bac0`  |
| 1239   | No file              | `ccf7ddd0bac0`  |
| 1230   | No file              | `ccf7ddd0bac0`  |
| 1226   | No file              | `ccf7ddd0bac0`  |
| 1220   | No file              | `ccf7ddd0bac0`  |
| 1217   | No file              | `ccf7ddd0bac0`  |
| 1211   | No file              | `ccf7ddd0bac0`  |
| 1210   | No file              | `ccf7ddd0bac0`  |
| 1208   | No file              | `ccf7ddd0bac0`  |
| 1203   | No file              | `ccf7ddd0bac0`  |
| 1197   | No file              | `ccf7ddd0bac0`  |
| 1194   | No file              | `ccf7ddd0bac0`  |
| 1192   | No file              | `ccf7ddd0bac0`  |
| 1187   | No file              | `ccf7ddd0bac0`  |
| 1183   | No file              | `ccf7ddd0bac0`  |
| 1177   | No file              | `ccf7ddd0bac0`  |
| 1173   | No file              | `ccf7ddd0bac0`  |
| 1167   | No file              | `ccf7ddd0bac0`  |
| 1164   | No file              | `ccf7ddd0bac0`  |
| 1156   | No file              | `ccf7ddd0bac0`  |
| 1149   | No file              | `ccf7ddd0bac0`  |
| 1144   | No file              | `ccf7ddd0bac0`  |
| 1137   | No file              | `ccf7ddd0bac0`  |
| 1132   | No file              | `ccf7ddd0bac0`  |
| 1127   | No file              | `ccf7ddd0bac0`  |
| 1122   | No file              | `ccf7ddd0bac0`  |
| 1118   | No file              | `ccf7ddd0bac0`  |
| 1114   | No file              | `ccf7ddd0bac0`  |
| 1109   | No file              | `ccf7ddd0bac0`  |
| 1102   | No file              | `ccf7ddd0bac0`  |
| 1096   | No file              | `ccf7ddd0bac0`  |
| 1088   | No file              | `ccf7ddd0bac0`  |
| 1081   | No file              | `ccf7ddd0bac0`  |
| 1076   | No file              | `ccf7ddd0bac0`  |
| 1069   | No file              | `ccf7ddd0bac0`  |
| 1064   | No file              | `ccf7ddd0bac0`  |
| 1058   | No file              | `ccf7ddd0bac0`  |
| 1051   | No file              | `ccf7ddd0bac0`  |
| 1044   | No file              | `ccf7ddd0bac0`  |
| 1036   | No file              | `ccf7ddd0bac0`  |
| 1026   | No file              | `ccf7ddd0bac0`  |
| 1016   | No file              | `ccf7ddd0bac0`  |
| 1009   | No file              | `ccf7ddd0bac0`  |
| 1005   | No file              | `ccf7ddd0bac0`  |
| 1000   | No file              | `ccf7ddd0bac0`  |
| 998    | No file              | `ccf7ddd0bac0`  |
| 990    | No file              | `ccf7ddd0bac0`  |
| 979    | No file              | `ccf7ddd0bac0`  |
| 972    | No file              | `ccf7ddd0bac0`  |
| 963    | No file              | `ccf7ddd0bac0`  |
| 955    | No file              | `ccf7ddd0bac0`  |
| 946    | No file              | `ccf7ddd0bac0`  |
| 938    | No file              | `ccf7ddd0bac0`  |
| 927    | No file              | `ccf7ddd0bac0`  |
| 911    | No file              | `ccf7ddd0bac0`  |
| 904    | No file              | `ccf7ddd0bac0`  |
| 899    | No file              | `ccf7ddd0bac0`  |
| 894    | No file              | `ccf7ddd0bac0`  |
| 885    | No file              | `ccf7ddd0bac0`  |
| 879    | No file              | `ccf7ddd0bac0`  |
| 872    | No file              | `ccf7ddd0bac0`  |
| 864    | No file              | `ccf7ddd0bac0`  |
| 855    | No file              | `ccf7ddd0bac0`  |
| 853    | No file              | `ccf7ddd0bac0`  |
| 845    | No file              | `ccf7ddd0bac0`  |
| 837    | No file              | `ccf7ddd0bac0`  |
| 829    | No file              | `ccf7ddd0bac0`  |
| 822    | No file              | `ccf7ddd0bac0`  |
| 814    | No file              | `ccf7ddd0bac0`  |
| 805    | No file              | `ccf7ddd0bac0`  |
| 794    | No file              | `ccf7ddd0bac0`  |
| 787    | No file              | `ccf7ddd0bac0`  |
| 780    | No file              | `ccf7ddd0bac0`  |
| 771    | No file              | `ccf7ddd0bac0`  |
| 760    | No file              | `ccf7ddd0bac0`  |
| 748    | No file              | `ccf7ddd0bac0`  |
| 741    | No file              | `ccf7ddd0bac0`  |
| 736    | No file              | `ccf7ddd0bac0`  |
| 731    | No file              | `ccf7ddd0bac0`  |
| 723    | No file              | `ccf7ddd0bac0`  |
| 711    | No file              | `ccf7ddd0bac0`  |
| 707    | No file              | `ccf7ddd0bac0`  |
| 697    | No file              | `ccf7ddd0bac0`  |
| 689    | No file              | `ccf7ddd0bac0`  |
| 683    | No file              | `ccf7ddd0bac0`  |
| 678    | No file              | `ccf7ddd0bac0`  |
| 670    | No file              | `ccf7ddd0bac0`  |
| 661    | No file              | `ccf7ddd0bac0`  |
| 656    | No file              | `ccf7ddd0bac0`  |
| 652    | No file              | `ccf7ddd0bac0`  |
| 643    | No file              | `ccf7ddd0bac0`  |
| 637    | No file              | `ccf7ddd0bac0`  |
| 630    | No file              | `ccf7ddd0bac0`  |
| 627    | No file              | `ccf7ddd0bac0`  |
| 621    | No file              | `ccf7ddd0bac0`  |
| 617    | No file              | `ccf7ddd0bac0`  |
| 615    | No file              | `ccf7ddd0bac0`  |
| 606    | No file              | `ccf7ddd0bac0`  |
| 599    | No file              | `ccf7ddd0bac0`  |
| 592    | No file              | `ccf7ddd0bac0`  |
| 586    | No file              | `ccf7ddd0bac0`  |
| 577    | No file              | `ccf7ddd0bac0`  |
| 569    | No file              | `ccf7ddd0bac0`  |
| 561    | No file              | `ccf7ddd0bac0`  |
| 554    | No file              | `ccf7ddd0bac0`  |
| 542    | No file              | `ccf7ddd0bac0`  |
| 532    | No file              | `ccf7ddd0bac0`  |
| 531    | No file              | `ccf7ddd0bac0`  |
| 526    | No file              | `ccf7ddd0bac0`  |
| 521    | No file              | `ccf7ddd0bac0`  |
| 517    | No file              | `ccf7ddd0bac0`  |
| 510    | No file              | `ccf7ddd0bac0`  |
| 508    | No file              | `ccf7ddd0bac0`  |
| 504    | No file              | `ccf7ddd0bac0`  |
| 497    | No file              | `ccf7ddd0bac0`  |
| 491    | No file              | `ccf7ddd0bac0`  |
| 485    | No file              | `ccf7ddd0bac0`  |
| 478    | No file              | `ccf7ddd0bac0`  |
| 472    | No file              | `ccf7ddd0bac0`  |
| 466    | No file              | `ccf7ddd0bac0`  |
| 457    | No file              | `ccf7ddd0bac0`  |
| 452    | No file              | `ccf7ddd0bac0`  |
| 449    | No file              | `ccf7ddd0bac0`  |
| 435    | No file              | `ccf7ddd0bac0`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                    |
| --------------------- | -------- | ----------------------- |
| `languagedata_en.loc` | Optional | Item names (LOC type 0) |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset                      | Type                      | Field                | Notes                                                       |
| --------------------------- | ------------------------- | -------------------- | ----------------------------------------------------------- |
| `+0x00`                     | char[4]                   | magic                | ASCII `PABR`                                                |
| `+0x04`                     | u32                       | row_count            | Number of rows                                              |
| `+0x08`                     | Row[row_count]            | rows                 | See Row                                                     |
| `rows+0x00`                 | u32                       | track_count          | Number of `tracks`; equals `row_count` (clients 2107 to 3482) |
| `rows+0x04`                 | Reward Track[track_count] | tracks               | One per row, in row order; see Reward Track                 |
| `tracks+0x00`               | u32[..table_start]        | unknown_after_tracks | 0 bytes up to client 3002, 48 on 3251, 168 on 3482; see Open Questions |
| `unknown_after_tracks+0x00` | String Table              | string_table         | See String Table                                            |
| `EOF-0x08`                  | u32                       | table_start          | Offset of the string table                                  |
| `EOF-0x04`                  | u32                       | zero                 | Always `0`                                                  |

### Row (43 bytes)

| Offset  | Type | Field             | Notes                                                                                     |
| ------- | ---- | ----------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u16  | pass_key          | Row key, `1` to `31` on client 3482; `ToClient_GetCurrentSpecialPassKey()`                  |
| `+0x02` | u64  | start_time        | Unix seconds (UTC); the start date of the period text on 30 of 31 rows (client 3482)       |
| `+0x0A` | u64  | end_time          | Unix seconds (UTC); the end date of the period text on 30 of 31 rows                       |
| `+0x12` | u64  | sale_end_time     | Unix seconds (UTC), between the two; the end of the `패스 판매 기간` (pass sale) the description names, 31 of 31 |
| `+0x1A` | u32  | title_index       | String table index of the title (`스페셜 패스 - 솔라레 스페셜`); `ToClient_GetSpecialPassTitle` |
| `+0x1E` | u32  | period_index      | String table index of the period text (`2026년 4월 30일 ~ 2026년 5월 28일`); `ToClient_GetSpecialPassPeriod` |
| `+0x22` | u32  | description_index | String table index of the description; `ToClient_GetSpecialPassDesc`                       |
| `+0x26` | u32  | content_type      | `__eSpecialPassContentType_*`; see Content Types                                           |
| `+0x2A` | u8   | unknown_2a        | `0` on every row (clients 3002 to 3482)                                                    |

### Reward Track (variable: 4 bytes + steps)

| Offset  | Type             | Field      | Notes                                                        |
| ------- | ---------------- | ---------- | ------------------------------------------------------------ |
| `+0x00` | u32              | step_count | Number of `steps`; `14` on every track (clients 2107 to 3482) |
| `+0x04` | Step[step_count] | steps      | See Step                                                     |

### Step (34 bytes)

| Offset  | Type | Field            | Notes                                                                           |
| ------- | ---- | ---------------- | ------------------------------------------------------------------------------- |
| `+0x00` | u16  | pass_key         | The `pass_key` of the track's row, on every step                                |
| `+0x02` | u32  | basic_item_key   | Free reward, packed as `enchant_level << 24 \| item_id`; `ToClient_GetSpecialPassItemEnchantKey(key, false, i)` |
| `+0x06` | u64  | basic_item_count | Amount of `basic_item_key`; `ToClient_GetSpecialPassItemCount(key, false, i)`    |
| `+0x0E` | u32  | pass_item_key    | Reward of pass holders, packed the same way; `isPass` `true`                     |
| `+0x12` | u64  | pass_item_count  | Amount of `pass_item_key`                                                        |
| `+0x1A` | u64  | reward_point     | Pass Points that unlock the step, rising step by step; `ToClient_GetSpecialPassItemRewardPoint` |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                   |
| ------- | ------------------ | ------------ | --------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; 68 on client 3482    |
| `+0x04` | pstr[string_count] | strings      | UTF-16LE Korean texts the rows index    |

## Layout 1

### Row (42 bytes)

| Offset  | Type | Field             | Notes                                      |
| ------- | ---- | ----------------- | ------------------------------------------ |
| `+0x00` | u16  | pass_key          |                                            |
| `+0x02` | u64  | start_time        |                                            |
| `+0x0A` | u64  | end_time          |                                            |
| `+0x12` | u64  | sale_end_time     |                                            |
| `+0x1A` | u32  | title_index       |                                            |
| `+0x1E` | u32  | period_index      |                                            |
| `+0x22` | u32  | description_index |                                            |
| `+0x26` | u32  | unknown_26        | `0` on every row (clients 2107 to 2765)    |

### Step (26 bytes)

| Offset  | Type | Field            | Notes                              |
| ------- | ---- | ---------------- | ---------------------------------- |
| `+0x00` | u16  | pass_key         |                                    |
| `+0x02` | u32  | basic_item_key   |                                    |
| `+0x06` | u64  | basic_item_count |                                    |
| `+0x0E` | u32  | pass_item_key    |                                    |
| `+0x12` | u64  | pass_item_count  | No `reward_point`: a step is a day |

## Content Types

The Lua lists the five `__eSpecialPassContentType_*` values in this order
for the window's type buttons; the titles of the rows give the numbers
(client 3482):

| Value | Lua enum  | Title of the rows        | English (LOC type 0 pass item) | Rows |
| ----- | --------- | ------------------------ | ------------------------------ | ---- |
| 1     | `Daily`   | (스페셜 패스 -) 데일리 스페셜 | Daily Special Pass           | 21   |
| 2     | `Solare`  | 스페셜 패스 - 솔라레 스페셜  | Solare Special Pass            | 5    |
| 3     | `Monster` | 스페셜 패스 - 사냥 스페셜    | Combat Special Pass            | 3    |
| 4     | `Barter`  | 스페셜 패스 - 항해 스페셜    | Sailing Special Pass           | 1    |
| 5     | `Collect` | 스페셜 패스 - 채집 스페셜    | Gathering Special Pass         | 1    |

The Daily tracks count days (`reward_point` `1` to `14`), the others
Pass Points: `2` to `70` (Solare), `500` to `16000` (Combat), `10` to
`400` (Sailing) and `50` to `5000` (Gathering) on client 3482. The LOC
type 0 text of the Gathering pass item says "Earn Pass Points through
gathering activities", that of the Sailing pass "Earn Pass Points from
bartering".

## Field Names

The Special Pass is newer than client 1784: the file is not in its archives
and no sheet of a private server's `DataSheets.bexcel` on that client
covers it. The names follow the getters of
`panel_event_specialpass_all_1.luac` (client 3482); the free item is the
`isPass` `false` slot because every step's second item is the better one
(Black Friday Box I and II, a 7-day Value Pack and a Classic Outfit Box).
The three times are named by the texts the row indexes: the period text
holds the dates of `start_time` and `end_time`, and every description
ends with the pass sale period, whose last day is `sale_end_time` on all
31 rows. Pass 5 starts at 2023-08-22 21:01 UTC, the evening before its
text's 23 August; pass 16 ends a week after its text's 27 November 2025.

## Notes

- Client 2107 has 1 pass, 2519 has 9, 2765 has 12 (Layout 1); 3002 has
  15, 3251 has 18 and 3474 and 3482 have 31 (Layout 2). Client 3251
  is the first with a type other than Daily (one Solare pass).
- The handler (`_bss/specialpass/`) shows one row per step, in file order:
  the pass key, type, title, the three times, the step number, Pass
  Points, both reward items with their counts and the description.

## Open Questions

### What the u32 Values After the Tracks Hold

`unknown_after_tracks` grows with the content types in use. Client 3251
(Daily and Solare) holds `0 0 0 0 1 | 0 0 0 0 5 2 3`, client 3482 (all
five types) `0 0 0 0 0 0 0 1 | 0 0 0 0 0 0 0 5 2 3 | 0 0 0 0 0 0 0 1 |
0 0 0 0 0 0 0 1 | 0 0 0 0 0 0 0 1`: one group per type in value order,
each a run of zeros (4 on 3251, 7 on 3482) and a `1`, the Solare group
`5 2 3`. Pass Points per action (one per day, monster, barter or
gathering, and per Solare result) fit the values, but no Lua getter reads
them and the zero runs do not match a count in the file.

### What `unknown_2a` and Layout 1 `unknown_26` Hold

The u8 at the end of a Layout 2 row is `0` on all 31 rows; Layout 1 has a
u32 `0` where Layout 2 has `content_type`. Whether the old u32 is the
content type before Daily was numbered `1` is open.
