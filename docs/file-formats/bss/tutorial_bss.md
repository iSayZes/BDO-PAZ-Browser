# `tutorial.bss` Format

## Purpose

The steps of the Black Spirit guide tutorials that `Panel_Widget_Tutorial_GuideUI`
plays: on client 3482 four pet tutorials (first meeting, summon and seal,
feeding, groups) with 21 steps. A step is keyed by tutorial type and index;
it has a start condition, the condition script that completes it, the
`tutorial_startevent.bss` events it starts (black and white highlight
boxes), the Black Spirit title and text, an optional artwork image, and
where the text box sits. When a step completes, the Lua asks for the step
with the next index of the same type and ends the tutorial when there is
none.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File           | Bytes | Records | Row bytes               |
| ------ | -------------- | -------------- | ----- | ------- | ----------------------- |
| 4      | 1725 and later | `tutorial.bss` | 7,919 | 21 Row  | 69 to 73, 72 on average |
| 3      | 1717           | `tutorial.bss` | 5,987 | 18 Row  | 68 to 72, 71 on average |
| 2      | 1710           | `tutorial.bss` | 4,088 | 13 Row  | 97                      |
| 1      | 1704           | `tutorial.bss` | 758   | 4 Row   | 64 to 68, 67 on average |

| Layout | File           | Known           | Unknown      |
| ------ | -------------- | --------------- | ------------ |
| 4      | `tutorial.bss` | 7,688 B (97.1%) | 231 B (2.9%) |
| 3      | `tutorial.bss` | 5,789 B (96.7%) | 198 B (3.3%) |
| 2      | `tutorial.bss` | 3,997 B (97.8%) | 91 B (2.2%)  |
| 1      | `tutorial.bss` | 694 B (91.6%)   | 64 B (8.4%)  |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 4 | `12a2c3c2cb4d`  |
| 3482   | Layout 4 | `12a2c3c2cb4d`  |
| 3474   | Layout 4 | `12a2c3c2cb4d`  |
| 3473   | Layout 4 | `12a2c3c2cb4d`  |
| 3464   | Layout 4 | `12a2c3c2cb4d`  |
| 3458   | Layout 4 | `12a2c3c2cb4d`  |
| 3454   | Layout 4 | `12a2c3c2cb4d`  |
| 3444   | Layout 4 | `12a2c3c2cb4d`  |
| 3435   | Layout 4 | `12a2c3c2cb4d`  |
| 3426   | Layout 4 | `12a2c3c2cb4d`  |
| 3418   | Layout 4 | `12a2c3c2cb4d`  |
| 3412   | Layout 4 | `12a2c3c2cb4d`  |
| 3402   | Layout 4 | `12a2c3c2cb4d`  |
| 3396   | Layout 4 | `12a2c3c2cb4d`  |
| 3387   | Layout 4 | `12a2c3c2cb4d`  |
| 3381   | Layout 4 | `12a2c3c2cb4d`  |
| 3373   | Layout 4 | `12a2c3c2cb4d`  |
| 3364   | Layout 4 | `12a2c3c2cb4d`  |
| 3356   | Layout 4 | `12a2c3c2cb4d`  |
| 3349   | Layout 4 | `12a2c3c2cb4d`  |
| 3342   | Layout 4 | `12a2c3c2cb4d`  |
| 3335   | Layout 4 | `12a2c3c2cb4d`  |
| 3326   | Layout 4 | `12a2c3c2cb4d`  |
| 3321   | Layout 4 | `12a2c3c2cb4d`  |
| 3314   | Layout 4 | `12a2c3c2cb4d`  |
| 3303   | Layout 4 | `12a2c3c2cb4d`  |
| 3302   | Layout 4 | `12a2c3c2cb4d`  |
| 3293   | Layout 4 | `12a2c3c2cb4d`  |
| 3283   | Layout 4 | `12a2c3c2cb4d`  |
| 3275   | Layout 4 | `12a2c3c2cb4d`  |
| 3267   | Layout 4 | `12a2c3c2cb4d`  |
| 3258   | Layout 4 | `12a2c3c2cb4d`  |
| 3251   | Layout 4 | `12a2c3c2cb4d`  |
| 3242   | Layout 4 | `12a2c3c2cb4d`  |
| 3235   | Layout 4 | `12a2c3c2cb4d`  |
| 3229   | Layout 4 | `12a2c3c2cb4d`  |
| 3212   | Layout 4 | `12a2c3c2cb4d`  |
| 3203   | Layout 4 | `12a2c3c2cb4d`  |
| 3193   | Layout 4 | `12a2c3c2cb4d`  |
| 3186   | Layout 4 | `12a2c3c2cb4d`  |
| 3177   | Layout 4 | `12a2c3c2cb4d`  |
| 3169   | Layout 4 | `12a2c3c2cb4d`  |
| 3158   | Layout 4 | `12a2c3c2cb4d`  |
| 3151   | Layout 4 | `12a2c3c2cb4d`  |
| 3144   | Layout 4 | `12a2c3c2cb4d`  |
| 3133   | Layout 4 | `12a2c3c2cb4d`  |
| 3125   | Layout 4 | `12a2c3c2cb4d`  |
| 3118   | Layout 4 | `12a2c3c2cb4d`  |
| 3111   | Layout 4 | `12a2c3c2cb4d`  |
| 3103   | Layout 4 | `12a2c3c2cb4d`  |
| 3095   | Layout 4 | `12a2c3c2cb4d`  |
| 3086   | Layout 4 | `12a2c3c2cb4d`  |
| 3072   | Layout 4 | `12a2c3c2cb4d`  |
| 3062   | Layout 4 | `12a2c3c2cb4d`  |
| 3052   | Layout 4 | `12a2c3c2cb4d`  |
| 3045   | Layout 4 | `12a2c3c2cb4d`  |
| 3037   | Layout 4 | `12a2c3c2cb4d`  |
| 3030   | Layout 4 | `12a2c3c2cb4d`  |
| 3021   | Layout 4 | `12a2c3c2cb4d`  |
| 3012   | Layout 4 | `12a2c3c2cb4d`  |
| 3002   | Layout 4 | `12a2c3c2cb4d`  |
| 2995   | Layout 4 | `12a2c3c2cb4d`  |
| 2987   | Layout 4 | `12a2c3c2cb4d`  |
| 2978   | Layout 4 | `12a2c3c2cb4d`  |
| 2970   | Layout 4 | `12a2c3c2cb4d`  |
| 2959   | Layout 4 | `12a2c3c2cb4d`  |
| 2951   | Layout 4 | `12a2c3c2cb4d`  |
| 2942   | Layout 4 | `12a2c3c2cb4d`  |
| 2935   | Layout 4 | `12a2c3c2cb4d`  |
| 2932   | Layout 4 | `12a2c3c2cb4d`  |
| 2923   | Layout 4 | `12a2c3c2cb4d`  |
| 2919   | Layout 4 | `12a2c3c2cb4d`  |
| 2907   | Layout 4 | `12a2c3c2cb4d`  |
| 2900   | Layout 4 | `12a2c3c2cb4d`  |
| 2891   | Layout 4 | `12a2c3c2cb4d`  |
| 2882   | Layout 4 | `12a2c3c2cb4d`  |
| 2872   | Layout 4 | `12a2c3c2cb4d`  |
| 2863   | Layout 4 | `12a2c3c2cb4d`  |
| 2855   | Layout 4 | `12a2c3c2cb4d`  |
| 2849   | Layout 4 | `12a2c3c2cb4d`  |
| 2844   | Layout 4 | `12a2c3c2cb4d`  |
| 2834   | Layout 4 | `12a2c3c2cb4d`  |
| 2825   | Layout 4 | `12a2c3c2cb4d`  |
| 2819   | Layout 4 | `12a2c3c2cb4d`  |
| 2811   | Layout 4 | `12a2c3c2cb4d`  |
| 2803   | Layout 4 | `12a2c3c2cb4d`  |
| 2794   | Layout 4 | `12a2c3c2cb4d`  |
| 2783   | Layout 4 | `12a2c3c2cb4d`  |
| 2774   | Layout 4 | `12a2c3c2cb4d`  |
| 2765   | Layout 4 | `12a2c3c2cb4d`  |
| 2756   | Layout 4 | `12a2c3c2cb4d`  |
| 2750   | Layout 4 | `12a2c3c2cb4d`  |
| 2743   | Layout 4 | `12a2c3c2cb4d`  |
| 2736   | Layout 4 | `12a2c3c2cb4d`  |
| 2726   | Layout 4 | `12a2c3c2cb4d`  |
| 2717   | Layout 4 | `12a2c3c2cb4d`  |
| 2709   | Layout 4 | `12a2c3c2cb4d`  |
| 2703   | Layout 4 | `12a2c3c2cb4d`  |
| 2695   | Layout 4 | `12a2c3c2cb4d`  |
| 2684   | Layout 4 | `12a2c3c2cb4d`  |
| 2672   | Layout 4 | `12a2c3c2cb4d`  |
| 2665   | Layout 4 | `12a2c3c2cb4d`  |
| 2657   | Layout 4 | `12a2c3c2cb4d`  |
| 2649   | Layout 4 | `12a2c3c2cb4d`  |
| 2644   | Layout 4 | `12a2c3c2cb4d`  |
| 2637   | Layout 4 | `12a2c3c2cb4d`  |
| 2629   | Layout 4 | `12a2c3c2cb4d`  |
| 2619   | Layout 4 | `12a2c3c2cb4d`  |
| 2612   | Layout 4 | `12a2c3c2cb4d`  |
| 2606   | Layout 4 | `12a2c3c2cb4d`  |
| 2602   | Layout 4 | `12a2c3c2cb4d`  |
| 2601   | Layout 4 | `12a2c3c2cb4d`  |
| 2592   | Layout 4 | `12a2c3c2cb4d`  |
| 2583   | Layout 4 | `12a2c3c2cb4d`  |
| 2575   | Layout 4 | `12a2c3c2cb4d`  |
| 2567   | Layout 4 | `12a2c3c2cb4d`  |
| 2560   | Layout 4 | `12a2c3c2cb4d`  |
| 2553   | Layout 4 | `12a2c3c2cb4d`  |
| 2545   | Layout 4 | `12a2c3c2cb4d`  |
| 2538   | Layout 4 | `12a2c3c2cb4d`  |
| 2529   | Layout 4 | `12a2c3c2cb4d`  |
| 2519   | Layout 4 | `12a2c3c2cb4d`  |
| 2513   | Layout 4 | `12a2c3c2cb4d`  |
| 2510   | Layout 4 | `12a2c3c2cb4d`  |
| 2507   | Layout 4 | `12a2c3c2cb4d`  |
| 2503   | Layout 4 | `12a2c3c2cb4d`  |
| 2498   | Layout 4 | `12a2c3c2cb4d`  |
| 2492   | Layout 4 | `12a2c3c2cb4d`  |
| 2487   | Layout 4 | `12a2c3c2cb4d`  |
| 2480   | Layout 4 | `12a2c3c2cb4d`  |
| 2474   | Layout 4 | `12a2c3c2cb4d`  |
| 2468   | Layout 4 | `12a2c3c2cb4d`  |
| 2460   | Layout 4 | `12a2c3c2cb4d`  |
| 2453   | Layout 4 | `12a2c3c2cb4d`  |
| 2444   | Layout 4 | `12a2c3c2cb4d`  |
| 2438   | Layout 4 | `12a2c3c2cb4d`  |
| 2434   | Layout 4 | `12a2c3c2cb4d`  |
| 2429   | Layout 4 | `12a2c3c2cb4d`  |
| 2421   | Layout 4 | `12a2c3c2cb4d`  |
| 2414   | Layout 4 | `12a2c3c2cb4d`  |
| 2407   | Layout 4 | `12a2c3c2cb4d`  |
| 2401   | Layout 4 | `12a2c3c2cb4d`  |
| 2397   | Layout 4 | `12a2c3c2cb4d`  |
| 2393   | Layout 4 | `12a2c3c2cb4d`  |
| 2384   | Layout 4 | `12a2c3c2cb4d`  |
| 2378   | Layout 4 | `12a2c3c2cb4d`  |
| 2372   | Layout 4 | `12a2c3c2cb4d`  |
| 2358   | Layout 4 | `12a2c3c2cb4d`  |
| 2352   | Layout 4 | `12a2c3c2cb4d`  |
| 2347   | Layout 4 | `12a2c3c2cb4d`  |
| 2343   | Layout 4 | `12a2c3c2cb4d`  |
| 2335   | Layout 4 | `12a2c3c2cb4d`  |
| 2327   | Layout 4 | `12a2c3c2cb4d`  |
| 2324   | Layout 4 | `12a2c3c2cb4d`  |
| 2319   | Layout 4 | `12a2c3c2cb4d`  |
| 2313   | Layout 4 | `12a2c3c2cb4d`  |
| 2308   | Layout 4 | `12a2c3c2cb4d`  |
| 2302   | Layout 4 | `12a2c3c2cb4d`  |
| 2295   | Layout 4 | `12a2c3c2cb4d`  |
| 2290   | Layout 4 | `12a2c3c2cb4d`  |
| 2284   | Layout 4 | `12a2c3c2cb4d`  |
| 2276   | Layout 4 | `12a2c3c2cb4d`  |
| 2269   | Layout 4 | `12a2c3c2cb4d`  |
| 2259   | Layout 4 | `12a2c3c2cb4d`  |
| 2250   | Layout 4 | `12a2c3c2cb4d`  |
| 2243   | Layout 4 | `12a2c3c2cb4d`  |
| 2235   | Layout 4 | `12a2c3c2cb4d`  |
| 2229   | Layout 4 | `12a2c3c2cb4d`  |
| 2224   | Layout 4 | `12a2c3c2cb4d`  |
| 2218   | Layout 4 | `12a2c3c2cb4d`  |
| 2215   | Layout 4 | `12a2c3c2cb4d`  |
| 2207   | Layout 4 | `12a2c3c2cb4d`  |
| 2203   | Layout 4 | `12a2c3c2cb4d`  |
| 2196   | Layout 4 | `12a2c3c2cb4d`  |
| 2192   | Layout 4 | `12a2c3c2cb4d`  |
| 2189   | Layout 4 | `12a2c3c2cb4d`  |
| 2183   | Layout 4 | `12a2c3c2cb4d`  |
| 2179   | Layout 4 | `12a2c3c2cb4d`  |
| 2171   | Layout 4 | `12a2c3c2cb4d`  |
| 2163   | Layout 4 | `12a2c3c2cb4d`  |
| 2156   | Layout 4 | `12a2c3c2cb4d`  |
| 2151   | Layout 4 | `12a2c3c2cb4d`  |
| 2147   | Layout 4 | `12a2c3c2cb4d`  |
| 2142   | Layout 4 | `12a2c3c2cb4d`  |
| 2138   | Layout 4 | `12a2c3c2cb4d`  |
| 2134   | Layout 4 | `12a2c3c2cb4d`  |
| 2130   | Layout 4 | `12a2c3c2cb4d`  |
| 2122   | Layout 4 | `12a2c3c2cb4d`  |
| 2107   | Layout 4 | `12a2c3c2cb4d`  |
| 2098   | Layout 4 | `12a2c3c2cb4d`  |
| 2089   | Layout 4 | `12a2c3c2cb4d`  |
| 2081   | Layout 4 | `12a2c3c2cb4d`  |
| 2073   | Layout 4 | `12a2c3c2cb4d`  |
| 2067   | Layout 4 | `12a2c3c2cb4d`  |
| 2063   | Layout 4 | `12a2c3c2cb4d`  |
| 2059   | Layout 4 | `12a2c3c2cb4d`  |
| 2052   | Layout 4 | `12a2c3c2cb4d`  |
| 2044   | Layout 4 | `12a2c3c2cb4d`  |
| 2039   | Layout 4 | `12a2c3c2cb4d`  |
| 2032   | Layout 4 | `12a2c3c2cb4d`  |
| 2025   | Layout 4 | `12a2c3c2cb4d`  |
| 2011   | Layout 4 | `12a2c3c2cb4d`  |
| 2005   | Layout 4 | `12a2c3c2cb4d`  |
| 2000   | Layout 4 | `12a2c3c2cb4d`  |
| 1996   | Layout 4 | `12a2c3c2cb4d`  |
| 1991   | Layout 4 | `12a2c3c2cb4d`  |
| 1985   | Layout 4 | `12a2c3c2cb4d`  |
| 1980   | Layout 4 | `12a2c3c2cb4d`  |
| 1969   | Layout 4 | `12a2c3c2cb4d`  |
| 1964   | Layout 4 | `12a2c3c2cb4d`  |
| 1958   | Layout 4 | `12a2c3c2cb4d`  |
| 1950   | Layout 4 | `12a2c3c2cb4d`  |
| 1945   | Layout 4 | `12a2c3c2cb4d`  |
| 1937   | Layout 4 | `12a2c3c2cb4d`  |
| 1933   | Layout 4 | `12a2c3c2cb4d`  |
| 1927   | Layout 4 | `12a2c3c2cb4d`  |
| 1921   | Layout 4 | `12a2c3c2cb4d`  |
| 1914   | Layout 4 | `12a2c3c2cb4d`  |
| 1908   | Layout 4 | `12a2c3c2cb4d`  |
| 1897   | Layout 4 | `12a2c3c2cb4d`  |
| 1892   | Layout 4 | `12a2c3c2cb4d`  |
| 1886   | Layout 4 | `12a2c3c2cb4d`  |
| 1881   | Layout 4 | `12a2c3c2cb4d`  |
| 1871   | Layout 4 | `12a2c3c2cb4d`  |
| 1866   | Layout 4 | `12a2c3c2cb4d`  |
| 1862   | Layout 4 | `12a2c3c2cb4d`  |
| 1854   | Layout 4 | `12a2c3c2cb4d`  |
| 1846   | Layout 4 | `12a2c3c2cb4d`  |
| 1838   | Layout 4 | `12a2c3c2cb4d`  |
| 1832   | Layout 4 | `12a2c3c2cb4d`  |
| 1826   | Layout 4 | `12a2c3c2cb4d`  |
| 1822   | Layout 4 | `12a2c3c2cb4d`  |
| 1818   | Layout 4 | `12a2c3c2cb4d`  |
| 1804   | Layout 4 | `12a2c3c2cb4d`  |
| 1794   | Layout 4 | `12a2c3c2cb4d`  |
| 1790   | Layout 4 | `12a2c3c2cb4d`  |
| 1784   | Layout 4 | `12a2c3c2cb4d`  |
| 1774   | Layout 4 | `12a2c3c2cb4d`  |
| 1771   | Layout 4 | `12a2c3c2cb4d`  |
| 1762   | Layout 4 | `12a2c3c2cb4d`  |
| 1759   | Layout 4 | `12a2c3c2cb4d`  |
| 1754   | Layout 4 | `12a2c3c2cb4d`  |
| 1749   | Layout 4 | `12a2c3c2cb4d`  |
| 1743   | Layout 4 | `12a2c3c2cb4d`  |
| 1737   | Layout 4 | `12a2c3c2cb4d`  |
| 1731   | Layout 4 | `12a2c3c2cb4d`  |
| 1725   | Layout 4 | `12a2c3c2cb4d`  |
| 1717   | Layout 3 | `12a2c3c2cb4d`  |
| 1710   | Layout 2 | `12a2c3c2cb4d`  |
| 1704   | Layout 1 | `12a2c3c2cb4d`  |
| 1698   | No file  | `12a2c3c2cb4d`  |
| 1690   | No file  | `12a2c3c2cb4d`  |
| 1685   | No file  | `12a2c3c2cb4d`  |
| 1680   | No file  | `12a2c3c2cb4d`  |
| 1674   | No file  | `12a2c3c2cb4d`  |
| 1668   | No file  | `12a2c3c2cb4d`  |
| 1659   | No file  | `12a2c3c2cb4d`  |
| 1649   | No file  | `12a2c3c2cb4d`  |
| 1642   | No file  | `12a2c3c2cb4d`  |
| 1636   | No file  | `12a2c3c2cb4d`  |
| 1628   | No file  | `12a2c3c2cb4d`  |
| 1622   | No file  | `12a2c3c2cb4d`  |
| 1614   | No file  | `12a2c3c2cb4d`  |
| 1608   | No file  | `12a2c3c2cb4d`  |
| 1602   | No file  | `12a2c3c2cb4d`  |
| 1598   | No file  | `12a2c3c2cb4d`  |
| 1594   | No file  | `12a2c3c2cb4d`  |
| 1590   | No file  | `12a2c3c2cb4d`  |
| 1587   | No file  | `12a2c3c2cb4d`  |
| 1584   | No file  | `12a2c3c2cb4d`  |
| 1579   | No file  | `12a2c3c2cb4d`  |
| 1572   | No file  | `12a2c3c2cb4d`  |
| 1565   | No file  | `12a2c3c2cb4d`  |
| 1559   | No file  | `12a2c3c2cb4d`  |
| 1554   | No file  | `12a2c3c2cb4d`  |
| 1547   | No file  | `12a2c3c2cb4d`  |
| 1537   | No file  | `12a2c3c2cb4d`  |
| 1529   | No file  | `12a2c3c2cb4d`  |
| 1524   | No file  | `12a2c3c2cb4d`  |
| 1519   | No file  | `12a2c3c2cb4d`  |
| 1509   | No file  | `12a2c3c2cb4d`  |
| 1506   | No file  | `12a2c3c2cb4d`  |
| 1504   | No file  | `12a2c3c2cb4d`  |
| 1500   | No file  | `12a2c3c2cb4d`  |
| 1493   | No file  | `12a2c3c2cb4d`  |
| 1489   | No file  | `12a2c3c2cb4d`  |
| 1485   | No file  | `12a2c3c2cb4d`  |
| 1481   | No file  | `12a2c3c2cb4d`  |
| 1474   | No file  | `12a2c3c2cb4d`  |
| 1466   | No file  | `12a2c3c2cb4d`  |
| 1462   | No file  | `12a2c3c2cb4d`  |
| 1459   | No file  | `12a2c3c2cb4d`  |
| 1453   | No file  | `12a2c3c2cb4d`  |
| 1450   | No file  | `12a2c3c2cb4d`  |
| 1445   | No file  | `12a2c3c2cb4d`  |
| 1439   | No file  | `12a2c3c2cb4d`  |
| 1433   | No file  | `12a2c3c2cb4d`  |
| 1430   | No file  | `12a2c3c2cb4d`  |
| 1426   | No file  | `12a2c3c2cb4d`  |
| 1421   | No file  | `12a2c3c2cb4d`  |
| 1417   | No file  | `12a2c3c2cb4d`  |
| 1416   | No file  | `12a2c3c2cb4d`  |
| 1409   | No file  | `12a2c3c2cb4d`  |
| 1405   | No file  | `12a2c3c2cb4d`  |
| 1401   | No file  | `12a2c3c2cb4d`  |
| 1396   | No file  | `12a2c3c2cb4d`  |
| 1391   | No file  | `12a2c3c2cb4d`  |
| 1390   | No file  | `12a2c3c2cb4d`  |
| 1386   | No file  | `12a2c3c2cb4d`  |
| 1381   | No file  | `12a2c3c2cb4d`  |
| 1379   | No file  | `12a2c3c2cb4d`  |
| 1372   | No file  | `12a2c3c2cb4d`  |
| 1366   | No file  | `12a2c3c2cb4d`  |
| 1364   | No file  | `12a2c3c2cb4d`  |
| 1363   | No file  | `12a2c3c2cb4d`  |
| 1360   | No file  | `12a2c3c2cb4d`  |
| 1358   | No file  | `12a2c3c2cb4d`  |
| 1355   | No file  | `12a2c3c2cb4d`  |
| 1351   | No file  | `12a2c3c2cb4d`  |
| 1348   | No file  | `12a2c3c2cb4d`  |
| 1346   | No file  | `12a2c3c2cb4d`  |
| 1341   | No file  | `12a2c3c2cb4d`  |
| 1340   | No file  | `12a2c3c2cb4d`  |
| 1338   | No file  | `12a2c3c2cb4d`  |
| 1335   | No file  | `12a2c3c2cb4d`  |
| 1333   | No file  | `12a2c3c2cb4d`  |
| 1329   | No file  | `12a2c3c2cb4d`  |
| 1327   | No file  | `12a2c3c2cb4d`  |
| 1324   | No file  | `12a2c3c2cb4d`  |
| 1321   | No file  | `12a2c3c2cb4d`  |
| 1319   | No file  | `12a2c3c2cb4d`  |
| 1318   | No file  | `12a2c3c2cb4d`  |
| 1316   | No file  | `12a2c3c2cb4d`  |
| 1313   | No file  | `12a2c3c2cb4d`  |
| 1311   | No file  | `12a2c3c2cb4d`  |
| 1309   | No file  | `12a2c3c2cb4d`  |
| 1304   | No file  | `12a2c3c2cb4d`  |
| 1292   | No file  | `12a2c3c2cb4d`  |
| 1286   | No file  | `12a2c3c2cb4d`  |
| 1280   | No file  | `12a2c3c2cb4d`  |
| 1276   | No file  | `12a2c3c2cb4d`  |
| 1267   | No file  | `12a2c3c2cb4d`  |
| 1261   | No file  | `12a2c3c2cb4d`  |
| 1256   | No file  | `12a2c3c2cb4d`  |
| 1250   | No file  | `12a2c3c2cb4d`  |
| 1246   | No file  | `12a2c3c2cb4d`  |
| 1239   | No file  | `12a2c3c2cb4d`  |
| 1230   | No file  | `12a2c3c2cb4d`  |
| 1226   | No file  | `12a2c3c2cb4d`  |
| 1220   | No file  | `12a2c3c2cb4d`  |
| 1217   | No file  | `12a2c3c2cb4d`  |
| 1211   | No file  | `12a2c3c2cb4d`  |
| 1210   | No file  | `12a2c3c2cb4d`  |
| 1208   | No file  | `12a2c3c2cb4d`  |
| 1203   | No file  | `12a2c3c2cb4d`  |
| 1197   | No file  | `12a2c3c2cb4d`  |
| 1194   | No file  | `12a2c3c2cb4d`  |
| 1192   | No file  | `12a2c3c2cb4d`  |
| 1187   | No file  | `12a2c3c2cb4d`  |
| 1183   | No file  | `12a2c3c2cb4d`  |
| 1177   | No file  | `12a2c3c2cb4d`  |
| 1173   | No file  | `12a2c3c2cb4d`  |
| 1167   | No file  | `12a2c3c2cb4d`  |
| 1164   | No file  | `12a2c3c2cb4d`  |
| 1156   | No file  | `12a2c3c2cb4d`  |
| 1149   | No file  | `12a2c3c2cb4d`  |
| 1144   | No file  | `12a2c3c2cb4d`  |
| 1137   | No file  | `12a2c3c2cb4d`  |
| 1132   | No file  | `12a2c3c2cb4d`  |
| 1127   | No file  | `12a2c3c2cb4d`  |
| 1122   | No file  | `12a2c3c2cb4d`  |
| 1118   | No file  | `12a2c3c2cb4d`  |
| 1114   | No file  | `12a2c3c2cb4d`  |
| 1109   | No file  | `12a2c3c2cb4d`  |
| 1102   | No file  | `12a2c3c2cb4d`  |
| 1096   | No file  | `12a2c3c2cb4d`  |
| 1088   | No file  | `12a2c3c2cb4d`  |
| 1081   | No file  | `12a2c3c2cb4d`  |
| 1076   | No file  | `12a2c3c2cb4d`  |
| 1069   | No file  | `12a2c3c2cb4d`  |
| 1064   | No file  | `12a2c3c2cb4d`  |
| 1058   | No file  | `12a2c3c2cb4d`  |
| 1051   | No file  | `12a2c3c2cb4d`  |
| 1044   | No file  | `12a2c3c2cb4d`  |
| 1036   | No file  | `12a2c3c2cb4d`  |
| 1026   | No file  | `12a2c3c2cb4d`  |
| 1016   | No file  | `12a2c3c2cb4d`  |
| 1009   | No file  | `12a2c3c2cb4d`  |
| 1005   | No file  | `12a2c3c2cb4d`  |
| 1000   | No file  | `12a2c3c2cb4d`  |
| 998    | No file  | `12a2c3c2cb4d`  |
| 990    | No file  | `12a2c3c2cb4d`  |
| 979    | No file  | `12a2c3c2cb4d`  |
| 972    | No file  | `12a2c3c2cb4d`  |
| 963    | No file  | `12a2c3c2cb4d`  |
| 955    | No file  | `12a2c3c2cb4d`  |
| 946    | No file  | `12a2c3c2cb4d`  |
| 938    | No file  | `12a2c3c2cb4d`  |
| 927    | No file  | `12a2c3c2cb4d`  |
| 911    | No file  | `12a2c3c2cb4d`  |
| 904    | No file  | `12a2c3c2cb4d`  |
| 899    | No file  | `12a2c3c2cb4d`  |
| 894    | No file  | `12a2c3c2cb4d`  |
| 885    | No file  | `12a2c3c2cb4d`  |
| 879    | No file  | `12a2c3c2cb4d`  |
| 872    | No file  | `12a2c3c2cb4d`  |
| 864    | No file  | `12a2c3c2cb4d`  |
| 855    | No file  | `12a2c3c2cb4d`  |
| 853    | No file  | `12a2c3c2cb4d`  |
| 845    | No file  | `12a2c3c2cb4d`  |
| 837    | No file  | `12a2c3c2cb4d`  |
| 829    | No file  | `12a2c3c2cb4d`  |
| 822    | No file  | `12a2c3c2cb4d`  |
| 814    | No file  | `12a2c3c2cb4d`  |
| 805    | No file  | `12a2c3c2cb4d`  |
| 794    | No file  | `12a2c3c2cb4d`  |
| 787    | No file  | `12a2c3c2cb4d`  |
| 780    | No file  | `12a2c3c2cb4d`  |
| 771    | No file  | `12a2c3c2cb4d`  |
| 760    | No file  | `12a2c3c2cb4d`  |
| 748    | No file  | `12a2c3c2cb4d`  |
| 741    | No file  | `12a2c3c2cb4d`  |
| 736    | No file  | `12a2c3c2cb4d`  |
| 731    | No file  | `12a2c3c2cb4d`  |
| 723    | No file  | `12a2c3c2cb4d`  |
| 711    | No file  | `12a2c3c2cb4d`  |
| 707    | No file  | `12a2c3c2cb4d`  |
| 697    | No file  | `12a2c3c2cb4d`  |
| 689    | No file  | `12a2c3c2cb4d`  |
| 683    | No file  | `12a2c3c2cb4d`  |
| 678    | No file  | `12a2c3c2cb4d`  |
| 670    | No file  | `12a2c3c2cb4d`  |
| 661    | No file  | `12a2c3c2cb4d`  |
| 656    | No file  | `12a2c3c2cb4d`  |
| 652    | No file  | `12a2c3c2cb4d`  |
| 643    | No file  | `12a2c3c2cb4d`  |
| 637    | No file  | `12a2c3c2cb4d`  |
| 630    | No file  | `12a2c3c2cb4d`  |
| 627    | No file  | `12a2c3c2cb4d`  |
| 621    | No file  | `12a2c3c2cb4d`  |
| 617    | No file  | `12a2c3c2cb4d`  |
| 615    | No file  | `12a2c3c2cb4d`  |
| 606    | No file  | `12a2c3c2cb4d`  |
| 599    | No file  | `12a2c3c2cb4d`  |
| 592    | No file  | `12a2c3c2cb4d`  |
| 586    | No file  | `12a2c3c2cb4d`  |
| 577    | No file  | `12a2c3c2cb4d`  |
| 569    | No file  | `12a2c3c2cb4d`  |
| 561    | No file  | `12a2c3c2cb4d`  |
| 554    | No file  | `12a2c3c2cb4d`  |
| 542    | No file  | `12a2c3c2cb4d`  |
| 532    | No file  | `12a2c3c2cb4d`  |
| 531    | No file  | `12a2c3c2cb4d`  |
| 526    | No file  | `12a2c3c2cb4d`  |
| 521    | No file  | `12a2c3c2cb4d`  |
| 517    | No file  | `12a2c3c2cb4d`  |
| 510    | No file  | `12a2c3c2cb4d`  |
| 508    | No file  | `12a2c3c2cb4d`  |
| 504    | No file  | `12a2c3c2cb4d`  |
| 497    | No file  | `12a2c3c2cb4d`  |
| 491    | No file  | `12a2c3c2cb4d`  |
| 485    | No file  | `12a2c3c2cb4d`  |
| 478    | No file  | `12a2c3c2cb4d`  |
| 472    | No file  | `12a2c3c2cb4d`  |
| 466    | No file  | `12a2c3c2cb4d`  |
| 457    | No file  | `12a2c3c2cb4d`  |
| 452    | No file  | `12a2c3c2cb4d`  |
| 449    | No file  | `12a2c3c2cb4d`  |
| 435    | No file  | `12a2c3c2cb4d`  |

<!-- versions:end -->

## Companion Files

None. The handler reads this file alone. Each of a step's
`start_event_keys` links to its
[`tutorial_startevent.bss`](tutorial_startevent_bss.md) row, and that
view links each start event back to the steps that list it.

All multi-byte values are little-endian.

## Layout 4

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of steps                               |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 69 bytes + start event keys)

Every `*_ref` field is an index into `strings`.

| Offset                  | Type                      | Field                        | Notes |
| ----------------------- | ------------------------- | ---------------------------- | ----- |
| `+0x00`                 | u16                       | tutorial_index               | Step number within its tutorial, from `0`; `TutorialKey:getIndex()` |
| `+0x02`                 | u16                       | tutorial_type                | Tutorial the step belongs to; `TutorialKey:getType()`, `1` to `4` on client 3482 |
| `+0x04`                 | u32                       | start_condition_ref          | Condition script that must hold before the step starts (`getItemCount(331059,0)>0;`); empty on 19 of 21 steps |
| `+0x08`                 | u32                       | complete_condition_ref       | Event that completes the step: `anyinput()`, `useitem(331059)`, `setshowpanel(Panel_Window_PetList_All, 1)` or `uiinputevent(<panel>, <control>, Mouse_LUp)` |
| `+0x0C`                 | u64                       | start_event_count            | `getStartEventCount()`; `0` or `1`                                  |
| `+0x14`                 | u32[start_event_count]    | start_event_keys             | `getStartEventKey(i)`: `tutorial_startevent.bss` keys, `1` to `17` |
| `start_event_keys+0x00` | u32                       | title_ref                    | `getTitle()`: Korean tutorial title, the same on every step of a type |
| `start_event_keys+0x04` | u32                       | desc_ref                     | `getDesc()`: Korean Black Spirit text with `<PAColor>` tags and `\n` escapes |
| `start_event_keys+0x08` | u32                       | image_path_ref               | `getImagePath()`: artwork shown under the text (`UI_Artwork/Tutorial_Pet_00.dds`); empty on 19 steps |
| `start_event_keys+0x0C` | u32                       | base_pos_panel_hash          | `getBasePosPanelID()`: `ascii_key_hash()` of the panel the text box is placed against (`Panel_Window_Inventory_All`, `Panel_Window_PetList_All`); `0` places it against the screen |
| `start_event_keys+0x10` | f32[2]                    | pos                          | `getPos()`: x and y used when `attr` has no flag for that axis      |
| `start_event_keys+0x18` | f32[2]                    | pan                          | `getPan()`: x and y offset from the aligned edge when `attr` has a flag for that axis |
| `start_event_keys+0x20` | u32                       | attr                         | `isAttr()` flags, see [Position Flags](#position-flags)             |
| `start_event_keys+0x24` | u8                        | unknown_start_event_keys_24  | `1` on every step; see Open Questions                               |
| `start_event_keys+0x25` | u8                        | accept_tutorial_type         | `2` on step `1.4` and `3` on step `2.4`, the last steps of types 1 and 2; else `0` |
| `start_event_keys+0x26` | bytes[10]                 | unknown_start_event_keys_26  | All zero on every step; see Open Questions                          |
| `start_event_keys+0x30` | u8                        | use_popup                    | `1` on the first steps of tutorials 1 and 4, else `0`               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                  |
| ------- | ------------------ | ------------ | ------------------------------------------------------ |
| `+0x00` | u32                | string_count | Number of strings; `46` on client 3482                 |
| `+0x04` | pstr[string_count] | strings      | String `0` is empty; each text is stored once          |

## Layout 3

Layout 4 without `use_popup`.

### Row (variable: 68 bytes + start event keys)

| Offset                  | Type                   | Field                       | Notes |
| ----------------------- | ---------------------- | --------------------------- | ----- |
| `+0x00`                 | u16                    | tutorial_index              |       |
| `+0x02`                 | u16                    | tutorial_type               |       |
| `+0x04`                 | u32                    | start_condition_ref         |       |
| `+0x08`                 | u32                    | complete_condition_ref      |       |
| `+0x0C`                 | u64                    | start_event_count           |       |
| `+0x14`                 | u32[start_event_count] | start_event_keys            |       |
| `start_event_keys+0x00` | u32                    | title_ref                   |       |
| `start_event_keys+0x04` | u32                    | desc_ref                    |       |
| `start_event_keys+0x08` | u32                    | image_path_ref              |       |
| `start_event_keys+0x0C` | u32                    | base_pos_panel_hash         |       |
| `start_event_keys+0x10` | f32[2]                 | pos                         |       |
| `start_event_keys+0x18` | f32[2]                 | pan                         |       |
| `start_event_keys+0x20` | u32                    | attr                        |       |
| `start_event_keys+0x24` | u8                     | unknown_start_event_keys_24 | `1` on every step |
| `start_event_keys+0x25` | u8                     | accept_tutorial_type        |       |
| `start_event_keys+0x26` | bytes[10]              | unknown_start_event_keys_26 | All zero on every step |

## Layout 2

Each step holds its one start event itself: a type, four parameter
strings and the black frame around the target. Client 1710 has no
`tutorial_startevent.bss` and no `start_event_keys`.

### Row (97 bytes)

| Offset  | Type   | Field                  | Notes |
| ------- | ------ | ---------------------- | ----- |
| `+0x00` | u16    | tutorial_index         |       |
| `+0x02` | u16    | tutorial_type          | `1` to `3` on client 1710 |
| `+0x04` | u32    | start_condition_ref    | Empty on all 13 steps |
| `+0x08` | u32    | complete_condition_ref |       |
| `+0x0C` | u8     | start_event_type       | `getStartEventType()`: `0` on the 6 steps whose parameters name a panel and a control (`__eTutorialStartEventType_FindControl`); `1` on the `useitem(331059)` step, whose parameters hold an item key (`_FindItemInInventory`); `2` on the 6 steps without parameters |
| `+0x0D` | u32[4] | param_value_refs       | `getParamValue(0)` to `(3)` as strings: panel name, control name and `1` for type `0` (the control to find, then the black frame on); `0` and `331059` for type `1` (item where type, item key); slot `3` is empty on every step |
| `+0x1D` | u32    | unknown_1d             | `0` on every step |
| `+0x21` | u32    | title_ref              |       |
| `+0x25` | u32    | desc_ref               |       |
| `+0x29` | u32    | image_path_ref         |       |
| `+0x2D` | u32    | base_pos_panel_hash    |       |
| `+0x31` | f32[2] | pos                    |       |
| `+0x39` | f32[2] | pan                    |       |
| `+0x41` | u32    | attr                   |       |
| `+0x45` | u8     | unknown_45             | `0` on every step |
| `+0x46` | u8     | unknown_46             | `1` on the 7 steps with start event type `0` or `1` and on step `1.4`, else `0` |
| `+0x47` | f32[2] | offset_black_bg        | `getOffsetBlackBG()`: x and y the black frame grows by around the found control; `30, 30` on the four `Panel_Window_PetList_All` steps, else `0, 0` |
| `+0x4F` | f32[2] | pos_black_bg           | `getPosBlackBG()`: `1500, 300` on step `1.1`, else `0, 0` |
| `+0x57` | f32[2] | size_black_bg          | `getSizeBlackBG()`: `500, 300` on step `1.1`, else `0, 0` |
| `+0x5F` | u8     | accept_tutorial_type   | `2` on step `1.4` and `3` on step `2.3`, the last steps of types 1 and 2 |
| `+0x60` | u8     | unknown_60             | `0` on every step |

## Layout 1

Each step lists `tutorial_initevent.bss` keys in place of start events and
has no start condition and no image path; the row ends at `attr`.

### Row (variable: 64 bytes + init event keys)

| Offset                 | Type                  | Field                      | Notes |
| ---------------------- | --------------------- | -------------------------- | ----- |
| `+0x00`                | u16                   | tutorial_index             |       |
| `+0x02`                | u16                   | tutorial_type              | `1` on all 4 steps of client 1704 |
| `+0x04`                | u64                   | init_event_count           | `getInitEventKeyCount()`; `0` or `1` |
| `+0x0C`                | u32[init_event_count] | init_event_keys            | `getInitEventKey(i)`: `tutorial_initevent.bss` keys `1`, `2` and `4`; the `useitem(331059)` step names key `2`, whose row holds item `331059` |
| `init_event_keys+0x00` | u32                   | complete_condition_ref     |       |
| `init_event_keys+0x04` | u32                   | title_ref                  | Set on step `1.0` only, to the title client 1710 shows on every step |
| `init_event_keys+0x08` | u32                   | desc_ref                   | `getDesc(0)`: the Black Spirit text; set on step `1.0` only |
| `init_event_keys+0x0C` | u32[4]                | unknown_init_event_keys_0c | Indexes into `strings`; slot `0` holds a short text on step `1.0` (`열어봐`, "open it"), the rest are empty; see Open Questions |
| `init_event_keys+0x1C` | u32                   | base_pos_panel_hash        |       |
| `init_event_keys+0x20` | f32[2]                | pos                        |       |
| `init_event_keys+0x28` | f32[2]                | pan                        |       |
| `init_event_keys+0x30` | u32                   | attr                       |       |

## Position Flags

`attr` against the `Pos` column of the `Tutorial_Table` sheet (21 of 21
steps, client 3482):

| `attr`    | Sheet `Pos`      | Flags                     |
| --------- | ---------------- | ------------------------- |
| `0x10001` | `left, middle`   | `0x1` left, `0x10000` middle |
| `0x10010` | `center, middle` | `0x10` center, `0x10000` middle |
| `0`       | `-700, 0`        | none: `pos` holds the sheet value |

The Lua also tests `__eTutorialAttrPos_Right`, `_Top` and `_Bottom`; no
step uses them, so their bits are not known.

## Field Names

The `Tutorial_Table` sheet of a private server's `DataSheets.bexcel` on
client 1784 has 21 rows, and the file is the same from client 1784 to
client 3482. Matched on all 21 rows: `Type` and `Index` (the key),
`StartCondition`, `CompleteCondition`, `StartEventKeyList`, `Title`,
`Desc`, `ImagePath`, `BasePosPanel` (hashed), `Pos` (as `pos` or as
`attr`), `Pan`, `AcceptTutorialType` and `UsePopup`. The Lua getters in
[`panel_widget_tutorial_guideui_1.luac`](../lua/panel_widget_tutorial_guideui_1_luac.md)
name the same fields (`getStartEventKey`, `getBasePosPanelID`, `getPan`,
`getPos`, `isAttr`, `getImagePath`, `isUseSkip`).

Layouts 1 to 3 have no sheet. Their fields take the Layout 4 name where
the same step (type and index) holds the same kind of value on the next
newer client, and the client's own copy of the script names the rest:
`getInitEventKeyCount()`, `getInitEventKey(i)` and `getDesc(0)` on client
1704, `getStartEventType()`, `getParamValue(i)`, `getOffsetBlackBG()`,
`getPosBlackBG()` and `getSizeBlackBG()` on client 1710.

## Notes

- The rows are not in key order: type 4 comes first, its steps from index
  3 down to 0.
- `complete_condition_ref` and `start_condition_ref` hold the step scripts
  as text; the `uiinputevent` panel and control names are the client's UI
  names.
- Layout 2 reads the three black frame pairs in the order the Lua uses
  them: the client 1710 script draws the frame at `pos_black_bg` with
  `size_black_bg` when both are above `0` (`1500, 300` and `500, 300` on
  the inventory step `1.1`), and around a found control grown by
  `offset_black_bg` (`30, 30` on the four pet list steps).
- On client 1704 string `0` is the first step's complete condition and
  string `1` is empty; every empty text field holds `1`.

## Open Questions

### Skip, No Translate and Not Input

The sheet's `UseSkip` and `DoNotTranslate` are `1` and `NotInput` is `0`
on all 21 rows, and `AllowKey` is empty. `unknown_start_event_keys_24` is
`1` on every step, so it is `UseSkip` (`isUseSkip()`) or
`DoNotTranslate`; the ten zero bytes of `unknown_start_event_keys_26` hold
`NotInput` (`isNotInput()` of the running tutorial) and the `AllowKey` list somewhere. No client
from 1784 on changes a byte of the file, so the data cannot place them.

### Text Slots of Client 1704

The client 1704 script reads only `getDesc(0)`, and the index says the
step holds more than one text. `unknown_init_event_keys_0c` is four string
indexes after `desc_ref`: slot `0` is a short text (`열어봐`) on step
`1.0` and the rest are empty, so they are desc slots `1` to `4` or fields
that no client 1704 script reads.

### Skip and Focus Flags of Client 1710

The client 1710 script reads `isUseSkip()` (the skip button) and
`isUseFocus()` (the black frame's focus layer), and Layout 2 has two
unnamed bytes, `unknown_45` (`0` on every step) and `unknown_46` (`1` on
the steps with a start event and on step `1.4`). Step `1.4` has no frame,
so `unknown_46` reads as `isUseSkip()`, but the other steps cannot tell
the two apart.
