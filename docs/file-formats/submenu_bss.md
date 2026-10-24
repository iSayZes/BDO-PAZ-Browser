# `submenu.bss` Format

## Purpose

The entries of the main menu (Esc menu) categories in
[`menu.bss`](menu_bss.md): one 49-byte entry per menu item, grouped by
category, with its title as a UI string key and its icon as a region of a
shared sprite sheet.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File          | Bytes  | Records                  | Row bytes |
| ------ | -------------- | ------- | ------------- | ------ | ------------------------ | --------- |
| 1      | 1466 and later | 3483    | `submenu.bss` | 12,882 | 155 Menu Entry, 12 Group | 49        |

| Layout | File          | Known            | Unknown         |
| ------ | ------------- | ---------------- | --------------- |
| 1      | `submenu.bss` | 11,487 B (89.2%) | 1,395 B (10.8%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `5cdeabc23a0d`  |
| 3482   | Layout 1 | `5cdeabc23a0d`  |
| 3474   | Layout 1 | `5cdeabc23a0d`  |
| 3473   | Layout 1 | `5cdeabc23a0d`  |
| 3464   | Layout 1 | `5cdeabc23a0d`  |
| 3458   | Layout 1 | `5cdeabc23a0d`  |
| 3454   | Layout 1 | `5cdeabc23a0d`  |
| 3444   | Layout 1 | `5cdeabc23a0d`  |
| 3435   | Layout 1 | `5cdeabc23a0d`  |
| 3426   | Layout 1 | `5cdeabc23a0d`  |
| 3418   | Layout 1 | `5cdeabc23a0d`  |
| 3412   | Layout 1 | `5cdeabc23a0d`  |
| 3402   | Layout 1 | `5cdeabc23a0d`  |
| 3396   | Layout 1 | `5cdeabc23a0d`  |
| 3387   | Layout 1 | `5cdeabc23a0d`  |
| 3381   | Layout 1 | `5cdeabc23a0d`  |
| 3373   | Layout 1 | `5cdeabc23a0d`  |
| 3364   | Layout 1 | `5cdeabc23a0d`  |
| 3356   | Layout 1 | `5cdeabc23a0d`  |
| 3349   | Layout 1 | `5cdeabc23a0d`  |
| 3342   | Layout 1 | `5cdeabc23a0d`  |
| 3335   | Layout 1 | `5cdeabc23a0d`  |
| 3326   | Layout 1 | `5cdeabc23a0d`  |
| 3321   | Layout 1 | `5cdeabc23a0d`  |
| 3314   | Layout 1 | `5cdeabc23a0d`  |
| 3303   | Layout 1 | `5cdeabc23a0d`  |
| 3302   | Layout 1 | `5cdeabc23a0d`  |
| 3293   | Layout 1 | `5cdeabc23a0d`  |
| 3283   | Layout 1 | `5cdeabc23a0d`  |
| 3275   | Layout 1 | `5cdeabc23a0d`  |
| 3267   | Layout 1 | `5cdeabc23a0d`  |
| 3258   | Layout 1 | `5cdeabc23a0d`  |
| 3251   | Layout 1 | `5cdeabc23a0d`  |
| 3242   | Layout 1 | `5cdeabc23a0d`  |
| 3235   | Layout 1 | `5cdeabc23a0d`  |
| 3229   | Layout 1 | `5cdeabc23a0d`  |
| 3212   | Layout 1 | `5cdeabc23a0d`  |
| 3203   | Layout 1 | `5cdeabc23a0d`  |
| 3193   | Layout 1 | `5cdeabc23a0d`  |
| 3186   | Layout 1 | `5cdeabc23a0d`  |
| 3177   | Layout 1 | `5cdeabc23a0d`  |
| 3169   | Layout 1 | `5cdeabc23a0d`  |
| 3158   | Layout 1 | `5cdeabc23a0d`  |
| 3151   | Layout 1 | `5cdeabc23a0d`  |
| 3144   | Layout 1 | `5cdeabc23a0d`  |
| 3133   | Layout 1 | `5cdeabc23a0d`  |
| 3125   | Layout 1 | `5cdeabc23a0d`  |
| 3118   | Layout 1 | `5cdeabc23a0d`  |
| 3111   | Layout 1 | `5cdeabc23a0d`  |
| 3103   | Layout 1 | `5cdeabc23a0d`  |
| 3095   | Layout 1 | `5cdeabc23a0d`  |
| 3086   | Layout 1 | `5cdeabc23a0d`  |
| 3072   | Layout 1 | `5cdeabc23a0d`  |
| 3062   | Layout 1 | `5cdeabc23a0d`  |
| 3052   | Layout 1 | `5cdeabc23a0d`  |
| 3045   | Layout 1 | `5cdeabc23a0d`  |
| 3037   | Layout 1 | `5cdeabc23a0d`  |
| 3030   | Layout 1 | `5cdeabc23a0d`  |
| 3021   | Layout 1 | `5cdeabc23a0d`  |
| 3012   | Layout 1 | `5cdeabc23a0d`  |
| 3002   | Layout 1 | `5cdeabc23a0d`  |
| 2995   | Layout 1 | `5cdeabc23a0d`  |
| 2987   | Layout 1 | `5cdeabc23a0d`  |
| 2978   | Layout 1 | `5cdeabc23a0d`  |
| 2970   | Layout 1 | `5cdeabc23a0d`  |
| 2959   | Layout 1 | `5cdeabc23a0d`  |
| 2951   | Layout 1 | `5cdeabc23a0d`  |
| 2942   | Layout 1 | `5cdeabc23a0d`  |
| 2935   | Layout 1 | `5cdeabc23a0d`  |
| 2932   | Layout 1 | `5cdeabc23a0d`  |
| 2923   | Layout 1 | `5cdeabc23a0d`  |
| 2919   | Layout 1 | `5cdeabc23a0d`  |
| 2907   | Layout 1 | `5cdeabc23a0d`  |
| 2900   | Layout 1 | `5cdeabc23a0d`  |
| 2891   | Layout 1 | `5cdeabc23a0d`  |
| 2882   | Layout 1 | `5cdeabc23a0d`  |
| 2872   | Layout 1 | `5cdeabc23a0d`  |
| 2863   | Layout 1 | `5cdeabc23a0d`  |
| 2855   | Layout 1 | `5cdeabc23a0d`  |
| 2849   | Layout 1 | `5cdeabc23a0d`  |
| 2844   | Layout 1 | `5cdeabc23a0d`  |
| 2834   | Layout 1 | `5cdeabc23a0d`  |
| 2825   | Layout 1 | `5cdeabc23a0d`  |
| 2819   | Layout 1 | `5cdeabc23a0d`  |
| 2811   | Layout 1 | `5cdeabc23a0d`  |
| 2803   | Layout 1 | `5cdeabc23a0d`  |
| 2794   | Layout 1 | `5cdeabc23a0d`  |
| 2783   | Layout 1 | `5cdeabc23a0d`  |
| 2774   | Layout 1 | `5cdeabc23a0d`  |
| 2765   | Layout 1 | `5cdeabc23a0d`  |
| 2756   | Layout 1 | `5cdeabc23a0d`  |
| 2750   | Layout 1 | `5cdeabc23a0d`  |
| 2743   | Layout 1 | `5cdeabc23a0d`  |
| 2736   | Layout 1 | `5cdeabc23a0d`  |
| 2726   | Layout 1 | `5cdeabc23a0d`  |
| 2717   | Layout 1 | `5cdeabc23a0d`  |
| 2709   | Layout 1 | `5cdeabc23a0d`  |
| 2703   | Layout 1 | `5cdeabc23a0d`  |
| 2695   | Layout 1 | `5cdeabc23a0d`  |
| 2684   | Layout 1 | `5cdeabc23a0d`  |
| 2672   | Layout 1 | `5cdeabc23a0d`  |
| 2665   | Layout 1 | `5cdeabc23a0d`  |
| 2657   | Layout 1 | `5cdeabc23a0d`  |
| 2649   | Layout 1 | `5cdeabc23a0d`  |
| 2644   | Layout 1 | `5cdeabc23a0d`  |
| 2637   | Layout 1 | `5cdeabc23a0d`  |
| 2629   | Layout 1 | `5cdeabc23a0d`  |
| 2619   | Layout 1 | `5cdeabc23a0d`  |
| 2612   | Layout 1 | `5cdeabc23a0d`  |
| 2606   | Layout 1 | `5cdeabc23a0d`  |
| 2602   | Layout 1 | `5cdeabc23a0d`  |
| 2601   | Layout 1 | `5cdeabc23a0d`  |
| 2592   | Layout 1 | `5cdeabc23a0d`  |
| 2583   | Layout 1 | `5cdeabc23a0d`  |
| 2575   | Layout 1 | `5cdeabc23a0d`  |
| 2567   | Layout 1 | `5cdeabc23a0d`  |
| 2560   | Layout 1 | `5cdeabc23a0d`  |
| 2553   | Layout 1 | `5cdeabc23a0d`  |
| 2545   | Layout 1 | `5cdeabc23a0d`  |
| 2538   | Layout 1 | `5cdeabc23a0d`  |
| 2529   | Layout 1 | `5cdeabc23a0d`  |
| 2519   | Layout 1 | `5cdeabc23a0d`  |
| 2513   | Layout 1 | `5cdeabc23a0d`  |
| 2510   | Layout 1 | `5cdeabc23a0d`  |
| 2507   | Layout 1 | `5cdeabc23a0d`  |
| 2503   | Layout 1 | `5cdeabc23a0d`  |
| 2498   | Layout 1 | `5cdeabc23a0d`  |
| 2492   | Layout 1 | `5cdeabc23a0d`  |
| 2487   | Layout 1 | `5cdeabc23a0d`  |
| 2480   | Layout 1 | `5cdeabc23a0d`  |
| 2474   | Layout 1 | `5cdeabc23a0d`  |
| 2468   | Layout 1 | `5cdeabc23a0d`  |
| 2460   | Layout 1 | `5cdeabc23a0d`  |
| 2453   | Layout 1 | `5cdeabc23a0d`  |
| 2444   | Layout 1 | `5cdeabc23a0d`  |
| 2438   | Layout 1 | `5cdeabc23a0d`  |
| 2434   | Layout 1 | `5cdeabc23a0d`  |
| 2429   | Layout 1 | `5cdeabc23a0d`  |
| 2421   | Layout 1 | `5cdeabc23a0d`  |
| 2414   | Layout 1 | `5cdeabc23a0d`  |
| 2407   | Layout 1 | `5cdeabc23a0d`  |
| 2401   | Layout 1 | `5cdeabc23a0d`  |
| 2397   | Layout 1 | `5cdeabc23a0d`  |
| 2393   | Layout 1 | `5cdeabc23a0d`  |
| 2384   | Layout 1 | `5cdeabc23a0d`  |
| 2378   | Layout 1 | `5cdeabc23a0d`  |
| 2372   | Layout 1 | `5cdeabc23a0d`  |
| 2358   | Layout 1 | `5cdeabc23a0d`  |
| 2352   | Layout 1 | `5cdeabc23a0d`  |
| 2347   | Layout 1 | `5cdeabc23a0d`  |
| 2343   | Layout 1 | `5cdeabc23a0d`  |
| 2335   | Layout 1 | `5cdeabc23a0d`  |
| 2327   | Layout 1 | `5cdeabc23a0d`  |
| 2324   | Layout 1 | `5cdeabc23a0d`  |
| 2319   | Layout 1 | `5cdeabc23a0d`  |
| 2313   | Layout 1 | `5cdeabc23a0d`  |
| 2308   | Layout 1 | `5cdeabc23a0d`  |
| 2302   | Layout 1 | `5cdeabc23a0d`  |
| 2295   | Layout 1 | `5cdeabc23a0d`  |
| 2290   | Layout 1 | `5cdeabc23a0d`  |
| 2284   | Layout 1 | `5cdeabc23a0d`  |
| 2276   | Layout 1 | `5cdeabc23a0d`  |
| 2269   | Layout 1 | `5cdeabc23a0d`  |
| 2259   | Layout 1 | `5cdeabc23a0d`  |
| 2250   | Layout 1 | `5cdeabc23a0d`  |
| 2243   | Layout 1 | `5cdeabc23a0d`  |
| 2235   | Layout 1 | `5cdeabc23a0d`  |
| 2229   | Layout 1 | `5cdeabc23a0d`  |
| 2224   | Layout 1 | `5cdeabc23a0d`  |
| 2218   | Layout 1 | `5cdeabc23a0d`  |
| 2215   | Layout 1 | `5cdeabc23a0d`  |
| 2207   | Layout 1 | `5cdeabc23a0d`  |
| 2203   | Layout 1 | `5cdeabc23a0d`  |
| 2196   | Layout 1 | `5cdeabc23a0d`  |
| 2192   | Layout 1 | `5cdeabc23a0d`  |
| 2189   | Layout 1 | `5cdeabc23a0d`  |
| 2183   | Layout 1 | `5cdeabc23a0d`  |
| 2179   | Layout 1 | `5cdeabc23a0d`  |
| 2171   | Layout 1 | `5cdeabc23a0d`  |
| 2163   | Layout 1 | `5cdeabc23a0d`  |
| 2156   | Layout 1 | `5cdeabc23a0d`  |
| 2151   | Layout 1 | `5cdeabc23a0d`  |
| 2147   | Layout 1 | `5cdeabc23a0d`  |
| 2142   | Layout 1 | `5cdeabc23a0d`  |
| 2138   | Layout 1 | `5cdeabc23a0d`  |
| 2134   | Layout 1 | `5cdeabc23a0d`  |
| 2130   | Layout 1 | `5cdeabc23a0d`  |
| 2122   | Layout 1 | `5cdeabc23a0d`  |
| 2107   | Layout 1 | `5cdeabc23a0d`  |
| 2098   | Layout 1 | `5cdeabc23a0d`  |
| 2089   | Layout 1 | `5cdeabc23a0d`  |
| 2081   | Layout 1 | `5cdeabc23a0d`  |
| 2073   | Layout 1 | `5cdeabc23a0d`  |
| 2067   | Layout 1 | `5cdeabc23a0d`  |
| 2063   | Layout 1 | `5cdeabc23a0d`  |
| 2059   | Layout 1 | `5cdeabc23a0d`  |
| 2052   | Layout 1 | `5cdeabc23a0d`  |
| 2044   | Layout 1 | `5cdeabc23a0d`  |
| 2039   | Layout 1 | `5cdeabc23a0d`  |
| 2032   | Layout 1 | `5cdeabc23a0d`  |
| 2025   | Layout 1 | `5cdeabc23a0d`  |
| 2011   | Layout 1 | `5cdeabc23a0d`  |
| 2005   | Layout 1 | `5cdeabc23a0d`  |
| 2000   | Layout 1 | `5cdeabc23a0d`  |
| 1996   | Layout 1 | `5cdeabc23a0d`  |
| 1991   | Layout 1 | `5cdeabc23a0d`  |
| 1985   | Layout 1 | `5cdeabc23a0d`  |
| 1980   | Layout 1 | `5cdeabc23a0d`  |
| 1969   | Layout 1 | `5cdeabc23a0d`  |
| 1964   | Layout 1 | `5cdeabc23a0d`  |
| 1958   | Layout 1 | `5cdeabc23a0d`  |
| 1950   | Layout 1 | `5cdeabc23a0d`  |
| 1945   | Layout 1 | `5cdeabc23a0d`  |
| 1937   | Layout 1 | `5cdeabc23a0d`  |
| 1933   | Layout 1 | `5cdeabc23a0d`  |
| 1927   | Layout 1 | `5cdeabc23a0d`  |
| 1921   | Layout 1 | `5cdeabc23a0d`  |
| 1914   | Layout 1 | `5cdeabc23a0d`  |
| 1908   | Layout 1 | `5cdeabc23a0d`  |
| 1897   | Layout 1 | `5cdeabc23a0d`  |
| 1892   | Layout 1 | `5cdeabc23a0d`  |
| 1886   | Layout 1 | `5cdeabc23a0d`  |
| 1881   | Layout 1 | `5cdeabc23a0d`  |
| 1871   | Layout 1 | `5cdeabc23a0d`  |
| 1866   | Layout 1 | `5cdeabc23a0d`  |
| 1862   | Layout 1 | `5cdeabc23a0d`  |
| 1854   | Layout 1 | `5cdeabc23a0d`  |
| 1846   | Layout 1 | `5cdeabc23a0d`  |
| 1838   | Layout 1 | `5cdeabc23a0d`  |
| 1832   | Layout 1 | `5cdeabc23a0d`  |
| 1826   | Layout 1 | `5cdeabc23a0d`  |
| 1822   | Layout 1 | `5cdeabc23a0d`  |
| 1818   | Layout 1 | `5cdeabc23a0d`  |
| 1804   | Layout 1 | `5cdeabc23a0d`  |
| 1794   | Layout 1 | `5cdeabc23a0d`  |
| 1790   | Layout 1 | `5cdeabc23a0d`  |
| 1784   | Layout 1 | `5cdeabc23a0d`  |
| 1774   | Layout 1 | `5cdeabc23a0d`  |
| 1771   | Layout 1 | `5cdeabc23a0d`  |
| 1762   | Layout 1 | `5cdeabc23a0d`  |
| 1759   | Layout 1 | `5cdeabc23a0d`  |
| 1754   | Layout 1 | `5cdeabc23a0d`  |
| 1749   | Layout 1 | `5cdeabc23a0d`  |
| 1743   | Layout 1 | `5cdeabc23a0d`  |
| 1737   | Layout 1 | `5cdeabc23a0d`  |
| 1731   | Layout 1 | `5cdeabc23a0d`  |
| 1725   | Layout 1 | `5cdeabc23a0d`  |
| 1717   | Layout 1 | `5cdeabc23a0d`  |
| 1710   | Layout 1 | `5cdeabc23a0d`  |
| 1704   | Layout 1 | `5cdeabc23a0d`  |
| 1698   | Layout 1 | `5cdeabc23a0d`  |
| 1690   | Layout 1 | `5cdeabc23a0d`  |
| 1685   | Layout 1 | `5cdeabc23a0d`  |
| 1680   | Layout 1 | `5cdeabc23a0d`  |
| 1674   | Layout 1 | `5cdeabc23a0d`  |
| 1668   | Layout 1 | `5cdeabc23a0d`  |
| 1659   | Layout 1 | `5cdeabc23a0d`  |
| 1649   | Layout 1 | `5cdeabc23a0d`  |
| 1642   | Layout 1 | `5cdeabc23a0d`  |
| 1636   | Layout 1 | `5cdeabc23a0d`  |
| 1628   | Layout 1 | `5cdeabc23a0d`  |
| 1622   | Layout 1 | `5cdeabc23a0d`  |
| 1614   | Layout 1 | `5cdeabc23a0d`  |
| 1608   | Layout 1 | `5cdeabc23a0d`  |
| 1602   | Layout 1 | `5cdeabc23a0d`  |
| 1598   | Layout 1 | `5cdeabc23a0d`  |
| 1594   | Layout 1 | `5cdeabc23a0d`  |
| 1590   | Layout 1 | `5cdeabc23a0d`  |
| 1587   | Layout 1 | `5cdeabc23a0d`  |
| 1584   | Layout 1 | `5cdeabc23a0d`  |
| 1579   | Layout 1 | `5cdeabc23a0d`  |
| 1572   | Layout 1 | `5cdeabc23a0d`  |
| 1565   | Layout 1 | `5cdeabc23a0d`  |
| 1559   | Layout 1 | `5cdeabc23a0d`  |
| 1554   | Layout 1 | `5cdeabc23a0d`  |
| 1547   | Layout 1 | `5cdeabc23a0d`  |
| 1537   | Layout 1 | `5cdeabc23a0d`  |
| 1529   | Layout 1 | `5cdeabc23a0d`  |
| 1524   | Layout 1 | `5cdeabc23a0d`  |
| 1519   | Layout 1 | `5cdeabc23a0d`  |
| 1509   | Layout 1 | `5cdeabc23a0d`  |
| 1506   | Layout 1 | `5cdeabc23a0d`  |
| 1504   | Layout 1 | `5cdeabc23a0d`  |
| 1500   | Layout 1 | `5cdeabc23a0d`  |
| 1493   | Layout 1 | `5cdeabc23a0d`  |
| 1489   | Layout 1 | `5cdeabc23a0d`  |
| 1485   | Layout 1 | `5cdeabc23a0d`  |
| 1481   | Layout 1 | `5cdeabc23a0d`  |
| 1474   | Layout 1 | `5cdeabc23a0d`  |
| 1466   | Layout 1 | `5cdeabc23a0d`  |
| 1462   | No file  | `5cdeabc23a0d`  |
| 1459   | No file  | `5cdeabc23a0d`  |
| 1453   | No file  | `5cdeabc23a0d`  |
| 1450   | No file  | `5cdeabc23a0d`  |
| 1445   | No file  | `5cdeabc23a0d`  |
| 1439   | No file  | `5cdeabc23a0d`  |
| 1433   | No file  | `5cdeabc23a0d`  |
| 1430   | No file  | `5cdeabc23a0d`  |
| 1426   | No file  | `5cdeabc23a0d`  |
| 1421   | No file  | `5cdeabc23a0d`  |
| 1417   | No file  | `5cdeabc23a0d`  |
| 1416   | No file  | `5cdeabc23a0d`  |
| 1409   | No file  | `5cdeabc23a0d`  |
| 1405   | No file  | `5cdeabc23a0d`  |
| 1401   | No file  | `5cdeabc23a0d`  |
| 1396   | No file  | `5cdeabc23a0d`  |
| 1391   | No file  | `5cdeabc23a0d`  |
| 1390   | No file  | `5cdeabc23a0d`  |
| 1386   | No file  | `5cdeabc23a0d`  |
| 1381   | No file  | `5cdeabc23a0d`  |
| 1379   | No file  | `5cdeabc23a0d`  |
| 1372   | No file  | `5cdeabc23a0d`  |
| 1366   | No file  | `5cdeabc23a0d`  |
| 1364   | No file  | `5cdeabc23a0d`  |
| 1363   | No file  | `5cdeabc23a0d`  |
| 1360   | No file  | `5cdeabc23a0d`  |
| 1358   | No file  | `5cdeabc23a0d`  |
| 1355   | No file  | `5cdeabc23a0d`  |
| 1351   | No file  | `5cdeabc23a0d`  |
| 1348   | No file  | `5cdeabc23a0d`  |
| 1346   | No file  | `5cdeabc23a0d`  |
| 1341   | No file  | `5cdeabc23a0d`  |
| 1340   | No file  | `5cdeabc23a0d`  |
| 1338   | No file  | `5cdeabc23a0d`  |
| 1335   | No file  | `5cdeabc23a0d`  |
| 1333   | No file  | `5cdeabc23a0d`  |
| 1329   | No file  | `5cdeabc23a0d`  |
| 1327   | No file  | `5cdeabc23a0d`  |
| 1324   | No file  | `5cdeabc23a0d`  |
| 1321   | No file  | `5cdeabc23a0d`  |
| 1319   | No file  | `5cdeabc23a0d`  |
| 1318   | No file  | `5cdeabc23a0d`  |
| 1316   | No file  | `5cdeabc23a0d`  |
| 1313   | No file  | `5cdeabc23a0d`  |
| 1311   | No file  | `5cdeabc23a0d`  |
| 1309   | No file  | `5cdeabc23a0d`  |
| 1304   | No file  | `5cdeabc23a0d`  |
| 1292   | No file  | `5cdeabc23a0d`  |
| 1286   | No file  | `5cdeabc23a0d`  |
| 1280   | No file  | `5cdeabc23a0d`  |
| 1276   | No file  | `5cdeabc23a0d`  |
| 1267   | No file  | `5cdeabc23a0d`  |
| 1261   | No file  | `5cdeabc23a0d`  |
| 1256   | No file  | `5cdeabc23a0d`  |
| 1250   | No file  | `5cdeabc23a0d`  |
| 1246   | No file  | `5cdeabc23a0d`  |
| 1239   | No file  | `5cdeabc23a0d`  |
| 1230   | No file  | `5cdeabc23a0d`  |
| 1226   | No file  | `5cdeabc23a0d`  |
| 1220   | No file  | `5cdeabc23a0d`  |
| 1217   | No file  | `5cdeabc23a0d`  |
| 1211   | No file  | `5cdeabc23a0d`  |
| 1210   | No file  | `5cdeabc23a0d`  |
| 1208   | No file  | `5cdeabc23a0d`  |
| 1203   | No file  | `5cdeabc23a0d`  |
| 1197   | No file  | `5cdeabc23a0d`  |
| 1194   | No file  | `5cdeabc23a0d`  |
| 1192   | No file  | `5cdeabc23a0d`  |
| 1187   | No file  | `5cdeabc23a0d`  |
| 1183   | No file  | `5cdeabc23a0d`  |
| 1177   | No file  | `5cdeabc23a0d`  |
| 1173   | No file  | `5cdeabc23a0d`  |
| 1167   | No file  | `5cdeabc23a0d`  |
| 1164   | No file  | `5cdeabc23a0d`  |
| 1156   | No file  | `5cdeabc23a0d`  |
| 1149   | No file  | `5cdeabc23a0d`  |
| 1144   | No file  | `5cdeabc23a0d`  |
| 1137   | No file  | `5cdeabc23a0d`  |
| 1132   | No file  | `5cdeabc23a0d`  |
| 1127   | No file  | `5cdeabc23a0d`  |
| 1122   | No file  | `5cdeabc23a0d`  |
| 1118   | No file  | `5cdeabc23a0d`  |
| 1114   | No file  | `5cdeabc23a0d`  |
| 1109   | No file  | `5cdeabc23a0d`  |
| 1102   | No file  | `5cdeabc23a0d`  |
| 1096   | No file  | `5cdeabc23a0d`  |
| 1088   | No file  | `5cdeabc23a0d`  |
| 1081   | No file  | `5cdeabc23a0d`  |
| 1076   | No file  | `5cdeabc23a0d`  |
| 1069   | No file  | `5cdeabc23a0d`  |
| 1064   | No file  | `5cdeabc23a0d`  |
| 1058   | No file  | `5cdeabc23a0d`  |
| 1051   | No file  | `5cdeabc23a0d`  |
| 1044   | No file  | `5cdeabc23a0d`  |
| 1036   | No file  | `5cdeabc23a0d`  |
| 1026   | No file  | `5cdeabc23a0d`  |
| 1016   | No file  | `5cdeabc23a0d`  |
| 1009   | No file  | `5cdeabc23a0d`  |
| 1005   | No file  | `5cdeabc23a0d`  |
| 1000   | No file  | `5cdeabc23a0d`  |
| 998    | No file  | `5cdeabc23a0d`  |
| 990    | No file  | `5cdeabc23a0d`  |
| 979    | No file  | `5cdeabc23a0d`  |
| 972    | No file  | `5cdeabc23a0d`  |
| 963    | No file  | `5cdeabc23a0d`  |
| 955    | No file  | `5cdeabc23a0d`  |
| 946    | No file  | `5cdeabc23a0d`  |
| 938    | No file  | `5cdeabc23a0d`  |
| 927    | No file  | `5cdeabc23a0d`  |
| 911    | No file  | `5cdeabc23a0d`  |
| 904    | No file  | `5cdeabc23a0d`  |
| 899    | No file  | `5cdeabc23a0d`  |
| 894    | No file  | `5cdeabc23a0d`  |
| 885    | No file  | `5cdeabc23a0d`  |
| 879    | No file  | `5cdeabc23a0d`  |
| 872    | No file  | `5cdeabc23a0d`  |
| 864    | No file  | `5cdeabc23a0d`  |
| 855    | No file  | `5cdeabc23a0d`  |
| 853    | No file  | `5cdeabc23a0d`  |
| 845    | No file  | `5cdeabc23a0d`  |
| 837    | No file  | `5cdeabc23a0d`  |
| 829    | No file  | `5cdeabc23a0d`  |
| 822    | No file  | `5cdeabc23a0d`  |
| 814    | No file  | `5cdeabc23a0d`  |
| 805    | No file  | `5cdeabc23a0d`  |
| 794    | No file  | `5cdeabc23a0d`  |
| 787    | No file  | `5cdeabc23a0d`  |
| 780    | No file  | `5cdeabc23a0d`  |
| 771    | No file  | `5cdeabc23a0d`  |
| 760    | No file  | `5cdeabc23a0d`  |
| 748    | No file  | `5cdeabc23a0d`  |
| 741    | No file  | `5cdeabc23a0d`  |
| 736    | No file  | `5cdeabc23a0d`  |
| 731    | No file  | `5cdeabc23a0d`  |
| 723    | No file  | `5cdeabc23a0d`  |
| 711    | No file  | `5cdeabc23a0d`  |
| 707    | No file  | `5cdeabc23a0d`  |
| 697    | No file  | `5cdeabc23a0d`  |
| 689    | No file  | `5cdeabc23a0d`  |
| 683    | No file  | `5cdeabc23a0d`  |
| 678    | No file  | `5cdeabc23a0d`  |
| 670    | No file  | `5cdeabc23a0d`  |
| 661    | No file  | `5cdeabc23a0d`  |
| 656    | No file  | `5cdeabc23a0d`  |
| 652    | No file  | `5cdeabc23a0d`  |
| 643    | No file  | `5cdeabc23a0d`  |
| 637    | No file  | `5cdeabc23a0d`  |
| 630    | No file  | `5cdeabc23a0d`  |
| 627    | No file  | `5cdeabc23a0d`  |
| 621    | No file  | `5cdeabc23a0d`  |
| 617    | No file  | `5cdeabc23a0d`  |
| 615    | No file  | `5cdeabc23a0d`  |
| 606    | No file  | `5cdeabc23a0d`  |
| 599    | No file  | `5cdeabc23a0d`  |
| 592    | No file  | `5cdeabc23a0d`  |
| 586    | No file  | `5cdeabc23a0d`  |
| 577    | No file  | `5cdeabc23a0d`  |
| 569    | No file  | `5cdeabc23a0d`  |
| 561    | No file  | `5cdeabc23a0d`  |
| 554    | No file  | `5cdeabc23a0d`  |
| 542    | No file  | `5cdeabc23a0d`  |
| 532    | No file  | `5cdeabc23a0d`  |
| 531    | No file  | `5cdeabc23a0d`  |
| 526    | No file  | `5cdeabc23a0d`  |
| 521    | No file  | `5cdeabc23a0d`  |
| 517    | No file  | `5cdeabc23a0d`  |
| 510    | No file  | `5cdeabc23a0d`  |
| 508    | No file  | `5cdeabc23a0d`  |
| 504    | No file  | `5cdeabc23a0d`  |
| 497    | No file  | `5cdeabc23a0d`  |
| 491    | No file  | `5cdeabc23a0d`  |
| 485    | No file  | `5cdeabc23a0d`  |
| 478    | No file  | `5cdeabc23a0d`  |
| 472    | No file  | `5cdeabc23a0d`  |
| 466    | No file  | `5cdeabc23a0d`  |
| 457    | No file  | `5cdeabc23a0d`  |
| 452    | No file  | `5cdeabc23a0d`  |
| 449    | No file  | `5cdeabc23a0d`  |
| 435    | No file  | `5cdeabc23a0d`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                                     |
| --------------------- | -------- | ------------------------------------------------------------------------ |
| `menu.bss`            | Optional | Category titles; `menu_id` names its row                                 |
| `stringtable.bss`     | Optional | Hash of the title key in its sheet, for the LOC lookup                   |
| `languagedata_en.loc` | Optional | Title text, LOC type 37 (`str_id1` = key hash, `str_id2` = sheet)        |

All multi-byte values are little-endian.

## Layout 1

### File Layout

Groups of entries instead of fixed rows, then the shared PABR string table
(`_common/pabr_strings.py`).

| Offset              | Type               | Field        | Notes                                                            |
| ------------------- | ------------------ | ------------ | ---------------------------------------------------------------- |
| `+0x00`             | char[4]            | magic        | ASCII `PABR`                                                     |
| `+0x04`             | u32                | group_count  | Number of groups; 12 on client 3458, the same as `menu.bss` rows |
| `+0x08`             | Group[group_count] | groups       | See Group                                                        |
| `groups+0x00`       | String Table       | string_table | See String Table                                                 |
| `string_table+0x00` | u32                | table_start  | Offset of the string table, where the groups end                 |
| `string_table+0x04` | u32                | zero         | Always 0                                                         |

The groups follow the `menu.bss` categories from Information (menu 2) on;
the last group is empty. Recently Used (menu 1) has no group of its own, so
group `i` holds the entries of menu `i + 2`.

### Group (variable: 4 bytes + entries)

| Offset  | Type                    | Field       | Notes                         |
| ------- | ----------------------- | ----------- | ----------------------------- |
| `+0x00` | u32                     | entry_count | Number of entries that follow |
| `+0x04` | Menu Entry[entry_count] | entries     | See Menu Entry                |

### Menu Entry (49 bytes)

Fields are unaligned.

| Offset  | Type | Field       | Notes                                                                 |
| ------- | ---- | ----------- | --------------------------------------------------------------------- |
| `+0x00` | u32  | entry_id    | Unique; 155 values on client 3458, not in group order                 |
| `+0x04` | u32  | menu_id     | The `menu.bss` category                                               |
| `+0x08` | u32  | position    | Position in the category, from 1                                      |
| `+0x0C` | u64  | unknown_0c  | `0` on 111 entries; see Open Questions                                |
| `+0x14` | u8   | unknown_14  | Always `0`                                                            |
| `+0x15` | u32  | icon_ref    | String table index of the sprite sheet, relative to `ui_texture/`     |
| `+0x19` | u32  | icon_x1     | Left edge of the icon region in the sheet, in pixels                  |
| `+0x1D` | u32  | icon_y1     | Top edge                                                              |
| `+0x21` | u32  | icon_x2     | Right edge; 151 of 155 regions are 55 x 55                            |
| `+0x25` | u32  | icon_y2     | Bottom edge                                                           |
| `+0x29` | u32  | sheet_ref   | String table index of the title key's sheet (`GAME` or `RESOURCE`)   |
| `+0x2D` | u32  | key_ref     | String table index of the title key (`LUA_MENU_REMAKE_MENU_HELP`)    |

### String Table (variable: 4 bytes + strings)

159 strings on client 3458: the two sprite sheets of `menu.bss`, the sheet
names `GAME` (91 entries) and `RESOURCE` (64), and one title key per entry.

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | 159 on client 3458  |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Notes

- The groups end exactly where the string table starts, and each group's
  entry count equals the `submenu_count` of its `menu.bss` category.
- 152 of the 155 title keys have LOC type 37 text on client 3458 through
  their sheet's `str_id2` (`GAME` = 1, `RESOURCE` = 2).
- Both sprite sheets ship under `ui_texture/combine/icon/`; four regions are
  not 55 x 55 (55 x 57 twice, 55 x 49, 56 x 55).
- The app indexes the icons by entry ID as a sprite kind:
  `IndexKind.SUBMENU_ICON` holds the sheet path and
  `IndexKind.SUBMENU_ICON_REGION` the `(x1, y1, x2, y2)` region, read through
  `icon_path()` and `icon_region()` with `IconKind.SUBMENU`.

## Open Questions

### What does `unknown_0c` hold?

It is `0` on 111 entries. On the other 44 the high word is a small number
(96 to 120) and the low word looks random (`0x8E80E004` on Guild,
`0xEF7A4404` on Settings). The set entries include newer or event windows
(Solare rankings, Black Spirit Adventure, Special Pass, Ticket Shop), so it
may mark a "new" badge or a content switch, but no value decodes as a date and
nothing in the client files seen so far reads it.
