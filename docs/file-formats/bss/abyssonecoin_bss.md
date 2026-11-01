# `abyssonecoin.bss` Format

## Purpose

A Magnus (`AbyssOne`) table with no PABR magic: rows of a u16 key and a
u64 value. On client 3482 the keys are `4001` to `4071`, one row each, and
the value grows with the key from `50` to `690` in steps of `10`. The file
name and the Magnus coin currency (`__eInventoryMoneyType_Abyss`) suggest
a coin amount per key; what the key counts is open (see Open Questions).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File               | Bytes | Records | Row bytes |
| ------ | -------------- | ------------------ | ----- | ------- | --------- |
| 1      | 2011 and later | `abyssonecoin.bss` | 714   | 71 Row  | 10        |

| Layout | File               | Known      | Unknown       |
| ------ | ------------------ | ---------- | ------------- |
| 1      | `abyssonecoin.bss` | 4 B (0.6%) | 710 B (99.4%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `5f3ee2f1f32a`  |
| 3482   | Layout 1             | `5f3ee2f1f32a`  |
| 3474   | Layout 1             | `5f3ee2f1f32a`  |
| 3473   | Layout 1             | `5f3ee2f1f32a`  |
| 3464   | Layout 1             | `5f3ee2f1f32a`  |
| 3458   | Layout 1             | `5f3ee2f1f32a`  |
| 3454   | Layout 1             | `5f3ee2f1f32a`  |
| 3444   | Layout 1             | `5f3ee2f1f32a`  |
| 3435   | Layout 1             | `5f3ee2f1f32a`  |
| 3426   | Layout 1             | `5f3ee2f1f32a`  |
| 3418   | Layout 1             | `5f3ee2f1f32a`  |
| 3412   | Layout 1             | `5f3ee2f1f32a`  |
| 3402   | Layout 1             | `5f3ee2f1f32a`  |
| 3396   | Layout 1             | `5f3ee2f1f32a`  |
| 3387   | Layout 1             | `5f3ee2f1f32a`  |
| 3381   | Layout 1             | `5f3ee2f1f32a`  |
| 3373   | Layout 1             | `5f3ee2f1f32a`  |
| 3364   | Layout 1             | `5f3ee2f1f32a`  |
| 3356   | Layout 1             | `5f3ee2f1f32a`  |
| 3349   | Layout 1             | `5f3ee2f1f32a`  |
| 3342   | Layout 1             | `5f3ee2f1f32a`  |
| 3335   | Layout 1             | `5f3ee2f1f32a`  |
| 3326   | Layout 1             | `5f3ee2f1f32a`  |
| 3321   | Layout 1             | `5f3ee2f1f32a`  |
| 3314   | Layout 1             | `5f3ee2f1f32a`  |
| 3303   | Layout 1             | `5f3ee2f1f32a`  |
| 3302   | Layout 1             | `5f3ee2f1f32a`  |
| 3293   | Layout 1             | `5f3ee2f1f32a`  |
| 3283   | Layout 1             | `5f3ee2f1f32a`  |
| 3275   | Layout 1             | `5f3ee2f1f32a`  |
| 3267   | Layout 1             | `5f3ee2f1f32a`  |
| 3258   | Layout 1             | `5f3ee2f1f32a`  |
| 3251   | Layout 1             | `5f3ee2f1f32a`  |
| 3242   | Layout 1             | `5f3ee2f1f32a`  |
| 3235   | Layout 1             | `5f3ee2f1f32a`  |
| 3229   | Layout 1             | `5f3ee2f1f32a`  |
| 3212   | Layout 1             | `5f3ee2f1f32a`  |
| 3203   | Layout 1             | `5f3ee2f1f32a`  |
| 3193   | Layout 1             | `5f3ee2f1f32a`  |
| 3186   | Layout 1             | `5f3ee2f1f32a`  |
| 3177   | Layout 1             | `5f3ee2f1f32a`  |
| 3169   | Layout 1             | `5f3ee2f1f32a`  |
| 3158   | Layout 1             | `5f3ee2f1f32a`  |
| 3151   | Layout 1             | `5f3ee2f1f32a`  |
| 3144   | Layout 1             | `5f3ee2f1f32a`  |
| 3133   | Layout 1             | `5f3ee2f1f32a`  |
| 3125   | Layout 1             | `5f3ee2f1f32a`  |
| 3118   | Layout 1             | `5f3ee2f1f32a`  |
| 3111   | Layout 1             | `5f3ee2f1f32a`  |
| 3103   | Layout 1             | `5f3ee2f1f32a`  |
| 3095   | Layout 1             | `5f3ee2f1f32a`  |
| 3086   | Layout 1             | `5f3ee2f1f32a`  |
| 3072   | Layout 1             | `5f3ee2f1f32a`  |
| 3062   | Layout 1             | `5f3ee2f1f32a`  |
| 3052   | Layout 1             | `5f3ee2f1f32a`  |
| 3045   | Layout 1             | `5f3ee2f1f32a`  |
| 3037   | Layout 1             | `5f3ee2f1f32a`  |
| 3030   | Layout 1             | `5f3ee2f1f32a`  |
| 3021   | Layout 1             | `5f3ee2f1f32a`  |
| 3012   | Layout 1             | `5f3ee2f1f32a`  |
| 3002   | Layout 1             | `5f3ee2f1f32a`  |
| 2995   | Layout 1             | `5f3ee2f1f32a`  |
| 2987   | Layout 1             | `5f3ee2f1f32a`  |
| 2978   | Layout 1             | `5f3ee2f1f32a`  |
| 2970   | Layout 1             | `5f3ee2f1f32a`  |
| 2959   | Layout 1             | `5f3ee2f1f32a`  |
| 2951   | Layout 1             | `5f3ee2f1f32a`  |
| 2942   | Layout 1             | `5f3ee2f1f32a`  |
| 2935   | Layout 1             | `5f3ee2f1f32a`  |
| 2932   | Layout 1             | `5f3ee2f1f32a`  |
| 2923   | Layout 1             | `5f3ee2f1f32a`  |
| 2919   | Layout 1             | `5f3ee2f1f32a`  |
| 2907   | Layout 1             | `5f3ee2f1f32a`  |
| 2900   | Layout 1             | `5f3ee2f1f32a`  |
| 2891   | Layout 1             | `5f3ee2f1f32a`  |
| 2882   | Layout 1             | `5f3ee2f1f32a`  |
| 2872   | Layout 1             | `5f3ee2f1f32a`  |
| 2863   | Layout 1             | `5f3ee2f1f32a`  |
| 2855   | Layout 1             | `5f3ee2f1f32a`  |
| 2849   | Layout 1             | `5f3ee2f1f32a`  |
| 2844   | Layout 1             | `5f3ee2f1f32a`  |
| 2834   | Layout 1             | `5f3ee2f1f32a`  |
| 2825   | Layout 1             | `5f3ee2f1f32a`  |
| 2819   | Layout 1             | `5f3ee2f1f32a`  |
| 2811   | Layout 1             | `5f3ee2f1f32a`  |
| 2803   | Layout 1             | `5f3ee2f1f32a`  |
| 2794   | Layout 1             | `5f3ee2f1f32a`  |
| 2783   | Layout 1             | `5f3ee2f1f32a`  |
| 2774   | Layout 1             | `5f3ee2f1f32a`  |
| 2765   | Layout 1             | `5f3ee2f1f32a`  |
| 2756   | Layout 1             | `5f3ee2f1f32a`  |
| 2750   | Layout 1             | `5f3ee2f1f32a`  |
| 2743   | Layout 1             | `5f3ee2f1f32a`  |
| 2736   | Layout 1             | `5f3ee2f1f32a`  |
| 2726   | Layout 1             | `5f3ee2f1f32a`  |
| 2717   | Layout 1             | `5f3ee2f1f32a`  |
| 2709   | Layout 1             | `5f3ee2f1f32a`  |
| 2703   | Layout 1             | `5f3ee2f1f32a`  |
| 2695   | Layout 1             | `5f3ee2f1f32a`  |
| 2684   | Layout 1             | `5f3ee2f1f32a`  |
| 2672   | Layout 1             | `5f3ee2f1f32a`  |
| 2665   | Layout 1             | `5f3ee2f1f32a`  |
| 2657   | Layout 1             | `5f3ee2f1f32a`  |
| 2649   | Layout 1             | `5f3ee2f1f32a`  |
| 2644   | Layout 1             | `5f3ee2f1f32a`  |
| 2637   | Layout 1             | `5f3ee2f1f32a`  |
| 2629   | Layout 1             | `5f3ee2f1f32a`  |
| 2619   | Layout 1             | `5f3ee2f1f32a`  |
| 2612   | Layout 1             | `5f3ee2f1f32a`  |
| 2606   | Layout 1             | `5f3ee2f1f32a`  |
| 2602   | Layout 1             | `5f3ee2f1f32a`  |
| 2601   | Layout 1             | `5f3ee2f1f32a`  |
| 2592   | Layout 1             | `5f3ee2f1f32a`  |
| 2583   | Layout 1             | `5f3ee2f1f32a`  |
| 2575   | Layout 1             | `5f3ee2f1f32a`  |
| 2567   | Layout 1             | `5f3ee2f1f32a`  |
| 2560   | Layout 1             | `5f3ee2f1f32a`  |
| 2553   | Layout 1             | `5f3ee2f1f32a`  |
| 2545   | Layout 1             | `5f3ee2f1f32a`  |
| 2538   | Layout 1             | `5f3ee2f1f32a`  |
| 2529   | Layout 1             | `5f3ee2f1f32a`  |
| 2519   | Layout 1             | `5f3ee2f1f32a`  |
| 2513   | Layout 1             | `5f3ee2f1f32a`  |
| 2510   | Layout 1             | `5f3ee2f1f32a`  |
| 2507   | Layout 1             | `5f3ee2f1f32a`  |
| 2503   | Layout 1             | `5f3ee2f1f32a`  |
| 2498   | Layout 1             | `5f3ee2f1f32a`  |
| 2492   | Layout 1             | `5f3ee2f1f32a`  |
| 2487   | Layout 1             | `5f3ee2f1f32a`  |
| 2480   | Layout 1             | `5f3ee2f1f32a`  |
| 2474   | Layout 1             | `5f3ee2f1f32a`  |
| 2468   | Layout 1             | `5f3ee2f1f32a`  |
| 2460   | Layout 1             | `5f3ee2f1f32a`  |
| 2453   | Layout 1             | `5f3ee2f1f32a`  |
| 2444   | Layout 1             | `5f3ee2f1f32a`  |
| 2438   | Layout 1             | `5f3ee2f1f32a`  |
| 2434   | Layout 1             | `5f3ee2f1f32a`  |
| 2429   | Layout 1             | `5f3ee2f1f32a`  |
| 2421   | Layout 1             | `5f3ee2f1f32a`  |
| 2414   | Layout 1             | `5f3ee2f1f32a`  |
| 2407   | Layout 1             | `5f3ee2f1f32a`  |
| 2401   | Layout 1             | `5f3ee2f1f32a`  |
| 2397   | Layout 1             | `5f3ee2f1f32a`  |
| 2393   | Layout 1             | `5f3ee2f1f32a`  |
| 2384   | Layout 1             | `5f3ee2f1f32a`  |
| 2378   | Layout 1             | `5f3ee2f1f32a`  |
| 2372   | Layout 1             | `5f3ee2f1f32a`  |
| 2358   | Layout 1             | `5f3ee2f1f32a`  |
| 2352   | Layout 1             | `5f3ee2f1f32a`  |
| 2347   | Layout 1             | `5f3ee2f1f32a`  |
| 2343   | Layout 1             | `5f3ee2f1f32a`  |
| 2335   | Layout 1             | `5f3ee2f1f32a`  |
| 2327   | Layout 1             | `5f3ee2f1f32a`  |
| 2324   | Layout 1             | `5f3ee2f1f32a`  |
| 2319   | Layout 1             | `5f3ee2f1f32a`  |
| 2313   | Layout 1             | `5f3ee2f1f32a`  |
| 2308   | Layout 1             | `5f3ee2f1f32a`  |
| 2302   | Layout 1             | `5f3ee2f1f32a`  |
| 2295   | Layout 1             | `5f3ee2f1f32a`  |
| 2290   | Layout 1             | `5f3ee2f1f32a`  |
| 2284   | Layout 1             | `5f3ee2f1f32a`  |
| 2276   | Layout 1             | `5f3ee2f1f32a`  |
| 2269   | Layout 1             | `5f3ee2f1f32a`  |
| 2259   | Layout 1             | `5f3ee2f1f32a`  |
| 2250   | Layout 1             | `5f3ee2f1f32a`  |
| 2243   | Layout 1             | `5f3ee2f1f32a`  |
| 2235   | Layout 1             | `5f3ee2f1f32a`  |
| 2229   | Layout 1             | `5f3ee2f1f32a`  |
| 2224   | Layout 1             | `5f3ee2f1f32a`  |
| 2218   | Layout 1             | `5f3ee2f1f32a`  |
| 2215   | Layout 1             | `5f3ee2f1f32a`  |
| 2207   | Layout 1             | `5f3ee2f1f32a`  |
| 2203   | Layout 1             | `5f3ee2f1f32a`  |
| 2196   | Layout 1             | `5f3ee2f1f32a`  |
| 2192   | Layout 1             | `5f3ee2f1f32a`  |
| 2189   | Layout 1             | `5f3ee2f1f32a`  |
| 2183   | Layout 1             | `5f3ee2f1f32a`  |
| 2179   | Layout 1             | `5f3ee2f1f32a`  |
| 2171   | Layout 1             | `5f3ee2f1f32a`  |
| 2163   | Layout 1             | `5f3ee2f1f32a`  |
| 2156   | Layout 1             | `5f3ee2f1f32a`  |
| 2151   | Layout 1             | `5f3ee2f1f32a`  |
| 2147   | Layout 1             | `5f3ee2f1f32a`  |
| 2142   | Layout 1             | `5f3ee2f1f32a`  |
| 2138   | Layout 1             | `5f3ee2f1f32a`  |
| 2134   | Layout 1             | `5f3ee2f1f32a`  |
| 2130   | Layout 1             | `5f3ee2f1f32a`  |
| 2122   | Layout 1             | `5f3ee2f1f32a`  |
| 2107   | Layout 1             | `5f3ee2f1f32a`  |
| 2098   | Layout 1             | `5f3ee2f1f32a`  |
| 2089   | Layout 1             | `5f3ee2f1f32a`  |
| 2081   | Layout 1             | `5f3ee2f1f32a`  |
| 2073   | Layout 1             | `5f3ee2f1f32a`  |
| 2067   | Layout 1             | `5f3ee2f1f32a`  |
| 2063   | Layout 1             | `5f3ee2f1f32a`  |
| 2059   | Layout 1             | `5f3ee2f1f32a`  |
| 2052   | Layout 1             | `5f3ee2f1f32a`  |
| 2044   | Layout 1             | `5f3ee2f1f32a`  |
| 2039   | Layout 1             | `5f3ee2f1f32a`  |
| 2032   | Layout 1             | `5f3ee2f1f32a`  |
| 2025   | Layout 1             | `5f3ee2f1f32a`  |
| 2011   | Layout 1             | `5f3ee2f1f32a`  |
| 2005   | No documented layout | `5f3ee2f1f32a`  |
| 2000   | No file              | `5f3ee2f1f32a`  |
| 1996   | No file              | `5f3ee2f1f32a`  |
| 1991   | No file              | `5f3ee2f1f32a`  |
| 1985   | No file              | `5f3ee2f1f32a`  |
| 1980   | No file              | `5f3ee2f1f32a`  |
| 1969   | No file              | `5f3ee2f1f32a`  |
| 1964   | No file              | `5f3ee2f1f32a`  |
| 1958   | No file              | `5f3ee2f1f32a`  |
| 1950   | No file              | `5f3ee2f1f32a`  |
| 1945   | No file              | `5f3ee2f1f32a`  |
| 1937   | No file              | `5f3ee2f1f32a`  |
| 1933   | No file              | `5f3ee2f1f32a`  |
| 1927   | No file              | `5f3ee2f1f32a`  |
| 1921   | No file              | `5f3ee2f1f32a`  |
| 1914   | No file              | `5f3ee2f1f32a`  |
| 1908   | No file              | `5f3ee2f1f32a`  |
| 1897   | No file              | `5f3ee2f1f32a`  |
| 1892   | No file              | `5f3ee2f1f32a`  |
| 1886   | No file              | `5f3ee2f1f32a`  |
| 1881   | No file              | `5f3ee2f1f32a`  |
| 1871   | No file              | `5f3ee2f1f32a`  |
| 1866   | No file              | `5f3ee2f1f32a`  |
| 1862   | No file              | `5f3ee2f1f32a`  |
| 1854   | No file              | `5f3ee2f1f32a`  |
| 1846   | No file              | `5f3ee2f1f32a`  |
| 1838   | No file              | `5f3ee2f1f32a`  |
| 1832   | No file              | `5f3ee2f1f32a`  |
| 1826   | No file              | `5f3ee2f1f32a`  |
| 1822   | No file              | `5f3ee2f1f32a`  |
| 1818   | No file              | `5f3ee2f1f32a`  |
| 1804   | No file              | `5f3ee2f1f32a`  |
| 1794   | No file              | `5f3ee2f1f32a`  |
| 1790   | No file              | `5f3ee2f1f32a`  |
| 1784   | No file              | `5f3ee2f1f32a`  |
| 1774   | No file              | `5f3ee2f1f32a`  |
| 1771   | No file              | `5f3ee2f1f32a`  |
| 1762   | No file              | `5f3ee2f1f32a`  |
| 1759   | No file              | `5f3ee2f1f32a`  |
| 1754   | No file              | `5f3ee2f1f32a`  |
| 1749   | No file              | `5f3ee2f1f32a`  |
| 1743   | No file              | `5f3ee2f1f32a`  |
| 1737   | No file              | `5f3ee2f1f32a`  |
| 1731   | No file              | `5f3ee2f1f32a`  |
| 1725   | No file              | `5f3ee2f1f32a`  |
| 1717   | No file              | `5f3ee2f1f32a`  |
| 1710   | No file              | `5f3ee2f1f32a`  |
| 1704   | No file              | `5f3ee2f1f32a`  |
| 1698   | No file              | `5f3ee2f1f32a`  |
| 1690   | No file              | `5f3ee2f1f32a`  |
| 1685   | No file              | `5f3ee2f1f32a`  |
| 1680   | No file              | `5f3ee2f1f32a`  |
| 1674   | No file              | `5f3ee2f1f32a`  |
| 1668   | No file              | `5f3ee2f1f32a`  |
| 1659   | No file              | `5f3ee2f1f32a`  |
| 1649   | No file              | `5f3ee2f1f32a`  |
| 1642   | No file              | `5f3ee2f1f32a`  |
| 1636   | No file              | `5f3ee2f1f32a`  |
| 1628   | No file              | `5f3ee2f1f32a`  |
| 1622   | No file              | `5f3ee2f1f32a`  |
| 1614   | No file              | `5f3ee2f1f32a`  |
| 1608   | No file              | `5f3ee2f1f32a`  |
| 1602   | No file              | `5f3ee2f1f32a`  |
| 1598   | No file              | `5f3ee2f1f32a`  |
| 1594   | No file              | `5f3ee2f1f32a`  |
| 1590   | No file              | `5f3ee2f1f32a`  |
| 1587   | No file              | `5f3ee2f1f32a`  |
| 1584   | No file              | `5f3ee2f1f32a`  |
| 1579   | No file              | `5f3ee2f1f32a`  |
| 1572   | No file              | `5f3ee2f1f32a`  |
| 1565   | No file              | `5f3ee2f1f32a`  |
| 1559   | No file              | `5f3ee2f1f32a`  |
| 1554   | No file              | `5f3ee2f1f32a`  |
| 1547   | No file              | `5f3ee2f1f32a`  |
| 1537   | No file              | `5f3ee2f1f32a`  |
| 1529   | No file              | `5f3ee2f1f32a`  |
| 1524   | No file              | `5f3ee2f1f32a`  |
| 1519   | No file              | `5f3ee2f1f32a`  |
| 1509   | No file              | `5f3ee2f1f32a`  |
| 1506   | No file              | `5f3ee2f1f32a`  |
| 1504   | No file              | `5f3ee2f1f32a`  |
| 1500   | No file              | `5f3ee2f1f32a`  |
| 1493   | No file              | `5f3ee2f1f32a`  |
| 1489   | No file              | `5f3ee2f1f32a`  |
| 1485   | No file              | `5f3ee2f1f32a`  |
| 1481   | No file              | `5f3ee2f1f32a`  |
| 1474   | No file              | `5f3ee2f1f32a`  |
| 1466   | No file              | `5f3ee2f1f32a`  |
| 1462   | No file              | `5f3ee2f1f32a`  |
| 1459   | No file              | `5f3ee2f1f32a`  |
| 1453   | No file              | `5f3ee2f1f32a`  |
| 1450   | No file              | `5f3ee2f1f32a`  |
| 1445   | No file              | `5f3ee2f1f32a`  |
| 1439   | No file              | `5f3ee2f1f32a`  |
| 1433   | No file              | `5f3ee2f1f32a`  |
| 1430   | No file              | `5f3ee2f1f32a`  |
| 1426   | No file              | `5f3ee2f1f32a`  |
| 1421   | No file              | `5f3ee2f1f32a`  |
| 1417   | No file              | `5f3ee2f1f32a`  |
| 1416   | No file              | `5f3ee2f1f32a`  |
| 1409   | No file              | `5f3ee2f1f32a`  |
| 1405   | No file              | `5f3ee2f1f32a`  |
| 1401   | No file              | `5f3ee2f1f32a`  |
| 1396   | No file              | `5f3ee2f1f32a`  |
| 1391   | No file              | `5f3ee2f1f32a`  |
| 1390   | No file              | `5f3ee2f1f32a`  |
| 1386   | No file              | `5f3ee2f1f32a`  |
| 1381   | No file              | `5f3ee2f1f32a`  |
| 1379   | No file              | `5f3ee2f1f32a`  |
| 1372   | No file              | `5f3ee2f1f32a`  |
| 1366   | No file              | `5f3ee2f1f32a`  |
| 1364   | No file              | `5f3ee2f1f32a`  |
| 1363   | No file              | `5f3ee2f1f32a`  |
| 1360   | No file              | `5f3ee2f1f32a`  |
| 1358   | No file              | `5f3ee2f1f32a`  |
| 1355   | No file              | `5f3ee2f1f32a`  |
| 1351   | No file              | `5f3ee2f1f32a`  |
| 1348   | No file              | `5f3ee2f1f32a`  |
| 1346   | No file              | `5f3ee2f1f32a`  |
| 1341   | No file              | `5f3ee2f1f32a`  |
| 1340   | No file              | `5f3ee2f1f32a`  |
| 1338   | No file              | `5f3ee2f1f32a`  |
| 1335   | No file              | `5f3ee2f1f32a`  |
| 1333   | No file              | `5f3ee2f1f32a`  |
| 1329   | No file              | `5f3ee2f1f32a`  |
| 1327   | No file              | `5f3ee2f1f32a`  |
| 1324   | No file              | `5f3ee2f1f32a`  |
| 1321   | No file              | `5f3ee2f1f32a`  |
| 1319   | No file              | `5f3ee2f1f32a`  |
| 1318   | No file              | `5f3ee2f1f32a`  |
| 1316   | No file              | `5f3ee2f1f32a`  |
| 1313   | No file              | `5f3ee2f1f32a`  |
| 1311   | No file              | `5f3ee2f1f32a`  |
| 1309   | No file              | `5f3ee2f1f32a`  |
| 1304   | No file              | `5f3ee2f1f32a`  |
| 1292   | No file              | `5f3ee2f1f32a`  |
| 1286   | No file              | `5f3ee2f1f32a`  |
| 1280   | No file              | `5f3ee2f1f32a`  |
| 1276   | No file              | `5f3ee2f1f32a`  |
| 1267   | No file              | `5f3ee2f1f32a`  |
| 1261   | No file              | `5f3ee2f1f32a`  |
| 1256   | No file              | `5f3ee2f1f32a`  |
| 1250   | No file              | `5f3ee2f1f32a`  |
| 1246   | No file              | `5f3ee2f1f32a`  |
| 1239   | No file              | `5f3ee2f1f32a`  |
| 1230   | No file              | `5f3ee2f1f32a`  |
| 1226   | No file              | `5f3ee2f1f32a`  |
| 1220   | No file              | `5f3ee2f1f32a`  |
| 1217   | No file              | `5f3ee2f1f32a`  |
| 1211   | No file              | `5f3ee2f1f32a`  |
| 1210   | No file              | `5f3ee2f1f32a`  |
| 1208   | No file              | `5f3ee2f1f32a`  |
| 1203   | No file              | `5f3ee2f1f32a`  |
| 1197   | No file              | `5f3ee2f1f32a`  |
| 1194   | No file              | `5f3ee2f1f32a`  |
| 1192   | No file              | `5f3ee2f1f32a`  |
| 1187   | No file              | `5f3ee2f1f32a`  |
| 1183   | No file              | `5f3ee2f1f32a`  |
| 1177   | No file              | `5f3ee2f1f32a`  |
| 1173   | No file              | `5f3ee2f1f32a`  |
| 1167   | No file              | `5f3ee2f1f32a`  |
| 1164   | No file              | `5f3ee2f1f32a`  |
| 1156   | No file              | `5f3ee2f1f32a`  |
| 1149   | No file              | `5f3ee2f1f32a`  |
| 1144   | No file              | `5f3ee2f1f32a`  |
| 1137   | No file              | `5f3ee2f1f32a`  |
| 1132   | No file              | `5f3ee2f1f32a`  |
| 1127   | No file              | `5f3ee2f1f32a`  |
| 1122   | No file              | `5f3ee2f1f32a`  |
| 1118   | No file              | `5f3ee2f1f32a`  |
| 1114   | No file              | `5f3ee2f1f32a`  |
| 1109   | No file              | `5f3ee2f1f32a`  |
| 1102   | No file              | `5f3ee2f1f32a`  |
| 1096   | No file              | `5f3ee2f1f32a`  |
| 1088   | No file              | `5f3ee2f1f32a`  |
| 1081   | No file              | `5f3ee2f1f32a`  |
| 1076   | No file              | `5f3ee2f1f32a`  |
| 1069   | No file              | `5f3ee2f1f32a`  |
| 1064   | No file              | `5f3ee2f1f32a`  |
| 1058   | No file              | `5f3ee2f1f32a`  |
| 1051   | No file              | `5f3ee2f1f32a`  |
| 1044   | No file              | `5f3ee2f1f32a`  |
| 1036   | No file              | `5f3ee2f1f32a`  |
| 1026   | No file              | `5f3ee2f1f32a`  |
| 1016   | No file              | `5f3ee2f1f32a`  |
| 1009   | No file              | `5f3ee2f1f32a`  |
| 1005   | No file              | `5f3ee2f1f32a`  |
| 1000   | No file              | `5f3ee2f1f32a`  |
| 998    | No file              | `5f3ee2f1f32a`  |
| 990    | No file              | `5f3ee2f1f32a`  |
| 979    | No file              | `5f3ee2f1f32a`  |
| 972    | No file              | `5f3ee2f1f32a`  |
| 963    | No file              | `5f3ee2f1f32a`  |
| 955    | No file              | `5f3ee2f1f32a`  |
| 946    | No file              | `5f3ee2f1f32a`  |
| 938    | No file              | `5f3ee2f1f32a`  |
| 927    | No file              | `5f3ee2f1f32a`  |
| 911    | No file              | `5f3ee2f1f32a`  |
| 904    | No file              | `5f3ee2f1f32a`  |
| 899    | No file              | `5f3ee2f1f32a`  |
| 894    | No file              | `5f3ee2f1f32a`  |
| 885    | No file              | `5f3ee2f1f32a`  |
| 879    | No file              | `5f3ee2f1f32a`  |
| 872    | No file              | `5f3ee2f1f32a`  |
| 864    | No file              | `5f3ee2f1f32a`  |
| 855    | No file              | `5f3ee2f1f32a`  |
| 853    | No file              | `5f3ee2f1f32a`  |
| 845    | No file              | `5f3ee2f1f32a`  |
| 837    | No file              | `5f3ee2f1f32a`  |
| 829    | No file              | `5f3ee2f1f32a`  |
| 822    | No file              | `5f3ee2f1f32a`  |
| 814    | No file              | `5f3ee2f1f32a`  |
| 805    | No file              | `5f3ee2f1f32a`  |
| 794    | No file              | `5f3ee2f1f32a`  |
| 787    | No file              | `5f3ee2f1f32a`  |
| 780    | No file              | `5f3ee2f1f32a`  |
| 771    | No file              | `5f3ee2f1f32a`  |
| 760    | No file              | `5f3ee2f1f32a`  |
| 748    | No file              | `5f3ee2f1f32a`  |
| 741    | No file              | `5f3ee2f1f32a`  |
| 736    | No file              | `5f3ee2f1f32a`  |
| 731    | No file              | `5f3ee2f1f32a`  |
| 723    | No file              | `5f3ee2f1f32a`  |
| 711    | No file              | `5f3ee2f1f32a`  |
| 707    | No file              | `5f3ee2f1f32a`  |
| 697    | No file              | `5f3ee2f1f32a`  |
| 689    | No file              | `5f3ee2f1f32a`  |
| 683    | No file              | `5f3ee2f1f32a`  |
| 678    | No file              | `5f3ee2f1f32a`  |
| 670    | No file              | `5f3ee2f1f32a`  |
| 661    | No file              | `5f3ee2f1f32a`  |
| 656    | No file              | `5f3ee2f1f32a`  |
| 652    | No file              | `5f3ee2f1f32a`  |
| 643    | No file              | `5f3ee2f1f32a`  |
| 637    | No file              | `5f3ee2f1f32a`  |
| 630    | No file              | `5f3ee2f1f32a`  |
| 627    | No file              | `5f3ee2f1f32a`  |
| 621    | No file              | `5f3ee2f1f32a`  |
| 617    | No file              | `5f3ee2f1f32a`  |
| 615    | No file              | `5f3ee2f1f32a`  |
| 606    | No file              | `5f3ee2f1f32a`  |
| 599    | No file              | `5f3ee2f1f32a`  |
| 592    | No file              | `5f3ee2f1f32a`  |
| 586    | No file              | `5f3ee2f1f32a`  |
| 577    | No file              | `5f3ee2f1f32a`  |
| 569    | No file              | `5f3ee2f1f32a`  |
| 561    | No file              | `5f3ee2f1f32a`  |
| 554    | No file              | `5f3ee2f1f32a`  |
| 542    | No file              | `5f3ee2f1f32a`  |
| 532    | No file              | `5f3ee2f1f32a`  |
| 531    | No file              | `5f3ee2f1f32a`  |
| 526    | No file              | `5f3ee2f1f32a`  |
| 521    | No file              | `5f3ee2f1f32a`  |
| 517    | No file              | `5f3ee2f1f32a`  |
| 510    | No file              | `5f3ee2f1f32a`  |
| 508    | No file              | `5f3ee2f1f32a`  |
| 504    | No file              | `5f3ee2f1f32a`  |
| 497    | No file              | `5f3ee2f1f32a`  |
| 491    | No file              | `5f3ee2f1f32a`  |
| 485    | No file              | `5f3ee2f1f32a`  |
| 478    | No file              | `5f3ee2f1f32a`  |
| 472    | No file              | `5f3ee2f1f32a`  |
| 466    | No file              | `5f3ee2f1f32a`  |
| 457    | No file              | `5f3ee2f1f32a`  |
| 452    | No file              | `5f3ee2f1f32a`  |
| 449    | No file              | `5f3ee2f1f32a`  |
| 435    | No file              | `5f3ee2f1f32a`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset  | Type           | Field     | Notes          |
| ------- | -------------- | --------- | -------------- |
| `+0x00` | u32            | row_count | Number of rows |
| `+0x04` | Row[row_count] | rows      | See Row        |

### Row (10 bytes)

| Offset  | Type | Field      | Notes                                                                  |
| ------- | ---- | ---------- | ---------------------------------------------------------------------- |
| `+0x00` | u16  | unknown_00 | Row key; `4001` to `4071` on client 3482, unique per row               |
| `+0x02` | u64  | unknown_02 | `50` to `690` on client 3482; see Values                               |

## Values

On client 3482 `unknown_02` is `(unknown_00 - 4001) x 10 + 50` for the
keys `4001` to `4061`. `4062` repeats the `650` of `4061`, so `4063` to
`4066` run one step behind (`660` to `690`), and `4067` to `4071` hold
`690` as well. The rows are not in key order: they run down from `4071` in blocks
(`4071` to `4064`, `4047` to `4032`, `4063` to `4048`, `4015` to `4001`,
`4031` to `4016`).

| Client | Rows | Keys           | Values      |
| ------ | ---- | -------------- | ----------- |
| 2107   | 66   | `4001`-`4066`  | `50`-`690`  |
| 3482   | 71   | `4001`-`4071`  | `50`-`690`  |

## Field Names

The Magnus is newer than client 1784: the file is not in its archives and
no sheet of a private server's `DataSheets.bexcel` on that client has
`Abyss` in its name. The keys match no LOC type 17 region and no
`regioninfo.bss` key, and their LOC entries in other types (item `4001`
Iron Ore, knowledge `4001` Parasitic Bee) have nothing to do with the
Magnus. Both fields stay unknown.

## Notes

- The u64 value fits the Magnus coin type: the equipment preset Lua reads
  its coin price as an s64 (`presetEquipSSW:getAbyssCoin()`,
  `panel_abyssone_equippresetlist.luac`), and
  [`abyssoneequipmentpreset.bss`](abyssoneequipmentpreset_bss.md) stores
  that price as a u64.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/abyssone_tables.py`: each
  row's bytes as hex, since no field is named.

## Open Questions

### What the Key Counts

The keys run from `4001` with no gap, and client 3482 adds `4067` to
`4071` to the 66 keys of client 2107 with the capped value `690`. A level
or tier of Magnus content would fit a key that only grows. The only coin
names with `Abyss` in the client 3482 Lua are `_ContentsGroup_AbyssOneCoin`,
`__eInventoryMoneyType_Abyss` and `getAbyssCoin()` of the equipment
presets, and none of them takes a key.
