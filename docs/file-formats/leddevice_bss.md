# `leddevice.bss` Format

## Purpose

The RGB lighting effects the client plays on Asus and Razer devices
(keyboard, mouse, headset, mousepad, Chroma Link) for game events. A PABR
list of rows; each row pairs an animation number with a device type and
names the Asus and the Razer effect for it, with a colour. On client 3482
it holds 16 animations for 5 device types, from `EnhancementFailed` to
`UnderWater`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File            | Bytes | Records | Row bytes |
| ------ | -------------- | ------- | --------------- | ----- | ------- | --------- |
| 4      | 1335 and later | 3483    | `leddevice.bss` | 3,028 | 80 Row  | 16        |
| 3      | 1321 to 1333   | 1333    | `leddevice.bss` | 2,868 | 80 Row  | 14        |
| 2      | 1156 to 1319   | 1319    | `leddevice.bss` | 2,708 | 80 Row  | 12        |
| 1      | 1137 to 1149   | 1149    | `leddevice.bss` | 470   | 16 Row  | 9         |

| Layout | File            | Known            | Unknown    |
| ------ | --------------- | ---------------- | ---------- |
| 4      | `leddevice.bss` | 3,028 B (100.0%) | 0 B (0.0%) |
| 3      | `leddevice.bss` | 2,868 B (100.0%) | 0 B (0.0%) |
| 2      | `leddevice.bss` | 2,708 B (100.0%) | 0 B (0.0%) |
| 1      | `leddevice.bss` | 470 B (100.0%)   | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 4 | `a34a1afb9162`  |
| 3482   | Layout 4 | `a34a1afb9162`  |
| 3474   | Layout 4 | `a34a1afb9162`  |
| 3473   | Layout 4 | `a34a1afb9162`  |
| 3464   | Layout 4 | `a34a1afb9162`  |
| 3458   | Layout 4 | `a34a1afb9162`  |
| 3454   | Layout 4 | `a34a1afb9162`  |
| 3444   | Layout 4 | `a34a1afb9162`  |
| 3435   | Layout 4 | `a34a1afb9162`  |
| 3426   | Layout 4 | `a34a1afb9162`  |
| 3418   | Layout 4 | `a34a1afb9162`  |
| 3412   | Layout 4 | `a34a1afb9162`  |
| 3402   | Layout 4 | `a34a1afb9162`  |
| 3396   | Layout 4 | `a34a1afb9162`  |
| 3387   | Layout 4 | `a34a1afb9162`  |
| 3381   | Layout 4 | `a34a1afb9162`  |
| 3373   | Layout 4 | `a34a1afb9162`  |
| 3364   | Layout 4 | `a34a1afb9162`  |
| 3356   | Layout 4 | `a34a1afb9162`  |
| 3349   | Layout 4 | `a34a1afb9162`  |
| 3342   | Layout 4 | `a34a1afb9162`  |
| 3335   | Layout 4 | `a34a1afb9162`  |
| 3326   | Layout 4 | `a34a1afb9162`  |
| 3321   | Layout 4 | `a34a1afb9162`  |
| 3314   | Layout 4 | `a34a1afb9162`  |
| 3303   | Layout 4 | `a34a1afb9162`  |
| 3302   | Layout 4 | `a34a1afb9162`  |
| 3293   | Layout 4 | `a34a1afb9162`  |
| 3283   | Layout 4 | `a34a1afb9162`  |
| 3275   | Layout 4 | `a34a1afb9162`  |
| 3267   | Layout 4 | `a34a1afb9162`  |
| 3258   | Layout 4 | `a34a1afb9162`  |
| 3251   | Layout 4 | `a34a1afb9162`  |
| 3242   | Layout 4 | `a34a1afb9162`  |
| 3235   | Layout 4 | `a34a1afb9162`  |
| 3229   | Layout 4 | `a34a1afb9162`  |
| 3212   | Layout 4 | `a34a1afb9162`  |
| 3203   | Layout 4 | `a34a1afb9162`  |
| 3193   | Layout 4 | `a34a1afb9162`  |
| 3186   | Layout 4 | `a34a1afb9162`  |
| 3177   | Layout 4 | `a34a1afb9162`  |
| 3169   | Layout 4 | `a34a1afb9162`  |
| 3158   | Layout 4 | `a34a1afb9162`  |
| 3151   | Layout 4 | `a34a1afb9162`  |
| 3144   | Layout 4 | `a34a1afb9162`  |
| 3133   | Layout 4 | `a34a1afb9162`  |
| 3125   | Layout 4 | `a34a1afb9162`  |
| 3118   | Layout 4 | `a34a1afb9162`  |
| 3111   | Layout 4 | `a34a1afb9162`  |
| 3103   | Layout 4 | `a34a1afb9162`  |
| 3095   | Layout 4 | `a34a1afb9162`  |
| 3086   | Layout 4 | `a34a1afb9162`  |
| 3072   | Layout 4 | `a34a1afb9162`  |
| 3062   | Layout 4 | `a34a1afb9162`  |
| 3052   | Layout 4 | `a34a1afb9162`  |
| 3045   | Layout 4 | `a34a1afb9162`  |
| 3037   | Layout 4 | `a34a1afb9162`  |
| 3030   | Layout 4 | `a34a1afb9162`  |
| 3021   | Layout 4 | `a34a1afb9162`  |
| 3012   | Layout 4 | `a34a1afb9162`  |
| 3002   | Layout 4 | `a34a1afb9162`  |
| 2995   | Layout 4 | `a34a1afb9162`  |
| 2987   | Layout 4 | `a34a1afb9162`  |
| 2978   | Layout 4 | `a34a1afb9162`  |
| 2970   | Layout 4 | `a34a1afb9162`  |
| 2959   | Layout 4 | `a34a1afb9162`  |
| 2951   | Layout 4 | `a34a1afb9162`  |
| 2942   | Layout 4 | `a34a1afb9162`  |
| 2935   | Layout 4 | `a34a1afb9162`  |
| 2932   | Layout 4 | `a34a1afb9162`  |
| 2923   | Layout 4 | `a34a1afb9162`  |
| 2919   | Layout 4 | `a34a1afb9162`  |
| 2907   | Layout 4 | `a34a1afb9162`  |
| 2900   | Layout 4 | `a34a1afb9162`  |
| 2891   | Layout 4 | `a34a1afb9162`  |
| 2882   | Layout 4 | `a34a1afb9162`  |
| 2872   | Layout 4 | `a34a1afb9162`  |
| 2863   | Layout 4 | `a34a1afb9162`  |
| 2855   | Layout 4 | `a34a1afb9162`  |
| 2849   | Layout 4 | `a34a1afb9162`  |
| 2844   | Layout 4 | `a34a1afb9162`  |
| 2834   | Layout 4 | `a34a1afb9162`  |
| 2825   | Layout 4 | `a34a1afb9162`  |
| 2819   | Layout 4 | `a34a1afb9162`  |
| 2811   | Layout 4 | `a34a1afb9162`  |
| 2803   | Layout 4 | `a34a1afb9162`  |
| 2794   | Layout 4 | `a34a1afb9162`  |
| 2783   | Layout 4 | `a34a1afb9162`  |
| 2774   | Layout 4 | `a34a1afb9162`  |
| 2765   | Layout 4 | `a34a1afb9162`  |
| 2756   | Layout 4 | `a34a1afb9162`  |
| 2750   | Layout 4 | `a34a1afb9162`  |
| 2743   | Layout 4 | `a34a1afb9162`  |
| 2736   | Layout 4 | `a34a1afb9162`  |
| 2726   | Layout 4 | `a34a1afb9162`  |
| 2717   | Layout 4 | `a34a1afb9162`  |
| 2709   | Layout 4 | `a34a1afb9162`  |
| 2703   | Layout 4 | `a34a1afb9162`  |
| 2695   | Layout 4 | `a34a1afb9162`  |
| 2684   | Layout 4 | `a34a1afb9162`  |
| 2672   | Layout 4 | `a34a1afb9162`  |
| 2665   | Layout 4 | `a34a1afb9162`  |
| 2657   | Layout 4 | `a34a1afb9162`  |
| 2649   | Layout 4 | `a34a1afb9162`  |
| 2644   | Layout 4 | `a34a1afb9162`  |
| 2637   | Layout 4 | `a34a1afb9162`  |
| 2629   | Layout 4 | `a34a1afb9162`  |
| 2619   | Layout 4 | `a34a1afb9162`  |
| 2612   | Layout 4 | `a34a1afb9162`  |
| 2606   | Layout 4 | `a34a1afb9162`  |
| 2602   | Layout 4 | `a34a1afb9162`  |
| 2601   | Layout 4 | `a34a1afb9162`  |
| 2592   | Layout 4 | `a34a1afb9162`  |
| 2583   | Layout 4 | `a34a1afb9162`  |
| 2575   | Layout 4 | `a34a1afb9162`  |
| 2567   | Layout 4 | `a34a1afb9162`  |
| 2560   | Layout 4 | `a34a1afb9162`  |
| 2553   | Layout 4 | `a34a1afb9162`  |
| 2545   | Layout 4 | `a34a1afb9162`  |
| 2538   | Layout 4 | `a34a1afb9162`  |
| 2529   | Layout 4 | `a34a1afb9162`  |
| 2519   | Layout 4 | `a34a1afb9162`  |
| 2513   | Layout 4 | `a34a1afb9162`  |
| 2510   | Layout 4 | `a34a1afb9162`  |
| 2507   | Layout 4 | `a34a1afb9162`  |
| 2503   | Layout 4 | `a34a1afb9162`  |
| 2498   | Layout 4 | `a34a1afb9162`  |
| 2492   | Layout 4 | `a34a1afb9162`  |
| 2487   | Layout 4 | `a34a1afb9162`  |
| 2480   | Layout 4 | `a34a1afb9162`  |
| 2474   | Layout 4 | `a34a1afb9162`  |
| 2468   | Layout 4 | `a34a1afb9162`  |
| 2460   | Layout 4 | `a34a1afb9162`  |
| 2453   | Layout 4 | `a34a1afb9162`  |
| 2444   | Layout 4 | `a34a1afb9162`  |
| 2438   | Layout 4 | `a34a1afb9162`  |
| 2434   | Layout 4 | `a34a1afb9162`  |
| 2429   | Layout 4 | `a34a1afb9162`  |
| 2421   | Layout 4 | `a34a1afb9162`  |
| 2414   | Layout 4 | `a34a1afb9162`  |
| 2407   | Layout 4 | `a34a1afb9162`  |
| 2401   | Layout 4 | `a34a1afb9162`  |
| 2397   | Layout 4 | `a34a1afb9162`  |
| 2393   | Layout 4 | `a34a1afb9162`  |
| 2384   | Layout 4 | `a34a1afb9162`  |
| 2378   | Layout 4 | `a34a1afb9162`  |
| 2372   | Layout 4 | `a34a1afb9162`  |
| 2358   | Layout 4 | `a34a1afb9162`  |
| 2352   | Layout 4 | `a34a1afb9162`  |
| 2347   | Layout 4 | `a34a1afb9162`  |
| 2343   | Layout 4 | `a34a1afb9162`  |
| 2335   | Layout 4 | `a34a1afb9162`  |
| 2327   | Layout 4 | `a34a1afb9162`  |
| 2324   | Layout 4 | `a34a1afb9162`  |
| 2319   | Layout 4 | `a34a1afb9162`  |
| 2313   | Layout 4 | `a34a1afb9162`  |
| 2308   | Layout 4 | `a34a1afb9162`  |
| 2302   | Layout 4 | `a34a1afb9162`  |
| 2295   | Layout 4 | `a34a1afb9162`  |
| 2290   | Layout 4 | `a34a1afb9162`  |
| 2284   | Layout 4 | `a34a1afb9162`  |
| 2276   | Layout 4 | `a34a1afb9162`  |
| 2269   | Layout 4 | `a34a1afb9162`  |
| 2259   | Layout 4 | `a34a1afb9162`  |
| 2250   | Layout 4 | `a34a1afb9162`  |
| 2243   | Layout 4 | `a34a1afb9162`  |
| 2235   | Layout 4 | `a34a1afb9162`  |
| 2229   | Layout 4 | `a34a1afb9162`  |
| 2224   | Layout 4 | `a34a1afb9162`  |
| 2218   | Layout 4 | `a34a1afb9162`  |
| 2215   | Layout 4 | `a34a1afb9162`  |
| 2207   | Layout 4 | `a34a1afb9162`  |
| 2203   | Layout 4 | `a34a1afb9162`  |
| 2196   | Layout 4 | `a34a1afb9162`  |
| 2192   | Layout 4 | `a34a1afb9162`  |
| 2189   | Layout 4 | `a34a1afb9162`  |
| 2183   | Layout 4 | `a34a1afb9162`  |
| 2179   | Layout 4 | `a34a1afb9162`  |
| 2171   | Layout 4 | `a34a1afb9162`  |
| 2163   | Layout 4 | `a34a1afb9162`  |
| 2156   | Layout 4 | `a34a1afb9162`  |
| 2151   | Layout 4 | `a34a1afb9162`  |
| 2147   | Layout 4 | `a34a1afb9162`  |
| 2142   | Layout 4 | `a34a1afb9162`  |
| 2138   | Layout 4 | `a34a1afb9162`  |
| 2134   | Layout 4 | `a34a1afb9162`  |
| 2130   | Layout 4 | `a34a1afb9162`  |
| 2122   | Layout 4 | `a34a1afb9162`  |
| 2107   | Layout 4 | `a34a1afb9162`  |
| 2098   | Layout 4 | `a34a1afb9162`  |
| 2089   | Layout 4 | `a34a1afb9162`  |
| 2081   | Layout 4 | `a34a1afb9162`  |
| 2073   | Layout 4 | `a34a1afb9162`  |
| 2067   | Layout 4 | `a34a1afb9162`  |
| 2063   | Layout 4 | `a34a1afb9162`  |
| 2059   | Layout 4 | `a34a1afb9162`  |
| 2052   | Layout 4 | `a34a1afb9162`  |
| 2044   | Layout 4 | `a34a1afb9162`  |
| 2039   | Layout 4 | `a34a1afb9162`  |
| 2032   | Layout 4 | `a34a1afb9162`  |
| 2025   | Layout 4 | `a34a1afb9162`  |
| 2011   | Layout 4 | `a34a1afb9162`  |
| 2005   | Layout 4 | `a34a1afb9162`  |
| 2000   | Layout 4 | `a34a1afb9162`  |
| 1996   | Layout 4 | `a34a1afb9162`  |
| 1991   | Layout 4 | `a34a1afb9162`  |
| 1985   | Layout 4 | `a34a1afb9162`  |
| 1980   | Layout 4 | `a34a1afb9162`  |
| 1969   | Layout 4 | `a34a1afb9162`  |
| 1964   | Layout 4 | `a34a1afb9162`  |
| 1958   | Layout 4 | `a34a1afb9162`  |
| 1950   | Layout 4 | `a34a1afb9162`  |
| 1945   | Layout 4 | `a34a1afb9162`  |
| 1937   | Layout 4 | `a34a1afb9162`  |
| 1933   | Layout 4 | `a34a1afb9162`  |
| 1927   | Layout 4 | `a34a1afb9162`  |
| 1921   | Layout 4 | `a34a1afb9162`  |
| 1914   | Layout 4 | `a34a1afb9162`  |
| 1908   | Layout 4 | `a34a1afb9162`  |
| 1897   | Layout 4 | `a34a1afb9162`  |
| 1892   | Layout 4 | `a34a1afb9162`  |
| 1886   | Layout 4 | `a34a1afb9162`  |
| 1881   | Layout 4 | `a34a1afb9162`  |
| 1871   | Layout 4 | `a34a1afb9162`  |
| 1866   | Layout 4 | `a34a1afb9162`  |
| 1862   | Layout 4 | `a34a1afb9162`  |
| 1854   | Layout 4 | `a34a1afb9162`  |
| 1846   | Layout 4 | `a34a1afb9162`  |
| 1838   | Layout 4 | `a34a1afb9162`  |
| 1832   | Layout 4 | `a34a1afb9162`  |
| 1826   | Layout 4 | `a34a1afb9162`  |
| 1822   | Layout 4 | `a34a1afb9162`  |
| 1818   | Layout 4 | `a34a1afb9162`  |
| 1804   | Layout 4 | `a34a1afb9162`  |
| 1794   | Layout 4 | `a34a1afb9162`  |
| 1790   | Layout 4 | `a34a1afb9162`  |
| 1784   | Layout 4 | `a34a1afb9162`  |
| 1774   | Layout 4 | `a34a1afb9162`  |
| 1771   | Layout 4 | `a34a1afb9162`  |
| 1762   | Layout 4 | `a34a1afb9162`  |
| 1759   | Layout 4 | `a34a1afb9162`  |
| 1754   | Layout 4 | `a34a1afb9162`  |
| 1749   | Layout 4 | `a34a1afb9162`  |
| 1743   | Layout 4 | `a34a1afb9162`  |
| 1737   | Layout 4 | `a34a1afb9162`  |
| 1731   | Layout 4 | `a34a1afb9162`  |
| 1725   | Layout 4 | `a34a1afb9162`  |
| 1717   | Layout 4 | `a34a1afb9162`  |
| 1710   | Layout 4 | `a34a1afb9162`  |
| 1704   | Layout 4 | `a34a1afb9162`  |
| 1698   | Layout 4 | `a34a1afb9162`  |
| 1690   | Layout 4 | `a34a1afb9162`  |
| 1685   | Layout 4 | `a34a1afb9162`  |
| 1680   | Layout 4 | `a34a1afb9162`  |
| 1674   | Layout 4 | `a34a1afb9162`  |
| 1668   | Layout 4 | `a34a1afb9162`  |
| 1659   | Layout 4 | `a34a1afb9162`  |
| 1649   | Layout 4 | `a34a1afb9162`  |
| 1642   | Layout 4 | `a34a1afb9162`  |
| 1636   | Layout 4 | `a34a1afb9162`  |
| 1628   | Layout 4 | `a34a1afb9162`  |
| 1622   | Layout 4 | `a34a1afb9162`  |
| 1614   | Layout 4 | `a34a1afb9162`  |
| 1608   | Layout 4 | `a34a1afb9162`  |
| 1602   | Layout 4 | `a34a1afb9162`  |
| 1598   | Layout 4 | `a34a1afb9162`  |
| 1594   | Layout 4 | `a34a1afb9162`  |
| 1590   | Layout 4 | `a34a1afb9162`  |
| 1587   | Layout 4 | `a34a1afb9162`  |
| 1584   | Layout 4 | `a34a1afb9162`  |
| 1579   | Layout 4 | `a34a1afb9162`  |
| 1572   | Layout 4 | `a34a1afb9162`  |
| 1565   | Layout 4 | `a34a1afb9162`  |
| 1559   | Layout 4 | `a34a1afb9162`  |
| 1554   | Layout 4 | `a34a1afb9162`  |
| 1547   | Layout 4 | `a34a1afb9162`  |
| 1537   | Layout 4 | `a34a1afb9162`  |
| 1529   | Layout 4 | `a34a1afb9162`  |
| 1524   | Layout 4 | `a34a1afb9162`  |
| 1519   | Layout 4 | `a34a1afb9162`  |
| 1509   | Layout 4 | `a34a1afb9162`  |
| 1506   | Layout 4 | `a34a1afb9162`  |
| 1504   | Layout 4 | `a34a1afb9162`  |
| 1500   | Layout 4 | `a34a1afb9162`  |
| 1493   | Layout 4 | `a34a1afb9162`  |
| 1489   | Layout 4 | `a34a1afb9162`  |
| 1485   | Layout 4 | `a34a1afb9162`  |
| 1481   | Layout 4 | `a34a1afb9162`  |
| 1474   | Layout 4 | `a34a1afb9162`  |
| 1466   | Layout 4 | `a34a1afb9162`  |
| 1462   | Layout 4 | `a34a1afb9162`  |
| 1459   | Layout 4 | `a34a1afb9162`  |
| 1453   | Layout 4 | `a34a1afb9162`  |
| 1450   | Layout 4 | `a34a1afb9162`  |
| 1445   | Layout 4 | `a34a1afb9162`  |
| 1439   | Layout 4 | `a34a1afb9162`  |
| 1433   | Layout 4 | `a34a1afb9162`  |
| 1430   | Layout 4 | `a34a1afb9162`  |
| 1426   | Layout 4 | `a34a1afb9162`  |
| 1421   | Layout 4 | `a34a1afb9162`  |
| 1417   | Layout 4 | `a34a1afb9162`  |
| 1416   | Layout 4 | `a34a1afb9162`  |
| 1409   | Layout 4 | `a34a1afb9162`  |
| 1405   | Layout 4 | `a34a1afb9162`  |
| 1401   | Layout 4 | `a34a1afb9162`  |
| 1396   | Layout 4 | `a34a1afb9162`  |
| 1391   | Layout 4 | `a34a1afb9162`  |
| 1390   | Layout 4 | `a34a1afb9162`  |
| 1386   | Layout 4 | `a34a1afb9162`  |
| 1381   | Layout 4 | `a34a1afb9162`  |
| 1379   | Layout 4 | `a34a1afb9162`  |
| 1372   | Layout 4 | `a34a1afb9162`  |
| 1366   | Layout 4 | `a34a1afb9162`  |
| 1364   | Layout 4 | `a34a1afb9162`  |
| 1363   | Layout 4 | `a34a1afb9162`  |
| 1360   | Layout 4 | `a34a1afb9162`  |
| 1358   | Layout 4 | `a34a1afb9162`  |
| 1355   | Layout 4 | `a34a1afb9162`  |
| 1351   | Layout 4 | `a34a1afb9162`  |
| 1348   | Layout 4 | `a34a1afb9162`  |
| 1346   | Layout 4 | `a34a1afb9162`  |
| 1341   | Layout 4 | `a34a1afb9162`  |
| 1340   | Layout 4 | `a34a1afb9162`  |
| 1338   | Layout 4 | `a34a1afb9162`  |
| 1335   | Layout 4 | `a34a1afb9162`  |
| 1333   | Layout 3 | `a34a1afb9162`  |
| 1329   | Layout 3 | `a34a1afb9162`  |
| 1327   | Layout 3 | `a34a1afb9162`  |
| 1324   | Layout 3 | `a34a1afb9162`  |
| 1321   | Layout 3 | `a34a1afb9162`  |
| 1319   | Layout 2 | `a34a1afb9162`  |
| 1318   | Layout 2 | `a34a1afb9162`  |
| 1316   | Layout 2 | `a34a1afb9162`  |
| 1313   | Layout 2 | `a34a1afb9162`  |
| 1311   | Layout 2 | `a34a1afb9162`  |
| 1309   | Layout 2 | `a34a1afb9162`  |
| 1304   | Layout 2 | `a34a1afb9162`  |
| 1292   | Layout 2 | `a34a1afb9162`  |
| 1286   | Layout 2 | `a34a1afb9162`  |
| 1280   | Layout 2 | `a34a1afb9162`  |
| 1276   | Layout 2 | `a34a1afb9162`  |
| 1267   | Layout 2 | `a34a1afb9162`  |
| 1261   | Layout 2 | `a34a1afb9162`  |
| 1256   | Layout 2 | `a34a1afb9162`  |
| 1250   | Layout 2 | `a34a1afb9162`  |
| 1246   | Layout 2 | `a34a1afb9162`  |
| 1239   | Layout 2 | `a34a1afb9162`  |
| 1230   | Layout 2 | `a34a1afb9162`  |
| 1226   | Layout 2 | `a34a1afb9162`  |
| 1220   | Layout 2 | `a34a1afb9162`  |
| 1217   | Layout 2 | `a34a1afb9162`  |
| 1211   | Layout 2 | `a34a1afb9162`  |
| 1210   | Layout 2 | `a34a1afb9162`  |
| 1208   | Layout 2 | `a34a1afb9162`  |
| 1203   | Layout 2 | `a34a1afb9162`  |
| 1197   | Layout 2 | `a34a1afb9162`  |
| 1194   | Layout 2 | `a34a1afb9162`  |
| 1192   | Layout 2 | `a34a1afb9162`  |
| 1187   | Layout 2 | `a34a1afb9162`  |
| 1183   | Layout 2 | `a34a1afb9162`  |
| 1177   | Layout 2 | `a34a1afb9162`  |
| 1173   | Layout 2 | `a34a1afb9162`  |
| 1167   | Layout 2 | `a34a1afb9162`  |
| 1164   | Layout 2 | `a34a1afb9162`  |
| 1156   | Layout 2 | `a34a1afb9162`  |
| 1149   | Layout 1 | `a34a1afb9162`  |
| 1144   | Layout 1 | `a34a1afb9162`  |
| 1137   | Layout 1 | `a34a1afb9162`  |
| 1132   | No file  | `a34a1afb9162`  |
| 1127   | No file  | `a34a1afb9162`  |
| 1122   | No file  | `a34a1afb9162`  |
| 1118   | No file  | `a34a1afb9162`  |
| 1114   | No file  | `a34a1afb9162`  |
| 1109   | No file  | `a34a1afb9162`  |
| 1102   | No file  | `a34a1afb9162`  |
| 1096   | No file  | `a34a1afb9162`  |
| 1088   | No file  | `a34a1afb9162`  |
| 1081   | No file  | `a34a1afb9162`  |
| 1076   | No file  | `a34a1afb9162`  |
| 1069   | No file  | `a34a1afb9162`  |
| 1064   | No file  | `a34a1afb9162`  |
| 1058   | No file  | `a34a1afb9162`  |
| 1051   | No file  | `a34a1afb9162`  |
| 1044   | No file  | `a34a1afb9162`  |
| 1036   | No file  | `a34a1afb9162`  |
| 1026   | No file  | `a34a1afb9162`  |
| 1016   | No file  | `a34a1afb9162`  |
| 1009   | No file  | `a34a1afb9162`  |
| 1005   | No file  | `a34a1afb9162`  |
| 1000   | No file  | `a34a1afb9162`  |
| 998    | No file  | `a34a1afb9162`  |
| 990    | No file  | `a34a1afb9162`  |
| 979    | No file  | `a34a1afb9162`  |
| 972    | No file  | `a34a1afb9162`  |
| 963    | No file  | `a34a1afb9162`  |
| 955    | No file  | `a34a1afb9162`  |
| 946    | No file  | `a34a1afb9162`  |
| 938    | No file  | `a34a1afb9162`  |
| 927    | No file  | `a34a1afb9162`  |
| 911    | No file  | `a34a1afb9162`  |
| 904    | No file  | `a34a1afb9162`  |
| 899    | No file  | `a34a1afb9162`  |
| 894    | No file  | `a34a1afb9162`  |
| 885    | No file  | `a34a1afb9162`  |
| 879    | No file  | `a34a1afb9162`  |
| 872    | No file  | `a34a1afb9162`  |
| 864    | No file  | `a34a1afb9162`  |
| 855    | No file  | `a34a1afb9162`  |
| 853    | No file  | `a34a1afb9162`  |
| 845    | No file  | `a34a1afb9162`  |
| 837    | No file  | `a34a1afb9162`  |
| 829    | No file  | `a34a1afb9162`  |
| 822    | No file  | `a34a1afb9162`  |
| 814    | No file  | `a34a1afb9162`  |
| 805    | No file  | `a34a1afb9162`  |
| 794    | No file  | `a34a1afb9162`  |
| 787    | No file  | `a34a1afb9162`  |
| 780    | No file  | `a34a1afb9162`  |
| 771    | No file  | `a34a1afb9162`  |
| 760    | No file  | `a34a1afb9162`  |
| 748    | No file  | `a34a1afb9162`  |
| 741    | No file  | `a34a1afb9162`  |
| 736    | No file  | `a34a1afb9162`  |
| 731    | No file  | `a34a1afb9162`  |
| 723    | No file  | `a34a1afb9162`  |
| 711    | No file  | `a34a1afb9162`  |
| 707    | No file  | `a34a1afb9162`  |
| 697    | No file  | `a34a1afb9162`  |
| 689    | No file  | `a34a1afb9162`  |
| 683    | No file  | `a34a1afb9162`  |
| 678    | No file  | `a34a1afb9162`  |
| 670    | No file  | `a34a1afb9162`  |
| 661    | No file  | `a34a1afb9162`  |
| 656    | No file  | `a34a1afb9162`  |
| 652    | No file  | `a34a1afb9162`  |
| 643    | No file  | `a34a1afb9162`  |
| 637    | No file  | `a34a1afb9162`  |
| 630    | No file  | `a34a1afb9162`  |
| 627    | No file  | `a34a1afb9162`  |
| 621    | No file  | `a34a1afb9162`  |
| 617    | No file  | `a34a1afb9162`  |
| 615    | No file  | `a34a1afb9162`  |
| 606    | No file  | `a34a1afb9162`  |
| 599    | No file  | `a34a1afb9162`  |
| 592    | No file  | `a34a1afb9162`  |
| 586    | No file  | `a34a1afb9162`  |
| 577    | No file  | `a34a1afb9162`  |
| 569    | No file  | `a34a1afb9162`  |
| 561    | No file  | `a34a1afb9162`  |
| 554    | No file  | `a34a1afb9162`  |
| 542    | No file  | `a34a1afb9162`  |
| 532    | No file  | `a34a1afb9162`  |
| 531    | No file  | `a34a1afb9162`  |
| 526    | No file  | `a34a1afb9162`  |
| 521    | No file  | `a34a1afb9162`  |
| 517    | No file  | `a34a1afb9162`  |
| 510    | No file  | `a34a1afb9162`  |
| 508    | No file  | `a34a1afb9162`  |
| 504    | No file  | `a34a1afb9162`  |
| 497    | No file  | `a34a1afb9162`  |
| 491    | No file  | `a34a1afb9162`  |
| 485    | No file  | `a34a1afb9162`  |
| 478    | No file  | `a34a1afb9162`  |
| 472    | No file  | `a34a1afb9162`  |
| 466    | No file  | `a34a1afb9162`  |
| 457    | No file  | `a34a1afb9162`  |
| 452    | No file  | `a34a1afb9162`  |
| 449    | No file  | `a34a1afb9162`  |
| 435    | No file  | `a34a1afb9162`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 4

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of rows, one per animation and device  |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (16 bytes)

| Offset  | Type | Field        | Notes                                                                        |
| ------- | ---- | ------------ | ---------------------------------------------------------------------------- |
| `+0x00` | u16  | device_type  | `0`, `1`, `3`, `4` or `5`; see Device Types                                  |
| `+0x02` | u16  | animation_no | The number `ToClient_StartLedDeviceAnimation` takes, `1` to `16`; see Animations |
| `+0x04` | u32  | asus_ref     | String table index of the Asus effect name; the empty string for types `3` to `5` |
| `+0x08` | u32  | razer_ref    | String table index of the Razer effect name                                  |
| `+0x0C` | i32  | real_rgb     | Colour as `0xRRGGBB`; `-1` for types `3` to `5`                              |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                          |
| ------- | ------------------ | ------------ | -------------------------------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `91` on client 3482                         |
| `+0x04` | pstr[string_count] | strings      | UTF-8 effect names in first-use order, starting with the empty string |

## Layout 3

### Row (14 bytes)

| Offset  | Type | Field        | Notes                                                                    |
| ------- | ---- | ------------ | ------------------------------------------------------------------------ |
| `+0x00` | u16  | device_type  | As in Layout 4                                                           |
| `+0x02` | u16  | animation_no | As in Layout 4                                                           |
| `+0x04` | u32  | asus_ref     | String table index of the Asus effect name                               |
| `+0x08` | u32  | razer_ref    | String table index of the Razer effect name                              |
| `+0x0C` | i16  | real_rgb     | The low 16 bits of the Layout 4 colour (`0x9B29` for `#FF9B29`); `-1` for types `3` to `5` |

## Layout 2

### Row (12 bytes)

| Offset  | Type | Field        | Notes                                      |
| ------- | ---- | ------------ | ------------------------------------------ |
| `+0x00` | u16  | device_type  | As in Layout 4                             |
| `+0x02` | u16  | animation_no | As in Layout 4                             |
| `+0x04` | u32  | asus_ref     | String table index of the Asus effect name  |
| `+0x08` | u32  | razer_ref    | String table index of the Razer effect name |

## Layout 1

### Row (9 bytes)

| Offset  | Type | Field        | Notes                                                    |
| ------- | ---- | ------------ | -------------------------------------------------------- |
| `+0x00` | u8   | animation_no | `1` to `16`, one row each; there is no device type       |
| `+0x01` | u32  | asus_ref     | String table index of the Asus effect name               |
| `+0x05` | u32  | razer_ref    | String table index of the Razer effect name              |

## Device Types

Every animation has one row per type. The Razer effect name of a type
ends in the suffix below:

| `device_type` | Razer suffix | Asus effect |
| ------------- | ------------ | ----------- |
| `0`           | none         | yes         |
| `1`           | `Mouse`      | yes         |
| `3`           | `Headset`    | none        |
| `4`           | `Mousepad`   | none        |
| `5`           | `Link`       | none        |

## Animations

Client 3482, the Razer effect of `device_type` `0` and its `real_rgb`:

| `animation_no` | Razer effect         | `real_rgb` |
| -------------- | -------------------- | ---------- |
| `1`            | `EnhancementFailed`  | `#FF0000`  |
| `2`            | `EnhancementSuccess` | `#ECD78E`  |
| `3`            | `LowHP`              | `#FF0000`  |
| `4`            | `Morning`            | `#FF7F27`  |
| `5`            | `Night`              | `#A3A3A3`  |
| `6`            | `Loading`            | `#C3C3C3`  |
| `7`            | `EnhancementLoading` | `#72FF6D`  |
| `8`            | `GetItem`            | `#4339FF`  |
| `9`            | `InvenFull`          | `#FF0000`  |
| `10`           | `LevelUp`            | `#2950FF`  |
| `11`           | `NewMail`            | `#FFE229`  |
| `12`           | `BossNotice`         | `#B4FF29`  |
| `13`           | `GoldenBell`         | `#FF9B29`  |
| `14`           | `LowHP4020`          | `#FF9B29`  |
| `15`           | `Black100`           | `#B029FF`  |
| `16`           | `UnderWater`         | `#29A6FF`  |

The Asus effect names match the Razer ones, with a `1` added on
animations `6`, `10`, `12`, `15` and `16` (`Loading1`, `LoadingMouse1`).

## Field Names

The names are the `AnimationNo`, `DeviceType`, `Asus`, `Razer` and
`RealRGB` columns of the `Leddevice` sheet of a private server's
`DataSheets.bexcel` on client 1784; the file stores `DeviceType` before
`AnimationNo`. All 80 of the sheet's rows match the file on all five
columns, keyed by animation and device type (an empty cell is the empty
string or `-1`). The client 1784 and client 3482 files are the same
3,028 bytes.

The client Lua of client 3482 calls `ToClient_StartLedDeviceAnimation(12)`
on a Kzarka or Nuberu boss notice (`noticealert.lua`) and
`ToClient_StartLedDeviceAnimation(6)` at the end of `Panel_Logo_Init`
(`panel_logo.lua`), as the client starts: animation `12` is `BossNotice`
and `6` is `Loading`.
The game option `UseLedAnimation` (`setUseLedAnimation`) turns the
effects on and off.

## Notes

- Layout 1 has one row per animation and no device type; its effect
  names are those of `device_type` `0`. Layout 2 adds the device types,
  Layout 3 the colour as an i16 (the low 16 bits of the Layout 4 value),
  Layout 4 the full i32 colour.
- The rows run animation by animation, devices `5`, `4`, `3`, `1`, `0`
  within each, in an order that is not the animation number.
- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/client_tables.py`, with
  the two effect names and the colour.

## Open Questions

### Device Type 2

No row has `device_type` `2`. The Razer Chroma device kinds the names
follow (keyboard, mouse, headset, mousepad, Chroma Link) also have a
keypad, which may be the missing type, but no client file names the
types.
