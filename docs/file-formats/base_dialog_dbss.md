# `base_dialog.dbss` Format

## Purpose

Stores a short base record for every NPC dialog in `detail_dialog.dbss`: the Korean display name the dialog shows for the character, and a list of short Korean lines. The lines are ambient chatter that the client shows in a speech bubble over the NPC's head (a pilgrim saying `아이고. 배야.` ("Ouch, my stomach.")).

## Versions

<!-- versions:begin - written by the doc check from the PAZ folder; edits between the markers are overwritten -->

Sizes and coverage from the client in the Checked column. The newest layout is the current one.

| Layout | Clients        | Checked | File                     | Bytes     | Records            | Row bytes                |
| ------ | -------------- | ------- | ------------------------ | --------- | ------------------ | ------------------------ |
| 1      | 1504 and later | 3483    | `base_dialog.dbss`       | 2,076,219 | 59,783 Base Record | 21 to 519, 35 on average |
| 1      | 1504 and later | 3483    | `base_dialogoffset.dbss` | 717,416   | 59,783 Index Row   | 12                       |

| Layout | File                     | Known               | Unknown           |
| ------ | ------------------------ | ------------------- | ----------------- |
| 1      | `base_dialog.dbss`       | 1,777,304 B (85.6%) | 298,915 B (14.4%) |
| 1      | `base_dialogoffset.dbss` | 717,416 B (100.0%)  | 0 B (0.0%)        |

Every client the doc check read, and the layout its files fit.

| Client | Result               | Checked against |
| ------ | -------------------- | --------------- |
| 3483   | Layout 1             | `27d9f3f71009`  |
| 3482   | Layout 1             | `27d9f3f71009`  |
| 3474   | Layout 1             | `27d9f3f71009`  |
| 3473   | Layout 1             | `27d9f3f71009`  |
| 3464   | Layout 1             | `27d9f3f71009`  |
| 3458   | Layout 1             | `27d9f3f71009`  |
| 3454   | Layout 1             | `27d9f3f71009`  |
| 3444   | Layout 1             | `27d9f3f71009`  |
| 3435   | Layout 1             | `27d9f3f71009`  |
| 3426   | Layout 1             | `27d9f3f71009`  |
| 3418   | Layout 1             | `27d9f3f71009`  |
| 3412   | Layout 1             | `27d9f3f71009`  |
| 3402   | Layout 1             | `27d9f3f71009`  |
| 3396   | Layout 1             | `27d9f3f71009`  |
| 3387   | Layout 1             | `27d9f3f71009`  |
| 3381   | Layout 1             | `27d9f3f71009`  |
| 3373   | Layout 1             | `27d9f3f71009`  |
| 3364   | Layout 1             | `27d9f3f71009`  |
| 3356   | Layout 1             | `27d9f3f71009`  |
| 3349   | Layout 1             | `27d9f3f71009`  |
| 3342   | Layout 1             | `27d9f3f71009`  |
| 3335   | Layout 1             | `27d9f3f71009`  |
| 3326   | Layout 1             | `27d9f3f71009`  |
| 3321   | Layout 1             | `27d9f3f71009`  |
| 3314   | Layout 1             | `27d9f3f71009`  |
| 3303   | Layout 1             | `27d9f3f71009`  |
| 3302   | Layout 1             | `27d9f3f71009`  |
| 3293   | Layout 1             | `27d9f3f71009`  |
| 3283   | Layout 1             | `27d9f3f71009`  |
| 3275   | Layout 1             | `27d9f3f71009`  |
| 3267   | Layout 1             | `27d9f3f71009`  |
| 3258   | Layout 1             | `27d9f3f71009`  |
| 3251   | Layout 1             | `27d9f3f71009`  |
| 3242   | Layout 1             | `27d9f3f71009`  |
| 3235   | Layout 1             | `27d9f3f71009`  |
| 3229   | Layout 1             | `27d9f3f71009`  |
| 3212   | Layout 1             | `27d9f3f71009`  |
| 3203   | Layout 1             | `27d9f3f71009`  |
| 3193   | Layout 1             | `27d9f3f71009`  |
| 3186   | Layout 1             | `27d9f3f71009`  |
| 3177   | Layout 1             | `27d9f3f71009`  |
| 3169   | Layout 1             | `27d9f3f71009`  |
| 3158   | Layout 1             | `27d9f3f71009`  |
| 3151   | Layout 1             | `27d9f3f71009`  |
| 3144   | Layout 1             | `27d9f3f71009`  |
| 3133   | Layout 1             | `27d9f3f71009`  |
| 3125   | Layout 1             | `27d9f3f71009`  |
| 3118   | Layout 1             | `27d9f3f71009`  |
| 3111   | Layout 1             | `27d9f3f71009`  |
| 3103   | Layout 1             | `27d9f3f71009`  |
| 3095   | Layout 1             | `27d9f3f71009`  |
| 3086   | Layout 1             | `27d9f3f71009`  |
| 3072   | Layout 1             | `27d9f3f71009`  |
| 3062   | Layout 1             | `27d9f3f71009`  |
| 3052   | Layout 1             | `27d9f3f71009`  |
| 3045   | Layout 1             | `27d9f3f71009`  |
| 3037   | Layout 1             | `27d9f3f71009`  |
| 3030   | Layout 1             | `27d9f3f71009`  |
| 3021   | Layout 1             | `27d9f3f71009`  |
| 3012   | Layout 1             | `27d9f3f71009`  |
| 3002   | Layout 1             | `27d9f3f71009`  |
| 2995   | Layout 1             | `27d9f3f71009`  |
| 2987   | Layout 1             | `27d9f3f71009`  |
| 2978   | Layout 1             | `27d9f3f71009`  |
| 2970   | Layout 1             | `27d9f3f71009`  |
| 2959   | Layout 1             | `27d9f3f71009`  |
| 2951   | Layout 1             | `27d9f3f71009`  |
| 2942   | Layout 1             | `27d9f3f71009`  |
| 2935   | Layout 1             | `27d9f3f71009`  |
| 2932   | Layout 1             | `27d9f3f71009`  |
| 2923   | Layout 1             | `27d9f3f71009`  |
| 2919   | Layout 1             | `27d9f3f71009`  |
| 2907   | Layout 1             | `27d9f3f71009`  |
| 2900   | Layout 1             | `27d9f3f71009`  |
| 2891   | Layout 1             | `27d9f3f71009`  |
| 2882   | Layout 1             | `27d9f3f71009`  |
| 2872   | Layout 1             | `27d9f3f71009`  |
| 2863   | Layout 1             | `27d9f3f71009`  |
| 2855   | Layout 1             | `27d9f3f71009`  |
| 2849   | Layout 1             | `27d9f3f71009`  |
| 2844   | Layout 1             | `27d9f3f71009`  |
| 2834   | Layout 1             | `27d9f3f71009`  |
| 2825   | Layout 1             | `27d9f3f71009`  |
| 2819   | Layout 1             | `27d9f3f71009`  |
| 2811   | Layout 1             | `27d9f3f71009`  |
| 2803   | Layout 1             | `27d9f3f71009`  |
| 2794   | Layout 1             | `27d9f3f71009`  |
| 2783   | Layout 1             | `27d9f3f71009`  |
| 2774   | Layout 1             | `27d9f3f71009`  |
| 2765   | Layout 1             | `27d9f3f71009`  |
| 2756   | Layout 1             | `27d9f3f71009`  |
| 2750   | Layout 1             | `27d9f3f71009`  |
| 2743   | Layout 1             | `27d9f3f71009`  |
| 2736   | Layout 1             | `27d9f3f71009`  |
| 2726   | Layout 1             | `27d9f3f71009`  |
| 2717   | Layout 1             | `27d9f3f71009`  |
| 2709   | Layout 1             | `27d9f3f71009`  |
| 2703   | Layout 1             | `27d9f3f71009`  |
| 2695   | Layout 1             | `27d9f3f71009`  |
| 2684   | Layout 1             | `27d9f3f71009`  |
| 2672   | Layout 1             | `27d9f3f71009`  |
| 2665   | Layout 1             | `27d9f3f71009`  |
| 2657   | Layout 1             | `27d9f3f71009`  |
| 2649   | Layout 1             | `27d9f3f71009`  |
| 2644   | Layout 1             | `27d9f3f71009`  |
| 2637   | Layout 1             | `27d9f3f71009`  |
| 2629   | Layout 1             | `27d9f3f71009`  |
| 2619   | Layout 1             | `27d9f3f71009`  |
| 2612   | Layout 1             | `27d9f3f71009`  |
| 2606   | Layout 1             | `27d9f3f71009`  |
| 2602   | Layout 1             | `27d9f3f71009`  |
| 2601   | Layout 1             | `27d9f3f71009`  |
| 2592   | Layout 1             | `27d9f3f71009`  |
| 2583   | Layout 1             | `27d9f3f71009`  |
| 2575   | Layout 1             | `27d9f3f71009`  |
| 2567   | Layout 1             | `27d9f3f71009`  |
| 2560   | Layout 1             | `27d9f3f71009`  |
| 2553   | Layout 1             | `27d9f3f71009`  |
| 2545   | Layout 1             | `27d9f3f71009`  |
| 2538   | Layout 1             | `27d9f3f71009`  |
| 2529   | Layout 1             | `27d9f3f71009`  |
| 2519   | Layout 1             | `27d9f3f71009`  |
| 2513   | Layout 1             | `27d9f3f71009`  |
| 2510   | Layout 1             | `27d9f3f71009`  |
| 2507   | Layout 1             | `27d9f3f71009`  |
| 2503   | Layout 1             | `27d9f3f71009`  |
| 2498   | Layout 1             | `27d9f3f71009`  |
| 2492   | Layout 1             | `27d9f3f71009`  |
| 2487   | Layout 1             | `27d9f3f71009`  |
| 2480   | Layout 1             | `27d9f3f71009`  |
| 2474   | Layout 1             | `27d9f3f71009`  |
| 2468   | Layout 1             | `27d9f3f71009`  |
| 2460   | Layout 1             | `27d9f3f71009`  |
| 2453   | Layout 1             | `27d9f3f71009`  |
| 2444   | Layout 1             | `27d9f3f71009`  |
| 2438   | Layout 1             | `27d9f3f71009`  |
| 2434   | Layout 1             | `27d9f3f71009`  |
| 2429   | Layout 1             | `27d9f3f71009`  |
| 2421   | Layout 1             | `27d9f3f71009`  |
| 2414   | Layout 1             | `27d9f3f71009`  |
| 2407   | Layout 1             | `27d9f3f71009`  |
| 2401   | Layout 1             | `27d9f3f71009`  |
| 2397   | Layout 1             | `27d9f3f71009`  |
| 2393   | Layout 1             | `27d9f3f71009`  |
| 2384   | Layout 1             | `27d9f3f71009`  |
| 2378   | Layout 1             | `27d9f3f71009`  |
| 2372   | Layout 1             | `27d9f3f71009`  |
| 2358   | Layout 1             | `27d9f3f71009`  |
| 2352   | Layout 1             | `27d9f3f71009`  |
| 2347   | Layout 1             | `27d9f3f71009`  |
| 2343   | Layout 1             | `27d9f3f71009`  |
| 2335   | Layout 1             | `27d9f3f71009`  |
| 2327   | Layout 1             | `27d9f3f71009`  |
| 2324   | Layout 1             | `27d9f3f71009`  |
| 2319   | Layout 1             | `27d9f3f71009`  |
| 2313   | Layout 1             | `27d9f3f71009`  |
| 2308   | Layout 1             | `27d9f3f71009`  |
| 2302   | Layout 1             | `27d9f3f71009`  |
| 2295   | Layout 1             | `27d9f3f71009`  |
| 2290   | Layout 1             | `27d9f3f71009`  |
| 2284   | Layout 1             | `27d9f3f71009`  |
| 2276   | Layout 1             | `27d9f3f71009`  |
| 2269   | Layout 1             | `27d9f3f71009`  |
| 2259   | Layout 1             | `27d9f3f71009`  |
| 2250   | Layout 1             | `27d9f3f71009`  |
| 2243   | Layout 1             | `27d9f3f71009`  |
| 2235   | Layout 1             | `27d9f3f71009`  |
| 2229   | Layout 1             | `27d9f3f71009`  |
| 2224   | Layout 1             | `27d9f3f71009`  |
| 2218   | Layout 1             | `27d9f3f71009`  |
| 2215   | Layout 1             | `27d9f3f71009`  |
| 2207   | Layout 1             | `27d9f3f71009`  |
| 2203   | Layout 1             | `27d9f3f71009`  |
| 2196   | Layout 1             | `27d9f3f71009`  |
| 2192   | Layout 1             | `27d9f3f71009`  |
| 2189   | Layout 1             | `27d9f3f71009`  |
| 2183   | Layout 1             | `27d9f3f71009`  |
| 2179   | Layout 1             | `27d9f3f71009`  |
| 2171   | Layout 1             | `27d9f3f71009`  |
| 2163   | Layout 1             | `27d9f3f71009`  |
| 2156   | Layout 1             | `27d9f3f71009`  |
| 2151   | Layout 1             | `27d9f3f71009`  |
| 2147   | Layout 1             | `27d9f3f71009`  |
| 2142   | Layout 1             | `27d9f3f71009`  |
| 2138   | Layout 1             | `27d9f3f71009`  |
| 2134   | Layout 1             | `27d9f3f71009`  |
| 2130   | Layout 1             | `27d9f3f71009`  |
| 2122   | Layout 1             | `27d9f3f71009`  |
| 2107   | Layout 1             | `27d9f3f71009`  |
| 2098   | Layout 1             | `27d9f3f71009`  |
| 2089   | Layout 1             | `27d9f3f71009`  |
| 2081   | Layout 1             | `27d9f3f71009`  |
| 2073   | Layout 1             | `27d9f3f71009`  |
| 2067   | Layout 1             | `27d9f3f71009`  |
| 2063   | Layout 1             | `27d9f3f71009`  |
| 2059   | Layout 1             | `27d9f3f71009`  |
| 2052   | Layout 1             | `27d9f3f71009`  |
| 2044   | Layout 1             | `27d9f3f71009`  |
| 2039   | Layout 1             | `27d9f3f71009`  |
| 2032   | Layout 1             | `27d9f3f71009`  |
| 2025   | Layout 1             | `27d9f3f71009`  |
| 2011   | Layout 1             | `27d9f3f71009`  |
| 2005   | Layout 1             | `27d9f3f71009`  |
| 2000   | Layout 1             | `27d9f3f71009`  |
| 1996   | Layout 1             | `27d9f3f71009`  |
| 1991   | Layout 1             | `27d9f3f71009`  |
| 1985   | Layout 1             | `27d9f3f71009`  |
| 1980   | Layout 1             | `27d9f3f71009`  |
| 1969   | Layout 1             | `27d9f3f71009`  |
| 1964   | Layout 1             | `27d9f3f71009`  |
| 1958   | Layout 1             | `27d9f3f71009`  |
| 1950   | Layout 1             | `27d9f3f71009`  |
| 1945   | Layout 1             | `27d9f3f71009`  |
| 1937   | Layout 1             | `27d9f3f71009`  |
| 1933   | Layout 1             | `27d9f3f71009`  |
| 1927   | Layout 1             | `27d9f3f71009`  |
| 1921   | Layout 1             | `27d9f3f71009`  |
| 1914   | Layout 1             | `27d9f3f71009`  |
| 1908   | Layout 1             | `27d9f3f71009`  |
| 1897   | Layout 1             | `27d9f3f71009`  |
| 1892   | Layout 1             | `27d9f3f71009`  |
| 1886   | Layout 1             | `27d9f3f71009`  |
| 1881   | Layout 1             | `27d9f3f71009`  |
| 1871   | Layout 1             | `27d9f3f71009`  |
| 1866   | Layout 1             | `27d9f3f71009`  |
| 1862   | Layout 1             | `27d9f3f71009`  |
| 1854   | Layout 1             | `27d9f3f71009`  |
| 1846   | Layout 1             | `27d9f3f71009`  |
| 1838   | Layout 1             | `27d9f3f71009`  |
| 1832   | Layout 1             | `27d9f3f71009`  |
| 1826   | Layout 1             | `27d9f3f71009`  |
| 1822   | Layout 1             | `27d9f3f71009`  |
| 1818   | Layout 1             | `27d9f3f71009`  |
| 1804   | Layout 1             | `27d9f3f71009`  |
| 1794   | Layout 1             | `27d9f3f71009`  |
| 1790   | Layout 1             | `27d9f3f71009`  |
| 1784   | Layout 1             | `27d9f3f71009`  |
| 1774   | Layout 1             | `27d9f3f71009`  |
| 1771   | Layout 1             | `27d9f3f71009`  |
| 1762   | Layout 1             | `27d9f3f71009`  |
| 1759   | Layout 1             | `27d9f3f71009`  |
| 1754   | Layout 1             | `27d9f3f71009`  |
| 1749   | Layout 1             | `27d9f3f71009`  |
| 1743   | Layout 1             | `27d9f3f71009`  |
| 1737   | Layout 1             | `27d9f3f71009`  |
| 1731   | Layout 1             | `27d9f3f71009`  |
| 1725   | Layout 1             | `27d9f3f71009`  |
| 1717   | Layout 1             | `27d9f3f71009`  |
| 1710   | Layout 1             | `27d9f3f71009`  |
| 1704   | Layout 1             | `27d9f3f71009`  |
| 1698   | Layout 1             | `27d9f3f71009`  |
| 1690   | Layout 1             | `27d9f3f71009`  |
| 1685   | Layout 1             | `27d9f3f71009`  |
| 1680   | Layout 1             | `27d9f3f71009`  |
| 1674   | Layout 1             | `27d9f3f71009`  |
| 1668   | Layout 1             | `27d9f3f71009`  |
| 1659   | Layout 1             | `27d9f3f71009`  |
| 1649   | Layout 1             | `27d9f3f71009`  |
| 1642   | Layout 1             | `27d9f3f71009`  |
| 1636   | Layout 1             | `27d9f3f71009`  |
| 1628   | Layout 1             | `27d9f3f71009`  |
| 1622   | Layout 1             | `27d9f3f71009`  |
| 1614   | Layout 1             | `27d9f3f71009`  |
| 1608   | Layout 1             | `27d9f3f71009`  |
| 1602   | Layout 1             | `27d9f3f71009`  |
| 1598   | Layout 1             | `27d9f3f71009`  |
| 1594   | Layout 1             | `27d9f3f71009`  |
| 1590   | Layout 1             | `27d9f3f71009`  |
| 1587   | Layout 1             | `27d9f3f71009`  |
| 1584   | Layout 1             | `27d9f3f71009`  |
| 1579   | Layout 1             | `27d9f3f71009`  |
| 1572   | Layout 1             | `27d9f3f71009`  |
| 1565   | Layout 1             | `27d9f3f71009`  |
| 1559   | Layout 1             | `27d9f3f71009`  |
| 1554   | Layout 1             | `27d9f3f71009`  |
| 1547   | Layout 1             | `27d9f3f71009`  |
| 1537   | Layout 1             | `27d9f3f71009`  |
| 1529   | Layout 1             | `27d9f3f71009`  |
| 1524   | Layout 1             | `27d9f3f71009`  |
| 1519   | Layout 1             | `27d9f3f71009`  |
| 1509   | Layout 1             | `27d9f3f71009`  |
| 1506   | Layout 1             | `27d9f3f71009`  |
| 1504   | Layout 1             | `27d9f3f71009`  |
| 1500   | No documented layout | `27d9f3f71009`  |
| 1493   | No documented layout | `27d9f3f71009`  |
| 1489   | No documented layout | `27d9f3f71009`  |
| 1485   | No documented layout | `27d9f3f71009`  |
| 1481   | No documented layout | `27d9f3f71009`  |
| 1474   | No documented layout | `27d9f3f71009`  |
| 1466   | No documented layout | `27d9f3f71009`  |
| 1462   | No documented layout | `27d9f3f71009`  |
| 1459   | No documented layout | `27d9f3f71009`  |
| 1453   | No documented layout | `27d9f3f71009`  |
| 1450   | No documented layout | `27d9f3f71009`  |
| 1445   | No documented layout | `27d9f3f71009`  |
| 1439   | No documented layout | `27d9f3f71009`  |
| 1433   | No documented layout | `27d9f3f71009`  |
| 1430   | No documented layout | `27d9f3f71009`  |
| 1426   | No documented layout | `27d9f3f71009`  |
| 1421   | No documented layout | `27d9f3f71009`  |
| 1417   | No documented layout | `27d9f3f71009`  |
| 1416   | No documented layout | `27d9f3f71009`  |
| 1409   | No documented layout | `27d9f3f71009`  |
| 1405   | No documented layout | `27d9f3f71009`  |
| 1401   | No documented layout | `27d9f3f71009`  |
| 1396   | No documented layout | `27d9f3f71009`  |
| 1391   | No documented layout | `27d9f3f71009`  |
| 1390   | No documented layout | `27d9f3f71009`  |
| 1386   | No documented layout | `27d9f3f71009`  |
| 1381   | No documented layout | `27d9f3f71009`  |
| 1379   | No documented layout | `27d9f3f71009`  |
| 1372   | No documented layout | `27d9f3f71009`  |
| 1366   | No documented layout | `27d9f3f71009`  |
| 1364   | No documented layout | `27d9f3f71009`  |
| 1363   | No documented layout | `27d9f3f71009`  |
| 1360   | No documented layout | `27d9f3f71009`  |
| 1358   | No documented layout | `27d9f3f71009`  |
| 1355   | No documented layout | `27d9f3f71009`  |
| 1351   | No documented layout | `27d9f3f71009`  |
| 1348   | No documented layout | `27d9f3f71009`  |
| 1346   | No documented layout | `27d9f3f71009`  |
| 1341   | No documented layout | `27d9f3f71009`  |
| 1340   | No documented layout | `27d9f3f71009`  |
| 1338   | No documented layout | `27d9f3f71009`  |
| 1335   | No documented layout | `27d9f3f71009`  |
| 1333   | No documented layout | `27d9f3f71009`  |
| 1329   | No documented layout | `27d9f3f71009`  |
| 1327   | No documented layout | `27d9f3f71009`  |
| 1324   | No documented layout | `27d9f3f71009`  |
| 1321   | No documented layout | `27d9f3f71009`  |
| 1319   | No documented layout | `27d9f3f71009`  |
| 1318   | No documented layout | `27d9f3f71009`  |
| 1316   | No documented layout | `27d9f3f71009`  |
| 1313   | No documented layout | `27d9f3f71009`  |
| 1311   | No documented layout | `27d9f3f71009`  |
| 1309   | No documented layout | `27d9f3f71009`  |
| 1304   | No documented layout | `27d9f3f71009`  |
| 1292   | No documented layout | `27d9f3f71009`  |
| 1286   | No documented layout | `27d9f3f71009`  |
| 1280   | No documented layout | `27d9f3f71009`  |
| 1276   | No documented layout | `27d9f3f71009`  |
| 1267   | No documented layout | `27d9f3f71009`  |
| 1261   | No documented layout | `27d9f3f71009`  |
| 1256   | No documented layout | `27d9f3f71009`  |
| 1250   | No documented layout | `27d9f3f71009`  |
| 1246   | No documented layout | `27d9f3f71009`  |
| 1239   | No documented layout | `27d9f3f71009`  |
| 1230   | No documented layout | `27d9f3f71009`  |
| 1226   | No file              | `27d9f3f71009`  |
| 1220   | No file              | `27d9f3f71009`  |
| 1217   | No file              | `27d9f3f71009`  |
| 1211   | No file              | `27d9f3f71009`  |
| 1210   | No file              | `27d9f3f71009`  |
| 1208   | No file              | `27d9f3f71009`  |
| 1203   | No file              | `27d9f3f71009`  |
| 1197   | No file              | `27d9f3f71009`  |
| 1194   | No file              | `27d9f3f71009`  |
| 1192   | No file              | `27d9f3f71009`  |
| 1187   | No file              | `27d9f3f71009`  |
| 1183   | No file              | `27d9f3f71009`  |
| 1177   | No file              | `27d9f3f71009`  |
| 1173   | No file              | `27d9f3f71009`  |
| 1167   | No file              | `27d9f3f71009`  |
| 1164   | No file              | `27d9f3f71009`  |
| 1156   | No file              | `27d9f3f71009`  |
| 1149   | No file              | `27d9f3f71009`  |
| 1144   | No file              | `27d9f3f71009`  |
| 1137   | No file              | `27d9f3f71009`  |
| 1132   | No file              | `27d9f3f71009`  |
| 1127   | No file              | `27d9f3f71009`  |
| 1122   | No file              | `27d9f3f71009`  |
| 1118   | No file              | `27d9f3f71009`  |
| 1114   | No file              | `27d9f3f71009`  |
| 1109   | No file              | `27d9f3f71009`  |
| 1102   | No file              | `27d9f3f71009`  |
| 1096   | No file              | `27d9f3f71009`  |
| 1088   | No file              | `27d9f3f71009`  |
| 1081   | No file              | `27d9f3f71009`  |
| 1076   | No file              | `27d9f3f71009`  |
| 1069   | No file              | `27d9f3f71009`  |
| 1064   | No file              | `27d9f3f71009`  |
| 1058   | No file              | `27d9f3f71009`  |
| 1051   | No file              | `27d9f3f71009`  |
| 1044   | No file              | `27d9f3f71009`  |
| 1036   | No file              | `27d9f3f71009`  |
| 1026   | No file              | `27d9f3f71009`  |
| 1016   | No file              | `27d9f3f71009`  |
| 1009   | No file              | `27d9f3f71009`  |
| 1005   | No file              | `27d9f3f71009`  |
| 1000   | No file              | `27d9f3f71009`  |
| 998    | No file              | `27d9f3f71009`  |
| 990    | No file              | `27d9f3f71009`  |
| 979    | No file              | `27d9f3f71009`  |
| 972    | No file              | `27d9f3f71009`  |
| 963    | No file              | `27d9f3f71009`  |
| 955    | No file              | `27d9f3f71009`  |
| 946    | No file              | `27d9f3f71009`  |
| 938    | No file              | `27d9f3f71009`  |
| 927    | No file              | `27d9f3f71009`  |
| 911    | No file              | `27d9f3f71009`  |
| 904    | No file              | `27d9f3f71009`  |
| 899    | No file              | `27d9f3f71009`  |
| 894    | No file              | `27d9f3f71009`  |
| 885    | No file              | `27d9f3f71009`  |
| 879    | No file              | `27d9f3f71009`  |
| 872    | No file              | `27d9f3f71009`  |
| 864    | No file              | `27d9f3f71009`  |
| 855    | No file              | `27d9f3f71009`  |
| 853    | No file              | `27d9f3f71009`  |
| 845    | No file              | `27d9f3f71009`  |
| 837    | No file              | `27d9f3f71009`  |
| 829    | No file              | `27d9f3f71009`  |
| 822    | No file              | `27d9f3f71009`  |
| 814    | No file              | `27d9f3f71009`  |
| 805    | No file              | `27d9f3f71009`  |
| 794    | No file              | `27d9f3f71009`  |
| 787    | No file              | `27d9f3f71009`  |
| 780    | No file              | `27d9f3f71009`  |
| 771    | No file              | `27d9f3f71009`  |
| 760    | No file              | `27d9f3f71009`  |
| 748    | No file              | `27d9f3f71009`  |
| 741    | No file              | `27d9f3f71009`  |
| 736    | No file              | `27d9f3f71009`  |
| 731    | No file              | `27d9f3f71009`  |
| 723    | No file              | `27d9f3f71009`  |
| 711    | No file              | `27d9f3f71009`  |
| 707    | No file              | `27d9f3f71009`  |
| 697    | No file              | `27d9f3f71009`  |
| 689    | No file              | `27d9f3f71009`  |
| 683    | No file              | `27d9f3f71009`  |
| 678    | No file              | `27d9f3f71009`  |
| 670    | No file              | `27d9f3f71009`  |
| 661    | No file              | `27d9f3f71009`  |
| 656    | No file              | `27d9f3f71009`  |
| 652    | No file              | `27d9f3f71009`  |
| 643    | No file              | `27d9f3f71009`  |
| 637    | No file              | `27d9f3f71009`  |
| 630    | No file              | `27d9f3f71009`  |
| 627    | No file              | `27d9f3f71009`  |
| 621    | No file              | `27d9f3f71009`  |
| 617    | No file              | `27d9f3f71009`  |
| 615    | No file              | `27d9f3f71009`  |
| 606    | No file              | `27d9f3f71009`  |
| 599    | No file              | `27d9f3f71009`  |
| 592    | No file              | `27d9f3f71009`  |
| 586    | No file              | `27d9f3f71009`  |
| 577    | No file              | `27d9f3f71009`  |
| 569    | No file              | `27d9f3f71009`  |
| 561    | No file              | `27d9f3f71009`  |
| 554    | No file              | `27d9f3f71009`  |
| 542    | No file              | `27d9f3f71009`  |
| 532    | No file              | `27d9f3f71009`  |
| 531    | No file              | `27d9f3f71009`  |
| 526    | No file              | `27d9f3f71009`  |
| 521    | No file              | `27d9f3f71009`  |
| 517    | No file              | `27d9f3f71009`  |
| 510    | No file              | `27d9f3f71009`  |
| 508    | No file              | `27d9f3f71009`  |
| 504    | No file              | `27d9f3f71009`  |
| 497    | No file              | `27d9f3f71009`  |
| 491    | No file              | `27d9f3f71009`  |
| 485    | No file              | `27d9f3f71009`  |
| 478    | No file              | `27d9f3f71009`  |
| 472    | No file              | `27d9f3f71009`  |
| 466    | No file              | `27d9f3f71009`  |
| 457    | No file              | `27d9f3f71009`  |
| 452    | No file              | `27d9f3f71009`  |
| 449    | No file              | `27d9f3f71009`  |
| 435    | No file              | `27d9f3f71009`  |

<!-- versions:end -->

## Companion Files

| File                     | Required | Role                                               |
| ------------------------ | -------- | -------------------------------------------------- |
| `base_dialogoffset.dbss` | Required | Maps each dialog key to its record offset and size |
| `languagedata_*.loc`     | Optional | The name and lines in the user's language (type `38`), character names (type `6`) |

All multi-byte values are little-endian. The keys are the same 59,776 keys as `detail_dialog.dbss`, in the same order (`dialog_index << 16 | character_id`, see [detail_dialog.dbss](detail_dialog_dbss.md)).

## Layout 1

### File Layout

| Offset  | Type               | Field   | Notes                                      |
| ------- | ------------------ | ------- | ------------------------------------------ |
| `+0x00` | u32                | count   | Number of records; matches the offset file |
| `+0x04` | Base Record[count] | records | Back to back; the first starts at `4`      |

Unlike `detail_dialog.dbss`, records are not preceded by a copy of their key: they tile the file from byte `4` to its end with no gap.

### Base Record (variable: 21 bytes + name and line text)

Each record sits at `offset` and is `size` bytes long, from its index row.

| Offset           | Type               | Field       | Notes                                                        |
| ---------------- | ------------------ | ----------- | ------------------------------------------------------------ |
| `+0x00`          | u32                | key         | Same as the index key                                        |
| `+0x04`          | str16              | name_kr     | Korean display name, e.g. `마티나 핀토`, `순례자` (pilgrim) |
| `name_kr+0x00`   | u32                | line_count  | `0` on 55,850 of 59,776 records, up to `10`                  |
| `name_kr+0x04`   | str16[line_count]  | lines       | Short Korean lines                                           |
| `lines+0x00`     | bytes[5]           | unknown_end | Always zero                                                  |

Every record of client 3458 walks with this layout and ends exactly at its index size.

### `base_dialogoffset.dbss`

The same layout as `detail_dialogoffset.dbss`: `PABR`, a u32 count, 12-byte rows and a 12-byte trailer (an empty PABR string table, the end offset of the rows, `u32 0`).

| Offset              | Type             | Field        | Notes                                    |
| ------------------- | ---------------- | ------------ | ---------------------------------------- |
| `+0x00`             | char[4]          | magic        | `PABR`                                   |
| `+0x04`             | u32              | count        | Number of index rows                     |
| `+0x08`             | Index Row[count] | rows         | See Index Row                            |
| `rows+0x00`         | String Table     | string_table | See String Table                         |
| `string_table+0x00` | u32              | rows_end     | End offset of the rows (`8 + 12 * count`) |
| `string_table+0x04` | u32              | zero         | Always `0`                               |

### Index Row (12 bytes)

| Offset  | Type | Field  | Notes                                            |
| ------- | ---- | ------ | ------------------------------------------------ |
| `+0x00` | u32  | key    | `dialog_index << 16 \| character_id`             |
| `+0x04` | u32  | offset | Byte offset of the record in `base_dialog.dbss`  |
| `+0x08` | u32  | size   | Record size in bytes                             |

### String Table (variable: 4 bytes + strings)

| Offset  | Type               | Field        | Notes       |
| ------- | ------------------ | ------------ | ----------- |
| `+0x00` | u32                | string_count | Always `0`  |
| `+0x04` | pstr[string_count] | strings      | Empty       |

## Notes

- The name and lines are localized in LOC type `38`: `str_id1 = character_id`, `str_id2 = dialog_index`, `str_id3 = 0`, and `str_id4` `0` for the name and `1`, `2`, ... for the lines in order. In client 3458 all 10,165 lines and 59,686 of the 59,776 names have a row; Martina Finto's first line reads "Oh David... Maybe I should open up a restaurant here at the farm...".
- `name_kr` is the dialog's own name: copies of a generic NPC such as `순례자` (pilgrim) share it, and it may differ from the LOC type `6` name of the character ID.
- The lines are the speech bubbles over the NPC's head, checked in game 2026-09-29: Martina Finto showed "Oh David... Maybe I should open up a restaurant here at the farm..." in a bubble, and a villager beside her "The commander said I was the best!" (character `506`, dialog `210`, line `2`). The bubble is `UI_Data/Actor/UI_Actor_BubbleBox.XML` (`OverheadUIType_BubbleBox`, a `bubble.dds` frame around a 120 px auto-wrapping text box), which is why the lines carry hand-placed `\n` breaks. The Lua only creates the bubble panel pool (`ToClient_InitializeBubbleBoxPanelPool`); the client code picks and sets the text.
- The lines never show in the dialog window: that opens with the `detail_dialog.dbss` greeting (Martina: "It's so lonely here, all by myself... David doesn't seem to know.").
