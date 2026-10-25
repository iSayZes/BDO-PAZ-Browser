# `eventmanagement.bss` Format

## Purpose

The scheduled world events and what each one switches on. The file holds two
tables. An event row has a name, a condition script that says when and on
which servers it runs (`checkPeriodbyGMT(0, 2026/09/17-09:00,
2026/10/08-09:00);`, `CheckWeekDayAndDuration(3,20,45,15);`,
`!CheckWorldNo(400);`) and the keys of the event contents it sets. An event
contents row is one action with up to four parameters: an event map or
sound (`c_seteventmap`, `c_setsoundevent`), a character or field boss spawn
(`s_spawncharacter`, `s_spawnrandomfieldboss`) or an EXP or drop rate bonus
(`s_addexp`, `s_addlifeexp`, `s_adddroprate`). On client 3483 the file
holds 1,386 events and 517 event contents.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients       | File                  | Bytes   | Records                           | Row bytes                   |
| ------ | ------------- | --------------------- | ------- | --------------------------------- | --------------------------- |
| 4      | 805 and later | `eventmanagement.bss` | 498,255 | 1,386 Event Row, 517 Contents Row | 15                          |
| 3      | 652 to 794    | `eventmanagement.bss` | 71,930  | 128 Event Row, 85 Contents Row    | 165 to 529, 488 on average  |
| 2      | 526 to 643    | `eventmanagement.bss` | 7,033   | 13 Event Row, 43 Contents Row     | 62 to 1,324, 111 on average |
| 1      | 435 to 521    | `eventmanagement.bss` | 6,196   | 14 Event Row, 33 Contents Row     | 64 to 1,326, 116 on average |

| Layout | File                  | Known             | Unknown        |
| ------ | --------------------- | ----------------- | -------------- |
| 4      | `eventmanagement.bss` | 496,869 B (99.7%) | 1,386 B (0.3%) |
| 3      | `eventmanagement.bss` | 71,802 B (99.8%)  | 128 B (0.2%)   |
| 2      | `eventmanagement.bss` | 7,020 B (99.8%)   | 13 B (0.2%)    |
| 1      | `eventmanagement.bss` | 6,182 B (99.8%)   | 14 B (0.2%)    |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 4 | `842ab8c748f9`  |
| 3482   | Layout 4 | `842ab8c748f9`  |
| 3474   | Layout 4 | `842ab8c748f9`  |
| 3473   | Layout 4 | `842ab8c748f9`  |
| 3464   | Layout 4 | `842ab8c748f9`  |
| 3458   | Layout 4 | `842ab8c748f9`  |
| 3454   | Layout 4 | `842ab8c748f9`  |
| 3444   | Layout 4 | `842ab8c748f9`  |
| 3435   | Layout 4 | `842ab8c748f9`  |
| 3426   | Layout 4 | `842ab8c748f9`  |
| 3418   | Layout 4 | `842ab8c748f9`  |
| 3412   | Layout 4 | `842ab8c748f9`  |
| 3402   | Layout 4 | `842ab8c748f9`  |
| 3396   | Layout 4 | `842ab8c748f9`  |
| 3387   | Layout 4 | `842ab8c748f9`  |
| 3381   | Layout 4 | `842ab8c748f9`  |
| 3373   | Layout 4 | `842ab8c748f9`  |
| 3364   | Layout 4 | `842ab8c748f9`  |
| 3356   | Layout 4 | `842ab8c748f9`  |
| 3349   | Layout 4 | `842ab8c748f9`  |
| 3342   | Layout 4 | `842ab8c748f9`  |
| 3335   | Layout 4 | `842ab8c748f9`  |
| 3326   | Layout 4 | `842ab8c748f9`  |
| 3321   | Layout 4 | `842ab8c748f9`  |
| 3314   | Layout 4 | `842ab8c748f9`  |
| 3303   | Layout 4 | `842ab8c748f9`  |
| 3302   | Layout 4 | `842ab8c748f9`  |
| 3293   | Layout 4 | `842ab8c748f9`  |
| 3283   | Layout 4 | `842ab8c748f9`  |
| 3275   | Layout 4 | `842ab8c748f9`  |
| 3267   | Layout 4 | `842ab8c748f9`  |
| 3258   | Layout 4 | `842ab8c748f9`  |
| 3251   | Layout 4 | `842ab8c748f9`  |
| 3242   | Layout 4 | `842ab8c748f9`  |
| 3235   | Layout 4 | `842ab8c748f9`  |
| 3229   | Layout 4 | `842ab8c748f9`  |
| 3212   | Layout 4 | `842ab8c748f9`  |
| 3203   | Layout 4 | `842ab8c748f9`  |
| 3193   | Layout 4 | `842ab8c748f9`  |
| 3186   | Layout 4 | `842ab8c748f9`  |
| 3177   | Layout 4 | `842ab8c748f9`  |
| 3169   | Layout 4 | `842ab8c748f9`  |
| 3158   | Layout 4 | `842ab8c748f9`  |
| 3151   | Layout 4 | `842ab8c748f9`  |
| 3144   | Layout 4 | `842ab8c748f9`  |
| 3133   | Layout 4 | `842ab8c748f9`  |
| 3125   | Layout 4 | `842ab8c748f9`  |
| 3118   | Layout 4 | `842ab8c748f9`  |
| 3111   | Layout 4 | `842ab8c748f9`  |
| 3103   | Layout 4 | `842ab8c748f9`  |
| 3095   | Layout 4 | `842ab8c748f9`  |
| 3086   | Layout 4 | `842ab8c748f9`  |
| 3072   | Layout 4 | `842ab8c748f9`  |
| 3062   | Layout 4 | `842ab8c748f9`  |
| 3052   | Layout 4 | `842ab8c748f9`  |
| 3045   | Layout 4 | `842ab8c748f9`  |
| 3037   | Layout 4 | `842ab8c748f9`  |
| 3030   | Layout 4 | `842ab8c748f9`  |
| 3021   | Layout 4 | `842ab8c748f9`  |
| 3012   | Layout 4 | `842ab8c748f9`  |
| 3002   | Layout 4 | `842ab8c748f9`  |
| 2995   | Layout 4 | `842ab8c748f9`  |
| 2987   | Layout 4 | `842ab8c748f9`  |
| 2978   | Layout 4 | `842ab8c748f9`  |
| 2970   | Layout 4 | `842ab8c748f9`  |
| 2959   | Layout 4 | `842ab8c748f9`  |
| 2951   | Layout 4 | `842ab8c748f9`  |
| 2942   | Layout 4 | `842ab8c748f9`  |
| 2935   | Layout 4 | `842ab8c748f9`  |
| 2932   | Layout 4 | `842ab8c748f9`  |
| 2923   | Layout 4 | `842ab8c748f9`  |
| 2919   | Layout 4 | `842ab8c748f9`  |
| 2907   | Layout 4 | `842ab8c748f9`  |
| 2900   | Layout 4 | `842ab8c748f9`  |
| 2891   | Layout 4 | `842ab8c748f9`  |
| 2882   | Layout 4 | `842ab8c748f9`  |
| 2872   | Layout 4 | `842ab8c748f9`  |
| 2863   | Layout 4 | `842ab8c748f9`  |
| 2855   | Layout 4 | `842ab8c748f9`  |
| 2849   | Layout 4 | `842ab8c748f9`  |
| 2844   | Layout 4 | `842ab8c748f9`  |
| 2834   | Layout 4 | `842ab8c748f9`  |
| 2825   | Layout 4 | `842ab8c748f9`  |
| 2819   | Layout 4 | `842ab8c748f9`  |
| 2811   | Layout 4 | `842ab8c748f9`  |
| 2803   | Layout 4 | `842ab8c748f9`  |
| 2794   | Layout 4 | `842ab8c748f9`  |
| 2783   | Layout 4 | `842ab8c748f9`  |
| 2774   | Layout 4 | `842ab8c748f9`  |
| 2765   | Layout 4 | `842ab8c748f9`  |
| 2756   | Layout 4 | `842ab8c748f9`  |
| 2750   | Layout 4 | `842ab8c748f9`  |
| 2743   | Layout 4 | `842ab8c748f9`  |
| 2736   | Layout 4 | `842ab8c748f9`  |
| 2726   | Layout 4 | `842ab8c748f9`  |
| 2717   | Layout 4 | `842ab8c748f9`  |
| 2709   | Layout 4 | `842ab8c748f9`  |
| 2703   | Layout 4 | `842ab8c748f9`  |
| 2695   | Layout 4 | `842ab8c748f9`  |
| 2684   | Layout 4 | `842ab8c748f9`  |
| 2672   | Layout 4 | `842ab8c748f9`  |
| 2665   | Layout 4 | `842ab8c748f9`  |
| 2657   | Layout 4 | `842ab8c748f9`  |
| 2649   | Layout 4 | `842ab8c748f9`  |
| 2644   | Layout 4 | `842ab8c748f9`  |
| 2637   | Layout 4 | `842ab8c748f9`  |
| 2629   | Layout 4 | `842ab8c748f9`  |
| 2619   | Layout 4 | `842ab8c748f9`  |
| 2612   | Layout 4 | `842ab8c748f9`  |
| 2606   | Layout 4 | `842ab8c748f9`  |
| 2602   | Layout 4 | `842ab8c748f9`  |
| 2601   | Layout 4 | `842ab8c748f9`  |
| 2592   | Layout 4 | `842ab8c748f9`  |
| 2583   | Layout 4 | `842ab8c748f9`  |
| 2575   | Layout 4 | `842ab8c748f9`  |
| 2567   | Layout 4 | `842ab8c748f9`  |
| 2560   | Layout 4 | `842ab8c748f9`  |
| 2553   | Layout 4 | `842ab8c748f9`  |
| 2545   | Layout 4 | `842ab8c748f9`  |
| 2538   | Layout 4 | `842ab8c748f9`  |
| 2529   | Layout 4 | `842ab8c748f9`  |
| 2519   | Layout 4 | `842ab8c748f9`  |
| 2513   | Layout 4 | `842ab8c748f9`  |
| 2510   | Layout 4 | `842ab8c748f9`  |
| 2507   | Layout 4 | `842ab8c748f9`  |
| 2503   | Layout 4 | `842ab8c748f9`  |
| 2498   | Layout 4 | `842ab8c748f9`  |
| 2492   | Layout 4 | `842ab8c748f9`  |
| 2487   | Layout 4 | `842ab8c748f9`  |
| 2480   | Layout 4 | `842ab8c748f9`  |
| 2474   | Layout 4 | `842ab8c748f9`  |
| 2468   | Layout 4 | `842ab8c748f9`  |
| 2460   | Layout 4 | `842ab8c748f9`  |
| 2453   | Layout 4 | `842ab8c748f9`  |
| 2444   | Layout 4 | `842ab8c748f9`  |
| 2438   | Layout 4 | `842ab8c748f9`  |
| 2434   | Layout 4 | `842ab8c748f9`  |
| 2429   | Layout 4 | `842ab8c748f9`  |
| 2421   | Layout 4 | `842ab8c748f9`  |
| 2414   | Layout 4 | `842ab8c748f9`  |
| 2407   | Layout 4 | `842ab8c748f9`  |
| 2401   | Layout 4 | `842ab8c748f9`  |
| 2397   | Layout 4 | `842ab8c748f9`  |
| 2393   | Layout 4 | `842ab8c748f9`  |
| 2384   | Layout 4 | `842ab8c748f9`  |
| 2378   | Layout 4 | `842ab8c748f9`  |
| 2372   | Layout 4 | `842ab8c748f9`  |
| 2358   | Layout 4 | `842ab8c748f9`  |
| 2352   | Layout 4 | `842ab8c748f9`  |
| 2347   | Layout 4 | `842ab8c748f9`  |
| 2343   | Layout 4 | `842ab8c748f9`  |
| 2335   | Layout 4 | `842ab8c748f9`  |
| 2327   | Layout 4 | `842ab8c748f9`  |
| 2324   | Layout 4 | `842ab8c748f9`  |
| 2319   | Layout 4 | `842ab8c748f9`  |
| 2313   | Layout 4 | `842ab8c748f9`  |
| 2308   | Layout 4 | `842ab8c748f9`  |
| 2302   | Layout 4 | `842ab8c748f9`  |
| 2295   | Layout 4 | `842ab8c748f9`  |
| 2290   | Layout 4 | `842ab8c748f9`  |
| 2284   | Layout 4 | `842ab8c748f9`  |
| 2276   | Layout 4 | `842ab8c748f9`  |
| 2269   | Layout 4 | `842ab8c748f9`  |
| 2259   | Layout 4 | `842ab8c748f9`  |
| 2250   | Layout 4 | `842ab8c748f9`  |
| 2243   | Layout 4 | `842ab8c748f9`  |
| 2235   | Layout 4 | `842ab8c748f9`  |
| 2229   | Layout 4 | `842ab8c748f9`  |
| 2224   | Layout 4 | `842ab8c748f9`  |
| 2218   | Layout 4 | `842ab8c748f9`  |
| 2215   | Layout 4 | `842ab8c748f9`  |
| 2207   | Layout 4 | `842ab8c748f9`  |
| 2203   | Layout 4 | `842ab8c748f9`  |
| 2196   | Layout 4 | `842ab8c748f9`  |
| 2192   | Layout 4 | `842ab8c748f9`  |
| 2189   | Layout 4 | `842ab8c748f9`  |
| 2183   | Layout 4 | `842ab8c748f9`  |
| 2179   | Layout 4 | `842ab8c748f9`  |
| 2171   | Layout 4 | `842ab8c748f9`  |
| 2163   | Layout 4 | `842ab8c748f9`  |
| 2156   | Layout 4 | `842ab8c748f9`  |
| 2151   | Layout 4 | `842ab8c748f9`  |
| 2147   | Layout 4 | `842ab8c748f9`  |
| 2142   | Layout 4 | `842ab8c748f9`  |
| 2138   | Layout 4 | `842ab8c748f9`  |
| 2134   | Layout 4 | `842ab8c748f9`  |
| 2130   | Layout 4 | `842ab8c748f9`  |
| 2122   | Layout 4 | `842ab8c748f9`  |
| 2107   | Layout 4 | `842ab8c748f9`  |
| 2098   | Layout 4 | `842ab8c748f9`  |
| 2089   | Layout 4 | `842ab8c748f9`  |
| 2081   | Layout 4 | `842ab8c748f9`  |
| 2073   | Layout 4 | `842ab8c748f9`  |
| 2067   | Layout 4 | `842ab8c748f9`  |
| 2063   | Layout 4 | `842ab8c748f9`  |
| 2059   | Layout 4 | `842ab8c748f9`  |
| 2052   | Layout 4 | `842ab8c748f9`  |
| 2044   | Layout 4 | `842ab8c748f9`  |
| 2039   | Layout 4 | `842ab8c748f9`  |
| 2032   | Layout 4 | `842ab8c748f9`  |
| 2025   | Layout 4 | `842ab8c748f9`  |
| 2011   | Layout 4 | `842ab8c748f9`  |
| 2005   | Layout 4 | `842ab8c748f9`  |
| 2000   | Layout 4 | `842ab8c748f9`  |
| 1996   | Layout 4 | `842ab8c748f9`  |
| 1991   | Layout 4 | `842ab8c748f9`  |
| 1985   | Layout 4 | `842ab8c748f9`  |
| 1980   | Layout 4 | `842ab8c748f9`  |
| 1969   | Layout 4 | `842ab8c748f9`  |
| 1964   | Layout 4 | `842ab8c748f9`  |
| 1958   | Layout 4 | `842ab8c748f9`  |
| 1950   | Layout 4 | `842ab8c748f9`  |
| 1945   | Layout 4 | `842ab8c748f9`  |
| 1937   | Layout 4 | `842ab8c748f9`  |
| 1933   | Layout 4 | `842ab8c748f9`  |
| 1927   | Layout 4 | `842ab8c748f9`  |
| 1921   | Layout 4 | `842ab8c748f9`  |
| 1914   | Layout 4 | `842ab8c748f9`  |
| 1908   | Layout 4 | `842ab8c748f9`  |
| 1897   | Layout 4 | `842ab8c748f9`  |
| 1892   | Layout 4 | `842ab8c748f9`  |
| 1886   | Layout 4 | `842ab8c748f9`  |
| 1881   | Layout 4 | `842ab8c748f9`  |
| 1871   | Layout 4 | `842ab8c748f9`  |
| 1866   | Layout 4 | `842ab8c748f9`  |
| 1862   | Layout 4 | `842ab8c748f9`  |
| 1854   | Layout 4 | `842ab8c748f9`  |
| 1846   | Layout 4 | `842ab8c748f9`  |
| 1838   | Layout 4 | `842ab8c748f9`  |
| 1832   | Layout 4 | `842ab8c748f9`  |
| 1826   | Layout 4 | `842ab8c748f9`  |
| 1822   | Layout 4 | `842ab8c748f9`  |
| 1818   | Layout 4 | `842ab8c748f9`  |
| 1804   | Layout 4 | `842ab8c748f9`  |
| 1794   | Layout 4 | `842ab8c748f9`  |
| 1790   | Layout 4 | `842ab8c748f9`  |
| 1784   | Layout 4 | `842ab8c748f9`  |
| 1774   | Layout 4 | `842ab8c748f9`  |
| 1771   | Layout 4 | `842ab8c748f9`  |
| 1762   | Layout 4 | `842ab8c748f9`  |
| 1759   | Layout 4 | `842ab8c748f9`  |
| 1754   | Layout 4 | `842ab8c748f9`  |
| 1749   | Layout 4 | `842ab8c748f9`  |
| 1743   | Layout 4 | `842ab8c748f9`  |
| 1737   | Layout 4 | `842ab8c748f9`  |
| 1731   | Layout 4 | `842ab8c748f9`  |
| 1725   | Layout 4 | `842ab8c748f9`  |
| 1717   | Layout 4 | `842ab8c748f9`  |
| 1710   | Layout 4 | `842ab8c748f9`  |
| 1704   | Layout 4 | `842ab8c748f9`  |
| 1698   | Layout 4 | `842ab8c748f9`  |
| 1690   | Layout 4 | `842ab8c748f9`  |
| 1685   | Layout 4 | `842ab8c748f9`  |
| 1680   | Layout 4 | `842ab8c748f9`  |
| 1674   | Layout 4 | `842ab8c748f9`  |
| 1668   | Layout 4 | `842ab8c748f9`  |
| 1659   | Layout 4 | `842ab8c748f9`  |
| 1649   | Layout 4 | `842ab8c748f9`  |
| 1642   | Layout 4 | `842ab8c748f9`  |
| 1636   | Layout 4 | `842ab8c748f9`  |
| 1628   | Layout 4 | `842ab8c748f9`  |
| 1622   | Layout 4 | `842ab8c748f9`  |
| 1614   | Layout 4 | `842ab8c748f9`  |
| 1608   | Layout 4 | `842ab8c748f9`  |
| 1602   | Layout 4 | `842ab8c748f9`  |
| 1598   | Layout 4 | `842ab8c748f9`  |
| 1594   | Layout 4 | `842ab8c748f9`  |
| 1590   | Layout 4 | `842ab8c748f9`  |
| 1587   | Layout 4 | `842ab8c748f9`  |
| 1584   | Layout 4 | `842ab8c748f9`  |
| 1579   | Layout 4 | `842ab8c748f9`  |
| 1572   | Layout 4 | `842ab8c748f9`  |
| 1565   | Layout 4 | `842ab8c748f9`  |
| 1559   | Layout 4 | `842ab8c748f9`  |
| 1554   | Layout 4 | `842ab8c748f9`  |
| 1547   | Layout 4 | `842ab8c748f9`  |
| 1537   | Layout 4 | `842ab8c748f9`  |
| 1529   | Layout 4 | `842ab8c748f9`  |
| 1524   | Layout 4 | `842ab8c748f9`  |
| 1519   | Layout 4 | `842ab8c748f9`  |
| 1509   | Layout 4 | `842ab8c748f9`  |
| 1506   | Layout 4 | `842ab8c748f9`  |
| 1504   | Layout 4 | `842ab8c748f9`  |
| 1500   | Layout 4 | `842ab8c748f9`  |
| 1493   | Layout 4 | `842ab8c748f9`  |
| 1489   | Layout 4 | `842ab8c748f9`  |
| 1485   | Layout 4 | `842ab8c748f9`  |
| 1481   | Layout 4 | `842ab8c748f9`  |
| 1474   | Layout 4 | `842ab8c748f9`  |
| 1466   | Layout 4 | `842ab8c748f9`  |
| 1462   | Layout 4 | `842ab8c748f9`  |
| 1459   | Layout 4 | `842ab8c748f9`  |
| 1453   | Layout 4 | `842ab8c748f9`  |
| 1450   | Layout 4 | `842ab8c748f9`  |
| 1445   | Layout 4 | `842ab8c748f9`  |
| 1439   | Layout 4 | `842ab8c748f9`  |
| 1433   | Layout 4 | `842ab8c748f9`  |
| 1430   | Layout 4 | `842ab8c748f9`  |
| 1426   | Layout 4 | `842ab8c748f9`  |
| 1421   | Layout 4 | `842ab8c748f9`  |
| 1417   | Layout 4 | `842ab8c748f9`  |
| 1416   | Layout 4 | `842ab8c748f9`  |
| 1409   | Layout 4 | `842ab8c748f9`  |
| 1405   | Layout 4 | `842ab8c748f9`  |
| 1401   | Layout 4 | `842ab8c748f9`  |
| 1396   | Layout 4 | `842ab8c748f9`  |
| 1391   | Layout 4 | `842ab8c748f9`  |
| 1390   | Layout 4 | `842ab8c748f9`  |
| 1386   | Layout 4 | `842ab8c748f9`  |
| 1381   | Layout 4 | `842ab8c748f9`  |
| 1379   | Layout 4 | `842ab8c748f9`  |
| 1372   | Layout 4 | `842ab8c748f9`  |
| 1366   | Layout 4 | `842ab8c748f9`  |
| 1364   | Layout 4 | `842ab8c748f9`  |
| 1363   | Layout 4 | `842ab8c748f9`  |
| 1360   | Layout 4 | `842ab8c748f9`  |
| 1358   | Layout 4 | `842ab8c748f9`  |
| 1355   | Layout 4 | `842ab8c748f9`  |
| 1351   | Layout 4 | `842ab8c748f9`  |
| 1348   | Layout 4 | `842ab8c748f9`  |
| 1346   | Layout 4 | `842ab8c748f9`  |
| 1341   | Layout 4 | `842ab8c748f9`  |
| 1340   | Layout 4 | `842ab8c748f9`  |
| 1338   | Layout 4 | `842ab8c748f9`  |
| 1335   | Layout 4 | `842ab8c748f9`  |
| 1333   | Layout 4 | `842ab8c748f9`  |
| 1329   | Layout 4 | `842ab8c748f9`  |
| 1327   | Layout 4 | `842ab8c748f9`  |
| 1324   | Layout 4 | `842ab8c748f9`  |
| 1321   | Layout 4 | `842ab8c748f9`  |
| 1319   | Layout 4 | `842ab8c748f9`  |
| 1318   | Layout 4 | `842ab8c748f9`  |
| 1316   | Layout 4 | `842ab8c748f9`  |
| 1313   | Layout 4 | `842ab8c748f9`  |
| 1311   | Layout 4 | `842ab8c748f9`  |
| 1309   | Layout 4 | `842ab8c748f9`  |
| 1304   | Layout 4 | `842ab8c748f9`  |
| 1292   | Layout 4 | `842ab8c748f9`  |
| 1286   | Layout 4 | `842ab8c748f9`  |
| 1280   | Layout 4 | `842ab8c748f9`  |
| 1276   | Layout 4 | `842ab8c748f9`  |
| 1267   | Layout 4 | `842ab8c748f9`  |
| 1261   | Layout 4 | `842ab8c748f9`  |
| 1256   | Layout 4 | `842ab8c748f9`  |
| 1250   | Layout 4 | `842ab8c748f9`  |
| 1246   | Layout 4 | `842ab8c748f9`  |
| 1239   | Layout 4 | `842ab8c748f9`  |
| 1230   | Layout 4 | `842ab8c748f9`  |
| 1226   | Layout 4 | `842ab8c748f9`  |
| 1220   | Layout 4 | `842ab8c748f9`  |
| 1217   | Layout 4 | `842ab8c748f9`  |
| 1211   | Layout 4 | `842ab8c748f9`  |
| 1210   | Layout 4 | `842ab8c748f9`  |
| 1208   | Layout 4 | `842ab8c748f9`  |
| 1203   | Layout 4 | `842ab8c748f9`  |
| 1197   | Layout 4 | `842ab8c748f9`  |
| 1194   | Layout 4 | `842ab8c748f9`  |
| 1192   | Layout 4 | `842ab8c748f9`  |
| 1187   | Layout 4 | `842ab8c748f9`  |
| 1183   | Layout 4 | `842ab8c748f9`  |
| 1177   | Layout 4 | `842ab8c748f9`  |
| 1173   | Layout 4 | `842ab8c748f9`  |
| 1167   | Layout 4 | `842ab8c748f9`  |
| 1164   | Layout 4 | `842ab8c748f9`  |
| 1156   | Layout 4 | `842ab8c748f9`  |
| 1149   | Layout 4 | `842ab8c748f9`  |
| 1144   | Layout 4 | `842ab8c748f9`  |
| 1137   | Layout 4 | `842ab8c748f9`  |
| 1132   | Layout 4 | `842ab8c748f9`  |
| 1127   | Layout 4 | `842ab8c748f9`  |
| 1122   | Layout 4 | `842ab8c748f9`  |
| 1118   | Layout 4 | `842ab8c748f9`  |
| 1114   | Layout 4 | `842ab8c748f9`  |
| 1109   | Layout 4 | `842ab8c748f9`  |
| 1102   | Layout 4 | `842ab8c748f9`  |
| 1096   | Layout 4 | `842ab8c748f9`  |
| 1088   | Layout 4 | `842ab8c748f9`  |
| 1081   | Layout 4 | `842ab8c748f9`  |
| 1076   | Layout 4 | `842ab8c748f9`  |
| 1069   | Layout 4 | `842ab8c748f9`  |
| 1064   | Layout 4 | `842ab8c748f9`  |
| 1058   | Layout 4 | `842ab8c748f9`  |
| 1051   | Layout 4 | `842ab8c748f9`  |
| 1044   | Layout 4 | `842ab8c748f9`  |
| 1036   | Layout 4 | `842ab8c748f9`  |
| 1026   | Layout 4 | `842ab8c748f9`  |
| 1016   | Layout 4 | `842ab8c748f9`  |
| 1009   | Layout 4 | `842ab8c748f9`  |
| 1005   | Layout 4 | `842ab8c748f9`  |
| 1000   | Layout 4 | `842ab8c748f9`  |
| 998    | Layout 4 | `842ab8c748f9`  |
| 990    | Layout 4 | `842ab8c748f9`  |
| 979    | Layout 4 | `842ab8c748f9`  |
| 972    | Layout 4 | `842ab8c748f9`  |
| 963    | Layout 4 | `842ab8c748f9`  |
| 955    | Layout 4 | `842ab8c748f9`  |
| 946    | Layout 4 | `842ab8c748f9`  |
| 938    | Layout 4 | `842ab8c748f9`  |
| 927    | Layout 4 | `842ab8c748f9`  |
| 911    | Layout 4 | `842ab8c748f9`  |
| 904    | Layout 4 | `842ab8c748f9`  |
| 899    | Layout 4 | `842ab8c748f9`  |
| 894    | Layout 4 | `842ab8c748f9`  |
| 885    | Layout 4 | `842ab8c748f9`  |
| 879    | Layout 4 | `842ab8c748f9`  |
| 872    | Layout 4 | `842ab8c748f9`  |
| 864    | Layout 4 | `842ab8c748f9`  |
| 855    | Layout 4 | `842ab8c748f9`  |
| 853    | Layout 4 | `842ab8c748f9`  |
| 845    | Layout 4 | `842ab8c748f9`  |
| 837    | Layout 4 | `842ab8c748f9`  |
| 829    | Layout 4 | `842ab8c748f9`  |
| 822    | Layout 4 | `842ab8c748f9`  |
| 814    | Layout 4 | `842ab8c748f9`  |
| 805    | Layout 4 | `842ab8c748f9`  |
| 794    | Layout 3 | `842ab8c748f9`  |
| 787    | Layout 3 | `842ab8c748f9`  |
| 780    | Layout 3 | `842ab8c748f9`  |
| 771    | Layout 3 | `842ab8c748f9`  |
| 760    | Layout 3 | `842ab8c748f9`  |
| 748    | Layout 3 | `842ab8c748f9`  |
| 741    | Layout 3 | `842ab8c748f9`  |
| 736    | Layout 3 | `842ab8c748f9`  |
| 731    | Layout 3 | `842ab8c748f9`  |
| 723    | Layout 3 | `842ab8c748f9`  |
| 711    | Layout 3 | `842ab8c748f9`  |
| 707    | Layout 3 | `842ab8c748f9`  |
| 697    | Layout 3 | `842ab8c748f9`  |
| 689    | Layout 3 | `842ab8c748f9`  |
| 683    | Layout 3 | `842ab8c748f9`  |
| 678    | Layout 3 | `842ab8c748f9`  |
| 670    | Layout 3 | `842ab8c748f9`  |
| 661    | Layout 3 | `842ab8c748f9`  |
| 656    | Layout 3 | `842ab8c748f9`  |
| 652    | Layout 3 | `842ab8c748f9`  |
| 643    | Layout 2 | `842ab8c748f9`  |
| 637    | Layout 2 | `842ab8c748f9`  |
| 630    | Layout 2 | `842ab8c748f9`  |
| 627    | Layout 2 | `842ab8c748f9`  |
| 621    | Layout 2 | `842ab8c748f9`  |
| 617    | Layout 2 | `842ab8c748f9`  |
| 615    | Layout 2 | `842ab8c748f9`  |
| 606    | Layout 2 | `842ab8c748f9`  |
| 599    | Layout 2 | `842ab8c748f9`  |
| 592    | Layout 2 | `842ab8c748f9`  |
| 586    | Layout 2 | `842ab8c748f9`  |
| 577    | Layout 2 | `842ab8c748f9`  |
| 569    | Layout 2 | `842ab8c748f9`  |
| 561    | Layout 2 | `842ab8c748f9`  |
| 554    | Layout 2 | `842ab8c748f9`  |
| 542    | Layout 2 | `842ab8c748f9`  |
| 532    | Layout 2 | `842ab8c748f9`  |
| 531    | Layout 2 | `842ab8c748f9`  |
| 526    | Layout 2 | `842ab8c748f9`  |
| 521    | Layout 1 | `842ab8c748f9`  |
| 517    | Layout 1 | `842ab8c748f9`  |
| 510    | Layout 1 | `842ab8c748f9`  |
| 508    | Layout 1 | `842ab8c748f9`  |
| 504    | Layout 1 | `842ab8c748f9`  |
| 497    | Layout 1 | `842ab8c748f9`  |
| 491    | Layout 1 | `842ab8c748f9`  |
| 485    | Layout 1 | `842ab8c748f9`  |
| 478    | Layout 1 | `842ab8c748f9`  |
| 472    | Layout 1 | `842ab8c748f9`  |
| 466    | Layout 1 | `842ab8c748f9`  |
| 457    | Layout 1 | `842ab8c748f9`  |
| 452    | Layout 1 | `842ab8c748f9`  |
| 449    | Layout 1 | `842ab8c748f9`  |
| 435    | Layout 1 | `842ab8c748f9`  |

<!-- versions:end -->

## Companion Files

None. Character names come from LOC type 6, else the Korean
`characterstatic.dbss` name (`CHARACTER_NAME_KR` lookup index).

All multi-byte values are little-endian.

## Layout 4

### File Layout

PABR with two counted tables back to back, then the counted string table
and 8-byte trailer of
[`npcsimply.bss`](npcsimply_bss.md#string-table-variable-4-bytes--strings)
(`_common/pabr_strings.py`). Every text of both tables is a string table
index.

| Offset                | Type                         | Field              | Notes                                          |
| --------------------- | ---------------------------- | ------------------ | ---------------------------------------------- |
| `+0x00`               | char[4]                      | magic              | ASCII `PABR`                                   |
| `+0x04`               | u32                          | event_count        | Number of events; 1,386 on client 3483         |
| `+0x08`               | Event Row[event_count]       | event_rows         | See Event Row                                  |
| `event_rows+0x00`     | u32                          | contents_count     | Number of event contents; 517 on client 3483   |
| `event_rows+0x04`     | Contents Row[contents_count] | contents_rows      | See Contents Row                               |
| `contents_rows+0x00`  | String Table                 | string_table       | See String Table                               |
| `string_table+0x00`   | u32                          | string_table_start | Offset of the string table, where the rows end |
| `string_table+0x04`   | u32                          | zero               | Always `0`                                     |

On client 3483 the file is 8 + 1,386 x 15 + 4 + 517 x 22 + 466,071 + 8 =
498,255 bytes.

### Event Row (15 bytes)

| Offset  | Type | Field            | Notes                                                                                     |
| ------- | ---- | ---------------- | ----------------------------------------------------------------------------------------- |
| `+0x00` | u16  | event_no         | Row key, unique; `2` to `9702` on client 3483                                             |
| `+0x02` | u32  | event_name_ref   | String table index of the event name (`DonghwaV2`, `GuildHouseAuction_NA`); 635 distinct names on 1,386 rows (client 3483) |
| `+0x06` | u32  | condition_ref    | String table index of the condition script; see Conditions                                |
| `+0x0A` | u32  | setted_event_ref | String table index of the event contents list: `event_contents_no` values joined by `,` (`3222`, `9075, 9072, 9013`) |
| `+0x0E` | u8   | unknown_0e       | `0` on every row of clients 1784 and 3483; see Open Questions                             |

### Contents Row (22 bytes)

| Offset  | Type | Field             | Notes                                                                    |
| ------- | ---- | ----------------- | ------------------------------------------------------------------------ |
| `+0x00` | u16  | event_contents_no | Row key, unique; `1001` to `24598` on client 3483                        |
| `+0x02` | u32  | function_ref      | String table index of the action name, lower case (`s_spawncharacter`); see Functions |
| `+0x06` | u32  | param_1_ref       | String table index of the first parameter                                |
| `+0x0A` | u32  | param_2_ref       | String table index of the second parameter; `0` as text on 356 of 517 rows (client 3483) |
| `+0x0E` | u32  | param_3_ref       | String table index of the third parameter                                |
| `+0x12` | u32  | param_4_ref       | String table index of the fourth parameter                               |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                     |
| ------- | ------------------ | ------------ | ----------------------------------------- |
| `+0x00` | u32                | string_count | `2405` on client 3483                     |
| `+0x04` | pstr[string_count] | strings      | Shared PABR entries; all UTF-16 on client 3483 |

Each text is stored once: rows with the same name, condition or parameter
share one index. On client 3483 the `0` of 1,380 parameter slots is the one
entry at index `2003`.

## Layout 3

No PABR header and no string table: the file opens with the event count,
and each row holds its texts inline as `str16`. The contents rows run to the
end of the file. Client 435 keeps the file in `gamecommondata/binary/`,
client 794 in `gamecommondata/binary/en/`; every text of both is ASCII.

### File Layout

| Offset            | Type                         | Field          | Notes                                        |
| ----------------- | ---------------------------- | -------------- | -------------------------------------------- |
| `+0x00`           | u32                          | event_count    | Number of events; 128 on client 794          |
| `+0x04`           | Event Row[event_count]       | event_rows     | See Event Row                                |
| `event_rows+0x00` | u32                          | contents_count | Number of event contents; 85 on client 794   |
| `event_rows+0x04` | Contents Row[contents_count] | contents_rows  | See Contents Row; the last row ends the file |

### Event Row (variable: 27 bytes + texts)

| Offset              | Type  | Field        | Notes                                                    |
| ------------------- | ----- | ------------ | -------------------------------------------------------- |
| `+0x00`             | u16   | event_no     | Row key, unique                                          |
| `+0x02`             | str16 | event_name   | Event name (`Cherry Blossom Event`, `BossSpawn_Thu_4_NA`) |
| `event_name+0x00`   | str16 | condition    | Condition script; see Conditions                         |
| `condition+0x00`    | str16 | setted_event | `event_contents_no` values joined by `,`                 |
| `setted_event+0x00` | u8    | unknown_0e   | `0` on every row of clients 652 to 794                   |

### Contents Row (variable: 42 bytes + texts)

| Offset          | Type  | Field             | Notes                                                       |
| --------------- | ----- | ----------------- | ----------------------------------------------------------- |
| `+0x00`         | u16   | event_contents_no | Row key, unique                                             |
| `+0x02`         | str16 | function          | Action name, lower case (`c_seteventmap`); see Functions    |
| `function+0x00` | str16 | param_1           | First parameter                                             |
| `param_1+0x00`  | str16 | param_2           | Second parameter; `0` on every row of clients 652 to 771    |
| `param_2+0x00`  | str16 | param_3           | Third parameter; `0` on every row of clients 652 to 771     |
| `param_3+0x00`  | str16 | param_4           | Fourth parameter; `0` on every row of clients 652 to 771    |

## Layout 2

A Contents Row holds two parameters; `param_2` is `0` on every row of
clients 435 to 643. Only the Contents Row differs from Layout 3.

### Contents Row (variable: 26 bytes + texts)

| Offset          | Type  | Field             | Notes |
| --------------- | ----- | ----------------- | ----- |
| `+0x00`         | u16   | event_contents_no |       |
| `+0x02`         | str16 | function          |       |
| `function+0x00` | str16 | param_1           |       |
| `param_1+0x00`  | str16 | param_2           |       |

## Layout 1

Both rows start with their key twice: `event_no_dup` equals `event_no` and
`event_contents_no_dup` equals `event_contents_no` on every row of clients
435 to 521. Only the two rows differ from Layout 2. On client 435 the file
holds 20 events (keys `1` to `22`) and 34 event contents (keys `1001` to
`4001`).

### Event Row (variable: 29 bytes + texts)

| Offset              | Type  | Field        | Notes                          |
| ------------------- | ----- | ------------ | ------------------------------ |
| `+0x00`             | u16   | event_no     |                                |
| `+0x02`             | u16   | event_no_dup | Copy of `event_no`             |
| `+0x04`             | str16 | event_name   |                                |
| `event_name+0x00`   | str16 | condition    |                                |
| `condition+0x00`    | str16 | setted_event |                                |
| `setted_event+0x00` | u8    | unknown_0e   | See Open Questions             |

### Contents Row (variable: 28 bytes + texts)

| Offset          | Type  | Field                 | Notes                       |
| --------------- | ----- | --------------------- | --------------------------- |
| `+0x00`         | u16   | event_contents_no     |                             |
| `+0x02`         | u16   | event_contents_no_dup | Copy of `event_contents_no` |
| `+0x04`         | str16 | function              |                             |
| `function+0x00` | str16 | param_1               |                             |
| `param_1+0x00`  | str16 | param_2               |                             |

## Conditions

The text of `condition_ref` is a list of calls separated by `;`, each one
optionally negated with `!`. Counted over the 1,386 events of client 3483
(an event with a call more than once counts once):

| Call                                                  | Events | Arguments                                                    |
| ----------------------------------------------------- | ------ | ------------------------------------------------------------ |
| `checkPeriod(start, end)`                             | 903    | Two times as `2025/07/10-09:00`                              |
| `checkPeriodbyGMT(n, start, end)`                     | 470    | `0` on every call, then two times                            |
| `CheckWeekDayAndDuration(day, hour, minute, minutes)` | 1,285  | Weekday `0` to `6`, start hour and minute, length in minutes |
| `CheckWorldNo(n)`                                     | 1,287  | Negated on every call (`!CheckWorldNo(400);`)                |
| `CheckServerType(type)`                               | 753    | Negated on 2,237 of 2,240 calls                              |
| `CheckMainChannel()`                                  | 740    | None                                                         |
| `BiWeeklyCheck(n)`                                    | 2      | `1` on both (`GuildHouseAuction_EU` and `_NA`)               |

No event has more than one period call, and 13 have none. The same calls
appear in the `visible_conditions` of [`newquest.bss`](newquest_bss.md) (as
`checkperiodbyGmt`).

## Functions

`function` names what an event contents row does. The `c_` functions act on
the client, the `s_` functions on the server. On client 3483:

| Function                 | Rows | Parameters                                                                     |
| ------------------------ | ---- | ------------------------------------------------------------------------------ |
| `s_spawncharacter`       | 230  | `param_1` character keys joined by `,` (`59128,59129,27199`), the rest `0`     |
| `s_addlifeexp`           | 120  | `param_1` an amount (`1000000`), `param_2` one of `0` to `6`, `8`, `9` or `11` (12 rows each) |
| `c_seteventmap`          | 41   | `param_1` an event map name (`xmas`, `halloween`)                              |
| `s_spawnrandomfieldboss` | 40   | `param_1` a field boss character key (`28922` Dastard Bheg), `param_2` and `param_3` `0` or `1` |
| `s_addexp`               | 17   | `param_1` an amount (`500000`)                                                 |
| `c_setsoundevent`        | 13   | `param_1` a time and region list (`DayTime-5, 30, 32, 77`), `param_2` a sound event (`Event_Xmas_Day`) |
| `s_addvehicleexp`        | 12   | `param_1` an amount                                                            |
| `s_adddroprate`          | 12   | `param_1` an amount (`100000`)                                                 |
| `s_addskillexp`          | 11   | `param_1` an amount                                                            |
| `c_seteventui`           | 5    | `param_1` an event name (`x-mas`, `ThanksGivingDay`)                           |
| `c_seteffectevent`       | 4    | `param_1` an effect name (`Aurora`, `firework`)                                |
| `s_changeselectrate`     | 3    | `param_1` a character key (`55944` Dog), then three numbers (`16001`, `0`, `3000`); see Open Questions |
| `s_copyequipitemevent`   | 2    | All `0`                                                                        |
| `c_navigationposition`   | 1    | `param_2` a list of positions, `param_3` the GAME sheet key `LUA_NAVIGATION_FISHING_EVENT` |

`s_varytemperature`, `s_showdroprateicon`, `s_showexpicon`,
`s_triggerexcution`, `s_feverpointmore` and `s_thanksgivingevent` have one
row each.

## Field Names

The event rows are the `EventManage` sheet and the event contents rows the
`EventContents` sheet of a private server's `DataSheets.bexcel` on client
1784. The private server's own compiled `eventmanagement.bss` matches its
sheets on 387 of 387 event keys and 229 of 229 contents keys in every
column (`function` ignoring case). The official client 1784 file matches by
key:

| Field                                    | Column            | Same value (client 1784) |
| ---------------------------------------- | ----------------- | ------------------------ |
| `event_no`                               | `EventNo`         | 387 of 387 keys          |
| `event_name_ref`                         | `EventName`       | 262 of 387               |
| `condition_ref`                          | `Condition`       | 255 of 387               |
| `setted_event_ref`                       | `SettedEvent`     | 387 of 387               |
| `event_contents_no`                      | `EventContentsNo` | 229 of 229 keys          |
| `function_ref`                           | `Function`        | 229 of 229, ignoring case |
| `param_1_ref` to `param_4_ref`           | `Param1` to `Param4` | 229 of 229            |

The name and condition misses are the private server's edits: boss spawn
names and times one hour apart (`BossSpawn_Sun_1400_NA` in the sheet,
`BossSpawn_Sun_1500_NA` in the file) and periods moved to other dates. The
official file has 402 event rows, 15 more than the sheet. Neither sheet has
a column for `unknown_0e`.

The 29-row `EventManage` table of a private server on client 519 has the
same four columns but holds 2017 events (`Flond_or_Goose` is key `2` there,
`4` on client 1784), so it names no field. Its `EventContents` table has the
six `EventContents` columns.

## Notes

- Neither table is stored in key order: the file starts with event `3050`
  and contents row `3049` (client 3483).
- On client 3483 every `setted_event` key (1,420 in all) is an
  `event_contents_no` of the file. 1,360 events set one contents row, 25 set
  two and one sets ten. 379 of the 517 contents rows are set by no event.
- 641 of the 673 distinct character keys in the `param_1` of
  `s_spawncharacter`, `s_spawnrandomfieldboss` and `s_changeselectrate` have
  a LOC type 6 name on client 3483.
- The sheet writes `function` in mixed case (`C_SetEventMap`,
  `S_SpawnCharacter`); the compiled file holds it in lower case. The
  parameters keep their case (`CherrBlossom_Festival`).
- The client Lua of client 3482 calls no getter on this table, and the
  2016 PDB has no struct for it.
- Clients 837 to 1246 name the file `#na#eventmanagement.bss`; the doc
  check reads that copy under the plain name. All 66 test clients of that
  range hold Layout 4.
- The contents keys run from `1001` to `4001` up to client 760. Client 771
  adds the `s_spawnrandomfieldboss` rows `7001` to `7012`, client 780 the
  `s_changeselectrate` rows `8004` to `8006` and the EXP and drop rate rows
  `9001` to `9022` (`s_addexp`, `s_adddroprate`), the first rows whose
  `param_2` to `param_4` are not `0` (`s_addlifeexp` `2000000`, `2`).
- The handler reads Layout 4 only.

## Open Questions

### What `unknown_0e` Holds

The byte after `setted_event_ref` is `0` on every row of the official
clients 1784 and 3483. In the private server's own client 1784 build it is
`1` on 6 of 390 rows (`SteamPunk_Halloween_2021`, `Cherry Blossom Event`
and four hot time and drop events), and no sheet column holds it. The only
official row with `1` is event `3` `Cherry Blossom Event` of clients 435 to
466 (Layout 1); every row of the test clients 472 to 1250 holds `0`. In the
client 1784 server's `Load_EventManage` the row keeps a u16 (set to `0x100`)
and a u8 (set to `0`) after the parsed `SettedEvent` list that no column
fills; one of them may be this byte.

### What the `s_changeselectrate` Parameters Name

The three `s_changeselectrate` rows hold `55944`, `55945` and `55946` in
`param_1` (LOC type 6 names all three Dog), then `16001`, `4998` or
`40218`, then `0`, then `3000`, `1500` or `13000` (client 3483). Which
table the second number keys and what the fourth one scales is not known.

### What `checkPeriodbyGMT` Reads From Its First Argument

`checkPeriodbyGMT` takes a number before its two times: `0` on every call
of the official clients 1784 (178 calls) and 3483 (470 calls). Only the
private server's client 1784 sheet writes `3` on some rows. It may be a
time zone offset or a mode; the data does not show which.
