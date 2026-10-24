# `siege2024revivepositionstaticstatus.bss` Format

## Purpose

Where Node War (the 2024 land siege) players can revive, per territory:
each row holds a territory key and up to three world positions, each
with an f32. On client 3482 the 8 rows cover Balenos, Serendia,
Calpheon, Ulukita, Mediah, Outer Edania, Valencia and Kamasylvia, in
that order, with 21 positions. The death window offers one revive
button per position of the player's territory.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                                      | Bytes | Records            | Row bytes |
| ------ | -------------- | ------- | ----------------------------------------- | ----- | ------------------ | --------- |
| 1      | 2519 and later | 3483    | `siege2024revivepositionstaticstatus.bss` | 404   | 21 Position, 8 Row | 16        |

| Layout | File                                      | Known         | Unknown      |
| ------ | ----------------------------------------- | ------------- | ------------ |
| 1      | `siege2024revivepositionstaticstatus.bss` | 320 B (79.2%) | 84 B (20.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `d9e3c0e63c72`  |
| 3482   | Layout 1 | `d9e3c0e63c72`  |
| 3474   | Layout 1 | `d9e3c0e63c72`  |
| 3473   | Layout 1 | `d9e3c0e63c72`  |
| 3464   | Layout 1 | `d9e3c0e63c72`  |
| 3458   | Layout 1 | `d9e3c0e63c72`  |
| 3454   | Layout 1 | `d9e3c0e63c72`  |
| 3444   | Layout 1 | `d9e3c0e63c72`  |
| 3435   | Layout 1 | `d9e3c0e63c72`  |
| 3426   | Layout 1 | `d9e3c0e63c72`  |
| 3418   | Layout 1 | `d9e3c0e63c72`  |
| 3412   | Layout 1 | `d9e3c0e63c72`  |
| 3402   | Layout 1 | `d9e3c0e63c72`  |
| 3396   | Layout 1 | `d9e3c0e63c72`  |
| 3387   | Layout 1 | `d9e3c0e63c72`  |
| 3381   | Layout 1 | `d9e3c0e63c72`  |
| 3373   | Layout 1 | `d9e3c0e63c72`  |
| 3364   | Layout 1 | `d9e3c0e63c72`  |
| 3356   | Layout 1 | `d9e3c0e63c72`  |
| 3349   | Layout 1 | `d9e3c0e63c72`  |
| 3342   | Layout 1 | `d9e3c0e63c72`  |
| 3335   | Layout 1 | `d9e3c0e63c72`  |
| 3326   | Layout 1 | `d9e3c0e63c72`  |
| 3321   | Layout 1 | `d9e3c0e63c72`  |
| 3314   | Layout 1 | `d9e3c0e63c72`  |
| 3303   | Layout 1 | `d9e3c0e63c72`  |
| 3302   | Layout 1 | `d9e3c0e63c72`  |
| 3293   | Layout 1 | `d9e3c0e63c72`  |
| 3283   | Layout 1 | `d9e3c0e63c72`  |
| 3275   | Layout 1 | `d9e3c0e63c72`  |
| 3267   | Layout 1 | `d9e3c0e63c72`  |
| 3258   | Layout 1 | `d9e3c0e63c72`  |
| 3251   | Layout 1 | `d9e3c0e63c72`  |
| 3242   | Layout 1 | `d9e3c0e63c72`  |
| 3235   | Layout 1 | `d9e3c0e63c72`  |
| 3229   | Layout 1 | `d9e3c0e63c72`  |
| 3212   | Layout 1 | `d9e3c0e63c72`  |
| 3203   | Layout 1 | `d9e3c0e63c72`  |
| 3193   | Layout 1 | `d9e3c0e63c72`  |
| 3186   | Layout 1 | `d9e3c0e63c72`  |
| 3177   | Layout 1 | `d9e3c0e63c72`  |
| 3169   | Layout 1 | `d9e3c0e63c72`  |
| 3158   | Layout 1 | `d9e3c0e63c72`  |
| 3151   | Layout 1 | `d9e3c0e63c72`  |
| 3144   | Layout 1 | `d9e3c0e63c72`  |
| 3133   | Layout 1 | `d9e3c0e63c72`  |
| 3125   | Layout 1 | `d9e3c0e63c72`  |
| 3118   | Layout 1 | `d9e3c0e63c72`  |
| 3111   | Layout 1 | `d9e3c0e63c72`  |
| 3103   | Layout 1 | `d9e3c0e63c72`  |
| 3095   | Layout 1 | `d9e3c0e63c72`  |
| 3086   | Layout 1 | `d9e3c0e63c72`  |
| 3072   | Layout 1 | `d9e3c0e63c72`  |
| 3062   | Layout 1 | `d9e3c0e63c72`  |
| 3052   | Layout 1 | `d9e3c0e63c72`  |
| 3045   | Layout 1 | `d9e3c0e63c72`  |
| 3037   | Layout 1 | `d9e3c0e63c72`  |
| 3030   | Layout 1 | `d9e3c0e63c72`  |
| 3021   | Layout 1 | `d9e3c0e63c72`  |
| 3012   | Layout 1 | `d9e3c0e63c72`  |
| 3002   | Layout 1 | `d9e3c0e63c72`  |
| 2995   | Layout 1 | `d9e3c0e63c72`  |
| 2987   | Layout 1 | `d9e3c0e63c72`  |
| 2978   | Layout 1 | `d9e3c0e63c72`  |
| 2970   | Layout 1 | `d9e3c0e63c72`  |
| 2959   | Layout 1 | `d9e3c0e63c72`  |
| 2951   | Layout 1 | `d9e3c0e63c72`  |
| 2942   | Layout 1 | `d9e3c0e63c72`  |
| 2935   | Layout 1 | `d9e3c0e63c72`  |
| 2932   | Layout 1 | `d9e3c0e63c72`  |
| 2923   | Layout 1 | `d9e3c0e63c72`  |
| 2919   | Layout 1 | `d9e3c0e63c72`  |
| 2907   | Layout 1 | `d9e3c0e63c72`  |
| 2900   | Layout 1 | `d9e3c0e63c72`  |
| 2891   | Layout 1 | `d9e3c0e63c72`  |
| 2882   | Layout 1 | `d9e3c0e63c72`  |
| 2872   | Layout 1 | `d9e3c0e63c72`  |
| 2863   | Layout 1 | `d9e3c0e63c72`  |
| 2855   | Layout 1 | `d9e3c0e63c72`  |
| 2849   | Layout 1 | `d9e3c0e63c72`  |
| 2844   | Layout 1 | `d9e3c0e63c72`  |
| 2834   | Layout 1 | `d9e3c0e63c72`  |
| 2825   | Layout 1 | `d9e3c0e63c72`  |
| 2819   | Layout 1 | `d9e3c0e63c72`  |
| 2811   | Layout 1 | `d9e3c0e63c72`  |
| 2803   | Layout 1 | `d9e3c0e63c72`  |
| 2794   | Layout 1 | `d9e3c0e63c72`  |
| 2783   | Layout 1 | `d9e3c0e63c72`  |
| 2774   | Layout 1 | `d9e3c0e63c72`  |
| 2765   | Layout 1 | `d9e3c0e63c72`  |
| 2756   | Layout 1 | `d9e3c0e63c72`  |
| 2750   | Layout 1 | `d9e3c0e63c72`  |
| 2743   | Layout 1 | `d9e3c0e63c72`  |
| 2736   | Layout 1 | `d9e3c0e63c72`  |
| 2726   | Layout 1 | `d9e3c0e63c72`  |
| 2717   | Layout 1 | `d9e3c0e63c72`  |
| 2709   | Layout 1 | `d9e3c0e63c72`  |
| 2703   | Layout 1 | `d9e3c0e63c72`  |
| 2695   | Layout 1 | `d9e3c0e63c72`  |
| 2684   | Layout 1 | `d9e3c0e63c72`  |
| 2672   | Layout 1 | `d9e3c0e63c72`  |
| 2665   | Layout 1 | `d9e3c0e63c72`  |
| 2657   | Layout 1 | `d9e3c0e63c72`  |
| 2649   | Layout 1 | `d9e3c0e63c72`  |
| 2644   | Layout 1 | `d9e3c0e63c72`  |
| 2637   | Layout 1 | `d9e3c0e63c72`  |
| 2629   | Layout 1 | `d9e3c0e63c72`  |
| 2619   | Layout 1 | `d9e3c0e63c72`  |
| 2612   | Layout 1 | `d9e3c0e63c72`  |
| 2606   | Layout 1 | `d9e3c0e63c72`  |
| 2602   | Layout 1 | `d9e3c0e63c72`  |
| 2601   | Layout 1 | `d9e3c0e63c72`  |
| 2592   | Layout 1 | `d9e3c0e63c72`  |
| 2583   | Layout 1 | `d9e3c0e63c72`  |
| 2575   | Layout 1 | `d9e3c0e63c72`  |
| 2567   | Layout 1 | `d9e3c0e63c72`  |
| 2560   | Layout 1 | `d9e3c0e63c72`  |
| 2553   | Layout 1 | `d9e3c0e63c72`  |
| 2545   | Layout 1 | `d9e3c0e63c72`  |
| 2538   | Layout 1 | `d9e3c0e63c72`  |
| 2529   | Layout 1 | `d9e3c0e63c72`  |
| 2519   | Layout 1 | `d9e3c0e63c72`  |
| 2513   | No file  | `d9e3c0e63c72`  |
| 2510   | No file  | `d9e3c0e63c72`  |
| 2507   | No file  | `d9e3c0e63c72`  |
| 2503   | No file  | `d9e3c0e63c72`  |
| 2498   | No file  | `d9e3c0e63c72`  |
| 2492   | No file  | `d9e3c0e63c72`  |
| 2487   | No file  | `d9e3c0e63c72`  |
| 2480   | No file  | `d9e3c0e63c72`  |
| 2474   | No file  | `d9e3c0e63c72`  |
| 2468   | No file  | `d9e3c0e63c72`  |
| 2460   | No file  | `d9e3c0e63c72`  |
| 2453   | No file  | `d9e3c0e63c72`  |
| 2444   | No file  | `d9e3c0e63c72`  |
| 2438   | No file  | `d9e3c0e63c72`  |
| 2434   | No file  | `d9e3c0e63c72`  |
| 2429   | No file  | `d9e3c0e63c72`  |
| 2421   | No file  | `d9e3c0e63c72`  |
| 2414   | No file  | `d9e3c0e63c72`  |
| 2407   | No file  | `d9e3c0e63c72`  |
| 2401   | No file  | `d9e3c0e63c72`  |
| 2397   | No file  | `d9e3c0e63c72`  |
| 2393   | No file  | `d9e3c0e63c72`  |
| 2384   | No file  | `d9e3c0e63c72`  |
| 2378   | No file  | `d9e3c0e63c72`  |
| 2372   | No file  | `d9e3c0e63c72`  |
| 2358   | No file  | `d9e3c0e63c72`  |
| 2352   | No file  | `d9e3c0e63c72`  |
| 2347   | No file  | `d9e3c0e63c72`  |
| 2343   | No file  | `d9e3c0e63c72`  |
| 2335   | No file  | `d9e3c0e63c72`  |
| 2327   | No file  | `d9e3c0e63c72`  |
| 2324   | No file  | `d9e3c0e63c72`  |
| 2319   | No file  | `d9e3c0e63c72`  |
| 2313   | No file  | `d9e3c0e63c72`  |
| 2308   | No file  | `d9e3c0e63c72`  |
| 2302   | No file  | `d9e3c0e63c72`  |
| 2295   | No file  | `d9e3c0e63c72`  |
| 2290   | No file  | `d9e3c0e63c72`  |
| 2284   | No file  | `d9e3c0e63c72`  |
| 2276   | No file  | `d9e3c0e63c72`  |
| 2269   | No file  | `d9e3c0e63c72`  |
| 2259   | No file  | `d9e3c0e63c72`  |
| 2250   | No file  | `d9e3c0e63c72`  |
| 2243   | No file  | `d9e3c0e63c72`  |
| 2235   | No file  | `d9e3c0e63c72`  |
| 2229   | No file  | `d9e3c0e63c72`  |
| 2224   | No file  | `d9e3c0e63c72`  |
| 2218   | No file  | `d9e3c0e63c72`  |
| 2215   | No file  | `d9e3c0e63c72`  |
| 2207   | No file  | `d9e3c0e63c72`  |
| 2203   | No file  | `d9e3c0e63c72`  |
| 2196   | No file  | `d9e3c0e63c72`  |
| 2192   | No file  | `d9e3c0e63c72`  |
| 2189   | No file  | `d9e3c0e63c72`  |
| 2183   | No file  | `d9e3c0e63c72`  |
| 2179   | No file  | `d9e3c0e63c72`  |
| 2171   | No file  | `d9e3c0e63c72`  |
| 2163   | No file  | `d9e3c0e63c72`  |
| 2156   | No file  | `d9e3c0e63c72`  |
| 2151   | No file  | `d9e3c0e63c72`  |
| 2147   | No file  | `d9e3c0e63c72`  |
| 2142   | No file  | `d9e3c0e63c72`  |
| 2138   | No file  | `d9e3c0e63c72`  |
| 2134   | No file  | `d9e3c0e63c72`  |
| 2130   | No file  | `d9e3c0e63c72`  |
| 2122   | No file  | `d9e3c0e63c72`  |
| 2107   | No file  | `d9e3c0e63c72`  |
| 2098   | No file  | `d9e3c0e63c72`  |
| 2089   | No file  | `d9e3c0e63c72`  |
| 2081   | No file  | `d9e3c0e63c72`  |
| 2073   | No file  | `d9e3c0e63c72`  |
| 2067   | No file  | `d9e3c0e63c72`  |
| 2063   | No file  | `d9e3c0e63c72`  |
| 2059   | No file  | `d9e3c0e63c72`  |
| 2052   | No file  | `d9e3c0e63c72`  |
| 2044   | No file  | `d9e3c0e63c72`  |
| 2039   | No file  | `d9e3c0e63c72`  |
| 2032   | No file  | `d9e3c0e63c72`  |
| 2025   | No file  | `d9e3c0e63c72`  |
| 2011   | No file  | `d9e3c0e63c72`  |
| 2005   | No file  | `d9e3c0e63c72`  |
| 2000   | No file  | `d9e3c0e63c72`  |
| 1996   | No file  | `d9e3c0e63c72`  |
| 1991   | No file  | `d9e3c0e63c72`  |
| 1985   | No file  | `d9e3c0e63c72`  |
| 1980   | No file  | `d9e3c0e63c72`  |
| 1969   | No file  | `d9e3c0e63c72`  |
| 1964   | No file  | `d9e3c0e63c72`  |
| 1958   | No file  | `d9e3c0e63c72`  |
| 1950   | No file  | `d9e3c0e63c72`  |
| 1945   | No file  | `d9e3c0e63c72`  |
| 1937   | No file  | `d9e3c0e63c72`  |
| 1933   | No file  | `d9e3c0e63c72`  |
| 1927   | No file  | `d9e3c0e63c72`  |
| 1921   | No file  | `d9e3c0e63c72`  |
| 1914   | No file  | `d9e3c0e63c72`  |
| 1908   | No file  | `d9e3c0e63c72`  |
| 1897   | No file  | `d9e3c0e63c72`  |
| 1892   | No file  | `d9e3c0e63c72`  |
| 1886   | No file  | `d9e3c0e63c72`  |
| 1881   | No file  | `d9e3c0e63c72`  |
| 1871   | No file  | `d9e3c0e63c72`  |
| 1866   | No file  | `d9e3c0e63c72`  |
| 1862   | No file  | `d9e3c0e63c72`  |
| 1854   | No file  | `d9e3c0e63c72`  |
| 1846   | No file  | `d9e3c0e63c72`  |
| 1838   | No file  | `d9e3c0e63c72`  |
| 1832   | No file  | `d9e3c0e63c72`  |
| 1826   | No file  | `d9e3c0e63c72`  |
| 1822   | No file  | `d9e3c0e63c72`  |
| 1818   | No file  | `d9e3c0e63c72`  |
| 1804   | No file  | `d9e3c0e63c72`  |
| 1794   | No file  | `d9e3c0e63c72`  |
| 1790   | No file  | `d9e3c0e63c72`  |
| 1784   | No file  | `d9e3c0e63c72`  |
| 1774   | No file  | `d9e3c0e63c72`  |
| 1771   | No file  | `d9e3c0e63c72`  |
| 1762   | No file  | `d9e3c0e63c72`  |
| 1759   | No file  | `d9e3c0e63c72`  |
| 1754   | No file  | `d9e3c0e63c72`  |
| 1749   | No file  | `d9e3c0e63c72`  |
| 1743   | No file  | `d9e3c0e63c72`  |
| 1737   | No file  | `d9e3c0e63c72`  |
| 1731   | No file  | `d9e3c0e63c72`  |
| 1725   | No file  | `d9e3c0e63c72`  |
| 1717   | No file  | `d9e3c0e63c72`  |
| 1710   | No file  | `d9e3c0e63c72`  |
| 1704   | No file  | `d9e3c0e63c72`  |
| 1698   | No file  | `d9e3c0e63c72`  |
| 1690   | No file  | `d9e3c0e63c72`  |
| 1685   | No file  | `d9e3c0e63c72`  |
| 1680   | No file  | `d9e3c0e63c72`  |
| 1674   | No file  | `d9e3c0e63c72`  |
| 1668   | No file  | `d9e3c0e63c72`  |
| 1659   | No file  | `d9e3c0e63c72`  |
| 1649   | No file  | `d9e3c0e63c72`  |
| 1642   | No file  | `d9e3c0e63c72`  |
| 1636   | No file  | `d9e3c0e63c72`  |
| 1628   | No file  | `d9e3c0e63c72`  |
| 1622   | No file  | `d9e3c0e63c72`  |
| 1614   | No file  | `d9e3c0e63c72`  |
| 1608   | No file  | `d9e3c0e63c72`  |
| 1602   | No file  | `d9e3c0e63c72`  |
| 1598   | No file  | `d9e3c0e63c72`  |
| 1594   | No file  | `d9e3c0e63c72`  |
| 1590   | No file  | `d9e3c0e63c72`  |
| 1587   | No file  | `d9e3c0e63c72`  |
| 1584   | No file  | `d9e3c0e63c72`  |
| 1579   | No file  | `d9e3c0e63c72`  |
| 1572   | No file  | `d9e3c0e63c72`  |
| 1565   | No file  | `d9e3c0e63c72`  |
| 1559   | No file  | `d9e3c0e63c72`  |
| 1554   | No file  | `d9e3c0e63c72`  |
| 1547   | No file  | `d9e3c0e63c72`  |
| 1537   | No file  | `d9e3c0e63c72`  |
| 1529   | No file  | `d9e3c0e63c72`  |
| 1524   | No file  | `d9e3c0e63c72`  |
| 1519   | No file  | `d9e3c0e63c72`  |
| 1509   | No file  | `d9e3c0e63c72`  |
| 1506   | No file  | `d9e3c0e63c72`  |
| 1504   | No file  | `d9e3c0e63c72`  |
| 1500   | No file  | `d9e3c0e63c72`  |
| 1493   | No file  | `d9e3c0e63c72`  |
| 1489   | No file  | `d9e3c0e63c72`  |
| 1485   | No file  | `d9e3c0e63c72`  |
| 1481   | No file  | `d9e3c0e63c72`  |
| 1474   | No file  | `d9e3c0e63c72`  |
| 1466   | No file  | `d9e3c0e63c72`  |
| 1462   | No file  | `d9e3c0e63c72`  |
| 1459   | No file  | `d9e3c0e63c72`  |
| 1453   | No file  | `d9e3c0e63c72`  |
| 1450   | No file  | `d9e3c0e63c72`  |
| 1445   | No file  | `d9e3c0e63c72`  |
| 1439   | No file  | `d9e3c0e63c72`  |
| 1433   | No file  | `d9e3c0e63c72`  |
| 1430   | No file  | `d9e3c0e63c72`  |
| 1426   | No file  | `d9e3c0e63c72`  |
| 1421   | No file  | `d9e3c0e63c72`  |
| 1417   | No file  | `d9e3c0e63c72`  |
| 1416   | No file  | `d9e3c0e63c72`  |
| 1409   | No file  | `d9e3c0e63c72`  |
| 1405   | No file  | `d9e3c0e63c72`  |
| 1401   | No file  | `d9e3c0e63c72`  |
| 1396   | No file  | `d9e3c0e63c72`  |
| 1391   | No file  | `d9e3c0e63c72`  |
| 1390   | No file  | `d9e3c0e63c72`  |
| 1386   | No file  | `d9e3c0e63c72`  |
| 1381   | No file  | `d9e3c0e63c72`  |
| 1379   | No file  | `d9e3c0e63c72`  |
| 1372   | No file  | `d9e3c0e63c72`  |
| 1366   | No file  | `d9e3c0e63c72`  |
| 1364   | No file  | `d9e3c0e63c72`  |
| 1363   | No file  | `d9e3c0e63c72`  |
| 1360   | No file  | `d9e3c0e63c72`  |
| 1358   | No file  | `d9e3c0e63c72`  |
| 1355   | No file  | `d9e3c0e63c72`  |
| 1351   | No file  | `d9e3c0e63c72`  |
| 1348   | No file  | `d9e3c0e63c72`  |
| 1346   | No file  | `d9e3c0e63c72`  |
| 1341   | No file  | `d9e3c0e63c72`  |
| 1340   | No file  | `d9e3c0e63c72`  |
| 1338   | No file  | `d9e3c0e63c72`  |
| 1335   | No file  | `d9e3c0e63c72`  |
| 1333   | No file  | `d9e3c0e63c72`  |
| 1329   | No file  | `d9e3c0e63c72`  |
| 1327   | No file  | `d9e3c0e63c72`  |
| 1324   | No file  | `d9e3c0e63c72`  |
| 1321   | No file  | `d9e3c0e63c72`  |
| 1319   | No file  | `d9e3c0e63c72`  |
| 1318   | No file  | `d9e3c0e63c72`  |
| 1316   | No file  | `d9e3c0e63c72`  |
| 1313   | No file  | `d9e3c0e63c72`  |
| 1311   | No file  | `d9e3c0e63c72`  |
| 1309   | No file  | `d9e3c0e63c72`  |
| 1304   | No file  | `d9e3c0e63c72`  |
| 1292   | No file  | `d9e3c0e63c72`  |
| 1286   | No file  | `d9e3c0e63c72`  |
| 1280   | No file  | `d9e3c0e63c72`  |
| 1276   | No file  | `d9e3c0e63c72`  |
| 1267   | No file  | `d9e3c0e63c72`  |
| 1261   | No file  | `d9e3c0e63c72`  |
| 1256   | No file  | `d9e3c0e63c72`  |
| 1250   | No file  | `d9e3c0e63c72`  |
| 1246   | No file  | `d9e3c0e63c72`  |
| 1239   | No file  | `d9e3c0e63c72`  |
| 1230   | No file  | `d9e3c0e63c72`  |
| 1226   | No file  | `d9e3c0e63c72`  |
| 1220   | No file  | `d9e3c0e63c72`  |
| 1217   | No file  | `d9e3c0e63c72`  |
| 1211   | No file  | `d9e3c0e63c72`  |
| 1210   | No file  | `d9e3c0e63c72`  |
| 1208   | No file  | `d9e3c0e63c72`  |
| 1203   | No file  | `d9e3c0e63c72`  |
| 1197   | No file  | `d9e3c0e63c72`  |
| 1194   | No file  | `d9e3c0e63c72`  |
| 1192   | No file  | `d9e3c0e63c72`  |
| 1187   | No file  | `d9e3c0e63c72`  |
| 1183   | No file  | `d9e3c0e63c72`  |
| 1177   | No file  | `d9e3c0e63c72`  |
| 1173   | No file  | `d9e3c0e63c72`  |
| 1167   | No file  | `d9e3c0e63c72`  |
| 1164   | No file  | `d9e3c0e63c72`  |
| 1156   | No file  | `d9e3c0e63c72`  |
| 1149   | No file  | `d9e3c0e63c72`  |
| 1144   | No file  | `d9e3c0e63c72`  |
| 1137   | No file  | `d9e3c0e63c72`  |
| 1132   | No file  | `d9e3c0e63c72`  |
| 1127   | No file  | `d9e3c0e63c72`  |
| 1122   | No file  | `d9e3c0e63c72`  |
| 1118   | No file  | `d9e3c0e63c72`  |
| 1114   | No file  | `d9e3c0e63c72`  |
| 1109   | No file  | `d9e3c0e63c72`  |
| 1102   | No file  | `d9e3c0e63c72`  |
| 1096   | No file  | `d9e3c0e63c72`  |
| 1088   | No file  | `d9e3c0e63c72`  |
| 1081   | No file  | `d9e3c0e63c72`  |
| 1076   | No file  | `d9e3c0e63c72`  |
| 1069   | No file  | `d9e3c0e63c72`  |
| 1064   | No file  | `d9e3c0e63c72`  |
| 1058   | No file  | `d9e3c0e63c72`  |
| 1051   | No file  | `d9e3c0e63c72`  |
| 1044   | No file  | `d9e3c0e63c72`  |
| 1036   | No file  | `d9e3c0e63c72`  |
| 1026   | No file  | `d9e3c0e63c72`  |
| 1016   | No file  | `d9e3c0e63c72`  |
| 1009   | No file  | `d9e3c0e63c72`  |
| 1005   | No file  | `d9e3c0e63c72`  |
| 1000   | No file  | `d9e3c0e63c72`  |
| 998    | No file  | `d9e3c0e63c72`  |
| 990    | No file  | `d9e3c0e63c72`  |
| 979    | No file  | `d9e3c0e63c72`  |
| 972    | No file  | `d9e3c0e63c72`  |
| 963    | No file  | `d9e3c0e63c72`  |
| 955    | No file  | `d9e3c0e63c72`  |
| 946    | No file  | `d9e3c0e63c72`  |
| 938    | No file  | `d9e3c0e63c72`  |
| 927    | No file  | `d9e3c0e63c72`  |
| 911    | No file  | `d9e3c0e63c72`  |
| 904    | No file  | `d9e3c0e63c72`  |
| 899    | No file  | `d9e3c0e63c72`  |
| 894    | No file  | `d9e3c0e63c72`  |
| 885    | No file  | `d9e3c0e63c72`  |
| 879    | No file  | `d9e3c0e63c72`  |
| 872    | No file  | `d9e3c0e63c72`  |
| 864    | No file  | `d9e3c0e63c72`  |
| 855    | No file  | `d9e3c0e63c72`  |
| 853    | No file  | `d9e3c0e63c72`  |
| 845    | No file  | `d9e3c0e63c72`  |
| 837    | No file  | `d9e3c0e63c72`  |
| 829    | No file  | `d9e3c0e63c72`  |
| 822    | No file  | `d9e3c0e63c72`  |
| 814    | No file  | `d9e3c0e63c72`  |
| 805    | No file  | `d9e3c0e63c72`  |
| 794    | No file  | `d9e3c0e63c72`  |
| 787    | No file  | `d9e3c0e63c72`  |
| 780    | No file  | `d9e3c0e63c72`  |
| 771    | No file  | `d9e3c0e63c72`  |
| 760    | No file  | `d9e3c0e63c72`  |
| 748    | No file  | `d9e3c0e63c72`  |
| 741    | No file  | `d9e3c0e63c72`  |
| 736    | No file  | `d9e3c0e63c72`  |
| 731    | No file  | `d9e3c0e63c72`  |
| 723    | No file  | `d9e3c0e63c72`  |
| 711    | No file  | `d9e3c0e63c72`  |
| 707    | No file  | `d9e3c0e63c72`  |
| 697    | No file  | `d9e3c0e63c72`  |
| 689    | No file  | `d9e3c0e63c72`  |
| 683    | No file  | `d9e3c0e63c72`  |
| 678    | No file  | `d9e3c0e63c72`  |
| 670    | No file  | `d9e3c0e63c72`  |
| 661    | No file  | `d9e3c0e63c72`  |
| 656    | No file  | `d9e3c0e63c72`  |
| 652    | No file  | `d9e3c0e63c72`  |
| 643    | No file  | `d9e3c0e63c72`  |
| 637    | No file  | `d9e3c0e63c72`  |
| 630    | No file  | `d9e3c0e63c72`  |
| 627    | No file  | `d9e3c0e63c72`  |
| 621    | No file  | `d9e3c0e63c72`  |
| 617    | No file  | `d9e3c0e63c72`  |
| 615    | No file  | `d9e3c0e63c72`  |
| 606    | No file  | `d9e3c0e63c72`  |
| 599    | No file  | `d9e3c0e63c72`  |
| 592    | No file  | `d9e3c0e63c72`  |
| 586    | No file  | `d9e3c0e63c72`  |
| 577    | No file  | `d9e3c0e63c72`  |
| 569    | No file  | `d9e3c0e63c72`  |
| 561    | No file  | `d9e3c0e63c72`  |
| 554    | No file  | `d9e3c0e63c72`  |
| 542    | No file  | `d9e3c0e63c72`  |
| 532    | No file  | `d9e3c0e63c72`  |
| 531    | No file  | `d9e3c0e63c72`  |
| 526    | No file  | `d9e3c0e63c72`  |
| 521    | No file  | `d9e3c0e63c72`  |
| 517    | No file  | `d9e3c0e63c72`  |
| 510    | No file  | `d9e3c0e63c72`  |
| 508    | No file  | `d9e3c0e63c72`  |
| 504    | No file  | `d9e3c0e63c72`  |
| 497    | No file  | `d9e3c0e63c72`  |
| 491    | No file  | `d9e3c0e63c72`  |
| 485    | No file  | `d9e3c0e63c72`  |
| 478    | No file  | `d9e3c0e63c72`  |
| 472    | No file  | `d9e3c0e63c72`  |
| 466    | No file  | `d9e3c0e63c72`  |
| 457    | No file  | `d9e3c0e63c72`  |
| 452    | No file  | `d9e3c0e63c72`  |
| 449    | No file  | `d9e3c0e63c72`  |
| 435    | No file  | `d9e3c0e63c72`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                         |
| --------------------- | -------- | ---------------------------- |
| `languagedata_en.loc` | Optional | Territory names, LOC type 12 |

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows, one per territory             |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 6 bytes + positions)

| Offset  | Type                     | Field          | Notes                                                       |
| ------- | ------------------------ | -------------- | ----------------------------------------------------------- |
| `+0x00` | u32                      | position_count | Number of positions; `1` to `3` on client 3482; the count comes before the key |
| `+0x04` | u16                      | territory_key  | `territoryinfo.bss` key, LOC type 12 name; one row each     |
| `+0x06` | Position[position_count] | positions      | See Position                                                |

### Position (16 bytes)

| Offset  | Type | Field      | Notes                                     |
| ------- | ---- | ---------- | ----------------------------------------- |
| `+0x00` | f32  | x          | World x                                   |
| `+0x04` | f32  | y          | Height                                    |
| `+0x08` | f32  | z          | World z                                   |
| `+0x0C` | f32  | unknown_0c | `500` on every position of client 3482    |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                          |
| ------- | ------------------ | ------------ | ---------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                        |

## Field Names

The file is newer than client 1784: it is not in that client's archives
and no sheet of a private server's `DataSheets.bexcel` on that client
covers it. `panel_window_deadmessage_all_1.luac` (client 3482) shows the
death window's `MinorSiegeOccupyModeRevivePosition0` to `3` buttons only
while the button index is below `ToClient_GetSiege2024RevivePositionCount()`
and the player takes part in the 2024 siege
(`ToClient_IsSelfParticipateInSiege2024()`); `panel_itemwarp_all_1.luac`
lists that many towns to warp to. The positions read as world
coordinates on the scale of the `regioninfo.bss` return points, and the
key is the territory they lie in: for 20 of the 21 positions of client
3482 the region with the nearest return point belongs to the row's
`territory_key` (LOC type 12: `0` Balenos, `1` Serendia, `2` Calpheon,
`3` Mediah, `4` Valencia, `6` Kamasylvia, `11` Ulukita, `12` Outer
Edania). The one other is a Calpheon position at `(-150360, -1424,
-144603)`, nearest the return point of Kamasylvia Castle.

## Notes

- Clients 2519 to 3251 hold six territories (328 bytes, no Ulukita or
  Outer Edania row) with the positions of client 3482, except one
  Valencia position at `(1262151, -3859, 181315)`, 278 units from the
  one client 3482 has there; client 2519 also has its second Serendia
  position at `(-12936, 248, -118908)`.
- The handler of `oceansiegereviveposition.bss`
  (`_bss/oceansiegereviveposition/`) previews this file with the reader
  in `_bss/siege2024revivepositionstaticstatus/`: one row per position,
  the territory key and name and the position rounded to whole units,
  in file order.

## Open Questions

### The f32 of Each Position

`unknown_0c` is `500` on every position. A spread radius around the
position fits, as the f32 after the positions of
[`oceansiegereviveposition.bss`](oceansiegereviveposition_bss.md) and
[`rosewarrevivepositionstaticstatus.bss`](rosewarrevivepositionstaticstatus_bss.md)
does, but nothing reads it.
