# `ui_skillgroup_*.bss` Format

## Purpose

The skill window layout of every class: one grid per class, cell by cell,
with the skill groups placed on it, the connecting lines between them, and the
tabs the skills are sorted into. Three files share the format:

| File                           | Window           | Classes on client 3458 |
| ------------------------------ | ---------------- | ---------------------- |
| `ui_skillgroup_combat.bss`     | Combat skills    | 32                     |
| `ui_skillgroup_awakening.bss`  | Awakening skills | 32                     |
| `ui_skillgroup_succession.bss` | Succession       | 0 (empty)              |

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                           | Bytes   | Records                                            | Row bytes             |
| ------ | -------------- | ------- | ------------------------------ | ------- | -------------------------------------------------- | --------------------- |
| 1      | 1363 and later | 3483    | `ui_skillgroup_awakening.bss`  | 69,380  | 7,552 Cell, 32 Class Grid, 68 Tab, 32 Class Tabs   | 9 to 11, 9 on average |
| 1      | 1363 and later | 3483    | `ui_skillgroup_combat.bss`     | 242,103 | 26,224 Cell, 32 Class Grid, 160 Tab, 32 Class Tabs | 9 to 11, 9 on average |
| 1      | 1363 and later | 3483    | `ui_skillgroup_succession.bss` | 230     | 1 String Table                                     | 4                     |

| Layout | File                           | Known             | Unknown          |
| ------ | ------------------------------ | ----------------- | ---------------- |
| 1      | `ui_skillgroup_awakening.bss`  | 61,498 B (88.6%)  | 7,882 B (11.4%)  |
| 1      | `ui_skillgroup_combat.bss`     | 215,549 B (89.0%) | 26,554 B (11.0%) |
| 1      | `ui_skillgroup_succession.bss` | 28 B (12.2%)      | 202 B (87.8%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `78f64f17be33`  |
| 3482   | Layout 1             | `78f64f17be33`  |
| 3474   | Layout 1             | `78f64f17be33`  |
| 3473   | Layout 1             | `78f64f17be33`  |
| 3464   | Layout 1             | `78f64f17be33`  |
| 3458   | Layout 1             | `78f64f17be33`  |
| 3454   | Layout 1             | `78f64f17be33`  |
| 3444   | Layout 1             | `78f64f17be33`  |
| 3435   | Layout 1             | `78f64f17be33`  |
| 3426   | Layout 1             | `78f64f17be33`  |
| 3418   | Layout 1             | `78f64f17be33`  |
| 3412   | Layout 1             | `78f64f17be33`  |
| 3402   | Layout 1             | `78f64f17be33`  |
| 3396   | Layout 1             | `78f64f17be33`  |
| 3387   | Layout 1             | `78f64f17be33`  |
| 3381   | Layout 1             | `78f64f17be33`  |
| 3373   | Layout 1             | `78f64f17be33`  |
| 3364   | Layout 1             | `78f64f17be33`  |
| 3356   | Layout 1             | `78f64f17be33`  |
| 3349   | Layout 1             | `78f64f17be33`  |
| 3342   | Layout 1             | `78f64f17be33`  |
| 3335   | Layout 1             | `78f64f17be33`  |
| 3326   | Layout 1             | `78f64f17be33`  |
| 3321   | Layout 1             | `78f64f17be33`  |
| 3314   | Layout 1             | `78f64f17be33`  |
| 3303   | Layout 1             | `78f64f17be33`  |
| 3302   | Layout 1             | `78f64f17be33`  |
| 3293   | Layout 1             | `78f64f17be33`  |
| 3283   | Layout 1             | `78f64f17be33`  |
| 3275   | Layout 1             | `78f64f17be33`  |
| 3267   | Layout 1             | `78f64f17be33`  |
| 3258   | Layout 1             | `78f64f17be33`  |
| 3251   | Layout 1             | `78f64f17be33`  |
| 3242   | Layout 1             | `78f64f17be33`  |
| 3235   | Layout 1             | `78f64f17be33`  |
| 3229   | Layout 1             | `78f64f17be33`  |
| 3212   | Layout 1             | `78f64f17be33`  |
| 3203   | Layout 1             | `78f64f17be33`  |
| 3193   | Layout 1             | `78f64f17be33`  |
| 3186   | Layout 1             | `78f64f17be33`  |
| 3177   | Layout 1             | `78f64f17be33`  |
| 3169   | Layout 1             | `78f64f17be33`  |
| 3158   | Layout 1             | `78f64f17be33`  |
| 3151   | Layout 1             | `78f64f17be33`  |
| 3144   | Layout 1             | `78f64f17be33`  |
| 3133   | Layout 1             | `78f64f17be33`  |
| 3125   | Layout 1             | `78f64f17be33`  |
| 3118   | Layout 1             | `78f64f17be33`  |
| 3111   | Layout 1             | `78f64f17be33`  |
| 3103   | Layout 1             | `78f64f17be33`  |
| 3095   | Layout 1             | `78f64f17be33`  |
| 3086   | Layout 1             | `78f64f17be33`  |
| 3072   | Layout 1             | `78f64f17be33`  |
| 3062   | Layout 1             | `78f64f17be33`  |
| 3052   | Layout 1             | `78f64f17be33`  |
| 3045   | Layout 1             | `78f64f17be33`  |
| 3037   | Layout 1             | `78f64f17be33`  |
| 3030   | Layout 1             | `78f64f17be33`  |
| 3021   | Layout 1             | `78f64f17be33`  |
| 3012   | Layout 1             | `78f64f17be33`  |
| 3002   | Layout 1             | `78f64f17be33`  |
| 2995   | Layout 1             | `78f64f17be33`  |
| 2987   | Layout 1             | `78f64f17be33`  |
| 2978   | Layout 1             | `78f64f17be33`  |
| 2970   | Layout 1             | `78f64f17be33`  |
| 2959   | Layout 1             | `78f64f17be33`  |
| 2951   | Layout 1             | `78f64f17be33`  |
| 2942   | Layout 1             | `78f64f17be33`  |
| 2935   | Layout 1             | `78f64f17be33`  |
| 2932   | Layout 1             | `78f64f17be33`  |
| 2923   | Layout 1             | `78f64f17be33`  |
| 2919   | Layout 1             | `78f64f17be33`  |
| 2907   | Layout 1             | `78f64f17be33`  |
| 2900   | Layout 1             | `78f64f17be33`  |
| 2891   | Layout 1             | `78f64f17be33`  |
| 2882   | Layout 1             | `78f64f17be33`  |
| 2872   | Layout 1             | `78f64f17be33`  |
| 2863   | Layout 1             | `78f64f17be33`  |
| 2855   | Layout 1             | `78f64f17be33`  |
| 2849   | Layout 1             | `78f64f17be33`  |
| 2844   | Layout 1             | `78f64f17be33`  |
| 2834   | Layout 1             | `78f64f17be33`  |
| 2825   | Layout 1             | `78f64f17be33`  |
| 2819   | Layout 1             | `78f64f17be33`  |
| 2811   | Layout 1             | `78f64f17be33`  |
| 2803   | Layout 1             | `78f64f17be33`  |
| 2794   | Layout 1             | `78f64f17be33`  |
| 2783   | Layout 1             | `78f64f17be33`  |
| 2774   | Layout 1             | `78f64f17be33`  |
| 2765   | Layout 1             | `78f64f17be33`  |
| 2756   | Layout 1             | `78f64f17be33`  |
| 2750   | Layout 1             | `78f64f17be33`  |
| 2743   | Layout 1             | `78f64f17be33`  |
| 2736   | Layout 1             | `78f64f17be33`  |
| 2726   | Layout 1             | `78f64f17be33`  |
| 2717   | Layout 1             | `78f64f17be33`  |
| 2709   | Layout 1             | `78f64f17be33`  |
| 2703   | Layout 1             | `78f64f17be33`  |
| 2695   | Layout 1             | `78f64f17be33`  |
| 2684   | Layout 1             | `78f64f17be33`  |
| 2672   | Layout 1             | `78f64f17be33`  |
| 2665   | Layout 1             | `78f64f17be33`  |
| 2657   | Layout 1             | `78f64f17be33`  |
| 2649   | Layout 1             | `78f64f17be33`  |
| 2644   | Layout 1             | `78f64f17be33`  |
| 2637   | Layout 1             | `78f64f17be33`  |
| 2629   | Layout 1             | `78f64f17be33`  |
| 2619   | Layout 1             | `78f64f17be33`  |
| 2612   | Layout 1             | `78f64f17be33`  |
| 2606   | Layout 1             | `78f64f17be33`  |
| 2602   | Layout 1             | `78f64f17be33`  |
| 2601   | Layout 1             | `78f64f17be33`  |
| 2592   | Layout 1             | `78f64f17be33`  |
| 2583   | Layout 1             | `78f64f17be33`  |
| 2575   | Layout 1             | `78f64f17be33`  |
| 2567   | Layout 1             | `78f64f17be33`  |
| 2560   | Layout 1             | `78f64f17be33`  |
| 2553   | Layout 1             | `78f64f17be33`  |
| 2545   | Layout 1             | `78f64f17be33`  |
| 2538   | Layout 1             | `78f64f17be33`  |
| 2529   | Layout 1             | `78f64f17be33`  |
| 2519   | Layout 1             | `78f64f17be33`  |
| 2513   | Layout 1             | `78f64f17be33`  |
| 2510   | Layout 1             | `78f64f17be33`  |
| 2507   | Layout 1             | `78f64f17be33`  |
| 2503   | Layout 1             | `78f64f17be33`  |
| 2498   | Layout 1             | `78f64f17be33`  |
| 2492   | Layout 1             | `78f64f17be33`  |
| 2487   | Layout 1             | `78f64f17be33`  |
| 2480   | Layout 1             | `78f64f17be33`  |
| 2474   | Layout 1             | `78f64f17be33`  |
| 2468   | Layout 1             | `78f64f17be33`  |
| 2460   | Layout 1             | `78f64f17be33`  |
| 2453   | Layout 1             | `78f64f17be33`  |
| 2444   | Layout 1             | `78f64f17be33`  |
| 2438   | Layout 1             | `78f64f17be33`  |
| 2434   | Layout 1             | `78f64f17be33`  |
| 2429   | Layout 1             | `78f64f17be33`  |
| 2421   | Layout 1             | `78f64f17be33`  |
| 2414   | Layout 1             | `78f64f17be33`  |
| 2407   | Layout 1             | `78f64f17be33`  |
| 2401   | Layout 1             | `78f64f17be33`  |
| 2397   | Layout 1             | `78f64f17be33`  |
| 2393   | Layout 1             | `78f64f17be33`  |
| 2384   | Layout 1             | `78f64f17be33`  |
| 2378   | Layout 1             | `78f64f17be33`  |
| 2372   | Layout 1             | `78f64f17be33`  |
| 2358   | Layout 1             | `78f64f17be33`  |
| 2352   | Layout 1             | `78f64f17be33`  |
| 2347   | Layout 1             | `78f64f17be33`  |
| 2343   | Layout 1             | `78f64f17be33`  |
| 2335   | Layout 1             | `78f64f17be33`  |
| 2327   | Layout 1             | `78f64f17be33`  |
| 2324   | Layout 1             | `78f64f17be33`  |
| 2319   | Layout 1             | `78f64f17be33`  |
| 2313   | Layout 1             | `78f64f17be33`  |
| 2308   | Layout 1             | `78f64f17be33`  |
| 2302   | Layout 1             | `78f64f17be33`  |
| 2295   | Layout 1             | `78f64f17be33`  |
| 2290   | Layout 1             | `78f64f17be33`  |
| 2284   | Layout 1             | `78f64f17be33`  |
| 2276   | Layout 1             | `78f64f17be33`  |
| 2269   | Layout 1             | `78f64f17be33`  |
| 2259   | Layout 1             | `78f64f17be33`  |
| 2250   | Layout 1             | `78f64f17be33`  |
| 2243   | Layout 1             | `78f64f17be33`  |
| 2235   | Layout 1             | `78f64f17be33`  |
| 2229   | Layout 1             | `78f64f17be33`  |
| 2224   | Layout 1             | `78f64f17be33`  |
| 2218   | Layout 1             | `78f64f17be33`  |
| 2215   | Layout 1             | `78f64f17be33`  |
| 2207   | Layout 1             | `78f64f17be33`  |
| 2203   | Layout 1             | `78f64f17be33`  |
| 2196   | Layout 1             | `78f64f17be33`  |
| 2192   | Layout 1             | `78f64f17be33`  |
| 2189   | Layout 1             | `78f64f17be33`  |
| 2183   | Layout 1             | `78f64f17be33`  |
| 2179   | Layout 1             | `78f64f17be33`  |
| 2171   | Layout 1             | `78f64f17be33`  |
| 2163   | Layout 1             | `78f64f17be33`  |
| 2156   | Layout 1             | `78f64f17be33`  |
| 2151   | Layout 1             | `78f64f17be33`  |
| 2147   | Layout 1             | `78f64f17be33`  |
| 2142   | Layout 1             | `78f64f17be33`  |
| 2138   | Layout 1             | `78f64f17be33`  |
| 2134   | Layout 1             | `78f64f17be33`  |
| 2130   | Layout 1             | `78f64f17be33`  |
| 2122   | Layout 1             | `78f64f17be33`  |
| 2107   | Layout 1             | `78f64f17be33`  |
| 2098   | Layout 1             | `78f64f17be33`  |
| 2089   | Layout 1             | `78f64f17be33`  |
| 2081   | Layout 1             | `78f64f17be33`  |
| 2073   | Layout 1             | `78f64f17be33`  |
| 2067   | Layout 1             | `78f64f17be33`  |
| 2063   | Layout 1             | `78f64f17be33`  |
| 2059   | Layout 1             | `78f64f17be33`  |
| 2052   | Layout 1             | `78f64f17be33`  |
| 2044   | Layout 1             | `78f64f17be33`  |
| 2039   | Layout 1             | `78f64f17be33`  |
| 2032   | Layout 1             | `78f64f17be33`  |
| 2025   | Layout 1             | `78f64f17be33`  |
| 2011   | Layout 1             | `78f64f17be33`  |
| 2005   | Layout 1             | `78f64f17be33`  |
| 2000   | Layout 1             | `78f64f17be33`  |
| 1996   | Layout 1             | `78f64f17be33`  |
| 1991   | Layout 1             | `78f64f17be33`  |
| 1985   | Layout 1             | `78f64f17be33`  |
| 1980   | Layout 1             | `78f64f17be33`  |
| 1969   | Layout 1             | `78f64f17be33`  |
| 1964   | Layout 1             | `78f64f17be33`  |
| 1958   | Layout 1             | `78f64f17be33`  |
| 1950   | Layout 1             | `78f64f17be33`  |
| 1945   | Layout 1             | `78f64f17be33`  |
| 1937   | Layout 1             | `78f64f17be33`  |
| 1933   | Layout 1             | `78f64f17be33`  |
| 1927   | Layout 1             | `78f64f17be33`  |
| 1921   | Layout 1             | `78f64f17be33`  |
| 1914   | Layout 1             | `78f64f17be33`  |
| 1908   | Layout 1             | `78f64f17be33`  |
| 1897   | Layout 1             | `78f64f17be33`  |
| 1892   | Layout 1             | `78f64f17be33`  |
| 1886   | Layout 1             | `78f64f17be33`  |
| 1881   | Layout 1             | `78f64f17be33`  |
| 1871   | Layout 1             | `78f64f17be33`  |
| 1866   | Layout 1             | `78f64f17be33`  |
| 1862   | Layout 1             | `78f64f17be33`  |
| 1854   | Layout 1             | `78f64f17be33`  |
| 1846   | Layout 1             | `78f64f17be33`  |
| 1838   | Layout 1             | `78f64f17be33`  |
| 1832   | Layout 1             | `78f64f17be33`  |
| 1826   | Layout 1             | `78f64f17be33`  |
| 1822   | Layout 1             | `78f64f17be33`  |
| 1818   | Layout 1             | `78f64f17be33`  |
| 1804   | Layout 1             | `78f64f17be33`  |
| 1794   | Layout 1             | `78f64f17be33`  |
| 1790   | Layout 1             | `78f64f17be33`  |
| 1784   | Layout 1             | `78f64f17be33`  |
| 1774   | Layout 1             | `78f64f17be33`  |
| 1771   | Layout 1             | `78f64f17be33`  |
| 1762   | Layout 1             | `78f64f17be33`  |
| 1759   | Layout 1             | `78f64f17be33`  |
| 1754   | Layout 1             | `78f64f17be33`  |
| 1749   | Layout 1             | `78f64f17be33`  |
| 1743   | Layout 1             | `78f64f17be33`  |
| 1737   | Layout 1             | `78f64f17be33`  |
| 1731   | Layout 1             | `78f64f17be33`  |
| 1725   | Layout 1             | `78f64f17be33`  |
| 1717   | Layout 1             | `78f64f17be33`  |
| 1710   | Layout 1             | `78f64f17be33`  |
| 1704   | Layout 1             | `78f64f17be33`  |
| 1698   | Layout 1             | `78f64f17be33`  |
| 1690   | Layout 1             | `78f64f17be33`  |
| 1685   | Layout 1             | `78f64f17be33`  |
| 1680   | Layout 1             | `78f64f17be33`  |
| 1674   | Layout 1             | `78f64f17be33`  |
| 1668   | Layout 1             | `78f64f17be33`  |
| 1659   | Layout 1             | `78f64f17be33`  |
| 1649   | Layout 1             | `78f64f17be33`  |
| 1642   | Layout 1             | `78f64f17be33`  |
| 1636   | Layout 1             | `78f64f17be33`  |
| 1628   | Layout 1             | `78f64f17be33`  |
| 1622   | Layout 1             | `78f64f17be33`  |
| 1614   | Layout 1             | `78f64f17be33`  |
| 1608   | Layout 1             | `78f64f17be33`  |
| 1602   | Layout 1             | `78f64f17be33`  |
| 1598   | Layout 1             | `78f64f17be33`  |
| 1594   | Layout 1             | `78f64f17be33`  |
| 1590   | Layout 1             | `78f64f17be33`  |
| 1587   | Layout 1             | `78f64f17be33`  |
| 1584   | Layout 1             | `78f64f17be33`  |
| 1579   | Layout 1             | `78f64f17be33`  |
| 1572   | Layout 1             | `78f64f17be33`  |
| 1565   | Layout 1             | `78f64f17be33`  |
| 1559   | Layout 1             | `78f64f17be33`  |
| 1554   | Layout 1             | `78f64f17be33`  |
| 1547   | Layout 1             | `78f64f17be33`  |
| 1537   | Layout 1             | `78f64f17be33`  |
| 1529   | Layout 1             | `78f64f17be33`  |
| 1524   | Layout 1             | `78f64f17be33`  |
| 1519   | Layout 1             | `78f64f17be33`  |
| 1509   | Layout 1             | `78f64f17be33`  |
| 1506   | Layout 1             | `78f64f17be33`  |
| 1504   | Layout 1             | `78f64f17be33`  |
| 1500   | Layout 1             | `78f64f17be33`  |
| 1493   | Layout 1             | `78f64f17be33`  |
| 1489   | Layout 1             | `78f64f17be33`  |
| 1485   | Layout 1             | `78f64f17be33`  |
| 1481   | Layout 1             | `78f64f17be33`  |
| 1474   | Layout 1             | `78f64f17be33`  |
| 1466   | Layout 1             | `78f64f17be33`  |
| 1462   | Layout 1             | `78f64f17be33`  |
| 1459   | Layout 1             | `78f64f17be33`  |
| 1453   | Layout 1             | `78f64f17be33`  |
| 1450   | Layout 1             | `78f64f17be33`  |
| 1445   | Layout 1             | `78f64f17be33`  |
| 1439   | Layout 1             | `78f64f17be33`  |
| 1433   | Layout 1             | `78f64f17be33`  |
| 1430   | Layout 1             | `78f64f17be33`  |
| 1426   | Layout 1             | `78f64f17be33`  |
| 1421   | Layout 1             | `78f64f17be33`  |
| 1417   | Layout 1             | `78f64f17be33`  |
| 1416   | Layout 1             | `78f64f17be33`  |
| 1409   | Layout 1             | `78f64f17be33`  |
| 1405   | Layout 1             | `78f64f17be33`  |
| 1401   | Layout 1             | `78f64f17be33`  |
| 1396   | Layout 1             | `78f64f17be33`  |
| 1391   | Layout 1             | `78f64f17be33`  |
| 1390   | Layout 1             | `78f64f17be33`  |
| 1386   | Layout 1             | `78f64f17be33`  |
| 1381   | Layout 1             | `78f64f17be33`  |
| 1379   | Layout 1             | `78f64f17be33`  |
| 1372   | Layout 1             | `78f64f17be33`  |
| 1366   | Layout 1             | `78f64f17be33`  |
| 1364   | Layout 1             | `78f64f17be33`  |
| 1363   | Layout 1             | `78f64f17be33`  |
| 1360   | No documented layout | `78f64f17be33`  |
| 1358   | No documented layout | `78f64f17be33`  |
| 1355   | No documented layout | `78f64f17be33`  |
| 1351   | No documented layout | `78f64f17be33`  |
| 1348   | No documented layout | `78f64f17be33`  |
| 1346   | No documented layout | `78f64f17be33`  |
| 1341   | No documented layout | `78f64f17be33`  |
| 1340   | No documented layout | `78f64f17be33`  |
| 1338   | No documented layout | `78f64f17be33`  |
| 1335   | No documented layout | `78f64f17be33`  |
| 1333   | No documented layout | `78f64f17be33`  |
| 1329   | No documented layout | `78f64f17be33`  |
| 1327   | No documented layout | `78f64f17be33`  |
| 1324   | No documented layout | `78f64f17be33`  |
| 1321   | No documented layout | `78f64f17be33`  |
| 1319   | No documented layout | `78f64f17be33`  |
| 1318   | No documented layout | `78f64f17be33`  |
| 1316   | No documented layout | `78f64f17be33`  |
| 1313   | No documented layout | `78f64f17be33`  |
| 1311   | No file              | `78f64f17be33`  |
| 1309   | No file              | `78f64f17be33`  |
| 1304   | No file              | `78f64f17be33`  |
| 1292   | No file              | `78f64f17be33`  |
| 1286   | No file              | `78f64f17be33`  |
| 1280   | No file              | `78f64f17be33`  |
| 1276   | No file              | `78f64f17be33`  |
| 1267   | No file              | `78f64f17be33`  |
| 1261   | No file              | `78f64f17be33`  |
| 1256   | No file              | `78f64f17be33`  |
| 1250   | No file              | `78f64f17be33`  |
| 1246   | No file              | `78f64f17be33`  |
| 1239   | No file              | `78f64f17be33`  |
| 1230   | No file              | `78f64f17be33`  |
| 1226   | No file              | `78f64f17be33`  |
| 1220   | No file              | `78f64f17be33`  |
| 1217   | No file              | `78f64f17be33`  |
| 1211   | No file              | `78f64f17be33`  |
| 1210   | No file              | `78f64f17be33`  |
| 1208   | No file              | `78f64f17be33`  |
| 1203   | No file              | `78f64f17be33`  |
| 1197   | No file              | `78f64f17be33`  |
| 1194   | No file              | `78f64f17be33`  |
| 1192   | No file              | `78f64f17be33`  |
| 1187   | No file              | `78f64f17be33`  |
| 1183   | No file              | `78f64f17be33`  |
| 1177   | No file              | `78f64f17be33`  |
| 1173   | No file              | `78f64f17be33`  |
| 1167   | No file              | `78f64f17be33`  |
| 1164   | No file              | `78f64f17be33`  |
| 1156   | No file              | `78f64f17be33`  |
| 1149   | No file              | `78f64f17be33`  |
| 1144   | No file              | `78f64f17be33`  |
| 1137   | No file              | `78f64f17be33`  |
| 1132   | No file              | `78f64f17be33`  |
| 1127   | No file              | `78f64f17be33`  |
| 1122   | No file              | `78f64f17be33`  |
| 1118   | No file              | `78f64f17be33`  |
| 1114   | No file              | `78f64f17be33`  |
| 1109   | No file              | `78f64f17be33`  |
| 1102   | No file              | `78f64f17be33`  |
| 1096   | No file              | `78f64f17be33`  |
| 1088   | No file              | `78f64f17be33`  |
| 1081   | No file              | `78f64f17be33`  |
| 1076   | No file              | `78f64f17be33`  |
| 1069   | No file              | `78f64f17be33`  |
| 1064   | No file              | `78f64f17be33`  |
| 1058   | No file              | `78f64f17be33`  |
| 1051   | No file              | `78f64f17be33`  |
| 1044   | No file              | `78f64f17be33`  |
| 1036   | No file              | `78f64f17be33`  |
| 1026   | No file              | `78f64f17be33`  |
| 1016   | No file              | `78f64f17be33`  |
| 1009   | No file              | `78f64f17be33`  |
| 1005   | No file              | `78f64f17be33`  |
| 1000   | No file              | `78f64f17be33`  |
| 998    | No file              | `78f64f17be33`  |
| 990    | No file              | `78f64f17be33`  |
| 979    | No file              | `78f64f17be33`  |
| 972    | No file              | `78f64f17be33`  |
| 963    | No file              | `78f64f17be33`  |
| 955    | No file              | `78f64f17be33`  |
| 946    | No file              | `78f64f17be33`  |
| 938    | No file              | `78f64f17be33`  |
| 927    | No file              | `78f64f17be33`  |
| 911    | No file              | `78f64f17be33`  |
| 904    | No file              | `78f64f17be33`  |
| 899    | No file              | `78f64f17be33`  |
| 894    | No file              | `78f64f17be33`  |
| 885    | No file              | `78f64f17be33`  |
| 879    | No file              | `78f64f17be33`  |
| 872    | No file              | `78f64f17be33`  |
| 864    | No file              | `78f64f17be33`  |
| 855    | No file              | `78f64f17be33`  |
| 853    | No file              | `78f64f17be33`  |
| 845    | No file              | `78f64f17be33`  |
| 837    | No file              | `78f64f17be33`  |
| 829    | No file              | `78f64f17be33`  |
| 822    | No file              | `78f64f17be33`  |
| 814    | No file              | `78f64f17be33`  |
| 805    | No file              | `78f64f17be33`  |
| 794    | No file              | `78f64f17be33`  |
| 787    | No file              | `78f64f17be33`  |
| 780    | No file              | `78f64f17be33`  |
| 771    | No file              | `78f64f17be33`  |
| 760    | No file              | `78f64f17be33`  |
| 748    | No file              | `78f64f17be33`  |
| 741    | No file              | `78f64f17be33`  |
| 736    | No file              | `78f64f17be33`  |
| 731    | No file              | `78f64f17be33`  |
| 723    | No file              | `78f64f17be33`  |
| 711    | No file              | `78f64f17be33`  |
| 707    | No file              | `78f64f17be33`  |
| 697    | No file              | `78f64f17be33`  |
| 689    | No file              | `78f64f17be33`  |
| 683    | No file              | `78f64f17be33`  |
| 678    | No file              | `78f64f17be33`  |
| 670    | No file              | `78f64f17be33`  |
| 661    | No file              | `78f64f17be33`  |
| 656    | No file              | `78f64f17be33`  |
| 652    | No file              | `78f64f17be33`  |
| 643    | No file              | `78f64f17be33`  |
| 637    | No file              | `78f64f17be33`  |
| 630    | No file              | `78f64f17be33`  |
| 627    | No file              | `78f64f17be33`  |
| 621    | No file              | `78f64f17be33`  |
| 617    | No file              | `78f64f17be33`  |
| 615    | No file              | `78f64f17be33`  |
| 606    | No file              | `78f64f17be33`  |
| 599    | No file              | `78f64f17be33`  |
| 592    | No file              | `78f64f17be33`  |
| 586    | No file              | `78f64f17be33`  |
| 577    | No file              | `78f64f17be33`  |
| 569    | No file              | `78f64f17be33`  |
| 561    | No file              | `78f64f17be33`  |
| 554    | No file              | `78f64f17be33`  |
| 542    | No file              | `78f64f17be33`  |
| 532    | No file              | `78f64f17be33`  |
| 531    | No file              | `78f64f17be33`  |
| 526    | No file              | `78f64f17be33`  |
| 521    | No file              | `78f64f17be33`  |
| 517    | No file              | `78f64f17be33`  |
| 510    | No file              | `78f64f17be33`  |
| 508    | No file              | `78f64f17be33`  |
| 504    | No file              | `78f64f17be33`  |
| 497    | No file              | `78f64f17be33`  |
| 491    | No file              | `78f64f17be33`  |
| 485    | No file              | `78f64f17be33`  |
| 478    | No file              | `78f64f17be33`  |
| 472    | No file              | `78f64f17be33`  |
| 466    | No file              | `78f64f17be33`  |
| 457    | No file              | `78f64f17be33`  |
| 452    | No file              | `78f64f17be33`  |
| 449    | No file              | `78f64f17be33`  |
| 435    | No file              | `78f64f17be33`  |

<!-- versions:end -->

## Companion Files

| File                  | Required | Role                                                              |
| --------------------- | -------- | ----------------------------------------------------------------- |
| `skillgroup.bss`      | Optional | The skills of each placed group, see [`skillgroup.bss`](skillgroup_bss.md) |
| `stringtable.bss`     | Optional | Hash of each tab name key, see [`stringtable.bss`](stringtable_bss.md) |
| `languagedata_en.loc` | Optional | Class names (type `21`) and tab names (type `37`, `GAME` sheet)   |

All multi-byte values are little-endian.

## Layout 1

### File Layout

A PABR file of class grids, then a tab directory and a class table, then the
shared counted string table and 8-byte trailer (see
[`npcsimply.bss` String Table](npcsimply_bss.md#string-table-variable-4-bytes--strings)).

| Offset                     | Type                         | Field               | Notes                                           |
| -------------------------- | ---------------------------- | ------------------- | ----------------------------------------------- |
| `+0x00`                    | char[4]                      | magic               | `PABR`                                          |
| `+0x04`                    | u32                          | class_count         | Number of class grids                           |
| `+0x08`                    | Class Grid[class_count]      | grids               | One per class, see Class Grid                   |
| `grids+0x00`               | u32                          | tab_class_count     | Number of tab entries, equal to `class_count`   |
| `grids+0x04`               | Class Tabs[tab_class_count]  | tabs                | One per class, see Class Tabs                   |
| `tabs+0x00`                | u32                          | class_slots         | Always `101`                                    |
| `tabs+0x04`                | u16[class_slots]             | unknown_class_table | Indexed by class type, see Developer Sheets     |
| `unknown_class_table+0x00` | String Table                 | string_table        | Tab name keys, e.g. `LUA_SKILLTREE_PANEL_NAME0` |
| `string_table+0x00`        | u32                          | string_table_start  | Where `unknown_class_table` ends                |
| `string_table+0x04`        | u32                          | zero                | Always `0`                                      |

`ui_skillgroup_succession.bss` has `class_count` `0`, no tabs, the class
table and an empty string table.

### Class Grid (variable: 9 bytes + cells)

| Offset  | Type                | Field      | Notes                                                                    |
| ------- | ------------------- | ---------- | ------------------------------------------------------------------------ |
| `+0x00` | u8                  | class_type | Class, LOC type `21` (`0` Warrior, `4` Ranger, `32` Seraph)              |
| `+0x01` | u32                 | width      | Sheet columns; `8` on every class                                        |
| `+0x05` | u32                 | height     | Sheet rows; `42` to `123` in the combat window, `21` to `38` in awakening |
| `+0x09` | Cell[width][height] | cells      | `width * height` cells, column by column: cell `column * height + row`   |

### Cell (variable: 8 bytes + types)

| Offset        | Type           | Field                  | Notes                                                         |
| ------------- | -------------- | ---------------------- | ------------------------------------------------------------- |
| `+0x00`       | u32            | type_count             | Number of drawing types                                       |
| `+0x04`       | u8[type_count] | types                  | Cell types, see Cell Types; `2` means the cell holds a skill group |
| `types+0x00`  | u16            | group_no               | `skillgroup.bss` group when `types` holds `2`                 |
| `types+0x02`  | u8             | unknown_after_group_no | `0` on every cell of clients 1784 and 3474                    |
| `types+0x03`  | u8             | subgroup               | The tab band of the cell's row, set on every cell; see Tabs   |

### Class Tabs (variable: 9 bytes + tabs)

| Offset  | Type           | Field      | Notes                                |
| ------- | -------------- | ---------- | ------------------------------------ |
| `+0x00` | u8             | class_type | Same classes as the grids            |
| `+0x01` | u32            | tab_count  | `4` for every combat class; `1` to `4` in awakening |
| `+0x05` | u32            | unknown_05 | Always `0`; see Developer Sheets     |
| `+0x09` | Tab[tab_count] | tabs       | See Tab                              |

### Tab (5 bytes)

| Offset  | Type | Field        | Notes                                      |
| ------- | ---- | ------------ | ------------------------------------------ |
| `+0x00` | u32  | string_index | String table index of the tab name key     |
| `+0x04` | u8   | subgroup     | The `subgroup` the tab names               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes               |
| ------- | ------------------ | ------------ | ------------------- |
| `+0x00` | u32                | string_count | Number of strings   |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries |

## Cell Types

The client enum is `__eSkillGroupCellType_*`. Its values are not in any Lua
file (the client defines them), but the skill window script
(`luacscript/x64/window/skill/panel_window_skillgroup_all_1.luac`) draws
every type from `3` up with the line sprite `type - 2`, and those sprites
(`Combine_Etc_Skill_LineA_01` to `_11` in `Combine_Etc_Skill_01.dds`) are
box-drawing pieces. The enum names follow a 3 by 3 grid of left, centre,
right and top, middle, bottom.

| Value | Enum         | Draws | Combat cells |
| ----- | ------------ | ----- | ------------ |
| 0     | `Undefined`  |       | 0            |
| 1     | `Blank`      | Nothing | 21,363     |
| 2     | `SkillGroup` | A skill group | 2,546 |
| 3     | `LT`         | ┌     | 0            |
| 4     | `CT`         | ┬     | 449          |
| 5     | `RT`         | ┐     | 61           |
| 6     | `LM`         | ├     | 80           |
| 7     | `CM`         | ┼     | 5            |
| 8     | `RM`         | ┤     | 0            |
| 9     | `LB`         | └     | 408          |
| 10    | `CB`         | ┴     | 4            |
| 11    | `RB`         | ┘     | 3            |
| 12    | `Hori`       | ─     | 4,013        |
| 13    | `Vert`       | │     | 590          |

`CT` and `RT` are the two names the script never uses; they are placed by
the grid naming. The script adds one extra vertical piece for `LM`, `CM`,
`RM`, `LB`, `CB`, `RB` and `Vert`, exactly the pieces whose line reaches the
top edge of the cell. `TypeCount` (14) ends the enum.

All 2,091 combat and 788 awakening groups placed on a grid are in
`skillgroup.bss`.

## Tabs

Each tab names a `subgroup` by a string table index. Every `subgroup` a
class's cells use is one of its tabs. The string is a `GAME` sheet key, so
the English tab name is LOC type `37` with the key's
[`stringtable.bss`](stringtable_bss.md) hash and `str_id2 = 1`:

| Key                              | English (LOC)                                   |
| -------------------------------- | ----------------------------------------------- |
| `LUA_SKILLTREE_PANEL_NAME0`      | Main Skills                                     |
| `LUA_SKILLTREE_PANEL_NAME3`      | Secondary Skills                                |
| `LUA_SKILLTREE_PANEL_NAME1`      | Passives                                        |
| `LUA_SKILLTREE_PANEL_NAME6`      | Ascension Skill                                 |
| `LUA_SKILLTREE_PANEL_NAME5`      | Selected Skills                                 |
| `LUA_SKILLTREE_PANEL_PJKD_NAME`  | Fighting Buddha Skills                          |
| `LUA_SKILLTREE_PANEL_PNYW_NAME`  | Flow Skills                                     |
| `LUA_SKILLTREE_PANEL_PQW_NAME`   | Dragonblood Skills - "Bloodbearer of the Skysoaring Dragon" |
| `LUA_SKILLTREE_PANEL_PQW_NAME2`  | Hexeblood Skills - "Bloodbearer of the Landroving Witch" |
| `LUA_SKILLTREE_PANEL_PDKL_NAME`  | Champion of the Holy Covenant                   |
| `LUA_SKILLTREE_PANEL_PDKL_NAME2` | Avatar of Condemnation                          |

The combat window uses the first four for every class, in the same order.
In the awakening window 27 classes have Main Skills and Selected Skills.
Wukong (3), Scholar (6), Drakania (7) and Seraph (32) add or swap in
class-specific tabs. Shai (17) has only Main Skills: her awakening is the
Sol talents, not an awakening weapon. Agent (35) has a grid and tabs but no
skill cells; Agent has no awakening weapon yet (2026-09-28).

In game the two windows are the Main and Awakening tabs of the skill
window, and each tab lists its sections by `subgroup` number, not in the
order of the tab entries. Checked 2026-09-29:

- Wizard (28), Main: Main Skills, Secondary Skills, Passives. Awakening:
  Main Skills, Selected Skills.
- Scholar (6), Awakening: Main Skills, Flow Skills, Selected Skills, with
  the skills the file places under each.
- Drakania (7), Awakening: Main Skills, Hexeblood Skills, Dragonblood
  Skills, Selected Skills. The tab entries run Main Skills (subgroup `0`),
  Dragonblood (`2`), Hexeblood (`1`), Selected Skills (`3`), so the window
  sorts by `subgroup`. The two blood tabs are separate skill groups: both
  have Tip of the Scale, Spiteful Soul, Sundering Roar, Crackling Flame,
  Savage Decree, Storm Piercer and Tectonic Slam; Hexeblood adds Extinction,
  Flow: Concealed Claw, Flow: Obliterate and Storm Maul; Dragonblood adds
  Flow: Cloud's Strife, Aerial Burst and Doombringer.

The window no longer draws the tree: each section is a list of skill cards
in three columns, and those are the developer sheet's columns `0`, `3` and
`6` (sheet columns A, D and G; the two columns between them hold the tree
lines). A cell's card column is `column * 3 // width` (`0` left, `1` middle,
`2` right). On client 3474 the combat skill cells sit in columns `0`, `3` and
`6` 922, 581 and 1,107 times, the awakening ones 283, 282 and 223 times, and
no skill cell sits in another column. Earlier versions of this doc read the
cells row by row and split the grid height into thirds; that rule gives the
same card column for all 3,398 skill cells, because a column-by-column index
divided by the width falls in the same third.

`subgroup` is the same on all 8 cells of a sheet row (3,278 combat and 944
awakening rows on client 3474, none mixed), so it marks horizontal tab bands
of the sheet, and blank and line cells carry it too.

Drakania's Awakening grid has 38 rows (checked 2026-09-29). Main Skills
shows Burning Resolve, Fate Beckons and Trion Training (column `0`) on the
left, Legacy, Flow: Dragon Flight and Impale (column `3`) in the middle and
Elvia: Edict Unbound (column `6`) on the right. Over all four sections the
three columns hold 13, 11 and 10 skills in game, exactly the file's skill
cells per column. Inside a column the cards follow the cells top to bottom.
Hexeblood's middle column has an empty card slot after Extinction, probably
an empty grid cell between Extinction and Storm Piercer.

Elvia: Edict Unbound is usable only while the 10-minute Elvia weapon buff
from the Elvia realm is active, so the grid lists temporary skills too.

The Ascension Skill section holds skills that equipped items grant, the
same three on all 32 classes, each ranked PRI to PEN with the item's
enhancement level:

| Skill               | Item                      |
| ------------------- | ------------------------- |
| Blessing of Taebaek | Taebaek's Belt (`12282`)  |
| Blessing of Asadal  | Asadal Necklace (`11688`) |
| Fury of Asadal      | Asadal Belt (`12285`)     |

The skill window script tests `LUA_SKILLTREE_PANEL_NAME6` next to
`_isActiveItemGroup` and `PaGlobalFunc_SkillGroup_All_IsActiveItemSkill`,
and the section did not show on my Wizard, so it most likely appears only
while one of the items is equipped. Taebaek's Belt: see the GrumpyG guide
(grumpygreen.cricket/taebaeks-belt).

## Developer Sheets

A private server on client 1784 ships the sheets the files are built from,
under `DataSheet/skilldatasheet/uiskilltree/`:
`ui_tree_awakening_weaponskill.xlsm` is the source of its
`ui_skillgroup_awakening.bss`, and `ui_tree_main_weaponskillNew.xlsm` and
`ui_tree_main_weaponskill2.xlsm` are older combat versions. Each class is a
grid sheet with no column headers: `END` in the first row and in column A
mark the grid's edges ("END marks the limit of the data, so it must be
written at the end of the first column and the end of the first row", a
note in `uiguildskilltreelayout.xlsm`), column I lists the tab keys, and a
cell holds a group number or a comma-separated list of line characters. A
trailing comma (`─,─,`) compiles to an extra type `1`. Read column by
column, the awakening sheet matches the 1784 file on 6,383 of 6,384 cells
(type list and group number); the one miss is Shai, whose sheet ends a row
early.

`unknown_class_table` is cell A2 of each class sheet: the compiler moves
that number into the table and writes a Blank cell in its place (24 of 24
classes in the awakening sheet, 21 of 21 in each older combat sheet). The
value is a `skillgroup.bss` group with one rank that is never placed on the
grid: in the combat file the class's Succession skill (Warrior `596`, skill
4062 "전승 : 워리어의 투지", Succession: Warrior's Spirit; Woosa and Maegu
hold their Predominance and Transcendence skills), in the awakening file the
class's Awakening skill (Warrior `563`, skill 1712 "각성 : 고옌의 대검",
Awakening: Goyen's Greatsword). Client 3474 keeps 99 of the 101 slots and
adds slots `33` and `35`. No sheet or code names the table, so it keeps its
name.

No sheet cell supplies `unknown_after_group_no` or `unknown_05`. The 2016
client read these sheets itself into `ge::UISkillTreeLayout_CellValue`
(u8 `_cellType`, u8 `_arrowType`, u16 `_skillNo`), whose arrow byte came
from `↑ ↓ ← →` in a cell; no current sheet holds an arrow and the 1784 cell
shape differs, so `_arrowType` stays a candidate for
`unknown_after_group_no`, not a name. `unknown_05` may be the upper half of
a u64 `tab_count`; the data cannot tell.

## Notes

- The grid and cell layout comes from bdo-data-extractor, which keeps the
  tab directory and class table as an opaque footer. Both are decoded here
  and walk exactly to the string table on all three files.
- The tab pairs read `u32 string_index` then `u8 subgroup`. In the combat
  window the two are equal for every tab, so only the awakening window (for
  example Scholar: strings `0`, `3`, `1` for subgroups `0`, `1`, `2`) shows
  the order. The game sorts the sections by `subgroup` (Drakania, see Tabs).

## Open Questions

### What does the client do with `unknown_class_table`?

The table holds each class's Succession group (combat file) or Awakening
group (awakening file), see Developer Sheets. The skill window Lua does not
read it by any name I found; whether the client uses it to show those
skills outside the grid is open.
