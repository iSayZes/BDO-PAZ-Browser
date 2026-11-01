# `quizactionstaticstatus.bss` Format

## Purpose

The social actions of the O/X quiz event: for each answer the action
names a character plays when the player picks it (`SOCIAL_PutUP_R_*`
for O, `SOCIAL_PutUP_L_*` for X) and a list of contents group keys. The
quiz window sends the answer with `ToClient_DoQuizAction(selectAnswer)`.

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the newest client of each row. The newest layout is the current one.

| Layout | Clients        | File                         | Bytes | Records | Row bytes |
| ------ | -------------- | ---------------------------- | ----- | ------- | --------- |
| 1      | 1674 and later | `quizactionstaticstatus.bss` | 62    | 2 Row   | 21        |

| Layout | File                         | Known         | Unknown    |
| ------ | ---------------------------- | ------------- | ---------- |
| 1      | `quizactionstaticstatus.bss` | 62 B (100.0%) | 0 B (0.0%) |

Every client the doc check read, and the layout its files fit.

| Client | Result   | Checked against |
| ------ | -------- | --------------- |
| 3483   | Layout 1 | `a4aa08b7224e`  |
| 3482   | Layout 1 | `a4aa08b7224e`  |
| 3474   | Layout 1 | `a4aa08b7224e`  |
| 3473   | Layout 1 | `a4aa08b7224e`  |
| 3464   | Layout 1 | `a4aa08b7224e`  |
| 3458   | Layout 1 | `a4aa08b7224e`  |
| 3454   | Layout 1 | `a4aa08b7224e`  |
| 3444   | Layout 1 | `a4aa08b7224e`  |
| 3435   | Layout 1 | `a4aa08b7224e`  |
| 3426   | Layout 1 | `a4aa08b7224e`  |
| 3418   | Layout 1 | `a4aa08b7224e`  |
| 3412   | Layout 1 | `a4aa08b7224e`  |
| 3402   | Layout 1 | `a4aa08b7224e`  |
| 3396   | Layout 1 | `a4aa08b7224e`  |
| 3387   | Layout 1 | `a4aa08b7224e`  |
| 3381   | Layout 1 | `a4aa08b7224e`  |
| 3373   | Layout 1 | `a4aa08b7224e`  |
| 3364   | Layout 1 | `a4aa08b7224e`  |
| 3356   | Layout 1 | `a4aa08b7224e`  |
| 3349   | Layout 1 | `a4aa08b7224e`  |
| 3342   | Layout 1 | `a4aa08b7224e`  |
| 3335   | Layout 1 | `a4aa08b7224e`  |
| 3326   | Layout 1 | `a4aa08b7224e`  |
| 3321   | Layout 1 | `a4aa08b7224e`  |
| 3314   | Layout 1 | `a4aa08b7224e`  |
| 3303   | Layout 1 | `a4aa08b7224e`  |
| 3302   | Layout 1 | `a4aa08b7224e`  |
| 3293   | Layout 1 | `a4aa08b7224e`  |
| 3283   | Layout 1 | `a4aa08b7224e`  |
| 3275   | Layout 1 | `a4aa08b7224e`  |
| 3267   | Layout 1 | `a4aa08b7224e`  |
| 3258   | Layout 1 | `a4aa08b7224e`  |
| 3251   | Layout 1 | `a4aa08b7224e`  |
| 3242   | Layout 1 | `a4aa08b7224e`  |
| 3235   | Layout 1 | `a4aa08b7224e`  |
| 3229   | Layout 1 | `a4aa08b7224e`  |
| 3212   | Layout 1 | `a4aa08b7224e`  |
| 3203   | Layout 1 | `a4aa08b7224e`  |
| 3193   | Layout 1 | `a4aa08b7224e`  |
| 3186   | Layout 1 | `a4aa08b7224e`  |
| 3177   | Layout 1 | `a4aa08b7224e`  |
| 3169   | Layout 1 | `a4aa08b7224e`  |
| 3158   | Layout 1 | `a4aa08b7224e`  |
| 3151   | Layout 1 | `a4aa08b7224e`  |
| 3144   | Layout 1 | `a4aa08b7224e`  |
| 3133   | Layout 1 | `a4aa08b7224e`  |
| 3125   | Layout 1 | `a4aa08b7224e`  |
| 3118   | Layout 1 | `a4aa08b7224e`  |
| 3111   | Layout 1 | `a4aa08b7224e`  |
| 3103   | Layout 1 | `a4aa08b7224e`  |
| 3095   | Layout 1 | `a4aa08b7224e`  |
| 3086   | Layout 1 | `a4aa08b7224e`  |
| 3072   | Layout 1 | `a4aa08b7224e`  |
| 3062   | Layout 1 | `a4aa08b7224e`  |
| 3052   | Layout 1 | `a4aa08b7224e`  |
| 3045   | Layout 1 | `a4aa08b7224e`  |
| 3037   | Layout 1 | `a4aa08b7224e`  |
| 3030   | Layout 1 | `a4aa08b7224e`  |
| 3021   | Layout 1 | `a4aa08b7224e`  |
| 3012   | Layout 1 | `a4aa08b7224e`  |
| 3002   | Layout 1 | `a4aa08b7224e`  |
| 2995   | Layout 1 | `a4aa08b7224e`  |
| 2987   | Layout 1 | `a4aa08b7224e`  |
| 2978   | Layout 1 | `a4aa08b7224e`  |
| 2970   | Layout 1 | `a4aa08b7224e`  |
| 2959   | Layout 1 | `a4aa08b7224e`  |
| 2951   | Layout 1 | `a4aa08b7224e`  |
| 2942   | Layout 1 | `a4aa08b7224e`  |
| 2935   | Layout 1 | `a4aa08b7224e`  |
| 2932   | Layout 1 | `a4aa08b7224e`  |
| 2923   | Layout 1 | `a4aa08b7224e`  |
| 2919   | Layout 1 | `a4aa08b7224e`  |
| 2907   | Layout 1 | `a4aa08b7224e`  |
| 2900   | Layout 1 | `a4aa08b7224e`  |
| 2891   | Layout 1 | `a4aa08b7224e`  |
| 2882   | Layout 1 | `a4aa08b7224e`  |
| 2872   | Layout 1 | `a4aa08b7224e`  |
| 2863   | Layout 1 | `a4aa08b7224e`  |
| 2855   | Layout 1 | `a4aa08b7224e`  |
| 2849   | Layout 1 | `a4aa08b7224e`  |
| 2844   | Layout 1 | `a4aa08b7224e`  |
| 2834   | Layout 1 | `a4aa08b7224e`  |
| 2825   | Layout 1 | `a4aa08b7224e`  |
| 2819   | Layout 1 | `a4aa08b7224e`  |
| 2811   | Layout 1 | `a4aa08b7224e`  |
| 2803   | Layout 1 | `a4aa08b7224e`  |
| 2794   | Layout 1 | `a4aa08b7224e`  |
| 2783   | Layout 1 | `a4aa08b7224e`  |
| 2774   | Layout 1 | `a4aa08b7224e`  |
| 2765   | Layout 1 | `a4aa08b7224e`  |
| 2756   | Layout 1 | `a4aa08b7224e`  |
| 2750   | Layout 1 | `a4aa08b7224e`  |
| 2743   | Layout 1 | `a4aa08b7224e`  |
| 2736   | Layout 1 | `a4aa08b7224e`  |
| 2726   | Layout 1 | `a4aa08b7224e`  |
| 2717   | Layout 1 | `a4aa08b7224e`  |
| 2709   | Layout 1 | `a4aa08b7224e`  |
| 2703   | Layout 1 | `a4aa08b7224e`  |
| 2695   | Layout 1 | `a4aa08b7224e`  |
| 2684   | Layout 1 | `a4aa08b7224e`  |
| 2672   | Layout 1 | `a4aa08b7224e`  |
| 2665   | Layout 1 | `a4aa08b7224e`  |
| 2657   | Layout 1 | `a4aa08b7224e`  |
| 2649   | Layout 1 | `a4aa08b7224e`  |
| 2644   | Layout 1 | `a4aa08b7224e`  |
| 2637   | Layout 1 | `a4aa08b7224e`  |
| 2629   | Layout 1 | `a4aa08b7224e`  |
| 2619   | Layout 1 | `a4aa08b7224e`  |
| 2612   | Layout 1 | `a4aa08b7224e`  |
| 2606   | Layout 1 | `a4aa08b7224e`  |
| 2602   | Layout 1 | `a4aa08b7224e`  |
| 2601   | Layout 1 | `a4aa08b7224e`  |
| 2592   | Layout 1 | `a4aa08b7224e`  |
| 2583   | Layout 1 | `a4aa08b7224e`  |
| 2575   | Layout 1 | `a4aa08b7224e`  |
| 2567   | Layout 1 | `a4aa08b7224e`  |
| 2560   | Layout 1 | `a4aa08b7224e`  |
| 2553   | Layout 1 | `a4aa08b7224e`  |
| 2545   | Layout 1 | `a4aa08b7224e`  |
| 2538   | Layout 1 | `a4aa08b7224e`  |
| 2529   | Layout 1 | `a4aa08b7224e`  |
| 2519   | Layout 1 | `a4aa08b7224e`  |
| 2513   | Layout 1 | `a4aa08b7224e`  |
| 2510   | Layout 1 | `a4aa08b7224e`  |
| 2507   | Layout 1 | `a4aa08b7224e`  |
| 2503   | Layout 1 | `a4aa08b7224e`  |
| 2498   | Layout 1 | `a4aa08b7224e`  |
| 2492   | Layout 1 | `a4aa08b7224e`  |
| 2487   | Layout 1 | `a4aa08b7224e`  |
| 2480   | Layout 1 | `a4aa08b7224e`  |
| 2474   | Layout 1 | `a4aa08b7224e`  |
| 2468   | Layout 1 | `a4aa08b7224e`  |
| 2460   | Layout 1 | `a4aa08b7224e`  |
| 2453   | Layout 1 | `a4aa08b7224e`  |
| 2444   | Layout 1 | `a4aa08b7224e`  |
| 2438   | Layout 1 | `a4aa08b7224e`  |
| 2434   | Layout 1 | `a4aa08b7224e`  |
| 2429   | Layout 1 | `a4aa08b7224e`  |
| 2421   | Layout 1 | `a4aa08b7224e`  |
| 2414   | Layout 1 | `a4aa08b7224e`  |
| 2407   | Layout 1 | `a4aa08b7224e`  |
| 2401   | Layout 1 | `a4aa08b7224e`  |
| 2397   | Layout 1 | `a4aa08b7224e`  |
| 2393   | Layout 1 | `a4aa08b7224e`  |
| 2384   | Layout 1 | `a4aa08b7224e`  |
| 2378   | Layout 1 | `a4aa08b7224e`  |
| 2372   | Layout 1 | `a4aa08b7224e`  |
| 2358   | Layout 1 | `a4aa08b7224e`  |
| 2352   | Layout 1 | `a4aa08b7224e`  |
| 2347   | Layout 1 | `a4aa08b7224e`  |
| 2343   | Layout 1 | `a4aa08b7224e`  |
| 2335   | Layout 1 | `a4aa08b7224e`  |
| 2327   | Layout 1 | `a4aa08b7224e`  |
| 2324   | Layout 1 | `a4aa08b7224e`  |
| 2319   | Layout 1 | `a4aa08b7224e`  |
| 2313   | Layout 1 | `a4aa08b7224e`  |
| 2308   | Layout 1 | `a4aa08b7224e`  |
| 2302   | Layout 1 | `a4aa08b7224e`  |
| 2295   | Layout 1 | `a4aa08b7224e`  |
| 2290   | Layout 1 | `a4aa08b7224e`  |
| 2284   | Layout 1 | `a4aa08b7224e`  |
| 2276   | Layout 1 | `a4aa08b7224e`  |
| 2269   | Layout 1 | `a4aa08b7224e`  |
| 2259   | Layout 1 | `a4aa08b7224e`  |
| 2250   | Layout 1 | `a4aa08b7224e`  |
| 2243   | Layout 1 | `a4aa08b7224e`  |
| 2235   | Layout 1 | `a4aa08b7224e`  |
| 2229   | Layout 1 | `a4aa08b7224e`  |
| 2224   | Layout 1 | `a4aa08b7224e`  |
| 2218   | Layout 1 | `a4aa08b7224e`  |
| 2215   | Layout 1 | `a4aa08b7224e`  |
| 2207   | Layout 1 | `a4aa08b7224e`  |
| 2203   | Layout 1 | `a4aa08b7224e`  |
| 2196   | Layout 1 | `a4aa08b7224e`  |
| 2192   | Layout 1 | `a4aa08b7224e`  |
| 2189   | Layout 1 | `a4aa08b7224e`  |
| 2183   | Layout 1 | `a4aa08b7224e`  |
| 2179   | Layout 1 | `a4aa08b7224e`  |
| 2171   | Layout 1 | `a4aa08b7224e`  |
| 2163   | Layout 1 | `a4aa08b7224e`  |
| 2156   | Layout 1 | `a4aa08b7224e`  |
| 2151   | Layout 1 | `a4aa08b7224e`  |
| 2147   | Layout 1 | `a4aa08b7224e`  |
| 2142   | Layout 1 | `a4aa08b7224e`  |
| 2138   | Layout 1 | `a4aa08b7224e`  |
| 2134   | Layout 1 | `a4aa08b7224e`  |
| 2130   | Layout 1 | `a4aa08b7224e`  |
| 2122   | Layout 1 | `a4aa08b7224e`  |
| 2107   | Layout 1 | `a4aa08b7224e`  |
| 2098   | Layout 1 | `a4aa08b7224e`  |
| 2089   | Layout 1 | `a4aa08b7224e`  |
| 2081   | Layout 1 | `a4aa08b7224e`  |
| 2073   | Layout 1 | `a4aa08b7224e`  |
| 2067   | Layout 1 | `a4aa08b7224e`  |
| 2063   | Layout 1 | `a4aa08b7224e`  |
| 2059   | Layout 1 | `a4aa08b7224e`  |
| 2052   | Layout 1 | `a4aa08b7224e`  |
| 2044   | Layout 1 | `a4aa08b7224e`  |
| 2039   | Layout 1 | `a4aa08b7224e`  |
| 2032   | Layout 1 | `a4aa08b7224e`  |
| 2025   | Layout 1 | `a4aa08b7224e`  |
| 2011   | Layout 1 | `a4aa08b7224e`  |
| 2005   | Layout 1 | `a4aa08b7224e`  |
| 2000   | Layout 1 | `a4aa08b7224e`  |
| 1996   | Layout 1 | `a4aa08b7224e`  |
| 1991   | Layout 1 | `a4aa08b7224e`  |
| 1985   | Layout 1 | `a4aa08b7224e`  |
| 1980   | Layout 1 | `a4aa08b7224e`  |
| 1969   | Layout 1 | `a4aa08b7224e`  |
| 1964   | Layout 1 | `a4aa08b7224e`  |
| 1958   | Layout 1 | `a4aa08b7224e`  |
| 1950   | Layout 1 | `a4aa08b7224e`  |
| 1945   | Layout 1 | `a4aa08b7224e`  |
| 1937   | Layout 1 | `a4aa08b7224e`  |
| 1933   | Layout 1 | `a4aa08b7224e`  |
| 1927   | Layout 1 | `a4aa08b7224e`  |
| 1921   | Layout 1 | `a4aa08b7224e`  |
| 1914   | Layout 1 | `a4aa08b7224e`  |
| 1908   | Layout 1 | `a4aa08b7224e`  |
| 1897   | Layout 1 | `a4aa08b7224e`  |
| 1892   | Layout 1 | `a4aa08b7224e`  |
| 1886   | Layout 1 | `a4aa08b7224e`  |
| 1881   | Layout 1 | `a4aa08b7224e`  |
| 1871   | Layout 1 | `a4aa08b7224e`  |
| 1866   | Layout 1 | `a4aa08b7224e`  |
| 1862   | Layout 1 | `a4aa08b7224e`  |
| 1854   | Layout 1 | `a4aa08b7224e`  |
| 1846   | Layout 1 | `a4aa08b7224e`  |
| 1838   | Layout 1 | `a4aa08b7224e`  |
| 1832   | Layout 1 | `a4aa08b7224e`  |
| 1826   | Layout 1 | `a4aa08b7224e`  |
| 1822   | Layout 1 | `a4aa08b7224e`  |
| 1818   | Layout 1 | `a4aa08b7224e`  |
| 1804   | Layout 1 | `a4aa08b7224e`  |
| 1794   | Layout 1 | `a4aa08b7224e`  |
| 1790   | Layout 1 | `a4aa08b7224e`  |
| 1784   | Layout 1 | `a4aa08b7224e`  |
| 1774   | Layout 1 | `a4aa08b7224e`  |
| 1771   | Layout 1 | `a4aa08b7224e`  |
| 1762   | Layout 1 | `a4aa08b7224e`  |
| 1759   | Layout 1 | `a4aa08b7224e`  |
| 1754   | Layout 1 | `a4aa08b7224e`  |
| 1749   | Layout 1 | `a4aa08b7224e`  |
| 1743   | Layout 1 | `a4aa08b7224e`  |
| 1737   | Layout 1 | `a4aa08b7224e`  |
| 1731   | Layout 1 | `a4aa08b7224e`  |
| 1725   | Layout 1 | `a4aa08b7224e`  |
| 1717   | Layout 1 | `a4aa08b7224e`  |
| 1710   | Layout 1 | `a4aa08b7224e`  |
| 1704   | Layout 1 | `a4aa08b7224e`  |
| 1698   | Layout 1 | `a4aa08b7224e`  |
| 1690   | Layout 1 | `a4aa08b7224e`  |
| 1685   | Layout 1 | `a4aa08b7224e`  |
| 1680   | Layout 1 | `a4aa08b7224e`  |
| 1674   | Layout 1 | `a4aa08b7224e`  |
| 1668   | No file  | `a4aa08b7224e`  |
| 1659   | No file  | `a4aa08b7224e`  |
| 1649   | No file  | `a4aa08b7224e`  |
| 1642   | No file  | `a4aa08b7224e`  |
| 1636   | No file  | `a4aa08b7224e`  |
| 1628   | No file  | `a4aa08b7224e`  |
| 1622   | No file  | `a4aa08b7224e`  |
| 1614   | No file  | `a4aa08b7224e`  |
| 1608   | No file  | `a4aa08b7224e`  |
| 1602   | No file  | `a4aa08b7224e`  |
| 1598   | No file  | `a4aa08b7224e`  |
| 1594   | No file  | `a4aa08b7224e`  |
| 1590   | No file  | `a4aa08b7224e`  |
| 1587   | No file  | `a4aa08b7224e`  |
| 1584   | No file  | `a4aa08b7224e`  |
| 1579   | No file  | `a4aa08b7224e`  |
| 1572   | No file  | `a4aa08b7224e`  |
| 1565   | No file  | `a4aa08b7224e`  |
| 1559   | No file  | `a4aa08b7224e`  |
| 1554   | No file  | `a4aa08b7224e`  |
| 1547   | No file  | `a4aa08b7224e`  |
| 1537   | No file  | `a4aa08b7224e`  |
| 1529   | No file  | `a4aa08b7224e`  |
| 1524   | No file  | `a4aa08b7224e`  |
| 1519   | No file  | `a4aa08b7224e`  |
| 1509   | No file  | `a4aa08b7224e`  |
| 1506   | No file  | `a4aa08b7224e`  |
| 1504   | No file  | `a4aa08b7224e`  |
| 1500   | No file  | `a4aa08b7224e`  |
| 1493   | No file  | `a4aa08b7224e`  |
| 1489   | No file  | `a4aa08b7224e`  |
| 1485   | No file  | `a4aa08b7224e`  |
| 1481   | No file  | `a4aa08b7224e`  |
| 1474   | No file  | `a4aa08b7224e`  |
| 1466   | No file  | `a4aa08b7224e`  |
| 1462   | No file  | `a4aa08b7224e`  |
| 1459   | No file  | `a4aa08b7224e`  |
| 1453   | No file  | `a4aa08b7224e`  |
| 1450   | No file  | `a4aa08b7224e`  |
| 1445   | No file  | `a4aa08b7224e`  |
| 1439   | No file  | `a4aa08b7224e`  |
| 1433   | No file  | `a4aa08b7224e`  |
| 1430   | No file  | `a4aa08b7224e`  |
| 1426   | No file  | `a4aa08b7224e`  |
| 1421   | No file  | `a4aa08b7224e`  |
| 1417   | No file  | `a4aa08b7224e`  |
| 1416   | No file  | `a4aa08b7224e`  |
| 1409   | No file  | `a4aa08b7224e`  |
| 1405   | No file  | `a4aa08b7224e`  |
| 1401   | No file  | `a4aa08b7224e`  |
| 1396   | No file  | `a4aa08b7224e`  |
| 1391   | No file  | `a4aa08b7224e`  |
| 1390   | No file  | `a4aa08b7224e`  |
| 1386   | No file  | `a4aa08b7224e`  |
| 1381   | No file  | `a4aa08b7224e`  |
| 1379   | No file  | `a4aa08b7224e`  |
| 1372   | No file  | `a4aa08b7224e`  |
| 1366   | No file  | `a4aa08b7224e`  |
| 1364   | No file  | `a4aa08b7224e`  |
| 1363   | No file  | `a4aa08b7224e`  |
| 1360   | No file  | `a4aa08b7224e`  |
| 1358   | No file  | `a4aa08b7224e`  |
| 1355   | No file  | `a4aa08b7224e`  |
| 1351   | No file  | `a4aa08b7224e`  |
| 1348   | No file  | `a4aa08b7224e`  |
| 1346   | No file  | `a4aa08b7224e`  |
| 1341   | No file  | `a4aa08b7224e`  |
| 1340   | No file  | `a4aa08b7224e`  |
| 1338   | No file  | `a4aa08b7224e`  |
| 1335   | No file  | `a4aa08b7224e`  |
| 1333   | No file  | `a4aa08b7224e`  |
| 1329   | No file  | `a4aa08b7224e`  |
| 1327   | No file  | `a4aa08b7224e`  |
| 1324   | No file  | `a4aa08b7224e`  |
| 1321   | No file  | `a4aa08b7224e`  |
| 1319   | No file  | `a4aa08b7224e`  |
| 1318   | No file  | `a4aa08b7224e`  |
| 1316   | No file  | `a4aa08b7224e`  |
| 1313   | No file  | `a4aa08b7224e`  |
| 1311   | No file  | `a4aa08b7224e`  |
| 1309   | No file  | `a4aa08b7224e`  |
| 1304   | No file  | `a4aa08b7224e`  |
| 1292   | No file  | `a4aa08b7224e`  |
| 1286   | No file  | `a4aa08b7224e`  |
| 1280   | No file  | `a4aa08b7224e`  |
| 1276   | No file  | `a4aa08b7224e`  |
| 1267   | No file  | `a4aa08b7224e`  |
| 1261   | No file  | `a4aa08b7224e`  |
| 1256   | No file  | `a4aa08b7224e`  |
| 1250   | No file  | `a4aa08b7224e`  |
| 1246   | No file  | `a4aa08b7224e`  |
| 1239   | No file  | `a4aa08b7224e`  |
| 1230   | No file  | `a4aa08b7224e`  |
| 1226   | No file  | `a4aa08b7224e`  |
| 1220   | No file  | `a4aa08b7224e`  |
| 1217   | No file  | `a4aa08b7224e`  |
| 1211   | No file  | `a4aa08b7224e`  |
| 1210   | No file  | `a4aa08b7224e`  |
| 1208   | No file  | `a4aa08b7224e`  |
| 1203   | No file  | `a4aa08b7224e`  |
| 1197   | No file  | `a4aa08b7224e`  |
| 1194   | No file  | `a4aa08b7224e`  |
| 1192   | No file  | `a4aa08b7224e`  |
| 1187   | No file  | `a4aa08b7224e`  |
| 1183   | No file  | `a4aa08b7224e`  |
| 1177   | No file  | `a4aa08b7224e`  |
| 1173   | No file  | `a4aa08b7224e`  |
| 1167   | No file  | `a4aa08b7224e`  |
| 1164   | No file  | `a4aa08b7224e`  |
| 1156   | No file  | `a4aa08b7224e`  |
| 1149   | No file  | `a4aa08b7224e`  |
| 1144   | No file  | `a4aa08b7224e`  |
| 1137   | No file  | `a4aa08b7224e`  |
| 1132   | No file  | `a4aa08b7224e`  |
| 1127   | No file  | `a4aa08b7224e`  |
| 1122   | No file  | `a4aa08b7224e`  |
| 1118   | No file  | `a4aa08b7224e`  |
| 1114   | No file  | `a4aa08b7224e`  |
| 1109   | No file  | `a4aa08b7224e`  |
| 1102   | No file  | `a4aa08b7224e`  |
| 1096   | No file  | `a4aa08b7224e`  |
| 1088   | No file  | `a4aa08b7224e`  |
| 1081   | No file  | `a4aa08b7224e`  |
| 1076   | No file  | `a4aa08b7224e`  |
| 1069   | No file  | `a4aa08b7224e`  |
| 1064   | No file  | `a4aa08b7224e`  |
| 1058   | No file  | `a4aa08b7224e`  |
| 1051   | No file  | `a4aa08b7224e`  |
| 1044   | No file  | `a4aa08b7224e`  |
| 1036   | No file  | `a4aa08b7224e`  |
| 1026   | No file  | `a4aa08b7224e`  |
| 1016   | No file  | `a4aa08b7224e`  |
| 1009   | No file  | `a4aa08b7224e`  |
| 1005   | No file  | `a4aa08b7224e`  |
| 1000   | No file  | `a4aa08b7224e`  |
| 998    | No file  | `a4aa08b7224e`  |
| 990    | No file  | `a4aa08b7224e`  |
| 979    | No file  | `a4aa08b7224e`  |
| 972    | No file  | `a4aa08b7224e`  |
| 963    | No file  | `a4aa08b7224e`  |
| 955    | No file  | `a4aa08b7224e`  |
| 946    | No file  | `a4aa08b7224e`  |
| 938    | No file  | `a4aa08b7224e`  |
| 927    | No file  | `a4aa08b7224e`  |
| 911    | No file  | `a4aa08b7224e`  |
| 904    | No file  | `a4aa08b7224e`  |
| 899    | No file  | `a4aa08b7224e`  |
| 894    | No file  | `a4aa08b7224e`  |
| 885    | No file  | `a4aa08b7224e`  |
| 879    | No file  | `a4aa08b7224e`  |
| 872    | No file  | `a4aa08b7224e`  |
| 864    | No file  | `a4aa08b7224e`  |
| 855    | No file  | `a4aa08b7224e`  |
| 853    | No file  | `a4aa08b7224e`  |
| 845    | No file  | `a4aa08b7224e`  |
| 837    | No file  | `a4aa08b7224e`  |
| 829    | No file  | `a4aa08b7224e`  |
| 822    | No file  | `a4aa08b7224e`  |
| 814    | No file  | `a4aa08b7224e`  |
| 805    | No file  | `a4aa08b7224e`  |
| 794    | No file  | `a4aa08b7224e`  |
| 787    | No file  | `a4aa08b7224e`  |
| 780    | No file  | `a4aa08b7224e`  |
| 771    | No file  | `a4aa08b7224e`  |
| 760    | No file  | `a4aa08b7224e`  |
| 748    | No file  | `a4aa08b7224e`  |
| 741    | No file  | `a4aa08b7224e`  |
| 736    | No file  | `a4aa08b7224e`  |
| 731    | No file  | `a4aa08b7224e`  |
| 723    | No file  | `a4aa08b7224e`  |
| 711    | No file  | `a4aa08b7224e`  |
| 707    | No file  | `a4aa08b7224e`  |
| 697    | No file  | `a4aa08b7224e`  |
| 689    | No file  | `a4aa08b7224e`  |
| 683    | No file  | `a4aa08b7224e`  |
| 678    | No file  | `a4aa08b7224e`  |
| 670    | No file  | `a4aa08b7224e`  |
| 661    | No file  | `a4aa08b7224e`  |
| 656    | No file  | `a4aa08b7224e`  |
| 652    | No file  | `a4aa08b7224e`  |
| 643    | No file  | `a4aa08b7224e`  |
| 637    | No file  | `a4aa08b7224e`  |
| 630    | No file  | `a4aa08b7224e`  |
| 627    | No file  | `a4aa08b7224e`  |
| 621    | No file  | `a4aa08b7224e`  |
| 617    | No file  | `a4aa08b7224e`  |
| 615    | No file  | `a4aa08b7224e`  |
| 606    | No file  | `a4aa08b7224e`  |
| 599    | No file  | `a4aa08b7224e`  |
| 592    | No file  | `a4aa08b7224e`  |
| 586    | No file  | `a4aa08b7224e`  |
| 577    | No file  | `a4aa08b7224e`  |
| 569    | No file  | `a4aa08b7224e`  |
| 561    | No file  | `a4aa08b7224e`  |
| 554    | No file  | `a4aa08b7224e`  |
| 542    | No file  | `a4aa08b7224e`  |
| 532    | No file  | `a4aa08b7224e`  |
| 531    | No file  | `a4aa08b7224e`  |
| 526    | No file  | `a4aa08b7224e`  |
| 521    | No file  | `a4aa08b7224e`  |
| 517    | No file  | `a4aa08b7224e`  |
| 510    | No file  | `a4aa08b7224e`  |
| 508    | No file  | `a4aa08b7224e`  |
| 504    | No file  | `a4aa08b7224e`  |
| 497    | No file  | `a4aa08b7224e`  |
| 491    | No file  | `a4aa08b7224e`  |
| 485    | No file  | `a4aa08b7224e`  |
| 478    | No file  | `a4aa08b7224e`  |
| 472    | No file  | `a4aa08b7224e`  |
| 466    | No file  | `a4aa08b7224e`  |
| 457    | No file  | `a4aa08b7224e`  |
| 452    | No file  | `a4aa08b7224e`  |
| 449    | No file  | `a4aa08b7224e`  |
| 435    | No file  | `a4aa08b7224e`  |

<!-- versions:end -->

## Companion Files

None.

All multi-byte values are little-endian.

## Layout 1

### File Layout

| Offset              | Type           | Field        | Notes                                         |
| ------------------- | -------------- | ------------ | --------------------------------------------- |
| `+0x00`             | char[4]        | magic        | ASCII `PABR`                                  |
| `+0x04`             | u32            | row_count    | Number of answers                             |
| `+0x08`             | Row[row_count] | rows         | See Row                                       |
| `rows+0x00`         | String Table   | string_table | See String Table                              |
| `string_table+0x00` | u32            | table_start  | Offset of the string table, where `rows` ends |
| `string_table+0x04` | u32            | zero         | Always `0`                                    |

### Row (variable: 9 bytes + hashes)

| Offset                | Type                      | Field                 | Notes                                                                 |
| --------------------- | ------------------------- | --------------------- | --------------------------------------------------------------------- |
| `+0x00`               | u8                        | answer_type           | `eQuizAnswerType`: `1` O, `2` X; see Answer Types                     |
| `+0x01`               | u32                       | action_count          | Number of action names                                                |
| `+0x05`               | u32[action_count]         | action_hashes         | `ascii_key_hash` of each action name, in sheet order                  |
| `action_hashes+0x00`  | u32                       | contents_group_count  | Number of contents groups                                             |
| `action_hashes+0x04`  | u32[contents_group_count] | contents_group_hashes | Contents group keys as the client's string hash of their decimal text, as in `characterstatic.dbss` |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes                                  |
| ------- | ------------------ | ------------ | -------------------------------------- |
| `+0x00` | u32                | string_count | Number of strings; `0` on every client checked |
| `+0x04` | pstr[string_count] | strings      | No field reads a string                |

## Answer Types

`panel_event_quizgm_all.luac` (client 3482) lists `eQuizAnswerType` as
`eQuizAnswerType_None = 0`, `eQuizAnswerType_OX_O = 1` and
`eQuizAnswerType_OX_X = 2`; the player's quiz window
(`panel_event_quiz_all_1.luac`) passes `__eQuizAnswerType_OX_O` or
`__eQuizAnswerType_OX_X` to `ToClient_DoQuizAction`. The rows on clients
1784 and 3482:

| `answer_type` | Answer | Actions                                       | Contents group |
| ------------- | ------ | --------------------------------------------- | -------------- |
| `1`           | O      | `SOCIAL_PutUP_R_Start`, `SOCIAL_PutUP_R_Ing`  | `1671`         |
| `2`           | X      | `SOCIAL_PutUP_L_Start`, `SOCIAL_PutUP_L_Ing`  | `1671`         |

## Field Names

The names follow the `Social_Quiz` sheet of a private server's
`DataSheets.bexcel` on client 1784, columns `AnswerType`, `ActionName`
and `ContentsGroupKey`. The file stores `AnswerType` first. Its 2 rows
match both rows of the client 1784 and client 3482 files (the files are
the same 62 bytes): each comma-separated `ActionName` list is the
`action_hashes` list by `ascii_key_hash` (`SOCIAL_PutUP_R_Start` is
`0x31C83250`), and `ContentsGroupKey` `1671` is `key_hash("1671")`,
`0x035FC574`. The sheet sits in `datasheet_socialaction.xlsm`, whose
`#^E_Merge Index` column is not compiled.

## Notes

- The handler for the PABR option tables (`_bss/pabr_values/`) previews
  this file with the layout in `_bss/pabr_values/ui_tables.py`: one row
  per answer with the answer name, the action names (the hash in hex for
  a name the sheet does not list) and the contents group keys.
