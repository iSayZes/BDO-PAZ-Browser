# `challengerewardlist.bss` Format

## Purpose

A sorted list of every item a challenge (the Rewards tab of the character
window, `panel_characterinfo_challenge_all`) hands out: one packed item key
(`enchant_level << 24 | item_id`) per entry, ascending, with no
repeats. The challenges themselves are in `challenge.dbss`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                      | Bytes | Records        | Row bytes |
| ------ | -------------- | ------- | ------------------------- | ----- | -------------- | --------- |
| 1      | 1333 and later | 3483    | `challengerewardlist.bss` | 3,564 | 1 String Table | 4         |

| Layout | File                      | Known            | Unknown    |
| ------ | ------------------------- | ---------------- | ---------- |
| 1      | `challengerewardlist.bss` | 3,564 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `fa2618d5b2a4`  |
| 3482   | Layout 1 | `fa2618d5b2a4`  |
| 3474   | Layout 1 | `fa2618d5b2a4`  |
| 3473   | Layout 1 | `fa2618d5b2a4`  |
| 3464   | Layout 1 | `fa2618d5b2a4`  |
| 3458   | Layout 1 | `fa2618d5b2a4`  |
| 3454   | Layout 1 | `fa2618d5b2a4`  |
| 3444   | Layout 1 | `fa2618d5b2a4`  |
| 3435   | Layout 1 | `fa2618d5b2a4`  |
| 3426   | Layout 1 | `fa2618d5b2a4`  |
| 3418   | Layout 1 | `fa2618d5b2a4`  |
| 3412   | Layout 1 | `fa2618d5b2a4`  |
| 3402   | Layout 1 | `fa2618d5b2a4`  |
| 3396   | Layout 1 | `fa2618d5b2a4`  |
| 3387   | Layout 1 | `fa2618d5b2a4`  |
| 3381   | Layout 1 | `fa2618d5b2a4`  |
| 3373   | Layout 1 | `fa2618d5b2a4`  |
| 3364   | Layout 1 | `fa2618d5b2a4`  |
| 3356   | Layout 1 | `fa2618d5b2a4`  |
| 3349   | Layout 1 | `fa2618d5b2a4`  |
| 3342   | Layout 1 | `fa2618d5b2a4`  |
| 3335   | Layout 1 | `fa2618d5b2a4`  |
| 3326   | Layout 1 | `fa2618d5b2a4`  |
| 3321   | Layout 1 | `fa2618d5b2a4`  |
| 3314   | Layout 1 | `fa2618d5b2a4`  |
| 3303   | Layout 1 | `fa2618d5b2a4`  |
| 3302   | Layout 1 | `fa2618d5b2a4`  |
| 3293   | Layout 1 | `fa2618d5b2a4`  |
| 3283   | Layout 1 | `fa2618d5b2a4`  |
| 3275   | Layout 1 | `fa2618d5b2a4`  |
| 3267   | Layout 1 | `fa2618d5b2a4`  |
| 3258   | Layout 1 | `fa2618d5b2a4`  |
| 3251   | Layout 1 | `fa2618d5b2a4`  |
| 3242   | Layout 1 | `fa2618d5b2a4`  |
| 3235   | Layout 1 | `fa2618d5b2a4`  |
| 3229   | Layout 1 | `fa2618d5b2a4`  |
| 3212   | Layout 1 | `fa2618d5b2a4`  |
| 3203   | Layout 1 | `fa2618d5b2a4`  |
| 3193   | Layout 1 | `fa2618d5b2a4`  |
| 3186   | Layout 1 | `fa2618d5b2a4`  |
| 3177   | Layout 1 | `fa2618d5b2a4`  |
| 3169   | Layout 1 | `fa2618d5b2a4`  |
| 3158   | Layout 1 | `fa2618d5b2a4`  |
| 3151   | Layout 1 | `fa2618d5b2a4`  |
| 3144   | Layout 1 | `fa2618d5b2a4`  |
| 3133   | Layout 1 | `fa2618d5b2a4`  |
| 3125   | Layout 1 | `fa2618d5b2a4`  |
| 3118   | Layout 1 | `fa2618d5b2a4`  |
| 3111   | Layout 1 | `fa2618d5b2a4`  |
| 3103   | Layout 1 | `fa2618d5b2a4`  |
| 3095   | Layout 1 | `fa2618d5b2a4`  |
| 3086   | Layout 1 | `fa2618d5b2a4`  |
| 3072   | Layout 1 | `fa2618d5b2a4`  |
| 3062   | Layout 1 | `fa2618d5b2a4`  |
| 3052   | Layout 1 | `fa2618d5b2a4`  |
| 3045   | Layout 1 | `fa2618d5b2a4`  |
| 3037   | Layout 1 | `fa2618d5b2a4`  |
| 3030   | Layout 1 | `fa2618d5b2a4`  |
| 3021   | Layout 1 | `fa2618d5b2a4`  |
| 3012   | Layout 1 | `fa2618d5b2a4`  |
| 3002   | Layout 1 | `fa2618d5b2a4`  |
| 2995   | Layout 1 | `fa2618d5b2a4`  |
| 2987   | Layout 1 | `fa2618d5b2a4`  |
| 2978   | Layout 1 | `fa2618d5b2a4`  |
| 2970   | Layout 1 | `fa2618d5b2a4`  |
| 2959   | Layout 1 | `fa2618d5b2a4`  |
| 2951   | Layout 1 | `fa2618d5b2a4`  |
| 2942   | Layout 1 | `fa2618d5b2a4`  |
| 2935   | Layout 1 | `fa2618d5b2a4`  |
| 2932   | Layout 1 | `fa2618d5b2a4`  |
| 2923   | Layout 1 | `fa2618d5b2a4`  |
| 2919   | Layout 1 | `fa2618d5b2a4`  |
| 2907   | Layout 1 | `fa2618d5b2a4`  |
| 2900   | Layout 1 | `fa2618d5b2a4`  |
| 2891   | Layout 1 | `fa2618d5b2a4`  |
| 2882   | Layout 1 | `fa2618d5b2a4`  |
| 2872   | Layout 1 | `fa2618d5b2a4`  |
| 2863   | Layout 1 | `fa2618d5b2a4`  |
| 2855   | Layout 1 | `fa2618d5b2a4`  |
| 2849   | Layout 1 | `fa2618d5b2a4`  |
| 2844   | Layout 1 | `fa2618d5b2a4`  |
| 2834   | Layout 1 | `fa2618d5b2a4`  |
| 2825   | Layout 1 | `fa2618d5b2a4`  |
| 2819   | Layout 1 | `fa2618d5b2a4`  |
| 2811   | Layout 1 | `fa2618d5b2a4`  |
| 2803   | Layout 1 | `fa2618d5b2a4`  |
| 2794   | Layout 1 | `fa2618d5b2a4`  |
| 2783   | Layout 1 | `fa2618d5b2a4`  |
| 2774   | Layout 1 | `fa2618d5b2a4`  |
| 2765   | Layout 1 | `fa2618d5b2a4`  |
| 2756   | Layout 1 | `fa2618d5b2a4`  |
| 2750   | Layout 1 | `fa2618d5b2a4`  |
| 2743   | Layout 1 | `fa2618d5b2a4`  |
| 2736   | Layout 1 | `fa2618d5b2a4`  |
| 2726   | Layout 1 | `fa2618d5b2a4`  |
| 2717   | Layout 1 | `fa2618d5b2a4`  |
| 2709   | Layout 1 | `fa2618d5b2a4`  |
| 2703   | Layout 1 | `fa2618d5b2a4`  |
| 2695   | Layout 1 | `fa2618d5b2a4`  |
| 2684   | Layout 1 | `fa2618d5b2a4`  |
| 2672   | Layout 1 | `fa2618d5b2a4`  |
| 2665   | Layout 1 | `fa2618d5b2a4`  |
| 2657   | Layout 1 | `fa2618d5b2a4`  |
| 2649   | Layout 1 | `fa2618d5b2a4`  |
| 2644   | Layout 1 | `fa2618d5b2a4`  |
| 2637   | Layout 1 | `fa2618d5b2a4`  |
| 2629   | Layout 1 | `fa2618d5b2a4`  |
| 2619   | Layout 1 | `fa2618d5b2a4`  |
| 2612   | Layout 1 | `fa2618d5b2a4`  |
| 2606   | Layout 1 | `fa2618d5b2a4`  |
| 2602   | Layout 1 | `fa2618d5b2a4`  |
| 2601   | Layout 1 | `fa2618d5b2a4`  |
| 2592   | Layout 1 | `fa2618d5b2a4`  |
| 2583   | Layout 1 | `fa2618d5b2a4`  |
| 2575   | Layout 1 | `fa2618d5b2a4`  |
| 2567   | Layout 1 | `fa2618d5b2a4`  |
| 2560   | Layout 1 | `fa2618d5b2a4`  |
| 2553   | Layout 1 | `fa2618d5b2a4`  |
| 2545   | Layout 1 | `fa2618d5b2a4`  |
| 2538   | Layout 1 | `fa2618d5b2a4`  |
| 2529   | Layout 1 | `fa2618d5b2a4`  |
| 2519   | Layout 1 | `fa2618d5b2a4`  |
| 2513   | Layout 1 | `fa2618d5b2a4`  |
| 2510   | Layout 1 | `fa2618d5b2a4`  |
| 2507   | Layout 1 | `fa2618d5b2a4`  |
| 2503   | Layout 1 | `fa2618d5b2a4`  |
| 2498   | Layout 1 | `fa2618d5b2a4`  |
| 2492   | Layout 1 | `fa2618d5b2a4`  |
| 2487   | Layout 1 | `fa2618d5b2a4`  |
| 2480   | Layout 1 | `fa2618d5b2a4`  |
| 2474   | Layout 1 | `fa2618d5b2a4`  |
| 2468   | Layout 1 | `fa2618d5b2a4`  |
| 2460   | Layout 1 | `fa2618d5b2a4`  |
| 2453   | Layout 1 | `fa2618d5b2a4`  |
| 2444   | Layout 1 | `fa2618d5b2a4`  |
| 2438   | Layout 1 | `fa2618d5b2a4`  |
| 2434   | Layout 1 | `fa2618d5b2a4`  |
| 2429   | Layout 1 | `fa2618d5b2a4`  |
| 2421   | Layout 1 | `fa2618d5b2a4`  |
| 2414   | Layout 1 | `fa2618d5b2a4`  |
| 2407   | Layout 1 | `fa2618d5b2a4`  |
| 2401   | Layout 1 | `fa2618d5b2a4`  |
| 2397   | Layout 1 | `fa2618d5b2a4`  |
| 2393   | Layout 1 | `fa2618d5b2a4`  |
| 2384   | Layout 1 | `fa2618d5b2a4`  |
| 2378   | Layout 1 | `fa2618d5b2a4`  |
| 2372   | Layout 1 | `fa2618d5b2a4`  |
| 2358   | Layout 1 | `fa2618d5b2a4`  |
| 2352   | Layout 1 | `fa2618d5b2a4`  |
| 2347   | Layout 1 | `fa2618d5b2a4`  |
| 2343   | Layout 1 | `fa2618d5b2a4`  |
| 2335   | Layout 1 | `fa2618d5b2a4`  |
| 2327   | Layout 1 | `fa2618d5b2a4`  |
| 2324   | Layout 1 | `fa2618d5b2a4`  |
| 2319   | Layout 1 | `fa2618d5b2a4`  |
| 2313   | Layout 1 | `fa2618d5b2a4`  |
| 2308   | Layout 1 | `fa2618d5b2a4`  |
| 2302   | Layout 1 | `fa2618d5b2a4`  |
| 2295   | Layout 1 | `fa2618d5b2a4`  |
| 2290   | Layout 1 | `fa2618d5b2a4`  |
| 2284   | Layout 1 | `fa2618d5b2a4`  |
| 2276   | Layout 1 | `fa2618d5b2a4`  |
| 2269   | Layout 1 | `fa2618d5b2a4`  |
| 2259   | Layout 1 | `fa2618d5b2a4`  |
| 2250   | Layout 1 | `fa2618d5b2a4`  |
| 2243   | Layout 1 | `fa2618d5b2a4`  |
| 2235   | Layout 1 | `fa2618d5b2a4`  |
| 2229   | Layout 1 | `fa2618d5b2a4`  |
| 2224   | Layout 1 | `fa2618d5b2a4`  |
| 2218   | Layout 1 | `fa2618d5b2a4`  |
| 2215   | Layout 1 | `fa2618d5b2a4`  |
| 2207   | Layout 1 | `fa2618d5b2a4`  |
| 2203   | Layout 1 | `fa2618d5b2a4`  |
| 2196   | Layout 1 | `fa2618d5b2a4`  |
| 2192   | Layout 1 | `fa2618d5b2a4`  |
| 2189   | Layout 1 | `fa2618d5b2a4`  |
| 2183   | Layout 1 | `fa2618d5b2a4`  |
| 2179   | Layout 1 | `fa2618d5b2a4`  |
| 2171   | Layout 1 | `fa2618d5b2a4`  |
| 2163   | Layout 1 | `fa2618d5b2a4`  |
| 2156   | Layout 1 | `fa2618d5b2a4`  |
| 2151   | Layout 1 | `fa2618d5b2a4`  |
| 2147   | Layout 1 | `fa2618d5b2a4`  |
| 2142   | Layout 1 | `fa2618d5b2a4`  |
| 2138   | Layout 1 | `fa2618d5b2a4`  |
| 2134   | Layout 1 | `fa2618d5b2a4`  |
| 2130   | Layout 1 | `fa2618d5b2a4`  |
| 2122   | Layout 1 | `fa2618d5b2a4`  |
| 2107   | Layout 1 | `fa2618d5b2a4`  |
| 2098   | Layout 1 | `fa2618d5b2a4`  |
| 2089   | Layout 1 | `fa2618d5b2a4`  |
| 2081   | Layout 1 | `fa2618d5b2a4`  |
| 2073   | Layout 1 | `fa2618d5b2a4`  |
| 2067   | Layout 1 | `fa2618d5b2a4`  |
| 2063   | Layout 1 | `fa2618d5b2a4`  |
| 2059   | Layout 1 | `fa2618d5b2a4`  |
| 2052   | Layout 1 | `fa2618d5b2a4`  |
| 2044   | Layout 1 | `fa2618d5b2a4`  |
| 2039   | Layout 1 | `fa2618d5b2a4`  |
| 2032   | Layout 1 | `fa2618d5b2a4`  |
| 2025   | Layout 1 | `fa2618d5b2a4`  |
| 2011   | Layout 1 | `fa2618d5b2a4`  |
| 2005   | Layout 1 | `fa2618d5b2a4`  |
| 2000   | Layout 1 | `fa2618d5b2a4`  |
| 1996   | Layout 1 | `fa2618d5b2a4`  |
| 1991   | Layout 1 | `fa2618d5b2a4`  |
| 1985   | Layout 1 | `fa2618d5b2a4`  |
| 1980   | Layout 1 | `fa2618d5b2a4`  |
| 1969   | Layout 1 | `fa2618d5b2a4`  |
| 1964   | Layout 1 | `fa2618d5b2a4`  |
| 1958   | Layout 1 | `fa2618d5b2a4`  |
| 1950   | Layout 1 | `fa2618d5b2a4`  |
| 1945   | Layout 1 | `fa2618d5b2a4`  |
| 1937   | Layout 1 | `fa2618d5b2a4`  |
| 1933   | Layout 1 | `fa2618d5b2a4`  |
| 1927   | Layout 1 | `fa2618d5b2a4`  |
| 1921   | Layout 1 | `fa2618d5b2a4`  |
| 1914   | Layout 1 | `fa2618d5b2a4`  |
| 1908   | Layout 1 | `fa2618d5b2a4`  |
| 1897   | Layout 1 | `fa2618d5b2a4`  |
| 1892   | Layout 1 | `fa2618d5b2a4`  |
| 1886   | Layout 1 | `fa2618d5b2a4`  |
| 1881   | Layout 1 | `fa2618d5b2a4`  |
| 1871   | Layout 1 | `fa2618d5b2a4`  |
| 1866   | Layout 1 | `fa2618d5b2a4`  |
| 1862   | Layout 1 | `fa2618d5b2a4`  |
| 1854   | Layout 1 | `fa2618d5b2a4`  |
| 1846   | Layout 1 | `fa2618d5b2a4`  |
| 1838   | Layout 1 | `fa2618d5b2a4`  |
| 1832   | Layout 1 | `fa2618d5b2a4`  |
| 1826   | Layout 1 | `fa2618d5b2a4`  |
| 1822   | Layout 1 | `fa2618d5b2a4`  |
| 1818   | Layout 1 | `fa2618d5b2a4`  |
| 1804   | Layout 1 | `fa2618d5b2a4`  |
| 1794   | Layout 1 | `fa2618d5b2a4`  |
| 1790   | Layout 1 | `fa2618d5b2a4`  |
| 1784   | Layout 1 | `fa2618d5b2a4`  |
| 1774   | Layout 1 | `fa2618d5b2a4`  |
| 1771   | Layout 1 | `fa2618d5b2a4`  |
| 1762   | Layout 1 | `fa2618d5b2a4`  |
| 1759   | Layout 1 | `fa2618d5b2a4`  |
| 1754   | Layout 1 | `fa2618d5b2a4`  |
| 1749   | Layout 1 | `fa2618d5b2a4`  |
| 1743   | Layout 1 | `fa2618d5b2a4`  |
| 1737   | Layout 1 | `fa2618d5b2a4`  |
| 1731   | Layout 1 | `fa2618d5b2a4`  |
| 1725   | Layout 1 | `fa2618d5b2a4`  |
| 1717   | Layout 1 | `fa2618d5b2a4`  |
| 1710   | Layout 1 | `fa2618d5b2a4`  |
| 1704   | Layout 1 | `fa2618d5b2a4`  |
| 1698   | Layout 1 | `fa2618d5b2a4`  |
| 1690   | Layout 1 | `fa2618d5b2a4`  |
| 1685   | Layout 1 | `fa2618d5b2a4`  |
| 1680   | Layout 1 | `fa2618d5b2a4`  |
| 1674   | Layout 1 | `fa2618d5b2a4`  |
| 1668   | Layout 1 | `fa2618d5b2a4`  |
| 1659   | Layout 1 | `fa2618d5b2a4`  |
| 1649   | Layout 1 | `fa2618d5b2a4`  |
| 1642   | Layout 1 | `fa2618d5b2a4`  |
| 1636   | Layout 1 | `fa2618d5b2a4`  |
| 1628   | Layout 1 | `fa2618d5b2a4`  |
| 1622   | Layout 1 | `fa2618d5b2a4`  |
| 1614   | Layout 1 | `fa2618d5b2a4`  |
| 1608   | Layout 1 | `fa2618d5b2a4`  |
| 1602   | Layout 1 | `fa2618d5b2a4`  |
| 1598   | Layout 1 | `fa2618d5b2a4`  |
| 1594   | Layout 1 | `fa2618d5b2a4`  |
| 1590   | Layout 1 | `fa2618d5b2a4`  |
| 1587   | Layout 1 | `fa2618d5b2a4`  |
| 1584   | Layout 1 | `fa2618d5b2a4`  |
| 1579   | Layout 1 | `fa2618d5b2a4`  |
| 1572   | Layout 1 | `fa2618d5b2a4`  |
| 1565   | Layout 1 | `fa2618d5b2a4`  |
| 1559   | Layout 1 | `fa2618d5b2a4`  |
| 1554   | Layout 1 | `fa2618d5b2a4`  |
| 1547   | Layout 1 | `fa2618d5b2a4`  |
| 1537   | Layout 1 | `fa2618d5b2a4`  |
| 1529   | Layout 1 | `fa2618d5b2a4`  |
| 1524   | Layout 1 | `fa2618d5b2a4`  |
| 1519   | Layout 1 | `fa2618d5b2a4`  |
| 1509   | Layout 1 | `fa2618d5b2a4`  |
| 1506   | Layout 1 | `fa2618d5b2a4`  |
| 1504   | Layout 1 | `fa2618d5b2a4`  |
| 1500   | Layout 1 | `fa2618d5b2a4`  |
| 1493   | Layout 1 | `fa2618d5b2a4`  |
| 1489   | Layout 1 | `fa2618d5b2a4`  |
| 1485   | Layout 1 | `fa2618d5b2a4`  |
| 1481   | Layout 1 | `fa2618d5b2a4`  |
| 1474   | Layout 1 | `fa2618d5b2a4`  |
| 1466   | Layout 1 | `fa2618d5b2a4`  |
| 1462   | Layout 1 | `fa2618d5b2a4`  |
| 1459   | Layout 1 | `fa2618d5b2a4`  |
| 1453   | Layout 1 | `fa2618d5b2a4`  |
| 1450   | Layout 1 | `fa2618d5b2a4`  |
| 1445   | Layout 1 | `fa2618d5b2a4`  |
| 1439   | Layout 1 | `fa2618d5b2a4`  |
| 1433   | Layout 1 | `fa2618d5b2a4`  |
| 1430   | Layout 1 | `fa2618d5b2a4`  |
| 1426   | Layout 1 | `fa2618d5b2a4`  |
| 1421   | Layout 1 | `fa2618d5b2a4`  |
| 1417   | Layout 1 | `fa2618d5b2a4`  |
| 1416   | Layout 1 | `fa2618d5b2a4`  |
| 1409   | Layout 1 | `fa2618d5b2a4`  |
| 1405   | Layout 1 | `fa2618d5b2a4`  |
| 1401   | Layout 1 | `fa2618d5b2a4`  |
| 1396   | Layout 1 | `fa2618d5b2a4`  |
| 1391   | Layout 1 | `fa2618d5b2a4`  |
| 1390   | Layout 1 | `fa2618d5b2a4`  |
| 1386   | Layout 1 | `fa2618d5b2a4`  |
| 1381   | Layout 1 | `fa2618d5b2a4`  |
| 1379   | Layout 1 | `fa2618d5b2a4`  |
| 1372   | Layout 1 | `fa2618d5b2a4`  |
| 1366   | Layout 1 | `fa2618d5b2a4`  |
| 1364   | Layout 1 | `fa2618d5b2a4`  |
| 1363   | Layout 1 | `fa2618d5b2a4`  |
| 1360   | Layout 1 | `fa2618d5b2a4`  |
| 1358   | Layout 1 | `fa2618d5b2a4`  |
| 1355   | Layout 1 | `fa2618d5b2a4`  |
| 1351   | Layout 1 | `fa2618d5b2a4`  |
| 1348   | Layout 1 | `fa2618d5b2a4`  |
| 1346   | Layout 1 | `fa2618d5b2a4`  |
| 1341   | Layout 1 | `fa2618d5b2a4`  |
| 1340   | Layout 1 | `fa2618d5b2a4`  |
| 1338   | Layout 1 | `fa2618d5b2a4`  |
| 1335   | Layout 1 | `fa2618d5b2a4`  |
| 1333   | Layout 1 | `fa2618d5b2a4`  |
| 1329   | No file  | `fa2618d5b2a4`  |
| 1327   | No file  | `fa2618d5b2a4`  |
| 1324   | No file  | `fa2618d5b2a4`  |
| 1321   | No file  | `fa2618d5b2a4`  |
| 1319   | No file  | `fa2618d5b2a4`  |
| 1318   | No file  | `fa2618d5b2a4`  |
| 1316   | No file  | `fa2618d5b2a4`  |
| 1313   | No file  | `fa2618d5b2a4`  |
| 1311   | No file  | `fa2618d5b2a4`  |
| 1309   | No file  | `fa2618d5b2a4`  |
| 1304   | No file  | `fa2618d5b2a4`  |
| 1292   | No file  | `fa2618d5b2a4`  |
| 1286   | No file  | `fa2618d5b2a4`  |
| 1280   | No file  | `fa2618d5b2a4`  |
| 1276   | No file  | `fa2618d5b2a4`  |
| 1267   | No file  | `fa2618d5b2a4`  |
| 1261   | No file  | `fa2618d5b2a4`  |
| 1256   | No file  | `fa2618d5b2a4`  |
| 1250   | No file  | `fa2618d5b2a4`  |
| 1246   | No file  | `fa2618d5b2a4`  |
| 1239   | No file  | `fa2618d5b2a4`  |
| 1230   | No file  | `fa2618d5b2a4`  |
| 1226   | No file  | `fa2618d5b2a4`  |
| 1220   | No file  | `fa2618d5b2a4`  |
| 1217   | No file  | `fa2618d5b2a4`  |
| 1211   | No file  | `fa2618d5b2a4`  |
| 1210   | No file  | `fa2618d5b2a4`  |
| 1208   | No file  | `fa2618d5b2a4`  |
| 1203   | No file  | `fa2618d5b2a4`  |
| 1197   | No file  | `fa2618d5b2a4`  |
| 1194   | No file  | `fa2618d5b2a4`  |
| 1192   | No file  | `fa2618d5b2a4`  |
| 1187   | No file  | `fa2618d5b2a4`  |
| 1183   | No file  | `fa2618d5b2a4`  |
| 1177   | No file  | `fa2618d5b2a4`  |
| 1173   | No file  | `fa2618d5b2a4`  |
| 1167   | No file  | `fa2618d5b2a4`  |
| 1164   | No file  | `fa2618d5b2a4`  |
| 1156   | No file  | `fa2618d5b2a4`  |
| 1149   | No file  | `fa2618d5b2a4`  |
| 1144   | No file  | `fa2618d5b2a4`  |
| 1137   | No file  | `fa2618d5b2a4`  |
| 1132   | No file  | `fa2618d5b2a4`  |
| 1127   | No file  | `fa2618d5b2a4`  |
| 1122   | No file  | `fa2618d5b2a4`  |
| 1118   | No file  | `fa2618d5b2a4`  |
| 1114   | No file  | `fa2618d5b2a4`  |
| 1109   | No file  | `fa2618d5b2a4`  |
| 1102   | No file  | `fa2618d5b2a4`  |
| 1096   | No file  | `fa2618d5b2a4`  |
| 1088   | No file  | `fa2618d5b2a4`  |
| 1081   | No file  | `fa2618d5b2a4`  |
| 1076   | No file  | `fa2618d5b2a4`  |
| 1069   | No file  | `fa2618d5b2a4`  |
| 1064   | No file  | `fa2618d5b2a4`  |
| 1058   | No file  | `fa2618d5b2a4`  |
| 1051   | No file  | `fa2618d5b2a4`  |
| 1044   | No file  | `fa2618d5b2a4`  |
| 1036   | No file  | `fa2618d5b2a4`  |
| 1026   | No file  | `fa2618d5b2a4`  |
| 1016   | No file  | `fa2618d5b2a4`  |
| 1009   | No file  | `fa2618d5b2a4`  |
| 1005   | No file  | `fa2618d5b2a4`  |
| 1000   | No file  | `fa2618d5b2a4`  |
| 998    | No file  | `fa2618d5b2a4`  |
| 990    | No file  | `fa2618d5b2a4`  |
| 979    | No file  | `fa2618d5b2a4`  |
| 972    | No file  | `fa2618d5b2a4`  |
| 963    | No file  | `fa2618d5b2a4`  |
| 955    | No file  | `fa2618d5b2a4`  |
| 946    | No file  | `fa2618d5b2a4`  |
| 938    | No file  | `fa2618d5b2a4`  |
| 927    | No file  | `fa2618d5b2a4`  |
| 911    | No file  | `fa2618d5b2a4`  |
| 904    | No file  | `fa2618d5b2a4`  |
| 899    | No file  | `fa2618d5b2a4`  |
| 894    | No file  | `fa2618d5b2a4`  |
| 885    | No file  | `fa2618d5b2a4`  |
| 879    | No file  | `fa2618d5b2a4`  |
| 872    | No file  | `fa2618d5b2a4`  |
| 864    | No file  | `fa2618d5b2a4`  |
| 855    | No file  | `fa2618d5b2a4`  |
| 853    | No file  | `fa2618d5b2a4`  |
| 845    | No file  | `fa2618d5b2a4`  |
| 837    | No file  | `fa2618d5b2a4`  |
| 829    | No file  | `fa2618d5b2a4`  |
| 822    | No file  | `fa2618d5b2a4`  |
| 814    | No file  | `fa2618d5b2a4`  |
| 805    | No file  | `fa2618d5b2a4`  |
| 794    | No file  | `fa2618d5b2a4`  |
| 787    | No file  | `fa2618d5b2a4`  |
| 780    | No file  | `fa2618d5b2a4`  |
| 771    | No file  | `fa2618d5b2a4`  |
| 760    | No file  | `fa2618d5b2a4`  |
| 748    | No file  | `fa2618d5b2a4`  |
| 741    | No file  | `fa2618d5b2a4`  |
| 736    | No file  | `fa2618d5b2a4`  |
| 731    | No file  | `fa2618d5b2a4`  |
| 723    | No file  | `fa2618d5b2a4`  |
| 711    | No file  | `fa2618d5b2a4`  |
| 707    | No file  | `fa2618d5b2a4`  |
| 697    | No file  | `fa2618d5b2a4`  |
| 689    | No file  | `fa2618d5b2a4`  |
| 683    | No file  | `fa2618d5b2a4`  |
| 678    | No file  | `fa2618d5b2a4`  |
| 670    | No file  | `fa2618d5b2a4`  |
| 661    | No file  | `fa2618d5b2a4`  |
| 656    | No file  | `fa2618d5b2a4`  |
| 652    | No file  | `fa2618d5b2a4`  |
| 643    | No file  | `fa2618d5b2a4`  |
| 637    | No file  | `fa2618d5b2a4`  |
| 630    | No file  | `fa2618d5b2a4`  |
| 627    | No file  | `fa2618d5b2a4`  |
| 621    | No file  | `fa2618d5b2a4`  |
| 617    | No file  | `fa2618d5b2a4`  |
| 615    | No file  | `fa2618d5b2a4`  |
| 606    | No file  | `fa2618d5b2a4`  |
| 599    | No file  | `fa2618d5b2a4`  |
| 592    | No file  | `fa2618d5b2a4`  |
| 586    | No file  | `fa2618d5b2a4`  |
| 577    | No file  | `fa2618d5b2a4`  |
| 569    | No file  | `fa2618d5b2a4`  |
| 561    | No file  | `fa2618d5b2a4`  |
| 554    | No file  | `fa2618d5b2a4`  |
| 542    | No file  | `fa2618d5b2a4`  |
| 532    | No file  | `fa2618d5b2a4`  |
| 531    | No file  | `fa2618d5b2a4`  |
| 526    | No file  | `fa2618d5b2a4`  |
| 521    | No file  | `fa2618d5b2a4`  |
| 517    | No file  | `fa2618d5b2a4`  |
| 510    | No file  | `fa2618d5b2a4`  |
| 508    | No file  | `fa2618d5b2a4`  |
| 504    | No file  | `fa2618d5b2a4`  |
| 497    | No file  | `fa2618d5b2a4`  |
| 491    | No file  | `fa2618d5b2a4`  |
| 485    | No file  | `fa2618d5b2a4`  |
| 478    | No file  | `fa2618d5b2a4`  |
| 472    | No file  | `fa2618d5b2a4`  |
| 466    | No file  | `fa2618d5b2a4`  |
| 457    | No file  | `fa2618d5b2a4`  |
| 452    | No file  | `fa2618d5b2a4`  |
| 449    | No file  | `fa2618d5b2a4`  |
| 435    | No file  | `fa2618d5b2a4`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                    |
| --------------------- | -------- | ----------------------- |
| `languagedata_en.loc` | Optional | Item names (LOC type 0) |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset             | Type             | Field        | Notes                                              |
| ------------------ | ---------------- | ------------ | -------------------------------------------------- |
| `+0x00`            | char[4]          | magic        | ASCII `PABR`                                       |
| `+0x04`            | u32              | item_count   | Number of `item_keys`                              |
| `+0x08`            | u32[item_count]  | item_keys    | Packed item keys, ascending; the first is `0`      |
| `item_keys+0x00`   | String Table     | string_table | See String Table                                   |
| `EOF-0x08`         | u32              | table_start  | Offset of the string table, where `item_keys` ends |
| `EOF-0x04`         | u32              | zero         | Always `0`                                         |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The keys are the reward items of the challenges: the `BaseReward` and
`SelectReward` columns (`item(7,0,100);`, item, level, count) of the
`Challenge_Table` sheet of a private server's `DataSheets.bexcel` on client
1784 hold 655 item keys, and 652 of the 653 keys of that client's file are
among them. The one left over is `0`; three sheet keys (`18461`, `50142`,
`750022`) are not in the file. The `WorldChallenge_Table` of a private
server on client 519 has the challenge columns (`Key`, `BaseReward`,
`SelectReward`): it is the twin of `challenge.dbss`, and this file is
derived from its rewards.

## Notes

- On client 3482 the 886 keys hold 885 items (one key is `0`); the
  highest keys are the four Capotia accessories at level 3 (`50343893`
  is Capotia Belt (3)). Client 1784 holds 653 keys, including Tuvala Earring
  at level 5 (`84580190`), which client 3482 no longer lists.
- No Lua function of client 3482 names the file; the challenge window
  reads its rewards through `ToClient_GetChallengeRewardInfoWrapper()`.
- The handler (`_bss/challengerewardlist/`) shows one row per key with
  its item ID, level and the item's icon and name.
