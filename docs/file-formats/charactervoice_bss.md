# `charactervoice.bss` Format

## Purpose

The voices a player character can pick in character customization: per
character key, one list of voice names for each of two appearance types
and a voice count for each. The names (`PC_VCE_1Warrior_1`,
`PC_VCE_MN_T01_JP_Warrior_1`) sit in the PABR string table and the rows
point at them by index. On client 3482 the file holds 76 characters and 64
voice names (45 and 55 on client 1784); only Wizard (`29`) and `39859`
fill the second list.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients       | File                 | Bytes  | Records                | Row bytes                |
| ------ | ------------- | -------------------- | ------ | ---------------------- | ------------------------ |
| 2      | 805 and later | `charactervoice.bss` | 4,801  | 152 Voice List, 76 Row | 4 to 60, 16 on average   |
| 1      | 435 to 794    | `charactervoice.bss` | 10,952 | 36 Voice List, 18 Row  | 4 to 604, 299 on average |

| Layout | File                 | Known             | Unknown    |
| ------ | -------------------- | ----------------- | ---------- |
| 2      | `charactervoice.bss` | 4,801 B (100.0%)  | 0 B (0.0%) |
| 1      | `charactervoice.bss` | 10,952 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 2 | `05ca4a4bc3b1`  |
| 3482   | Layout 2 | `05ca4a4bc3b1`  |
| 3474   | Layout 2 | `05ca4a4bc3b1`  |
| 3473   | Layout 2 | `05ca4a4bc3b1`  |
| 3464   | Layout 2 | `05ca4a4bc3b1`  |
| 3458   | Layout 2 | `05ca4a4bc3b1`  |
| 3454   | Layout 2 | `05ca4a4bc3b1`  |
| 3444   | Layout 2 | `05ca4a4bc3b1`  |
| 3435   | Layout 2 | `05ca4a4bc3b1`  |
| 3426   | Layout 2 | `05ca4a4bc3b1`  |
| 3418   | Layout 2 | `05ca4a4bc3b1`  |
| 3412   | Layout 2 | `05ca4a4bc3b1`  |
| 3402   | Layout 2 | `05ca4a4bc3b1`  |
| 3396   | Layout 2 | `05ca4a4bc3b1`  |
| 3387   | Layout 2 | `05ca4a4bc3b1`  |
| 3381   | Layout 2 | `05ca4a4bc3b1`  |
| 3373   | Layout 2 | `05ca4a4bc3b1`  |
| 3364   | Layout 2 | `05ca4a4bc3b1`  |
| 3356   | Layout 2 | `05ca4a4bc3b1`  |
| 3349   | Layout 2 | `05ca4a4bc3b1`  |
| 3342   | Layout 2 | `05ca4a4bc3b1`  |
| 3335   | Layout 2 | `05ca4a4bc3b1`  |
| 3326   | Layout 2 | `05ca4a4bc3b1`  |
| 3321   | Layout 2 | `05ca4a4bc3b1`  |
| 3314   | Layout 2 | `05ca4a4bc3b1`  |
| 3303   | Layout 2 | `05ca4a4bc3b1`  |
| 3302   | Layout 2 | `05ca4a4bc3b1`  |
| 3293   | Layout 2 | `05ca4a4bc3b1`  |
| 3283   | Layout 2 | `05ca4a4bc3b1`  |
| 3275   | Layout 2 | `05ca4a4bc3b1`  |
| 3267   | Layout 2 | `05ca4a4bc3b1`  |
| 3258   | Layout 2 | `05ca4a4bc3b1`  |
| 3251   | Layout 2 | `05ca4a4bc3b1`  |
| 3242   | Layout 2 | `05ca4a4bc3b1`  |
| 3235   | Layout 2 | `05ca4a4bc3b1`  |
| 3229   | Layout 2 | `05ca4a4bc3b1`  |
| 3212   | Layout 2 | `05ca4a4bc3b1`  |
| 3203   | Layout 2 | `05ca4a4bc3b1`  |
| 3193   | Layout 2 | `05ca4a4bc3b1`  |
| 3186   | Layout 2 | `05ca4a4bc3b1`  |
| 3177   | Layout 2 | `05ca4a4bc3b1`  |
| 3169   | Layout 2 | `05ca4a4bc3b1`  |
| 3158   | Layout 2 | `05ca4a4bc3b1`  |
| 3151   | Layout 2 | `05ca4a4bc3b1`  |
| 3144   | Layout 2 | `05ca4a4bc3b1`  |
| 3133   | Layout 2 | `05ca4a4bc3b1`  |
| 3125   | Layout 2 | `05ca4a4bc3b1`  |
| 3118   | Layout 2 | `05ca4a4bc3b1`  |
| 3111   | Layout 2 | `05ca4a4bc3b1`  |
| 3103   | Layout 2 | `05ca4a4bc3b1`  |
| 3095   | Layout 2 | `05ca4a4bc3b1`  |
| 3086   | Layout 2 | `05ca4a4bc3b1`  |
| 3072   | Layout 2 | `05ca4a4bc3b1`  |
| 3062   | Layout 2 | `05ca4a4bc3b1`  |
| 3052   | Layout 2 | `05ca4a4bc3b1`  |
| 3045   | Layout 2 | `05ca4a4bc3b1`  |
| 3037   | Layout 2 | `05ca4a4bc3b1`  |
| 3030   | Layout 2 | `05ca4a4bc3b1`  |
| 3021   | Layout 2 | `05ca4a4bc3b1`  |
| 3012   | Layout 2 | `05ca4a4bc3b1`  |
| 3002   | Layout 2 | `05ca4a4bc3b1`  |
| 2995   | Layout 2 | `05ca4a4bc3b1`  |
| 2987   | Layout 2 | `05ca4a4bc3b1`  |
| 2978   | Layout 2 | `05ca4a4bc3b1`  |
| 2970   | Layout 2 | `05ca4a4bc3b1`  |
| 2959   | Layout 2 | `05ca4a4bc3b1`  |
| 2951   | Layout 2 | `05ca4a4bc3b1`  |
| 2942   | Layout 2 | `05ca4a4bc3b1`  |
| 2935   | Layout 2 | `05ca4a4bc3b1`  |
| 2932   | Layout 2 | `05ca4a4bc3b1`  |
| 2923   | Layout 2 | `05ca4a4bc3b1`  |
| 2919   | Layout 2 | `05ca4a4bc3b1`  |
| 2907   | Layout 2 | `05ca4a4bc3b1`  |
| 2900   | Layout 2 | `05ca4a4bc3b1`  |
| 2891   | Layout 2 | `05ca4a4bc3b1`  |
| 2882   | Layout 2 | `05ca4a4bc3b1`  |
| 2872   | Layout 2 | `05ca4a4bc3b1`  |
| 2863   | Layout 2 | `05ca4a4bc3b1`  |
| 2855   | Layout 2 | `05ca4a4bc3b1`  |
| 2849   | Layout 2 | `05ca4a4bc3b1`  |
| 2844   | Layout 2 | `05ca4a4bc3b1`  |
| 2834   | Layout 2 | `05ca4a4bc3b1`  |
| 2825   | Layout 2 | `05ca4a4bc3b1`  |
| 2819   | Layout 2 | `05ca4a4bc3b1`  |
| 2811   | Layout 2 | `05ca4a4bc3b1`  |
| 2803   | Layout 2 | `05ca4a4bc3b1`  |
| 2794   | Layout 2 | `05ca4a4bc3b1`  |
| 2783   | Layout 2 | `05ca4a4bc3b1`  |
| 2774   | Layout 2 | `05ca4a4bc3b1`  |
| 2765   | Layout 2 | `05ca4a4bc3b1`  |
| 2756   | Layout 2 | `05ca4a4bc3b1`  |
| 2750   | Layout 2 | `05ca4a4bc3b1`  |
| 2743   | Layout 2 | `05ca4a4bc3b1`  |
| 2736   | Layout 2 | `05ca4a4bc3b1`  |
| 2726   | Layout 2 | `05ca4a4bc3b1`  |
| 2717   | Layout 2 | `05ca4a4bc3b1`  |
| 2709   | Layout 2 | `05ca4a4bc3b1`  |
| 2703   | Layout 2 | `05ca4a4bc3b1`  |
| 2695   | Layout 2 | `05ca4a4bc3b1`  |
| 2684   | Layout 2 | `05ca4a4bc3b1`  |
| 2672   | Layout 2 | `05ca4a4bc3b1`  |
| 2665   | Layout 2 | `05ca4a4bc3b1`  |
| 2657   | Layout 2 | `05ca4a4bc3b1`  |
| 2649   | Layout 2 | `05ca4a4bc3b1`  |
| 2644   | Layout 2 | `05ca4a4bc3b1`  |
| 2637   | Layout 2 | `05ca4a4bc3b1`  |
| 2629   | Layout 2 | `05ca4a4bc3b1`  |
| 2619   | Layout 2 | `05ca4a4bc3b1`  |
| 2612   | Layout 2 | `05ca4a4bc3b1`  |
| 2606   | Layout 2 | `05ca4a4bc3b1`  |
| 2602   | Layout 2 | `05ca4a4bc3b1`  |
| 2601   | Layout 2 | `05ca4a4bc3b1`  |
| 2592   | Layout 2 | `05ca4a4bc3b1`  |
| 2583   | Layout 2 | `05ca4a4bc3b1`  |
| 2575   | Layout 2 | `05ca4a4bc3b1`  |
| 2567   | Layout 2 | `05ca4a4bc3b1`  |
| 2560   | Layout 2 | `05ca4a4bc3b1`  |
| 2553   | Layout 2 | `05ca4a4bc3b1`  |
| 2545   | Layout 2 | `05ca4a4bc3b1`  |
| 2538   | Layout 2 | `05ca4a4bc3b1`  |
| 2529   | Layout 2 | `05ca4a4bc3b1`  |
| 2519   | Layout 2 | `05ca4a4bc3b1`  |
| 2513   | Layout 2 | `05ca4a4bc3b1`  |
| 2510   | Layout 2 | `05ca4a4bc3b1`  |
| 2507   | Layout 2 | `05ca4a4bc3b1`  |
| 2503   | Layout 2 | `05ca4a4bc3b1`  |
| 2498   | Layout 2 | `05ca4a4bc3b1`  |
| 2492   | Layout 2 | `05ca4a4bc3b1`  |
| 2487   | Layout 2 | `05ca4a4bc3b1`  |
| 2480   | Layout 2 | `05ca4a4bc3b1`  |
| 2474   | Layout 2 | `05ca4a4bc3b1`  |
| 2468   | Layout 2 | `05ca4a4bc3b1`  |
| 2460   | Layout 2 | `05ca4a4bc3b1`  |
| 2453   | Layout 2 | `05ca4a4bc3b1`  |
| 2444   | Layout 2 | `05ca4a4bc3b1`  |
| 2438   | Layout 2 | `05ca4a4bc3b1`  |
| 2434   | Layout 2 | `05ca4a4bc3b1`  |
| 2429   | Layout 2 | `05ca4a4bc3b1`  |
| 2421   | Layout 2 | `05ca4a4bc3b1`  |
| 2414   | Layout 2 | `05ca4a4bc3b1`  |
| 2407   | Layout 2 | `05ca4a4bc3b1`  |
| 2401   | Layout 2 | `05ca4a4bc3b1`  |
| 2397   | Layout 2 | `05ca4a4bc3b1`  |
| 2393   | Layout 2 | `05ca4a4bc3b1`  |
| 2384   | Layout 2 | `05ca4a4bc3b1`  |
| 2378   | Layout 2 | `05ca4a4bc3b1`  |
| 2372   | Layout 2 | `05ca4a4bc3b1`  |
| 2358   | Layout 2 | `05ca4a4bc3b1`  |
| 2352   | Layout 2 | `05ca4a4bc3b1`  |
| 2347   | Layout 2 | `05ca4a4bc3b1`  |
| 2343   | Layout 2 | `05ca4a4bc3b1`  |
| 2335   | Layout 2 | `05ca4a4bc3b1`  |
| 2327   | Layout 2 | `05ca4a4bc3b1`  |
| 2324   | Layout 2 | `05ca4a4bc3b1`  |
| 2319   | Layout 2 | `05ca4a4bc3b1`  |
| 2313   | Layout 2 | `05ca4a4bc3b1`  |
| 2308   | Layout 2 | `05ca4a4bc3b1`  |
| 2302   | Layout 2 | `05ca4a4bc3b1`  |
| 2295   | Layout 2 | `05ca4a4bc3b1`  |
| 2290   | Layout 2 | `05ca4a4bc3b1`  |
| 2284   | Layout 2 | `05ca4a4bc3b1`  |
| 2276   | Layout 2 | `05ca4a4bc3b1`  |
| 2269   | Layout 2 | `05ca4a4bc3b1`  |
| 2259   | Layout 2 | `05ca4a4bc3b1`  |
| 2250   | Layout 2 | `05ca4a4bc3b1`  |
| 2243   | Layout 2 | `05ca4a4bc3b1`  |
| 2235   | Layout 2 | `05ca4a4bc3b1`  |
| 2229   | Layout 2 | `05ca4a4bc3b1`  |
| 2224   | Layout 2 | `05ca4a4bc3b1`  |
| 2218   | Layout 2 | `05ca4a4bc3b1`  |
| 2215   | Layout 2 | `05ca4a4bc3b1`  |
| 2207   | Layout 2 | `05ca4a4bc3b1`  |
| 2203   | Layout 2 | `05ca4a4bc3b1`  |
| 2196   | Layout 2 | `05ca4a4bc3b1`  |
| 2192   | Layout 2 | `05ca4a4bc3b1`  |
| 2189   | Layout 2 | `05ca4a4bc3b1`  |
| 2183   | Layout 2 | `05ca4a4bc3b1`  |
| 2179   | Layout 2 | `05ca4a4bc3b1`  |
| 2171   | Layout 2 | `05ca4a4bc3b1`  |
| 2163   | Layout 2 | `05ca4a4bc3b1`  |
| 2156   | Layout 2 | `05ca4a4bc3b1`  |
| 2151   | Layout 2 | `05ca4a4bc3b1`  |
| 2147   | Layout 2 | `05ca4a4bc3b1`  |
| 2142   | Layout 2 | `05ca4a4bc3b1`  |
| 2138   | Layout 2 | `05ca4a4bc3b1`  |
| 2134   | Layout 2 | `05ca4a4bc3b1`  |
| 2130   | Layout 2 | `05ca4a4bc3b1`  |
| 2122   | Layout 2 | `05ca4a4bc3b1`  |
| 2107   | Layout 2 | `05ca4a4bc3b1`  |
| 2098   | Layout 2 | `05ca4a4bc3b1`  |
| 2089   | Layout 2 | `05ca4a4bc3b1`  |
| 2081   | Layout 2 | `05ca4a4bc3b1`  |
| 2073   | Layout 2 | `05ca4a4bc3b1`  |
| 2067   | Layout 2 | `05ca4a4bc3b1`  |
| 2063   | Layout 2 | `05ca4a4bc3b1`  |
| 2059   | Layout 2 | `05ca4a4bc3b1`  |
| 2052   | Layout 2 | `05ca4a4bc3b1`  |
| 2044   | Layout 2 | `05ca4a4bc3b1`  |
| 2039   | Layout 2 | `05ca4a4bc3b1`  |
| 2032   | Layout 2 | `05ca4a4bc3b1`  |
| 2025   | Layout 2 | `05ca4a4bc3b1`  |
| 2011   | Layout 2 | `05ca4a4bc3b1`  |
| 2005   | Layout 2 | `05ca4a4bc3b1`  |
| 2000   | Layout 2 | `05ca4a4bc3b1`  |
| 1996   | Layout 2 | `05ca4a4bc3b1`  |
| 1991   | Layout 2 | `05ca4a4bc3b1`  |
| 1985   | Layout 2 | `05ca4a4bc3b1`  |
| 1980   | Layout 2 | `05ca4a4bc3b1`  |
| 1969   | Layout 2 | `05ca4a4bc3b1`  |
| 1964   | Layout 2 | `05ca4a4bc3b1`  |
| 1958   | Layout 2 | `05ca4a4bc3b1`  |
| 1950   | Layout 2 | `05ca4a4bc3b1`  |
| 1945   | Layout 2 | `05ca4a4bc3b1`  |
| 1937   | Layout 2 | `05ca4a4bc3b1`  |
| 1933   | Layout 2 | `05ca4a4bc3b1`  |
| 1927   | Layout 2 | `05ca4a4bc3b1`  |
| 1921   | Layout 2 | `05ca4a4bc3b1`  |
| 1914   | Layout 2 | `05ca4a4bc3b1`  |
| 1908   | Layout 2 | `05ca4a4bc3b1`  |
| 1897   | Layout 2 | `05ca4a4bc3b1`  |
| 1892   | Layout 2 | `05ca4a4bc3b1`  |
| 1886   | Layout 2 | `05ca4a4bc3b1`  |
| 1881   | Layout 2 | `05ca4a4bc3b1`  |
| 1871   | Layout 2 | `05ca4a4bc3b1`  |
| 1866   | Layout 2 | `05ca4a4bc3b1`  |
| 1862   | Layout 2 | `05ca4a4bc3b1`  |
| 1854   | Layout 2 | `05ca4a4bc3b1`  |
| 1846   | Layout 2 | `05ca4a4bc3b1`  |
| 1838   | Layout 2 | `05ca4a4bc3b1`  |
| 1832   | Layout 2 | `05ca4a4bc3b1`  |
| 1826   | Layout 2 | `05ca4a4bc3b1`  |
| 1822   | Layout 2 | `05ca4a4bc3b1`  |
| 1818   | Layout 2 | `05ca4a4bc3b1`  |
| 1804   | Layout 2 | `05ca4a4bc3b1`  |
| 1794   | Layout 2 | `05ca4a4bc3b1`  |
| 1790   | Layout 2 | `05ca4a4bc3b1`  |
| 1784   | Layout 2 | `05ca4a4bc3b1`  |
| 1774   | Layout 2 | `05ca4a4bc3b1`  |
| 1771   | Layout 2 | `05ca4a4bc3b1`  |
| 1762   | Layout 2 | `05ca4a4bc3b1`  |
| 1759   | Layout 2 | `05ca4a4bc3b1`  |
| 1754   | Layout 2 | `05ca4a4bc3b1`  |
| 1749   | Layout 2 | `05ca4a4bc3b1`  |
| 1743   | Layout 2 | `05ca4a4bc3b1`  |
| 1737   | Layout 2 | `05ca4a4bc3b1`  |
| 1731   | Layout 2 | `05ca4a4bc3b1`  |
| 1725   | Layout 2 | `05ca4a4bc3b1`  |
| 1717   | Layout 2 | `05ca4a4bc3b1`  |
| 1710   | Layout 2 | `05ca4a4bc3b1`  |
| 1704   | Layout 2 | `05ca4a4bc3b1`  |
| 1698   | Layout 2 | `05ca4a4bc3b1`  |
| 1690   | Layout 2 | `05ca4a4bc3b1`  |
| 1685   | Layout 2 | `05ca4a4bc3b1`  |
| 1680   | Layout 2 | `05ca4a4bc3b1`  |
| 1674   | Layout 2 | `05ca4a4bc3b1`  |
| 1668   | Layout 2 | `05ca4a4bc3b1`  |
| 1659   | Layout 2 | `05ca4a4bc3b1`  |
| 1649   | Layout 2 | `05ca4a4bc3b1`  |
| 1642   | Layout 2 | `05ca4a4bc3b1`  |
| 1636   | Layout 2 | `05ca4a4bc3b1`  |
| 1628   | Layout 2 | `05ca4a4bc3b1`  |
| 1622   | Layout 2 | `05ca4a4bc3b1`  |
| 1614   | Layout 2 | `05ca4a4bc3b1`  |
| 1608   | Layout 2 | `05ca4a4bc3b1`  |
| 1602   | Layout 2 | `05ca4a4bc3b1`  |
| 1598   | Layout 2 | `05ca4a4bc3b1`  |
| 1594   | Layout 2 | `05ca4a4bc3b1`  |
| 1590   | Layout 2 | `05ca4a4bc3b1`  |
| 1587   | Layout 2 | `05ca4a4bc3b1`  |
| 1584   | Layout 2 | `05ca4a4bc3b1`  |
| 1579   | Layout 2 | `05ca4a4bc3b1`  |
| 1572   | Layout 2 | `05ca4a4bc3b1`  |
| 1565   | Layout 2 | `05ca4a4bc3b1`  |
| 1559   | Layout 2 | `05ca4a4bc3b1`  |
| 1554   | Layout 2 | `05ca4a4bc3b1`  |
| 1547   | Layout 2 | `05ca4a4bc3b1`  |
| 1537   | Layout 2 | `05ca4a4bc3b1`  |
| 1529   | Layout 2 | `05ca4a4bc3b1`  |
| 1524   | Layout 2 | `05ca4a4bc3b1`  |
| 1519   | Layout 2 | `05ca4a4bc3b1`  |
| 1509   | Layout 2 | `05ca4a4bc3b1`  |
| 1506   | Layout 2 | `05ca4a4bc3b1`  |
| 1504   | Layout 2 | `05ca4a4bc3b1`  |
| 1500   | Layout 2 | `05ca4a4bc3b1`  |
| 1493   | Layout 2 | `05ca4a4bc3b1`  |
| 1489   | Layout 2 | `05ca4a4bc3b1`  |
| 1485   | Layout 2 | `05ca4a4bc3b1`  |
| 1481   | Layout 2 | `05ca4a4bc3b1`  |
| 1474   | Layout 2 | `05ca4a4bc3b1`  |
| 1466   | Layout 2 | `05ca4a4bc3b1`  |
| 1462   | Layout 2 | `05ca4a4bc3b1`  |
| 1459   | Layout 2 | `05ca4a4bc3b1`  |
| 1453   | Layout 2 | `05ca4a4bc3b1`  |
| 1450   | Layout 2 | `05ca4a4bc3b1`  |
| 1445   | Layout 2 | `05ca4a4bc3b1`  |
| 1439   | Layout 2 | `05ca4a4bc3b1`  |
| 1433   | Layout 2 | `05ca4a4bc3b1`  |
| 1430   | Layout 2 | `05ca4a4bc3b1`  |
| 1426   | Layout 2 | `05ca4a4bc3b1`  |
| 1421   | Layout 2 | `05ca4a4bc3b1`  |
| 1417   | Layout 2 | `05ca4a4bc3b1`  |
| 1416   | Layout 2 | `05ca4a4bc3b1`  |
| 1409   | Layout 2 | `05ca4a4bc3b1`  |
| 1405   | Layout 2 | `05ca4a4bc3b1`  |
| 1401   | Layout 2 | `05ca4a4bc3b1`  |
| 1396   | Layout 2 | `05ca4a4bc3b1`  |
| 1391   | Layout 2 | `05ca4a4bc3b1`  |
| 1390   | Layout 2 | `05ca4a4bc3b1`  |
| 1386   | Layout 2 | `05ca4a4bc3b1`  |
| 1381   | Layout 2 | `05ca4a4bc3b1`  |
| 1379   | Layout 2 | `05ca4a4bc3b1`  |
| 1372   | Layout 2 | `05ca4a4bc3b1`  |
| 1366   | Layout 2 | `05ca4a4bc3b1`  |
| 1364   | Layout 2 | `05ca4a4bc3b1`  |
| 1363   | Layout 2 | `05ca4a4bc3b1`  |
| 1360   | Layout 2 | `05ca4a4bc3b1`  |
| 1358   | Layout 2 | `05ca4a4bc3b1`  |
| 1355   | Layout 2 | `05ca4a4bc3b1`  |
| 1351   | Layout 2 | `05ca4a4bc3b1`  |
| 1348   | Layout 2 | `05ca4a4bc3b1`  |
| 1346   | Layout 2 | `05ca4a4bc3b1`  |
| 1341   | Layout 2 | `05ca4a4bc3b1`  |
| 1340   | Layout 2 | `05ca4a4bc3b1`  |
| 1338   | Layout 2 | `05ca4a4bc3b1`  |
| 1335   | Layout 2 | `05ca4a4bc3b1`  |
| 1333   | Layout 2 | `05ca4a4bc3b1`  |
| 1329   | Layout 2 | `05ca4a4bc3b1`  |
| 1327   | Layout 2 | `05ca4a4bc3b1`  |
| 1324   | Layout 2 | `05ca4a4bc3b1`  |
| 1321   | Layout 2 | `05ca4a4bc3b1`  |
| 1319   | Layout 2 | `05ca4a4bc3b1`  |
| 1318   | Layout 2 | `05ca4a4bc3b1`  |
| 1316   | Layout 2 | `05ca4a4bc3b1`  |
| 1313   | Layout 2 | `05ca4a4bc3b1`  |
| 1311   | Layout 2 | `05ca4a4bc3b1`  |
| 1309   | Layout 2 | `05ca4a4bc3b1`  |
| 1304   | Layout 2 | `05ca4a4bc3b1`  |
| 1292   | Layout 2 | `05ca4a4bc3b1`  |
| 1286   | Layout 2 | `05ca4a4bc3b1`  |
| 1280   | Layout 2 | `05ca4a4bc3b1`  |
| 1276   | Layout 2 | `05ca4a4bc3b1`  |
| 1267   | Layout 2 | `05ca4a4bc3b1`  |
| 1261   | Layout 2 | `05ca4a4bc3b1`  |
| 1256   | Layout 2 | `05ca4a4bc3b1`  |
| 1250   | Layout 2 | `05ca4a4bc3b1`  |
| 1246   | No file  | `05ca4a4bc3b1`  |
| 1239   | No file  | `05ca4a4bc3b1`  |
| 1230   | No file  | `05ca4a4bc3b1`  |
| 1226   | No file  | `05ca4a4bc3b1`  |
| 1220   | No file  | `05ca4a4bc3b1`  |
| 1217   | No file  | `05ca4a4bc3b1`  |
| 1211   | No file  | `05ca4a4bc3b1`  |
| 1210   | No file  | `05ca4a4bc3b1`  |
| 1208   | No file  | `05ca4a4bc3b1`  |
| 1203   | No file  | `05ca4a4bc3b1`  |
| 1197   | No file  | `05ca4a4bc3b1`  |
| 1194   | No file  | `05ca4a4bc3b1`  |
| 1192   | No file  | `05ca4a4bc3b1`  |
| 1187   | No file  | `05ca4a4bc3b1`  |
| 1183   | No file  | `05ca4a4bc3b1`  |
| 1177   | No file  | `05ca4a4bc3b1`  |
| 1173   | No file  | `05ca4a4bc3b1`  |
| 1167   | No file  | `05ca4a4bc3b1`  |
| 1164   | No file  | `05ca4a4bc3b1`  |
| 1156   | No file  | `05ca4a4bc3b1`  |
| 1149   | No file  | `05ca4a4bc3b1`  |
| 1144   | Layout 2 | `05ca4a4bc3b1`  |
| 1137   | Layout 2 | `05ca4a4bc3b1`  |
| 1132   | Layout 2 | `05ca4a4bc3b1`  |
| 1127   | Layout 2 | `05ca4a4bc3b1`  |
| 1122   | Layout 2 | `05ca4a4bc3b1`  |
| 1118   | Layout 2 | `05ca4a4bc3b1`  |
| 1114   | Layout 2 | `05ca4a4bc3b1`  |
| 1109   | Layout 2 | `05ca4a4bc3b1`  |
| 1102   | No file  | `05ca4a4bc3b1`  |
| 1096   | No file  | `05ca4a4bc3b1`  |
| 1088   | No file  | `05ca4a4bc3b1`  |
| 1081   | No file  | `05ca4a4bc3b1`  |
| 1076   | No file  | `05ca4a4bc3b1`  |
| 1069   | No file  | `05ca4a4bc3b1`  |
| 1064   | No file  | `05ca4a4bc3b1`  |
| 1058   | No file  | `05ca4a4bc3b1`  |
| 1051   | No file  | `05ca4a4bc3b1`  |
| 1044   | No file  | `05ca4a4bc3b1`  |
| 1036   | No file  | `05ca4a4bc3b1`  |
| 1026   | No file  | `05ca4a4bc3b1`  |
| 1016   | No file  | `05ca4a4bc3b1`  |
| 1009   | No file  | `05ca4a4bc3b1`  |
| 1005   | No file  | `05ca4a4bc3b1`  |
| 1000   | No file  | `05ca4a4bc3b1`  |
| 998    | No file  | `05ca4a4bc3b1`  |
| 990    | No file  | `05ca4a4bc3b1`  |
| 979    | No file  | `05ca4a4bc3b1`  |
| 972    | No file  | `05ca4a4bc3b1`  |
| 963    | No file  | `05ca4a4bc3b1`  |
| 955    | No file  | `05ca4a4bc3b1`  |
| 946    | No file  | `05ca4a4bc3b1`  |
| 938    | No file  | `05ca4a4bc3b1`  |
| 927    | No file  | `05ca4a4bc3b1`  |
| 911    | No file  | `05ca4a4bc3b1`  |
| 904    | No file  | `05ca4a4bc3b1`  |
| 899    | No file  | `05ca4a4bc3b1`  |
| 894    | No file  | `05ca4a4bc3b1`  |
| 885    | No file  | `05ca4a4bc3b1`  |
| 879    | No file  | `05ca4a4bc3b1`  |
| 872    | No file  | `05ca4a4bc3b1`  |
| 864    | No file  | `05ca4a4bc3b1`  |
| 855    | No file  | `05ca4a4bc3b1`  |
| 853    | No file  | `05ca4a4bc3b1`  |
| 845    | No file  | `05ca4a4bc3b1`  |
| 837    | No file  | `05ca4a4bc3b1`  |
| 829    | Layout 2 | `05ca4a4bc3b1`  |
| 822    | Layout 2 | `05ca4a4bc3b1`  |
| 814    | Layout 2 | `05ca4a4bc3b1`  |
| 805    | Layout 2 | `05ca4a4bc3b1`  |
| 794    | Layout 1 | `05ca4a4bc3b1`  |
| 787    | Layout 1 | `05ca4a4bc3b1`  |
| 780    | Layout 1 | `05ca4a4bc3b1`  |
| 771    | Layout 1 | `05ca4a4bc3b1`  |
| 760    | Layout 1 | `05ca4a4bc3b1`  |
| 748    | Layout 1 | `05ca4a4bc3b1`  |
| 741    | Layout 1 | `05ca4a4bc3b1`  |
| 736    | Layout 1 | `05ca4a4bc3b1`  |
| 731    | Layout 1 | `05ca4a4bc3b1`  |
| 723    | Layout 1 | `05ca4a4bc3b1`  |
| 711    | Layout 1 | `05ca4a4bc3b1`  |
| 707    | Layout 1 | `05ca4a4bc3b1`  |
| 697    | Layout 1 | `05ca4a4bc3b1`  |
| 689    | Layout 1 | `05ca4a4bc3b1`  |
| 683    | Layout 1 | `05ca4a4bc3b1`  |
| 678    | Layout 1 | `05ca4a4bc3b1`  |
| 670    | Layout 1 | `05ca4a4bc3b1`  |
| 661    | Layout 1 | `05ca4a4bc3b1`  |
| 656    | Layout 1 | `05ca4a4bc3b1`  |
| 652    | Layout 1 | `05ca4a4bc3b1`  |
| 643    | Layout 1 | `05ca4a4bc3b1`  |
| 637    | Layout 1 | `05ca4a4bc3b1`  |
| 630    | Layout 1 | `05ca4a4bc3b1`  |
| 627    | Layout 1 | `05ca4a4bc3b1`  |
| 621    | Layout 1 | `05ca4a4bc3b1`  |
| 617    | Layout 1 | `05ca4a4bc3b1`  |
| 615    | Layout 1 | `05ca4a4bc3b1`  |
| 606    | Layout 1 | `05ca4a4bc3b1`  |
| 599    | Layout 1 | `05ca4a4bc3b1`  |
| 592    | Layout 1 | `05ca4a4bc3b1`  |
| 586    | Layout 1 | `05ca4a4bc3b1`  |
| 577    | Layout 1 | `05ca4a4bc3b1`  |
| 569    | Layout 1 | `05ca4a4bc3b1`  |
| 561    | Layout 1 | `05ca4a4bc3b1`  |
| 554    | Layout 1 | `05ca4a4bc3b1`  |
| 542    | Layout 1 | `05ca4a4bc3b1`  |
| 532    | Layout 1 | `05ca4a4bc3b1`  |
| 531    | Layout 1 | `05ca4a4bc3b1`  |
| 526    | Layout 1 | `05ca4a4bc3b1`  |
| 521    | Layout 1 | `05ca4a4bc3b1`  |
| 517    | Layout 1 | `05ca4a4bc3b1`  |
| 510    | Layout 1 | `05ca4a4bc3b1`  |
| 508    | Layout 1 | `05ca4a4bc3b1`  |
| 504    | Layout 1 | `05ca4a4bc3b1`  |
| 497    | Layout 1 | `05ca4a4bc3b1`  |
| 491    | Layout 1 | `05ca4a4bc3b1`  |
| 485    | Layout 1 | `05ca4a4bc3b1`  |
| 478    | Layout 1 | `05ca4a4bc3b1`  |
| 472    | Layout 1 | `05ca4a4bc3b1`  |
| 466    | Layout 1 | `05ca4a4bc3b1`  |
| 457    | Layout 1 | `05ca4a4bc3b1`  |
| 452    | Layout 1 | `05ca4a4bc3b1`  |
| 449    | Layout 1 | `05ca4a4bc3b1`  |
| 435    | Layout 1 | `05ca4a4bc3b1`  |

<!-- versions:end -->

## Companion Files

| File                         | Required | Role                                                                        |
| ---------------------------- | -------- | --------------------------------------------------------------------------- |
| `characterstaticoffset.dbss` | Optional | The `characterstatic.dbss` keys, so a key without a row shows as plain text |
| `languagedata_en.loc`        | Optional | Character names, LOC type 6                                                 |

All multi-byte values are little-endian.

## Layout 2

### File Layout

| Offset              | Type              | Field              | Notes                                  |
| ------------------- | ----------------- | ------------------ | -------------------------------------- |
| `+0x00`             | char[4]           | magic              | ASCII `PABR`                           |
| `+0x04`             | u32               | record_count       | Number of rows                         |
| `+0x08`             | Row[record_count] | records            | See Row                                |
| `records+0x00`      | String Table      | string_table       | The voice names                        |
| `string_table+0x00` | u32               | string_table_start | Absolute offset of `string_count`      |
| `string_table+0x04` | u32               | zero               | `0`                                    |

### Row (variable: 10 bytes + voice lists)

| Offset         | Type          | Field         | Notes                                                                        |
| -------------- | ------------- | ------------- | ---------------------------------------------------------------------------- |
| `+0x00`        | u16           | character_key | Row key: a `characterstatic.dbss` character; each key once                   |
| `+0x02`        | Voice List[2] | voices        | Appearance type 0, then appearance type 1; see Voice List                    |
| `voices+0x00`  | u32[2]        | voice_count   | Voice count of appearance type 0, then 1; see Notes                          |

The rows are in no key order; client 3482 opens with 1, 2, 3, 4, 6, 5.

### Voice List (variable: 4 bytes + voice types)

| Offset  | Type                  | Field            | Notes                                         |
| ------- | --------------------- | ---------------- | --------------------------------------------- |
| `+0x00` | u32                   | voice_type_count | Number of `voice_types`; `0` for an unused appearance type |
| `+0x04` | u32[voice_type_count] | voice_types      | Index into `strings`, in the sheet's `VoiceType1` to `VoiceType20` order |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                                      |
| ------- | ------------------ | ------------ | ---------------------------------------------------------- |
| `+0x00` | u32                | string_count | 64 on client 3482                                          |
| `+0x04` | pstr[string_count] | strings      | Voice names, UTF-8 (`is_wide` `0`); every string has an index pointing at it (clients 1784 and 3482) |

## Layout 1

No PABR magic and no string table: the file opens with the row count and
each list holds the voice names inline. The Row is the same as in Layout 2.

### File Layout

| Offset  | Type              | Field        | Notes          |
| ------- | ----------------- | ------------ | -------------- |
| `+0x00` | u32               | record_count | Number of rows |
| `+0x04` | Row[record_count] | records      | See Row        |

### Voice List (variable: 4 bytes + voice types)

| Offset  | Type                   | Field            | Notes                                          |
| ------- | ---------------------- | ---------------- | ---------------------------------------------- |
| `+0x00` | u32                    | voice_type_count | Number of `voice_types`                        |
| `+0x04` | str8[voice_type_count] | voice_types      | Voice names inline (`PC_VCE_1Warrior_1`)        |

Client 794 stores the file as `gamecommondata/binary/en/charactervoice.bss`
with 18 rows: 7 lists hold 17 names with a `voice_count` of 8 and 11 hold
19 names with a count of 12.

## Field Names

The `CharacterVoice_Table` sheet of a private server's `DataSheets.bexcel`
on client 1784 has the columns `CharacterKey`, `CharName`,
`AppearanceType`, `VoiceCount` and `VoiceType1` to `VoiceType20`, one row
per character and appearance type: 46 rows, 45 of type `0` and one of type
`1` (character `29`). Each row matches one list of the client file.

| Field         | Column                         | Same value (client 1784) | Same value (client 3482) |
| ------------- | ------------------------------ | ------------------------ | ------------------------ |
| character_key | `CharacterKey`                 | 45 of 45                 | 25 of 45                 |
| voice_types   | `VoiceType1` to `VoiceType20`  | 46 of 46 lists           | 24 of 26 lists           |
| voice_count   | `VoiceCount`                   | 46 of 46                 | 25 of 26                 |

`AppearanceType` picks the list (`voices` entry `0` or `1`); `CharName` is
a note (`PC-워리어`) the client file does not hold. On client 3482 the 20
sheet keys `65001` to `65020` are gone; the file lists 33 keys from
`39831` to `39866` in their place. Character `8` (Wukong) holds one voice where the sheet has
`PC_VCE_6Blader_1`, and character `10` (Scholar) one where the sheet lists
eight.

## Notes

- `voice_count` equals the list length on 73 of 76 rows (client 3482). The
  three others (`30` Archer, `39860` and `39863`) list 8, 8 and 1 voices
  with a count of `2`; client 1784 has the same for `30`.
- The client Lua (`panel_customization_voice_renew.luac`, client 3482)
  fills the voice list from `getClassVoiceCount()` and picks a voice with
  `applyVoice(index, ...)`; no Lua call names a field of this table.
- The 33 keys from `39831` to `39866` (client 3482) are named
  `집사 PC-<class>` in `characterstatic.dbss`, with no LOC name; `39859` is
  `집사 PC-위자드`.
