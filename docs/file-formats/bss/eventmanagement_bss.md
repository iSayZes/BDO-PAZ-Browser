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

| Layout | Clients       | File                  | Bytes   | Records                           | Row bytes |
| ------ | ------------- | --------------------- | ------- | --------------------------------- | --------- |
| 1      | 805 and later | `eventmanagement.bss` | 498,255 | 1,386 Event Row, 517 Contents Row | 15        |

| Layout | File                  | Known             | Unknown        |
| ------ | --------------------- | ----------------- | -------------- |
| 1      | `eventmanagement.bss` | 496,869 B (99.7%) | 1,386 B (0.3%) |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `a68c9fd23782`  |
| 3482   | Layout 1             | `a68c9fd23782`  |
| 3474   | Layout 1             | `a68c9fd23782`  |
| 3473   | Layout 1             | `a68c9fd23782`  |
| 3464   | Layout 1             | `a68c9fd23782`  |
| 3458   | Layout 1             | `a68c9fd23782`  |
| 3454   | Layout 1             | `a68c9fd23782`  |
| 3444   | Layout 1             | `a68c9fd23782`  |
| 3435   | Layout 1             | `a68c9fd23782`  |
| 3426   | Layout 1             | `a68c9fd23782`  |
| 3418   | Layout 1             | `a68c9fd23782`  |
| 3412   | Layout 1             | `a68c9fd23782`  |
| 3402   | Layout 1             | `a68c9fd23782`  |
| 3396   | Layout 1             | `a68c9fd23782`  |
| 3387   | Layout 1             | `a68c9fd23782`  |
| 3381   | Layout 1             | `a68c9fd23782`  |
| 3373   | Layout 1             | `a68c9fd23782`  |
| 3364   | Layout 1             | `a68c9fd23782`  |
| 3356   | Layout 1             | `a68c9fd23782`  |
| 3349   | Layout 1             | `a68c9fd23782`  |
| 3342   | Layout 1             | `a68c9fd23782`  |
| 3335   | Layout 1             | `a68c9fd23782`  |
| 3326   | Layout 1             | `a68c9fd23782`  |
| 3321   | Layout 1             | `a68c9fd23782`  |
| 3314   | Layout 1             | `a68c9fd23782`  |
| 3303   | Layout 1             | `a68c9fd23782`  |
| 3302   | Layout 1             | `a68c9fd23782`  |
| 3293   | Layout 1             | `a68c9fd23782`  |
| 3283   | Layout 1             | `a68c9fd23782`  |
| 3275   | Layout 1             | `a68c9fd23782`  |
| 3267   | Layout 1             | `a68c9fd23782`  |
| 3258   | Layout 1             | `a68c9fd23782`  |
| 3251   | Layout 1             | `a68c9fd23782`  |
| 3242   | Layout 1             | `a68c9fd23782`  |
| 3235   | Layout 1             | `a68c9fd23782`  |
| 3229   | Layout 1             | `a68c9fd23782`  |
| 3212   | Layout 1             | `a68c9fd23782`  |
| 3203   | Layout 1             | `a68c9fd23782`  |
| 3193   | Layout 1             | `a68c9fd23782`  |
| 3186   | Layout 1             | `a68c9fd23782`  |
| 3177   | Layout 1             | `a68c9fd23782`  |
| 3169   | Layout 1             | `a68c9fd23782`  |
| 3158   | Layout 1             | `a68c9fd23782`  |
| 3151   | Layout 1             | `a68c9fd23782`  |
| 3144   | Layout 1             | `a68c9fd23782`  |
| 3133   | Layout 1             | `a68c9fd23782`  |
| 3125   | Layout 1             | `a68c9fd23782`  |
| 3118   | Layout 1             | `a68c9fd23782`  |
| 3111   | Layout 1             | `a68c9fd23782`  |
| 3103   | Layout 1             | `a68c9fd23782`  |
| 3095   | Layout 1             | `a68c9fd23782`  |
| 3086   | Layout 1             | `a68c9fd23782`  |
| 3072   | Layout 1             | `a68c9fd23782`  |
| 3062   | Layout 1             | `a68c9fd23782`  |
| 3052   | Layout 1             | `a68c9fd23782`  |
| 3045   | Layout 1             | `a68c9fd23782`  |
| 3037   | Layout 1             | `a68c9fd23782`  |
| 3030   | Layout 1             | `a68c9fd23782`  |
| 3021   | Layout 1             | `a68c9fd23782`  |
| 3012   | Layout 1             | `a68c9fd23782`  |
| 3002   | Layout 1             | `a68c9fd23782`  |
| 2995   | Layout 1             | `a68c9fd23782`  |
| 2987   | Layout 1             | `a68c9fd23782`  |
| 2978   | Layout 1             | `a68c9fd23782`  |
| 2970   | Layout 1             | `a68c9fd23782`  |
| 2959   | Layout 1             | `a68c9fd23782`  |
| 2951   | Layout 1             | `a68c9fd23782`  |
| 2942   | Layout 1             | `a68c9fd23782`  |
| 2935   | Layout 1             | `a68c9fd23782`  |
| 2932   | Layout 1             | `a68c9fd23782`  |
| 2923   | Layout 1             | `a68c9fd23782`  |
| 2919   | Layout 1             | `a68c9fd23782`  |
| 2907   | Layout 1             | `a68c9fd23782`  |
| 2900   | Layout 1             | `a68c9fd23782`  |
| 2891   | Layout 1             | `a68c9fd23782`  |
| 2882   | Layout 1             | `a68c9fd23782`  |
| 2872   | Layout 1             | `a68c9fd23782`  |
| 2863   | Layout 1             | `a68c9fd23782`  |
| 2855   | Layout 1             | `a68c9fd23782`  |
| 2849   | Layout 1             | `a68c9fd23782`  |
| 2844   | Layout 1             | `a68c9fd23782`  |
| 2834   | Layout 1             | `a68c9fd23782`  |
| 2825   | Layout 1             | `a68c9fd23782`  |
| 2819   | Layout 1             | `a68c9fd23782`  |
| 2811   | Layout 1             | `a68c9fd23782`  |
| 2803   | Layout 1             | `a68c9fd23782`  |
| 2794   | Layout 1             | `a68c9fd23782`  |
| 2783   | Layout 1             | `a68c9fd23782`  |
| 2774   | Layout 1             | `a68c9fd23782`  |
| 2765   | Layout 1             | `a68c9fd23782`  |
| 2756   | Layout 1             | `a68c9fd23782`  |
| 2750   | Layout 1             | `a68c9fd23782`  |
| 2743   | Layout 1             | `a68c9fd23782`  |
| 2736   | Layout 1             | `a68c9fd23782`  |
| 2726   | Layout 1             | `a68c9fd23782`  |
| 2717   | Layout 1             | `a68c9fd23782`  |
| 2709   | Layout 1             | `a68c9fd23782`  |
| 2703   | Layout 1             | `a68c9fd23782`  |
| 2695   | Layout 1             | `a68c9fd23782`  |
| 2684   | Layout 1             | `a68c9fd23782`  |
| 2672   | Layout 1             | `a68c9fd23782`  |
| 2665   | Layout 1             | `a68c9fd23782`  |
| 2657   | Layout 1             | `a68c9fd23782`  |
| 2649   | Layout 1             | `a68c9fd23782`  |
| 2644   | Layout 1             | `a68c9fd23782`  |
| 2637   | Layout 1             | `a68c9fd23782`  |
| 2629   | Layout 1             | `a68c9fd23782`  |
| 2619   | Layout 1             | `a68c9fd23782`  |
| 2612   | Layout 1             | `a68c9fd23782`  |
| 2606   | Layout 1             | `a68c9fd23782`  |
| 2602   | Layout 1             | `a68c9fd23782`  |
| 2601   | Layout 1             | `a68c9fd23782`  |
| 2592   | Layout 1             | `a68c9fd23782`  |
| 2583   | Layout 1             | `a68c9fd23782`  |
| 2575   | Layout 1             | `a68c9fd23782`  |
| 2567   | Layout 1             | `a68c9fd23782`  |
| 2560   | Layout 1             | `a68c9fd23782`  |
| 2553   | Layout 1             | `a68c9fd23782`  |
| 2545   | Layout 1             | `a68c9fd23782`  |
| 2538   | Layout 1             | `a68c9fd23782`  |
| 2529   | Layout 1             | `a68c9fd23782`  |
| 2519   | Layout 1             | `a68c9fd23782`  |
| 2513   | Layout 1             | `a68c9fd23782`  |
| 2510   | Layout 1             | `a68c9fd23782`  |
| 2507   | Layout 1             | `a68c9fd23782`  |
| 2503   | Layout 1             | `a68c9fd23782`  |
| 2498   | Layout 1             | `a68c9fd23782`  |
| 2492   | Layout 1             | `a68c9fd23782`  |
| 2487   | Layout 1             | `a68c9fd23782`  |
| 2480   | Layout 1             | `a68c9fd23782`  |
| 2474   | Layout 1             | `a68c9fd23782`  |
| 2468   | Layout 1             | `a68c9fd23782`  |
| 2460   | Layout 1             | `a68c9fd23782`  |
| 2453   | Layout 1             | `a68c9fd23782`  |
| 2444   | Layout 1             | `a68c9fd23782`  |
| 2438   | Layout 1             | `a68c9fd23782`  |
| 2434   | Layout 1             | `a68c9fd23782`  |
| 2429   | Layout 1             | `a68c9fd23782`  |
| 2421   | Layout 1             | `a68c9fd23782`  |
| 2414   | Layout 1             | `a68c9fd23782`  |
| 2407   | Layout 1             | `a68c9fd23782`  |
| 2401   | Layout 1             | `a68c9fd23782`  |
| 2397   | Layout 1             | `a68c9fd23782`  |
| 2393   | Layout 1             | `a68c9fd23782`  |
| 2384   | Layout 1             | `a68c9fd23782`  |
| 2378   | Layout 1             | `a68c9fd23782`  |
| 2372   | Layout 1             | `a68c9fd23782`  |
| 2358   | Layout 1             | `a68c9fd23782`  |
| 2352   | Layout 1             | `a68c9fd23782`  |
| 2347   | Layout 1             | `a68c9fd23782`  |
| 2343   | Layout 1             | `a68c9fd23782`  |
| 2335   | Layout 1             | `a68c9fd23782`  |
| 2327   | Layout 1             | `a68c9fd23782`  |
| 2324   | Layout 1             | `a68c9fd23782`  |
| 2319   | Layout 1             | `a68c9fd23782`  |
| 2313   | Layout 1             | `a68c9fd23782`  |
| 2308   | Layout 1             | `a68c9fd23782`  |
| 2302   | Layout 1             | `a68c9fd23782`  |
| 2295   | Layout 1             | `a68c9fd23782`  |
| 2290   | Layout 1             | `a68c9fd23782`  |
| 2284   | Layout 1             | `a68c9fd23782`  |
| 2276   | Layout 1             | `a68c9fd23782`  |
| 2269   | Layout 1             | `a68c9fd23782`  |
| 2259   | Layout 1             | `a68c9fd23782`  |
| 2250   | Layout 1             | `a68c9fd23782`  |
| 2243   | Layout 1             | `a68c9fd23782`  |
| 2235   | Layout 1             | `a68c9fd23782`  |
| 2229   | Layout 1             | `a68c9fd23782`  |
| 2224   | Layout 1             | `a68c9fd23782`  |
| 2218   | Layout 1             | `a68c9fd23782`  |
| 2215   | Layout 1             | `a68c9fd23782`  |
| 2207   | Layout 1             | `a68c9fd23782`  |
| 2203   | Layout 1             | `a68c9fd23782`  |
| 2196   | Layout 1             | `a68c9fd23782`  |
| 2192   | Layout 1             | `a68c9fd23782`  |
| 2189   | Layout 1             | `a68c9fd23782`  |
| 2183   | Layout 1             | `a68c9fd23782`  |
| 2179   | Layout 1             | `a68c9fd23782`  |
| 2171   | Layout 1             | `a68c9fd23782`  |
| 2163   | Layout 1             | `a68c9fd23782`  |
| 2156   | Layout 1             | `a68c9fd23782`  |
| 2151   | Layout 1             | `a68c9fd23782`  |
| 2147   | Layout 1             | `a68c9fd23782`  |
| 2142   | Layout 1             | `a68c9fd23782`  |
| 2138   | Layout 1             | `a68c9fd23782`  |
| 2134   | Layout 1             | `a68c9fd23782`  |
| 2130   | Layout 1             | `a68c9fd23782`  |
| 2122   | Layout 1             | `a68c9fd23782`  |
| 2107   | Layout 1             | `a68c9fd23782`  |
| 2098   | Layout 1             | `a68c9fd23782`  |
| 2089   | Layout 1             | `a68c9fd23782`  |
| 2081   | Layout 1             | `a68c9fd23782`  |
| 2073   | Layout 1             | `a68c9fd23782`  |
| 2067   | Layout 1             | `a68c9fd23782`  |
| 2063   | Layout 1             | `a68c9fd23782`  |
| 2059   | Layout 1             | `a68c9fd23782`  |
| 2052   | Layout 1             | `a68c9fd23782`  |
| 2044   | Layout 1             | `a68c9fd23782`  |
| 2039   | Layout 1             | `a68c9fd23782`  |
| 2032   | Layout 1             | `a68c9fd23782`  |
| 2025   | Layout 1             | `a68c9fd23782`  |
| 2011   | Layout 1             | `a68c9fd23782`  |
| 2005   | Layout 1             | `a68c9fd23782`  |
| 2000   | Layout 1             | `a68c9fd23782`  |
| 1996   | Layout 1             | `a68c9fd23782`  |
| 1991   | Layout 1             | `a68c9fd23782`  |
| 1985   | Layout 1             | `a68c9fd23782`  |
| 1980   | Layout 1             | `a68c9fd23782`  |
| 1969   | Layout 1             | `a68c9fd23782`  |
| 1964   | Layout 1             | `a68c9fd23782`  |
| 1958   | Layout 1             | `a68c9fd23782`  |
| 1950   | Layout 1             | `a68c9fd23782`  |
| 1945   | Layout 1             | `a68c9fd23782`  |
| 1937   | Layout 1             | `a68c9fd23782`  |
| 1933   | Layout 1             | `a68c9fd23782`  |
| 1927   | Layout 1             | `a68c9fd23782`  |
| 1921   | Layout 1             | `a68c9fd23782`  |
| 1914   | Layout 1             | `a68c9fd23782`  |
| 1908   | Layout 1             | `a68c9fd23782`  |
| 1897   | Layout 1             | `a68c9fd23782`  |
| 1892   | Layout 1             | `a68c9fd23782`  |
| 1886   | Layout 1             | `a68c9fd23782`  |
| 1881   | Layout 1             | `a68c9fd23782`  |
| 1871   | Layout 1             | `a68c9fd23782`  |
| 1866   | Layout 1             | `a68c9fd23782`  |
| 1862   | Layout 1             | `a68c9fd23782`  |
| 1854   | Layout 1             | `a68c9fd23782`  |
| 1846   | Layout 1             | `a68c9fd23782`  |
| 1838   | Layout 1             | `a68c9fd23782`  |
| 1832   | Layout 1             | `a68c9fd23782`  |
| 1826   | Layout 1             | `a68c9fd23782`  |
| 1822   | Layout 1             | `a68c9fd23782`  |
| 1818   | Layout 1             | `a68c9fd23782`  |
| 1804   | Layout 1             | `a68c9fd23782`  |
| 1794   | Layout 1             | `a68c9fd23782`  |
| 1790   | Layout 1             | `a68c9fd23782`  |
| 1784   | Layout 1             | `a68c9fd23782`  |
| 1774   | Layout 1             | `a68c9fd23782`  |
| 1771   | Layout 1             | `a68c9fd23782`  |
| 1762   | Layout 1             | `a68c9fd23782`  |
| 1759   | Layout 1             | `a68c9fd23782`  |
| 1754   | Layout 1             | `a68c9fd23782`  |
| 1749   | Layout 1             | `a68c9fd23782`  |
| 1743   | Layout 1             | `a68c9fd23782`  |
| 1737   | Layout 1             | `a68c9fd23782`  |
| 1731   | Layout 1             | `a68c9fd23782`  |
| 1725   | Layout 1             | `a68c9fd23782`  |
| 1717   | Layout 1             | `a68c9fd23782`  |
| 1710   | Layout 1             | `a68c9fd23782`  |
| 1704   | Layout 1             | `a68c9fd23782`  |
| 1698   | Layout 1             | `a68c9fd23782`  |
| 1690   | Layout 1             | `a68c9fd23782`  |
| 1685   | Layout 1             | `a68c9fd23782`  |
| 1680   | Layout 1             | `a68c9fd23782`  |
| 1674   | Layout 1             | `a68c9fd23782`  |
| 1668   | Layout 1             | `a68c9fd23782`  |
| 1659   | Layout 1             | `a68c9fd23782`  |
| 1649   | Layout 1             | `a68c9fd23782`  |
| 1642   | Layout 1             | `a68c9fd23782`  |
| 1636   | Layout 1             | `a68c9fd23782`  |
| 1628   | Layout 1             | `a68c9fd23782`  |
| 1622   | Layout 1             | `a68c9fd23782`  |
| 1614   | Layout 1             | `a68c9fd23782`  |
| 1608   | Layout 1             | `a68c9fd23782`  |
| 1602   | Layout 1             | `a68c9fd23782`  |
| 1598   | Layout 1             | `a68c9fd23782`  |
| 1594   | Layout 1             | `a68c9fd23782`  |
| 1590   | Layout 1             | `a68c9fd23782`  |
| 1587   | Layout 1             | `a68c9fd23782`  |
| 1584   | Layout 1             | `a68c9fd23782`  |
| 1579   | Layout 1             | `a68c9fd23782`  |
| 1572   | Layout 1             | `a68c9fd23782`  |
| 1565   | Layout 1             | `a68c9fd23782`  |
| 1559   | Layout 1             | `a68c9fd23782`  |
| 1554   | Layout 1             | `a68c9fd23782`  |
| 1547   | Layout 1             | `a68c9fd23782`  |
| 1537   | Layout 1             | `a68c9fd23782`  |
| 1529   | Layout 1             | `a68c9fd23782`  |
| 1524   | Layout 1             | `a68c9fd23782`  |
| 1519   | Layout 1             | `a68c9fd23782`  |
| 1509   | Layout 1             | `a68c9fd23782`  |
| 1506   | Layout 1             | `a68c9fd23782`  |
| 1504   | Layout 1             | `a68c9fd23782`  |
| 1500   | Layout 1             | `a68c9fd23782`  |
| 1493   | Layout 1             | `a68c9fd23782`  |
| 1489   | Layout 1             | `a68c9fd23782`  |
| 1485   | Layout 1             | `a68c9fd23782`  |
| 1481   | Layout 1             | `a68c9fd23782`  |
| 1474   | Layout 1             | `a68c9fd23782`  |
| 1466   | Layout 1             | `a68c9fd23782`  |
| 1462   | Layout 1             | `a68c9fd23782`  |
| 1459   | Layout 1             | `a68c9fd23782`  |
| 1453   | Layout 1             | `a68c9fd23782`  |
| 1450   | Layout 1             | `a68c9fd23782`  |
| 1445   | Layout 1             | `a68c9fd23782`  |
| 1439   | Layout 1             | `a68c9fd23782`  |
| 1433   | Layout 1             | `a68c9fd23782`  |
| 1430   | Layout 1             | `a68c9fd23782`  |
| 1426   | Layout 1             | `a68c9fd23782`  |
| 1421   | Layout 1             | `a68c9fd23782`  |
| 1417   | Layout 1             | `a68c9fd23782`  |
| 1416   | Layout 1             | `a68c9fd23782`  |
| 1409   | Layout 1             | `a68c9fd23782`  |
| 1405   | Layout 1             | `a68c9fd23782`  |
| 1401   | Layout 1             | `a68c9fd23782`  |
| 1396   | Layout 1             | `a68c9fd23782`  |
| 1391   | Layout 1             | `a68c9fd23782`  |
| 1390   | Layout 1             | `a68c9fd23782`  |
| 1386   | Layout 1             | `a68c9fd23782`  |
| 1381   | Layout 1             | `a68c9fd23782`  |
| 1379   | Layout 1             | `a68c9fd23782`  |
| 1372   | Layout 1             | `a68c9fd23782`  |
| 1366   | Layout 1             | `a68c9fd23782`  |
| 1364   | Layout 1             | `a68c9fd23782`  |
| 1363   | Layout 1             | `a68c9fd23782`  |
| 1360   | Layout 1             | `a68c9fd23782`  |
| 1358   | Layout 1             | `a68c9fd23782`  |
| 1355   | Layout 1             | `a68c9fd23782`  |
| 1351   | Layout 1             | `a68c9fd23782`  |
| 1348   | Layout 1             | `a68c9fd23782`  |
| 1346   | Layout 1             | `a68c9fd23782`  |
| 1341   | Layout 1             | `a68c9fd23782`  |
| 1340   | Layout 1             | `a68c9fd23782`  |
| 1338   | Layout 1             | `a68c9fd23782`  |
| 1335   | Layout 1             | `a68c9fd23782`  |
| 1333   | Layout 1             | `a68c9fd23782`  |
| 1329   | Layout 1             | `a68c9fd23782`  |
| 1327   | Layout 1             | `a68c9fd23782`  |
| 1324   | Layout 1             | `a68c9fd23782`  |
| 1321   | Layout 1             | `a68c9fd23782`  |
| 1319   | Layout 1             | `a68c9fd23782`  |
| 1318   | Layout 1             | `a68c9fd23782`  |
| 1316   | Layout 1             | `a68c9fd23782`  |
| 1313   | Layout 1             | `a68c9fd23782`  |
| 1311   | Layout 1             | `a68c9fd23782`  |
| 1309   | Layout 1             | `a68c9fd23782`  |
| 1304   | Layout 1             | `a68c9fd23782`  |
| 1292   | Layout 1             | `a68c9fd23782`  |
| 1286   | Layout 1             | `a68c9fd23782`  |
| 1280   | Layout 1             | `a68c9fd23782`  |
| 1276   | Layout 1             | `a68c9fd23782`  |
| 1267   | Layout 1             | `a68c9fd23782`  |
| 1261   | Layout 1             | `a68c9fd23782`  |
| 1256   | Layout 1             | `a68c9fd23782`  |
| 1250   | Layout 1             | `a68c9fd23782`  |
| 1246   | No file              | `a68c9fd23782`  |
| 1239   | No file              | `a68c9fd23782`  |
| 1230   | No file              | `a68c9fd23782`  |
| 1226   | No file              | `a68c9fd23782`  |
| 1220   | No file              | `a68c9fd23782`  |
| 1217   | No file              | `a68c9fd23782`  |
| 1211   | No file              | `a68c9fd23782`  |
| 1210   | No file              | `a68c9fd23782`  |
| 1208   | No file              | `a68c9fd23782`  |
| 1203   | No file              | `a68c9fd23782`  |
| 1197   | No file              | `a68c9fd23782`  |
| 1194   | No file              | `a68c9fd23782`  |
| 1192   | No file              | `a68c9fd23782`  |
| 1187   | No file              | `a68c9fd23782`  |
| 1183   | No file              | `a68c9fd23782`  |
| 1177   | No file              | `a68c9fd23782`  |
| 1173   | No file              | `a68c9fd23782`  |
| 1167   | No file              | `a68c9fd23782`  |
| 1164   | No file              | `a68c9fd23782`  |
| 1156   | No file              | `a68c9fd23782`  |
| 1149   | No file              | `a68c9fd23782`  |
| 1144   | No file              | `a68c9fd23782`  |
| 1137   | No file              | `a68c9fd23782`  |
| 1132   | No file              | `a68c9fd23782`  |
| 1127   | No file              | `a68c9fd23782`  |
| 1122   | No file              | `a68c9fd23782`  |
| 1118   | No file              | `a68c9fd23782`  |
| 1114   | No file              | `a68c9fd23782`  |
| 1109   | No file              | `a68c9fd23782`  |
| 1102   | No file              | `a68c9fd23782`  |
| 1096   | No file              | `a68c9fd23782`  |
| 1088   | No file              | `a68c9fd23782`  |
| 1081   | No file              | `a68c9fd23782`  |
| 1076   | No file              | `a68c9fd23782`  |
| 1069   | No file              | `a68c9fd23782`  |
| 1064   | No file              | `a68c9fd23782`  |
| 1058   | No file              | `a68c9fd23782`  |
| 1051   | No file              | `a68c9fd23782`  |
| 1044   | No file              | `a68c9fd23782`  |
| 1036   | No file              | `a68c9fd23782`  |
| 1026   | No file              | `a68c9fd23782`  |
| 1016   | No file              | `a68c9fd23782`  |
| 1009   | No file              | `a68c9fd23782`  |
| 1005   | No file              | `a68c9fd23782`  |
| 1000   | No file              | `a68c9fd23782`  |
| 998    | No file              | `a68c9fd23782`  |
| 990    | No file              | `a68c9fd23782`  |
| 979    | No file              | `a68c9fd23782`  |
| 972    | No file              | `a68c9fd23782`  |
| 963    | No file              | `a68c9fd23782`  |
| 955    | No file              | `a68c9fd23782`  |
| 946    | No file              | `a68c9fd23782`  |
| 938    | No file              | `a68c9fd23782`  |
| 927    | No file              | `a68c9fd23782`  |
| 911    | No file              | `a68c9fd23782`  |
| 904    | No file              | `a68c9fd23782`  |
| 899    | No file              | `a68c9fd23782`  |
| 894    | No file              | `a68c9fd23782`  |
| 885    | No file              | `a68c9fd23782`  |
| 879    | No file              | `a68c9fd23782`  |
| 872    | No file              | `a68c9fd23782`  |
| 864    | No file              | `a68c9fd23782`  |
| 855    | No file              | `a68c9fd23782`  |
| 853    | No file              | `a68c9fd23782`  |
| 845    | No file              | `a68c9fd23782`  |
| 837    | No file              | `a68c9fd23782`  |
| 829    | Layout 1             | `a68c9fd23782`  |
| 822    | Layout 1             | `a68c9fd23782`  |
| 814    | Layout 1             | `a68c9fd23782`  |
| 805    | Layout 1             | `a68c9fd23782`  |
| 794    | No documented layout | `a68c9fd23782`  |
| 787    | No documented layout | `a68c9fd23782`  |
| 780    | No documented layout | `a68c9fd23782`  |
| 771    | No documented layout | `a68c9fd23782`  |
| 760    | No documented layout | `a68c9fd23782`  |
| 748    | No documented layout | `a68c9fd23782`  |
| 741    | No documented layout | `a68c9fd23782`  |
| 736    | No documented layout | `a68c9fd23782`  |
| 731    | No documented layout | `a68c9fd23782`  |
| 723    | No documented layout | `a68c9fd23782`  |
| 711    | No documented layout | `a68c9fd23782`  |
| 707    | No documented layout | `a68c9fd23782`  |
| 697    | No documented layout | `a68c9fd23782`  |
| 689    | No documented layout | `a68c9fd23782`  |
| 683    | No documented layout | `a68c9fd23782`  |
| 678    | No documented layout | `a68c9fd23782`  |
| 670    | No documented layout | `a68c9fd23782`  |
| 661    | No documented layout | `a68c9fd23782`  |
| 656    | No documented layout | `a68c9fd23782`  |
| 652    | No documented layout | `a68c9fd23782`  |
| 643    | No documented layout | `a68c9fd23782`  |
| 637    | No documented layout | `a68c9fd23782`  |
| 630    | No documented layout | `a68c9fd23782`  |
| 627    | No documented layout | `a68c9fd23782`  |
| 621    | No documented layout | `a68c9fd23782`  |
| 617    | No documented layout | `a68c9fd23782`  |
| 615    | No documented layout | `a68c9fd23782`  |
| 606    | No documented layout | `a68c9fd23782`  |
| 599    | No documented layout | `a68c9fd23782`  |
| 592    | No documented layout | `a68c9fd23782`  |
| 586    | No documented layout | `a68c9fd23782`  |
| 577    | No documented layout | `a68c9fd23782`  |
| 569    | No documented layout | `a68c9fd23782`  |
| 561    | No documented layout | `a68c9fd23782`  |
| 554    | No documented layout | `a68c9fd23782`  |
| 542    | No documented layout | `a68c9fd23782`  |
| 532    | No documented layout | `a68c9fd23782`  |
| 531    | No documented layout | `a68c9fd23782`  |
| 526    | No documented layout | `a68c9fd23782`  |
| 521    | No documented layout | `a68c9fd23782`  |
| 517    | No documented layout | `a68c9fd23782`  |
| 510    | No documented layout | `a68c9fd23782`  |
| 508    | No documented layout | `a68c9fd23782`  |
| 504    | No documented layout | `a68c9fd23782`  |
| 497    | No documented layout | `a68c9fd23782`  |
| 491    | No documented layout | `a68c9fd23782`  |
| 485    | No documented layout | `a68c9fd23782`  |
| 478    | No documented layout | `a68c9fd23782`  |
| 472    | No documented layout | `a68c9fd23782`  |
| 466    | No documented layout | `a68c9fd23782`  |
| 457    | No documented layout | `a68c9fd23782`  |
| 452    | No documented layout | `a68c9fd23782`  |
| 449    | No documented layout | `a68c9fd23782`  |
| 435    | No documented layout | `a68c9fd23782`  |

<!-- versions:end -->

## Companion Files

None. Character names come from LOC type 6, else the Korean
`characterstatic.dbss` name (`CHARACTER_NAME_KR` lookup index).

All multi-byte values are little-endian.

## Layout 1

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
- The `No file` clients 837 to 1246 name the file
  `#na#eventmanagement.bss` (clients 1000 and 1230 checked).
- Clients 435 to 794 store the file without PABR magic: the texts are
  inline `str16` and an event row starts with its u16 key twice (client
  435). No layout here reads them yet.

## Open Questions

### What `unknown_0e` Holds

The byte after `setted_event_ref` is `0` on every row of the official
clients 1784 and 3483. In the private server's own client 1784 build it is
`1` on 6 of 390 rows (`SteamPunk_Halloween_2021`, `Cherry Blossom Event`
and four hot time and drop events), and no sheet column holds it. In the
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
